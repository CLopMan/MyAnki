from data_objects.question import Question


class TrueFalseQuestion(Question):
    def __init__(self, question, tags, answers: dict[str, bool]):
        super().__init__(question, tags)
        self.answers = answers
        self.answer_num = len(answers.keys())

    def evaluate(self, answer: dict[str, bool]):
        result = True
        for key in answer.keys():
            result = result and (answer[key] == self.answers[key])

        return result

