# Hugging face

## Setup

```bash title=""
pdm add transformers
pdm add 'transformers[sentencepiece]'
pdm add 'transformers[torch]'
```

Default cache folder `~/.cache/huggingface/` but can be customized with `HF_HOME` env variable

## Transformers library

The goal is to provide a single API through which any Transformer model can be loaded, trained, and saved.

Main features:

- Easy of use
- Flexibility
- Simplicity

## Pipeline

[pipeline](https://huggingface.co/docs/transformers/main_classes/pipelines)
`pipeline()`
: It connects a model with its necessary preprocessing and postprocessing steps, allowing us to directly input any text and get an intelligible answer

A model finetune for the task is used by default. The input are preprocessed, fed to the model, and the output are postprocessed to be understandable.

### Task
```python title=""
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a HuggingFace course my whole life.")
```
```bash title=""
[{'label': 'POSITIVE', 'score': 0.9598047137260437}]
```

Some pipelines availables:

- feature-extraction (get the vector representation of a text)
- fill-mask
- ner (named entity recognition)
- question-answering
- sentiment-analysis
- summarization
- text-generation
- translation
- zero-shot-classification

### Model
```python title=""
pipe = pipeline(model="roberta-large-mnli")
pipe("This restaurant is awesome")
```

### Step by step
```python title=""
preprocessed = pipe.preprocess(inputs)
model_outputs = pipe.forward(preprocessed)
outputs = pipe.postprocess(model_outputs)
```

## AutoTokenizer

The tokenizer is responsible for:

- splitting the input into words, subwords, or symbols (like punctuation) that are called tokens
- mapping each token to an integer
- adding additional inputs that may be useful to the model

### Use
```python title=""
from transformers import AutoTokenizer

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
raw_inputs = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]
inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")
print(inputs)
```
```bash title=""
{
    'input_ids': tensor([
        [  101,  1045,  1005,  2310,  2042,  3403,  2005,  1037, 17662, 12172, 2607,  2026,  2878,  2166,  1012,   102],
        [  101,  1045,  5223,  2023,  2061,  2172,   999,   102,     0,     0,     0,     0,     0,     0,     0,     0]
    ]),
    'attention_mask': tensor([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
}
```

### Step by step
```python title=""
sequence = "Using a Transformer network is simple"
tokens = tokenizer.tokenize(sequence)
ids = tokenizer.convert_tokens_to_ids(tokens)
```

### Decode
```python title=""
decoded_string = tokenizer.decode([7993, 170, 11303, 1200, 2443, 1110, 3014])
```

Different kind of tokenizers:

- text based: basic but can lead to issues (dogs $\neq$ dog)
- character based: better but a lot of token to process
$\rightarrow$ subword tokenizers: tokenize wisely, divided in sentences or words sementicaly
- byte-level
- sentencepiece
- wordpiece

## AutoModel

The AutoModel class and all of its relatives are actually simple wrappers over the wide variety of models available in the library. It’s a clever wrapper as it can automatically guess the appropriate model architecture for your checkpoint, and then instantiates a model with this architecture.

### Load
```python title=""
from transformers import AutoModel

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModel.from_pretrained(checkpoint)
outputs = model(**inputs)
print(outputs.last_hidden_state.shape)
```
```bash title=""
torch.Size([2, 16, 768])
```

### Save
```python title=""
model.save_pretrained("directory_on_my_computer")
```
```bash title=""
ls directory_on_my_computer
config.json pytorch_model.bin
```

## Finetuning

### Preprocessing

### Trainer

```python title=""
from transformers import Trainer

trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
)
trainer.train()
```

or more sophisticated

```python title=""
def compute_metrics(eval_preds):
    metric = evaluate.load("glue", "mrpc")
    logits, labels = eval_preds
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

training_args = TrainingArguments("test-trainer", evaluation_strategy="epoch")
model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)

trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

trainer.train()
```



## Resources


??? question "What is the order of the language modeling pipeline?"
    The tokenizer handles text and returns IDs. The model handles these IDs and outputs a prediction. The tokenizer can then be used once again to convert these predictions back to some text

??? question "How many dimensions does the tensor output by the base Transformer model have, and what are they?"
    - sequence length
    - batch size
    - hidden size

??? question "What is the point of applying a SoftMax function to the logits output by a sequence classification model?"
    The total sum of the output is then 1, resulting in a possible probabilistic interpretation.
