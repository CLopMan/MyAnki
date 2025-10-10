from adapters.question_adapter import QuestionAdapter
from dtos.deck_dto import DeckDto
from data_objects.deck import Deck

class DeckAdapter:
    def __init__(self, question_adapter=QuestionAdapter()):
        self.question_adapter = question_adapter

    def adapt_deck(self, deck_dto: DeckDto):
        return Deck(
                deck_name=deck_dto.title,
                questions=self.question_adapter.adapt_questions(deck_dto.questions)
                )


