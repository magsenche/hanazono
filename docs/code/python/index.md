# Python

## Install python 3.11
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11-full
```
## Dataclass

Use dataclass for data class container in python

[9 Reasons Why You Should Start Using Python Dataclasses](https://towardsdatascience.com/9-reasons-why-you-should-start-using-python-dataclasses-98271adadc66)


```python
@dataclass
class Person:
    first_name: str = "Nesgam"
    last_name: str = "Inibehc"
    age: int = 27
    job: str = "Engineer"
```

## Flashcards