from data_objects.question import Question
 
class Deck:
    title: str
    questions: list[Question]
    card_num: int

    def __init__(self, deck_name: str, questions: list[Question]):
        self.title = deck_name
        self.questions = questions
        self.card_num = len(questions)

        possible_tags: set[str] = set()
        for q in questions:
            possible_tags = possible_tags.union( set(q.tags))

        self.possible_tags: set[str] = possible_tags

    def filter(self, tags: list[str]):
        if len(tags) <= 0:
            return self
        tags_set = set(tags)
        return Deck(
                deck_name=self.title,
                questions=[q for q in self.questions if len(tags_set.intersection(set(q.tags))) > 0]
            )
        

    def __len__(self) -> int:
        return self.card_num
