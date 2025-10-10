from enum import Enum
from pydantic import BaseModel

class QuestionType(Enum):
    multi_select = "multi-select"
    true_false = "trueFalse"
    normal = "normal"

class QuestionDto(BaseModel):
    question: str
    question_type: QuestionType
    right_answers: list[str]
    wrong_answers: list[str]
    tags: list[str]
