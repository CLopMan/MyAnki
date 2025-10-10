from data_objects.normal_question import NormalQuestion
from data_objects.question import Question
from dtos.question_dto import QuestionType, QuestionDto

class QuestionAdapter:
    def __init__(self):
        self.map = \
        {
            QuestionType.multi_select: self.__adapt_multiselect,
            QuestionType.normal: self.__adapt_normal,
            QuestionType.true_false: self.__adapt_true_false
        }

    def adapt_questions(self, questions) -> list[Question]:
        result: list[Question] = []
        for q in questions:
            result.append(self.map.get(q.question_type, lambda question: None)(q))
        return result


    def __adapt_multiselect(self, question):
        return NotImplemented

    def __adapt_true_false(self, question):
        return NotImplemented

    def __adapt_normal(self, question: QuestionDto) -> NormalQuestion:
        return NormalQuestion(
                    question=question.question,
                    tags=question.tags,
                    right=question.right_answers[0]
                )
        
        
