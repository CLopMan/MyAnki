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
    tags: list[str]
    next_time: str | None = None
    value: Optional[int] = None
    img: Optional[str] = None

class NormalDto(QuestionDto):
    right_answers: list[str]
    wrong_answers: list[str]

class ComboBoxOptionDto(BaseModel):
    question: str
    options: list[str]
    correct: str | int

class ComboBoxDto(QuestionDto):
    comboboxes: list[ComboBoxOptionDto]
