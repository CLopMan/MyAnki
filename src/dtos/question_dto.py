from enum import Enum
from pydantic import BaseModel
from typing import Optional

class QuestionType(Enum):
    multi_select = "multi-select"
    true_false = "trueFalse"
    normal = "normal"

class QuestionDto(BaseModel):
    question: str
    question_type: QuestionType
    right_answers: list[str]
    wrong_answers: list[str]
    value: Optional[int] = None
    tags: list[str]
