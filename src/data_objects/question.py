from abc import ABC, abstractmethod

class Question(ABC):
    question: str
    answer_num: int # the number of available answers
    tags: list[str]

    def __init__(self, question, tags):
        self.question = question
        self.tags = tags
    
    @abstractmethod
    def evaluate(self, answer) -> bool:
        return NotImplemented

