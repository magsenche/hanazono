# Llama

## Install

- download weights via [facebook research repo](https://github.com/facebookresearch/llama#download)
    - clone the llama repo
    - ask for weights
    - run `./download.sh` with provided url
- quantize weights using [llama.cpp](https://github.com/ggerganov/llama.cpp)
    - clone the llama.cpp repo
    - build it with `make`
    - convert weights to ggml format `python convert.py ../llama/llama-2-7b-chat`
    - quantize weights to make them smaller `./quantize ../llama/llama-2-7b-chat/ggml-model-f16.gguf ../llama/llama-2-7b-chat/ggml-model-q4_0.gguf q4_0`

## Use

Check the ReadMe [llama.cpp](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

example: `./main -m ../llama/llama-2-7b-chat/ggml-model-q4_0.gguf -p "The list of the name of all european country:"

## Ressources
-  [Llama 2 for Mac M1](https://medium.com/@auslei/llama-2-for-mac-m1-ed67bbd9a0c2)
