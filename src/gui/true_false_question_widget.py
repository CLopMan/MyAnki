from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QWidget
from data_objects.true_false_question import TrueFalseQuestion
from gui.question_widget import QuestionWidget
from random import shuffle


class TrueFalseQuestionWidget(QuestionWidget):
    def __init__(self, question: TrueFalseQuestion):
        super().__init__(question)
        self.data: TrueFalseQuestion = question

    def create_answer(self):
        answer = QWidget()
        answer_layout: QVBoxLayout = QVBoxLayout()
        questions: list[str] = list(self.data.answers.keys())
        shuffle(questions)
        for q in questions:
            aux_layout: QHBoxLayout = QHBoxLayout()
            aux_layout.addWidget(QLabel(q))
            aux_layout.addWidget(QCheckBox())
            answer_layout.addLayout(aux_layout)
        answer.setLayout(answer_layout)
        return answer

    def show_answer(self):
        data_answers = self.data.answers
        gui_answers: list[QLabel] = [label for label in self.answer.children() if type(label) == QLabel]
        gui_checkbox: list[QCheckBox] = [box for box in self.answer.children() if type(box) == QCheckBox]
        for exc in gui_answers:
            if data_answers[exc.text()]:
                exc.setStyleSheet("color: #009933")
            else:
                exc.setStyleSheet("color: #990033")
        self._set_correct(self.data.evaluate(dict(zip([x.text() for x in gui_answers], [x.isChecked() for x in gui_checkbox]))))
        
