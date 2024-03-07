# Litellm
Provides a unified interface to call 100+ llms with the same input/output format

## Install
`pdm add litellm`

`pdm add litellm[proxy]`

## Run autogen locally
Litellm to act as a proxy server. You can use OpenAI's API with your own local model, using e.g. Ollama.

1. Launch the your model through litellm:
```bash
litellm --model ollama/<ollama-model-name>
```
```
Proxy running on http://0.0.0.0:8000
```
1. Configure your llm (see [autogen](./autogen.md#agents))
```python
config_list = [
    {
        'model':"no"
        'base_url': "http://0.0.0.0:8000",
        'api_key': "NULL"
    }
]
llm_config = {"config_list": config_list}
```
Only the `base_url` is needed, other are just placeholders as they are already defined by your local model

1. Leave the rest unchanged
!!! warning
    For now, you can only use `AssistantAgent`.
    `GPTAssistantAgent` is not supported, so no function calling available.

## Resources

- [Power Each AI Agent With A Different LOCAL LLM (AutoGen + Ollama Tutorial)](https://www.youtube.com/watch?v=y7wMTwJN7rA&t=693s)
- [Microsoft taskweaver](https://microsoft.github.io/TaskWeaver/docs/llms/liteLLM/)