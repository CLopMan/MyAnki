from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QWidget
from data_objects.true_false_question import TrueFalseQuestion
from gui.question_widget import QuestionWidget


class TrueFalseQuestionWidget(QuestionWidget):
    def __init__(self, question: TrueFalseQuestion):
        super().__init__(question)
        self.data: TrueFalseQuestion = question

    def create_answer(self):
        answer = QWidget()
        answer_layout: QVBoxLayout = QVBoxLayout()
        # TODO: suffle answer
        for key in self.data.answers.keys():
            aux_layout: QHBoxLayout = QHBoxLayout()
            aux_layout.addWidget(QLabel(key))
            aux_layout.addWidget(QCheckBox())
            answer_layout.addLayout(aux_layout)
        answer.setLayout(answer_layout)
        return answer

    def show_answer(self):
        pass
        
