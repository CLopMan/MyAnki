from data_objects.normal_question import NormalQuestion
from data_objects.true_false_question import TrueFalseQuestion
from data_objects.combo_box_question import ComboBoxQuestion, ComboBoxOption
from data_objects.question import Question
from dtos.question_dto import QuestionType, QuestionDto, NormalDto, ComboBoxOptionDto, ComboBoxDto

class QuestionAdapter:
    def __init__(self):
        self.map = \
        {
            QuestionType.combo_box: self.__adapt_combo_box,
            QuestionType.normal: self.__adapt_normal,
            QuestionType.true_false: self.__adapt_true_false
        }

    def adapt_questions(self, questions: list[QuestionDto]) -> list[Question]:
        result: list[Question] = []
        for q in questions:
            result.append(self.map.get(q.question_type, lambda _: None)(q))
        return result

    def __adapt_combo_option(self, option: ComboBoxOptionDto):
       return ComboBoxOption(
                  excercise=option.question,
                  options=option.options,
                  correct=option.correct
            )

    def __adapt_combo_box(self, question: ComboBoxDto):
        return ComboBoxQuestion(
                    question=question.question,
                    tags=question.tags,
                    options=[self.__adapt_combo_option(op) for op in question.comboboxes],
                    image=question.img
                )

    def __adapt_true_false(self, question: NormalDto):
        answers = {}
        for right in question.right_answers:
            answers[right] = True
        for wrong in question.wrong_answers:
            answers[wrong] = False

        return TrueFalseQuestion(
                    question=question.question,
                    tags=question.tags,
                    answers=answers,
                    image=question.img
                )

    def __adapt_normal(self, question: NormalDto) -> NormalQuestion:
        return NormalQuestion(
                    question=question.question,
                    tags=question.tags,
                    right=question.right_answers[0],
                    image=question.img
                )
        
