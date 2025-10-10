from dataclasses import dataclass
from data_objects.question import Question

@dataclass
class OptionAnswer:
    answer: str
    value: bool

    

#class TrueFalseQuestion(Question):
#    answers: list[OptionAnswer]
#
#    def __init__(self, question, tags, answers):
#        super().__init__(question, tags)
#        self.answers: list[OptionAnswer] = [OptionAnswer(**answer) for answer in answers]
#        self.answer_num: int =  len(answers)
#
#    def evaluate(self, answer: list[bool]) -> bool:
#        for i, x in enumerate(answer):
#            if x != self.answers[i].value:
#                return False
#        return True
#
#    def to_json(self) -> str:
#        return \
#f"{{\
#    \"type\": \"normal\",\
#    \"tags\": {str(self.tags)},\
#    \"answerNum\": 1,\
#}}"
#
#    def __str__(self):
#        return f"{self.question.upper()}:\n\t- {"\n\t- ".join([f"{a.answer} : {a.value}" for a in self.answers])}\n\ttags: {", ".join(self.tags)}"

#class MultiSelectQuestion(TrueFalseQuestion):
#
#    def __init__(self, question, tags, answers, num = 0):
#        super().__init__(question, tags, answers)
#        self.answer_num: int = num if num > 0 else len(answers)
#
#    def evaluate(self, answer: list[int]) -> bool:
#        out = len(answer) > 0
#        for i in answer:
#            out = out and self.answers[i].value
#        return out
#
#    def to_json(self) -> str:
#        return \
#f"{{\
#\"type\": \"normal\",\
#\"tags\": {str(self.tags)},\
#\"answerNum\": 1,\
#}}"

 
class Deck:
    title: str
    questions: list[Question]
    card_num: int

    def __init__(self, deck_name: str, questions: list[Question]):
        self.title = deck_name
        self.questions = questions
        self.card_num = len(questions)

    def __len__(self) -> int:
        return self.card_num
