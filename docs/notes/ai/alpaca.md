# Alpaca

- wait for support on ggml to gguf weight conversion
- wait alpaca weights to be available

```bash
(llama.cpp-3.11) ➜  llama.cpp git:(master) ✗ python convert-llama-ggml-to-gguf.py -i models/ggml-alpaca-7b-q4.bin -o models/ggml-alpaca-7b-q4.gguf
* Using config: Namespace(input=PosixPath('models/ggml-alpaca-7b-q4.bin'), output=PosixPath('models/ggml-alpaca-7b-q4.gguf'), name=None, desc=None, gqa=1, eps='5.0e-06', context_length=2048, model_metadata_dir=None, vocab_dir=None, vocabtype='spm')

=== WARNING === Be aware that this conversion script is best-effort. Use a native GGUF model if possible. === WARNING ===

- Note: If converting LLaMA2, specifying "--eps 1e-5" is required. 70B models also need "--gqa 8".
* Scanning GGML input file
* File format: GGMLv1 with ftype MOSTLY_Q4_0
Traceback (most recent call last):
  File "/Users/gamnes/Documents/code/llama.cpp/convert-llama-ggml-to-gguf.py", line 451, in <module>
    main()
  File "/Users/gamnes/Documents/code/llama.cpp/convert-llama-ggml-to-gguf.py", line 428, in main
    offset = model.load(data, 0)
             ^^^^^^^^^^^^^^^^^^^
  File "/Users/gamnes/Documents/code/llama.cpp/convert-llama-ggml-to-gguf.py", line 194, in load
    self.validate_conversion(hp.ftype)
  File "/Users/gamnes/Documents/code/llama.cpp/convert-llama-ggml-to-gguf.py", line 187, in validate_conversion
    raise ValueError(f'{err} Sorry, your {self.file_format.name}v{self.format_version} file of type {ftype.name} is not eligible for conversion.')
ValueError: Quantizations changed in GGJTv2. Can only convert unquantized GGML files older than GGJTv2. Sorry, your GGMLv1 file of type MOSTLY_Q4_0 is not eligible for conversion.
```

## Flashcards