from deck import Deck 
import random

class Game:
    deck_title: str
    failed: list[int]
    right: list[int]
    objective: int
    deck: Deck
    

    def __init__(self, deck_name: str, objective: int) -> None:
        self.deck_title: str = deck_name
        self.deck: Deck = Deck(deck_name)
        self.failed: list[int] = []
        self.right: list[int] = []
        self.objective: int = objective

    def generate_order(self, upper_bound: int|None = None) -> list[int]:
        if upper_bound is None:
            upper_bound = len(self.deck)
        return random.sample(range(len(self.deck)), upper_bound)

    def answer_question(self, answer, index):
        if self.deck.questions[index].evaluate(answer):
            self.right.append(index)
        else: 
            self.failed.append(index)

    def stadistics(self):
        return round(len(self.right) / (len(self.right) + len(self.failed)) * 10, 2)


if __name__ == "__main__":
    game: Game = Game("testdeck", 10)
    game.answer_question(False, 2)
    game.answer_question([False, True], 1)
    game.answer_question([0], 0)
    print(game.stadistics())

