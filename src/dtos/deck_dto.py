from pydantic import BaseModel
from dtos.question_dto import QuestionDto

class DeckDto(BaseModel):
    title: str
    questions: list[QuestionDto]

    def __len__(self):
        return len(self.questions)
