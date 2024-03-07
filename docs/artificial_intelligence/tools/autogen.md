# Autogen

AutoGen provides a ** multi-agent conversation framework as a high-level abstraction**. It is an **open-source** library for enabling next-generation Large Language Model (LLM) applications with multi-agent collaborations, teachability, and personalization. It allows users to build LLM workflows, where **multiple agents can converse with each other to solve tasks**.

## Agents

![](../fig/autogen-class.png)

### ConversableAgent
The `ConversableAgent`  is class for generic conversable agents which can be configured as assistant or user proxy.

After receiving each message, the agent will send a reply to the sender unless the msg is a termination msg. For example, `AssistantAgent` and `UserProxyAgent` are subclasses of this class, configured with different default settings.

### AssistantAgent
The `AssistantAgent` is designed to act as an AI assistant, using LLMs by default but not requiring human input or code execution. It could write Python code (in a Python coding block) for a user to execute when a message (typically a description of a task that needs to be solved) is receive

### UserProxy
The `UserProxyAgent` is conceptually a proxy agent for humans, soliciting human input as the agent's reply at each interaction turn by default and also having the capability to execute code and call functions or tools.

The `UserProxyAgent` triggers code execution automatically when it detects an executable code block in the received message and no human user input is provided

??? question "Define a simple assistant agent that can do a google search using autogen"
    Write the instructions explaining the role
    ```python
    instructions = """
    You are a world class researcher, who can do detailed research on any topic and produce facts based results; you do not make things up, you will try as hard as possible to gather facts & data to back up the research
    Please make sure you complete the objective above with the following rules:
    1/ You should do enough research to gather as much information as possible about the objective
    2/ If there are url of relevant links & articles, you will scrape it to gather more information
    3/ After scraping & search, you should think "is there any new things i should search & scraping based on the data I collected to increase research quality?" If answer is yes, continue; But don't do this more than 3 iterations
    4/ You should not make things up, you should only write facts & data that you have gathered
    5/ In the final output, You should always include all reference data & links to back up your research; You should include all reference data & links to back up your research
    """
    ```

    Define model configuration
    ```python
    config_list = {"model":"gpt-3.5-turbo-1106","api-key":"xxxx"}
    ```

    Define tools binded to the `search_fn` used
    ```python
    tools = [
        {
            "type": "function",
            "function": {
                "name": "google_search",
                "description": "google search to return results of search of search keywords",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "A great search keyword that is most likely to return result for the information you are looking for",
                        }
                    },
                    "required": ["keyword"],
                },
            },
        },
    ]
    ```

    Create the agent
    ```python
    research_agent = GPTAssistantAgent(
        name="Browser agent",
        instructions: instructions,
        llm_config: {"config_list": config_list, "tools": tools},
        function_map={"google_search": search_fn}
    )
    ```

### Retrieve Assistant

`RetrieveAssistantAgent` & `RetrieveUserProxyAgent` classes.

Check out [Retrieval Augmentation](https://microsoft.github.io/autogen/docs/topics/retrieval_augmentation) section.

## Multi-agent Conversation Framework
AutoGen abstracts and implements conversable agents designed to solve tasks through inter-agent conversations (see the [docs](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat#a-basic-two-agent-conversation-example))

??? question "Create a small researcher team using `Research`,`ResearchManager` agents"
    Create agents
    ```python
    import autogen

    researcher_agent = Researcher()
    research_manager_agent = ResearchManager()
    user_proxy = autogen.UserProxyAgent(
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
        name="user_proxy",
        max_consecutive_auto_reply=1,
        description="The boss that give tasks and say when the job is done.",
    )
    ```

    Gather them into a group chat to interact
    ```python title=""
    groupchat = autogen.GroupChat(
        agents=[
            user_proxy,
            research_manager_agent,
            researcher_agent,
        ],
        messages=[],
    )
    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config={"config_list": config_list},
    )
    ```

    Initiate conversation
    ```python
    prompt = "Make a research about <something>"
    user_proxy.initiate_chat(manager, message=user_prompt)
    ```

### Group-chat
Several agent contributes to the same thread. A `GroupChatManager` agent is responsible for:

- picking the next speaker
- receiving message from it
- broadcasting it to all agents in the groupchat

It is possible to control the dynamic of the conversation via several parameters:

- `speaker_selection_method` $\in$ `['auto', 'manual', 'random', 'round_robin']`
- `allowed_or_disallowed_speaker_transitions` by defining ~~dis~~allowed next speakers for each agent
- `send_introductions` to make sure agent present themselves

Check more on the [conversation patterns](https://microsoft.github.io/autogen/docs/tutorial/conversation-patterns) docs

### Nested chat
You can register [nested-chat](https://microsoft.github.io/autogen/docs/tutorial/conversation-patterns#nested-chats) as agent's inner dialog.

It exposes a single conversation interface which can be useful to integrate it in larger workflows or just to set up a personnal assistant.

## Other
### Caching
Autogen supports [llm caching](https://microsoft.github.io/autogen/docs/topics/llm-caching) which is useful when performing the same request several time e.g. when testing or playing.

```pyhton
from autogen import Cache

# Use Redis as cache
with Cache.redis(redis_url="redis://localhost:6379/0") as cache:
    user.initiate_chat(assistant, message=coding_task, cache=cache)

# Use DiskCache as cache
with Cache.disk() as cache:
    user.initiate_chat(assistant, message=coding_task, cache=cache)
```

## Resources

- [Examples](https://microsoft.github.io/autogen/docs/Examples)
- [Getting Started with AutoGen](https://microsoft.github.io/autogen/docs/Getting-Started/)
- [AutoGen Full Tutorial with Python (YouTube)](https://www.youtube.com/watch?v=V2qZ_lgxTzg)
- [GitHub Repository](https://github.com/microsoft/autogen)
- ["Research agent 3.0 - Build a group of AI researchers"](https://www.youtube.com/watch?v=AVInhYBUnKs)
- [Nested-chat](https://microsoft.github.io/autogen/docs/notebooks/agentchat_nestedchat/)