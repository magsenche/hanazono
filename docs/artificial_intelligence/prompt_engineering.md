# Prompt Engineering
## General tips

- **start simple** and add elements and context as you aim for better results: it's an iterative process
- **use commands** to instruct the model what you want to do, e.g. "write", "translate", "summarize"
- **separate instructions from context** by using some clear separators such as ‘### Instruction ###‘
- **say what to do, not what not to do**
- **be very specific** as the more descriptive the prompt is, the better the results

Other good practices by [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)

## LLM settings
There are few parameters available to tweak LLMs behaviors:

### Temperature
Controls the creativity of the model.

- Low `temperature` $\rightarrow$ **predictible**
- High `temperature` $\rightarrow$ **creative**

It controls how often the model outputs a less likely token. You may want low `temperature` for fact-based QA tasks and high `temperature` for creative ones.

### Top P
Decides how deterministic the model is.

- Low `top_p` $\rightarrow$ **exact and factual**
- High `top_p` $\rightarrow$ **diverse**

`top_p` decides how many possible words to consider. It will only consider words that together add up to `top_p` of the total proability. Also called nucleus sampling. Generally we tweak either `temperature` or `top_p` but not both.

??? question "What are the `temperature` and `top_p` parameters for? "
    - `temperature` controls the creativity of the model by changing how often the model outputs a less likely token
    - `top_p` controls how deterministic a model is by deciding how many words to consider

### Max length
Limits the number of token the model generates.

`max_length` can be used to prevent long or irrelevant responses and high costs.

### Stop sequences
Specifies a set of tokens that, when generated, will cause th text generation to stop.

### Frequency penalty
Reduces repetition of tokens.

`frequency_penalty` applies a penalty to the next tokens proportionnal to how many times it has already been generated in the response and prompt.

### Presence penalty
Reduces repetition of tokens.

`presence_penalty` is the same as `frequency_penalty` but applies the same penalty no matter how many time the tokens already appeared. Generally we tweak either  `frequency_penalty` or `presence_penalty` but not both.

## Techniques

### Zero-shot
Biggest models are able to performs tasks without any example.

When it doesn't work, you can provide examples in the prompt:

### Few-shot
Enables in-context learning by provinding example of the task in the prompt itself. Examples serve as conditionning the answer.

The more difficult the task, the more example are needed (1-shot vs 5-shot, 10-shot, etc.)

- **format** plays a key role in performance
- both **inputs and labels distribution** are important even if labels are wrong for individual inputs!

### Chain-of-Thought
Enables complex reasoning capabilities through intermediate reasoning steps. Can be combined with [few-short prompting](#few-shot) to get better results.

=== "Prompt"
    ```
    The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
    A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

    The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
    A: Adding all the odd numbers (17, 19) gives 36. The answer is True.

    The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
    A: Adding all the odd numbers (11, 13) gives 24. The answer is True.

    The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
    A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False.

    The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
    A:
    ```
=== "Output"
    ```
    Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.
    ```

#### Zero-shot COT
Just add `Let'sthink step-by-step` to the original prompt.

=== "Prompt"
    ```
    I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?

    Let's think step by step.
    ```
=== "Output"
    ```
    First, you started with 10 apples.
    You gave away 2 apples to the neighbor and 2 to the repairman, so you had 6 apples left.
    Then you bought 5 more apples, so now you had 11 apples.
    Finally, you ate 1 apple, so you would remain with 10 apples.
    ```

#### Auto-COT
Samples questions with diversity and generates reasoning chains to construct the demonstrations to avoid having to handcraft many Q/A examples. Idea from [Automatic Chain of Thought Prompting in Large Language Models](https://arxiv.org/pdf/2210.03493.pdf) with [code](https://github.com/amazon-science/auto-cot).

#### Self-consistency
Samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths. Idea from [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/pdf/2203.11171.pdf).

??? question "What is COT (Chain-Of-Thought)? Name few example of other techniques related to it"
    **COT** enables complex reasoning capabilities through intermediate reasoning steps provided as context.
    Some methods improve the original techniques:

    - Zero-shot COT
    - Auto-COT
    - Self-consistency

### Prompt chaining
Splits the task into subtasks with the idea to create a chain of prompt operations.

- is useful to perform complex tasks
- helps to boost transparency of your LLM application
- increases controllability and reliability

=== "Prompt 1"
    ```
    You are a helpful assistant. Your task is to help answer a question given a document. The first step is to extract quotes relevant to the question from the document, delimited by ####. Please output the list of quotes using <quotes></quotes>. Respond with "No relevant quotes found!" if no relevant quotes were found.
    ####
    {{document}}
    ####
    ```
=== "Output 1"
    ```
    <quotes>
    - Chain-of-thought (CoT) prompting[27]
    - Generated knowledge prompting[37]
    - Least-to-most prompting[38]
    - Self-consistency decoding[39]
    - Complexity-based prompting[41]
    - Self-refine[42]
    - Tree-of-thought prompting[43]
    - Maieutic prompting[45]
    - Directional-stimulus prompting[46]
    - Textual inversion and embeddings[59]
    - Using gradient descent to search for prompts[61][62][63][64]
    - Prompt injection[65][66][67]
    </quotes>
    ```
=== "Prompt 2"
    ```
    Given a set of relevant quotes (delimited by <quotes></quotes>) extracted from a document and the original document (delimited by ####), please compose an answer to the question. Ensure that the answer is accurate, has a friendly tone, and sounds helpful.
    ####
    {{document}}
    ####
    <quotes>
    - Chain-of-thought (CoT) prompting[27]
    - Generated knowledge prompting[37]
    - Least-to-most prompting[38]
    - Self-consistency decoding[39]
    - Complexity-based prompting[41]
    - Self-refine[42]
    - Tree-of-thought prompting[43]
    - Maieutic prompting[45]
    - Directional-stimulus prompting[46]
    - Textual inversion and embeddings[59]
    - Using gradient descent to search for prompts[61][62][63][64]
    - Prompt injection[65][66][67]
    </quotes>
    ```
=== "Output 2"
    ```
    The prompting techniques mentioned in the document include:
    1. Chain-of-thought (CoT) prompting[27]
    2. Generated knowledge prompting[37]
    3. Least-to-most prompting[38]
    4. Self-consistency decoding[39]
    5. Complexity-based prompting[41]
    6. Self-refine[42]
    7. Tree-of-thought prompting[43]
    8. Maieutic prompting[45]
    9. Directional-stimulus prompting[46]
    10. Textual inversion and embeddings[59]
    11. Using gradient descent to search for prompts[61][62][63][64]
    12. Prompt injection[65][66][67]
    Each of these techniques employs unique strategies to enhance or specify the interactions with large language models to produce the desired outcomes.
    ```

More on [Anthropic AI guide](https://docs.anthropic.com/claude/docs/prompt-chaining)

### Retrieval Augmented Generation
Combines an information retrieval componenent with a text generator model. It allows LLMs to bypass retraining as the internal knowledge can be modified in an efficient manner. Idea by [Meta AI](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/).

1. takes an input and retrieves a set of relevant documents given a source
2. concatenates as context with the original input prompt
3. feeds it to the text generator to produce the final output

??? question "What is RAG?"
    **Retrieval Augmented Generation** combines an information retrieval componenent with a text generator model. It allows LLMs to bypass retraining as the internal knowledge can be modified in an efficient manner

### Prompt function
Encapsulates prompts into functions to create a workflow.

- start with a meta prompt to define the task for the LLM
- define desired functions
- combine them to perform the target task

=== "Meta prompt"
    ```
    Hello, ChatGPT! I hope you are doing well. I am reaching out to you for assistance with a specific function. I understand that you have the capability to process information and perform various tasks based on the instructions provided. In order to help you understand my request more easily, I will be using a template to describe the function, input, and instructions on what to do with the input. Please find the details below:

    function_name: [Function Name]
    input: [Input]
    rule: [Instructions on how to process the input]

    I kindly request you to provide the output for this function, based on the details I have provided. Your assistance is greatly appreciated. Thank you!
    I will replace the text inside the brackets with the relevant information for the function I want you to perform. This detailed introduction should help you understand my request more efficiently and provide the desired output. The format is function_name(input) If you understand, just answer one word with ok.
    ```
=== "Function 1 prompt"
    ```
    function_name: [trans_word]
    input: ["text"]
    rule: [I want you to act as an English translator, spelling corrector and improver. I will provide you with input forms including "text" in any language and you will detect the language, translate it and answer in the corrected of my text, in English.]
    ```
=== "Function 2 prompt"
    ```
    function_name: [expand_word]
    input: ["text"]
    rule: [Please serve as a Chatterbox, spelling corrector, and language enhancer. I will provide you with input forms including "text" in any language, and output the original language.I want you to Keep the meaning same, but make them more literary.]
    ```
=== "Function 3 prompt"
    ```
    function_name: [fix_english]
    input: ["text"]
    rule: [Please serve as an English master, spelling corrector, and language enhancer. I will provide you with input forms including "text", I want you to improve the text's vocabulary and sentences with more natural and elegent. Keep the meaning same.]
    ```
=== "Task prompt"
    ```title=""
    trans_word('婆罗摩火山处于享有“千岛之国”美称的印度尼西亚. 多岛之国印尼有4500座之多的火山, 世界著名的十大活火山有三座在这里.')
    fix_english('Finally, you can run the function independently or chain them together.')
    fix_english(expand_word(trans_word('婆罗摩火山处于享有“千岛之国”美称的印度尼西亚. 多岛之国印尼有4500座之多的火山, 世界著名的十大活火山有三座在这里.')))
    ```

??? question "What's the principle behind prompt-chaining and prompt function techniques"
    - **prompt-chaining** is spliting the task into subtasks with the idea to create a chain of prompt operations
    - **prompt function** consists of encapsulating prompts into functions to create a workflow

### Others
Check the prompt engineering [guide](https://www.promptingguide.ai/techniques) for more techniques

## Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Prompt Engineering guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic AI prompt design guide](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)
