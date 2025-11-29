from enum import Enum
from pydantic import BaseModel
from typing import Optional

class QuestionType(Enum):
    multi_select = "multi-select"
    true_false = "trueFalse"
    normal = "normal"
    combo_box = "combobox"

class QuestionDto(BaseModel):
    question: str
    question_type: QuestionType
    value: Optional[int] = None
    tags: list[str]
    next_time: str | None = None

class NormalDto(QuestionDto):
    right_answers: list[str]
    wrong_answers: list[str]

class ComboBoxOptionDto(BaseModel):
    question: str
    options: list[str]
    correct: str | int

class ComboBoxDto(QuestionDto):
    comboboxes: list[ComboBoxOptionDto]
