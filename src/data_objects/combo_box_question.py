from data_objects.question import Question

class ComboBoxOption:
    exercise: str
    options: list[str]
    correct: str
    
    def __init__(self, excercise: str, options: list[str], correct: str|int):
        self.exercise = excercise
        self.options = options.copy()
        if isinstance(correct, int):
            self.correct = self._int_correct(options, correct)
        elif isinstance(correct, str):
            self.correct = self._str_correct(options, correct)

    def _int_correct(self, options, correct):
        return options[correct]

    def _str_correct(self, options, correct):
        if correct not in options:
            raise Exception(f"{correct} is not part of the options ({options})")
        return correct

    def evaluate(self, answer: str) -> bool:
        return (answer == self.correct)
        
class ComboBoxQuestion(Question):
    def __init__(self, question, tags, options: list[ComboBoxOption], image: str|None = None):
        super().__init__(question, tags, image=image)
        self.options: dict[str, ComboBoxOption] = {op.exercise: op for op in options}


    def evaluate(self, answer: dict[str, str]) -> bool:
        result = True
        for key, val in answer.items():
            result = result and (self.options[key].evaluate(val))
        return result
