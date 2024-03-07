# LangChain
LangChain is a framework for developing applications powered by language models.

## Libraries
LangChain is divided into many parts/libraries:

### Python and JavaScript libraries
Contains interfaces and integrations for a myriad of components, a basic run time for combining these components into chains and agents, and off-the-shelf implementations of chains and agents.

- **langchain-core**: Base abstractions and LangChain Expression Language.
- **langchain-community**: Third party integrations.
- **langchain**: Chains, agents, and retrieval strategies that make up an application's cognitive architecture.

Many third party libraries are integrated into LangChain. To use them, just install them in your environment.
`pdm add ollama`

### LangChain Templates
A collection of easily deployable reference architectures for a wide variety of tasks. These templates provide a **starting point** for your application, saving you time and effort.

### LangServe
A library for deploying LangChain chains as a REST API. This allows you to easily **integrate** your language models into other applications and services.

### LangSmith
A developer platform that lets you **debug**, **test**, **evaluate**, and **monitor** chains built on any LLM framework and seamlessly integrates with LangChain.

## Chains
Chains are a core concept in LangChain, representing a sequence of components that process an input and return an output. There are several types of chains available in LangChain, including:

* **LLMChain**: A chain that uses a language model to generate a response based on an input prompt.
* **RetrievalChain**: A chain that retrieves relevant documents from a vector store based on an input query, and then uses a language model to generate a response based on the retrieved documents.
* **ConversationalChain**: A chain that maintains state across multiple turns of a conversation, allowing for more natural and contextually aware responses.

Here's an example of using an LLMChain to generate a response to a user's question:
```python
from langchain_core.chains import LLMChain
from langchain_community.llms import Ollama

prompt = "What is the capital of France?"

llm = Ollama(model="llama2")

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run()
```

With the [pipe chaining operator](#pipe-chaining-operator):
??? question "Load and run a simple llm with langchain using a local model"

    Prepare a prompt
    ```python
    from langchain_core.prompts import ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class technical documentation writer."),
        ("user", "{input}")
    ])
    ```
    Choose a model
    ```python
    from langchain_community.llms import Ollama
    llm = Ollama(model="llama2")
    ```
    Run the whole chain
    ```python
    chain = prompt | llm
    chain.invoke({"input":"how can langsmith help with testing?"})
    ```

## Vector Stores
Vector stores are a key component of many LangChain applications, allowing for efficient similarity search over large collections of documents. LangChain supports several types of vector stores, including:

* **FAISS**: A library for efficient similarity search, developed by Facebook AI Research.
* **Pinecone**: A managed vector database service.
* **Hnswlib**: A library for approximate nearest neighbor search, developed

## Agents
Agents are another important concept in LangChain, representing autonomous entities that can interact with their environment to achieve a goal. Agents can be thought of as a higher-level abstraction built on top of chains. There are several types of agents available in LangChain, including:

* **ToolAgent**: An agent that uses a set of tools (e.g. web search, APIs) to accomplish a task.
* **LLMAgent**: An agent that uses a language model to generate actions and interact with its environment.
* **ConversationalAgent**: An agent that can engage in natural language conversation with a user to accomplish a task.

Here's an example of using a ToolAgent to answer a question that requires information from the web:
```python
from langchain_core.agents import ToolAgent
from langchain_community.tools import SerpAPI

question = "What is the current temperature in New York City?"

tool = SerpAPI()

agent = ToolAgent(tools=[tool], llm=Ollama(model="llama2"))

answer = agent.run(question)
```

## Tools
### LCEL
`LCEL`
:The LangChain Expression Language (LCEL) is a declarative way to compose Runnables into chains. Any chain constructed this way will automatically have sync, async, batch, and streaming support.

The `Runnable` protocol is implemented for most components. This is a **standard interface**, which makes it easy to define custom chains as well as invoke them in a standard way. It includes:

- `stream`: stream back chunks of the response
- `invoke`: call the chain on an input
- `batch`: call the chain on a list of inputs

see more [here](https://python.langchain.com/docs/expression_language/interface)

### Prompt
Use `{}` placeholders for inputs

```python
prompt = PromptTemplate.from_template("tell me a short joke about {topic}")
print(prompt.invoke({"topic": "ice cream"}))
```
```sh
"tell me a short joke about ice cream"
```

### Pipe chaining operator
The | symbol is similar to a pipe operator, which **chains together the different components** feeds the output from one component as input into the next component.

```python
model = Ollama(model="mixtral")
formatting_model = LLMChain(llm=model, prompt=fc_prompt)

document_chain = create_stuff_documents_chain(model, input_prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

chain = retrieval_chain | formatting_model
```

You can check output of a smaller chain to see intermediate results and build the chain step-by-step:

```python
response_1 = retrieval_chain.invoke({"input": "zinc"})
print(response.keys())
```
```sh
dict_keys(['input', 'context', 'answer'])
```

## Resources

- [Langchain python doc](https://python.langchain.com/docs/get_started)
