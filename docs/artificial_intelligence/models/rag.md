# RAG

Retrieval Augmented Generation (RAG) is a technique that combines an information retrieval component with a text generator model. It allows LLMs to bypass retraining as the internal knowledge can be modified in an efficient manner. Idea by [Meta AI](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/).

1. takes an input and retrieves a set of relevant documents given a source
2. concatenates as context with the original input prompt
3. feeds it to the text generator to produce the final output

??? question "What is RAG?"
    **Retrieval Augmented Generation** combines an information retrieval component with a text generator model. It allows LLMs to bypass retraining as the internal knowledge can be modified in an efficient manner.

## Core Components

- **Retriever Component:** Finds relevant documents or information from a large dataset or knowledge base.
- **Embedding Model:** Converts the user query and documents into vector representations for effective retrieval.
- **Vector Database (Vector Index):** Stores precomputed vector embeddings of documents.
- **Generator Component:** The LLM that generates the final text output using the retrieved information and the original query.
- **Synthesis Module:** Combines retrieved information with the generated response to create a coherent and integrated final output.
- **Query Processing Module:** Prepares the user query for embedding and retrieval, including preprocessing steps like tokenization and normalization.
- **Post-Retrieval Filtering:** Filters out irrelevant or low-quality data after the initial retrieval process.
- **Contextualization Module:** Provides additional context by considering interaction history or related queries.
- **Hybrid Retrieval System:** Combines dense and sparse retrieval methods to balance semantic understanding and exact matches.

??? question "What are the core components of RAG?"
    - Retriever Component
    - Embedding Model
    - Vector Database (Vector Index)
    - Generator Component
    - Synthesis Module
    - Query Processing Module
    - Post-Retrieval Filtering
    - Contextualization Module
    - Hybrid Retrieval System

## Basic Workflow

1. **Query Processing:** Convert the user query into a vector.
2. **Vector Database Retrieval:** Use the query vector to search the database for relevant contexts.
3. **Context Retrieval:** Retrieve and feed the most relevant info into the LLM.
4. **Response Generation:** The LLM generates a response using both the original query and the retrieved contexts.
5. **Final Output:** Produce an informed and accurate response.

## Applications

- **Chatbots & Conversational Agents:** Provides detailed, accurate customer support.
- **Content Generation:** Improves accuracy and depth in automated content creation.
- **Question-Answering Systems:** Offers detailed explanations and summaries in education and research.
- **Healthcare:** Assists in diagnosis and treatment by retrieving relevant medical data.

## Advantages

- **Accuracy:** Reduces hallucination by grounding responses in real documents.
- **Up-to-date Information:** Retrieves the most recent data, ensuring current responses.
- **Enhanced Reasoning:** Provides logical, fact-based responses by integrating external context.
- **Customizable:** Tailors to specific domains like legal or medical.

## Challenges and Limitations:

- **Complexity:** Increases model complexity by combining retrieval and generation.
- **Scalability:** Challenges in managing large databases.
- **Latency:** Retrieval processes can slow down real-time responses.
- **Context Limitation:** May struggle with large context requirements.
- **Bias:** Retrieval sources can introduce or amplify biases.

??? question "What are the advantages and challenges of RAG?"
    Advantages:

    - Accuracy
    - Up-to-date Information
    - Enhanced Reasoning
    - Customizable

    Challenges:

    - Complexity
    - Scalability
    - Latency
    - Context Limitation
    - Bias