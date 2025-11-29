from .question import Question


class NormalQuestion(Question):
    right_answer: str

    def __init__(self, question, tags, right: str, image: str | None = None):
        super().__init__(question, tags, image=image)
        self.right_answer = right
        self.answer_num = 1

    def __str__(self):
        return f"{self.question.upper()}:\n\t{self.right_answer}\n\ttags: {", ".join(self.tags)}"

    def evaluate(self, answer: bool) -> bool:
        return answer
