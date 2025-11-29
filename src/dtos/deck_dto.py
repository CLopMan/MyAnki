from pydantic import BaseModel
from dtos.question_dto import NormalDto, ComboBoxDto

class DeckDto(BaseModel):
    title: str
    questions: list[NormalDto | ComboBoxDto]

    def __len__(self):
        return len(self.questions)
