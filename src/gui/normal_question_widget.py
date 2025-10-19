from PyQt5.QtWidgets import QLabel
from data_objects.normal_question import NormalQuestion
from gui.question_widget import QuestionWidget


class NormalQuestionWidget(QuestionWidget):
    def __init__(self, question: NormalQuestion):
        super().__init__(question)
        self.data: NormalQuestion = question # not necesary. Added for typehinting in the editor
        self.setStyleSheet("border: 1px solid red")

    def show_answer(self):
        self.answer.setVisible(True)

    def create_answer(self):
        answer = QLabel(self.data.right_answer)
        answer.setVisible(False)
        no_resize = answer.sizePolicy()
        no_resize.setRetainSizeWhenHidden(True)
        answer.setSizePolicy(no_resize)
        answer.setWordWrap(True)
        return answer
