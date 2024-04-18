import django

django.setup()
import argparse
import pathlib

from crewai import Agent, Crew, Process, Task
from langchain.embeddings.ollama import OllamaEmbeddings
from langchain_openai import ChatOpenAI

from aiasan import prompts, tools, vectorstore
from aiasan.utils import get_crewai_tool
from hanazono.flashcards.models import Flashcard

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--n_topics", type=int, default=3)
    parser.add_argument("-f", "--favored", type=str, default="")
    args = parser.parse_args()

    outputs_path = pathlib.Path("outputs") / f"{args.favored}_{args.n_topics}"
    outputs_path.mkdir(exist_ok=True, parents=True)

    # Vectorstore
    store_path = pathlib.Path("outputs/store")
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    docs_path = pathlib.Path("/Users/gamnes/Documents/hanazono/docs")

    db_exists = (store_path / "index.faiss").is_file()
    if db_exists:
        db = vectorstore.VectorStore(store_path, embedding)
        db.load()
    else:
        db = vectorstore.VectorStore.initialize(store_path, embedding, docs_path)
        db.save()

    # Tools
    google_search = get_crewai_tool(tools.search, "google search")
    listdir = get_crewai_tool(tools.listdir, "list directory", dir_path=docs_path)
    readfile = get_crewai_tool(tools.readfile, "read file", dir_path=docs_path)
    retrieve = get_crewai_tool(tools.retrieve_documents, "retrieve notes", db=db, k=3)
    flashcards_by_box = get_crewai_tool(Flashcard.objects.by_box, "flashcards by box")
    file_stats = get_crewai_tool(Flashcard.objects.file_stats, "flashcard file stats")
    extraction = get_crewai_tool(Flashcard.objects.extract, "extract flashcards")

    # AI agents
    model = ChatOpenAI(model="gpt-4-turbo-2024-04-09")

    teacher = Agent(
        llm=model,
        role="Senior Teacher",
        goal="Add knowledge to the second brain with leitner based learning",
        backstory=prompts.TEACHER,
        verbose=True,
        allow_delegation=False,
    )
    researcher = Agent(
        llm=model,
        role="Senior Researcher",
        goal="Research about specific subjects to make sure accurate information and knowledge is learnt and written in the second brain",
        backstory=prompts.WEB_RESEARCHER,
        verbose=True,
        allow_delegation=False,
    )

    # Tasks
    stats_task = Task(
        description=("Make some stats about flashcards"),
        expected_output="A statistical report about flaschards",
        tools=[flashcards_by_box, file_stats],
        agent=researcher,
    )
    analyze_task = Task(
        description=(
            "Analyze existing notes to identify knowledge gaps and areas for further exploration."
            "Recommend a balanced selection of {n_topics} topics with a focus on both strong foundations"
            "and areas of curiosity, prioritizing {favored} topics while maintaining a diverse learning journey."
            "For each identified topic, craft a concise section summarizing what you currently know, utilizing"
            "clear and concise language."
            f"You have acces to following files: {listdir.run()}"
        ),
        expected_output=(
            "A report with {n_topics} sections, each with a title and summary of your current knowledge"
            "about the corresponding topic. Additionally, the report will include a list of recommended topics"
            "with corresponding file paths in your notes."
        ),
        tools=[readfile, retrieve],
        agent=teacher,
        output_file=str(outputs_path / "analyze.md"),
    )
    add_task = Task(
        description=(
            "Embark on a research expedition to gather high-quality content for the chosen topics."
            "Integrate diverse resources like scholarly articles, documentaries, and trusted websites."
            "Ensure the information is well-supported by credible sources and presented in an engaging format."
        ),
        expected_output=(
            "A detailed {n_topics} section report with at least 3 sections each,"
            "enriched with relevant links and resources for further exploration."
        ),
        tools=[google_search],
        agent=researcher,
        output_file=str(outputs_path / "add.md"),
    )
    final_task = Task(
        description=(
            "Weave the newly acquired knowledge into your existing notes."
            "Seamlessly integrate new sections and paragraphs within the relevant topic sections, maintaining clarity and conciseness."
            "Include links and resource references for future exploration."
            "Craft new flashcards (question/answer pairs) to solidify your understanding."
            f"You have acces to following files: {listdir.run()}"
        ),
        expected_output=(
            "A markdown note with the following enhancements:"
            "\n  * Added sections and paragraphs for the new information"
            "\n  * Included links and resource references for further exploration"
            "\n  * Created new flashcards (question/answer pairs)"
            "\n  * Maintained the original style of the note"
        ),
        tools=[readfile],
        agent=teacher,
        context=[analyze_task, add_task],
        output_file=str(outputs_path / "update.md"),
    )
    flashcard_task = Task(
        description=(
            "Craft new flashcards (question/answer pairs) for the added content to solidify your understanding."
            "Make sure flashcards cover the note's knowledge well."
            f"You have acces to following files: {listdir.run()}"
        ),
        expected_output=("A markdown created new flashcards (question/answer pairs)"),
        tools=[readfile, extraction],
        agent=teacher,
        output_file=str(outputs_path / "flaschards.md"),
    )

    # Crew
    crew = Crew(
        agents=[researcher, teacher],
        tasks=[stats_task, analyze_task, add_task, final_task, flashcard_task],
        process=Process.sequential,
        max_rpm=100,
    )

    result = crew.kickoff(inputs={"n_topics": args.n_topics, "favored": args.favored})
