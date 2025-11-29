from abc import ABC, abstractmethod

class Question(ABC):
    question: str
    answer_num: int # the number of available answers
    tags: list[str]

    def __init__(self, question, tags, value: int | None = None, image: str | None = None):
        self.question = question
        self.tags = tags
        self.value = 1 if value is None else value
        self.image = image
    
    @abstractmethod
    def evaluate(self, answer) -> bool:
        return NotImplemented

