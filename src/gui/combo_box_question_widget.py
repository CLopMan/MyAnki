from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QWidget
from data_objects.combo_box_question import ComboBoxQuestion, ComboBoxOption
from gui.question_widget import QuestionWidget
from random import shuffle

class ComboBoxQuestionWidget(QuestionWidget):
    def __init__(self, question: ComboBoxQuestion):
        super().__init__(question)
        self.data: ComboBoxQuestion = question

    def create_answer(self):
        answer = QWidget()
        answer_layout: QVBoxLayout = QVBoxLayout()
        questions: list[ComboBoxOption] = list(self.data.options.values())
        shuffle(questions)
        for q in questions:
            selection_box = QComboBox()
            options = q.options.copy()
            shuffle(options)
            selection_box.addItems(options)
            selection_box.addItem("")
            selection_box.setCurrentIndex(len(options))
            
            aux_layout: QHBoxLayout = QHBoxLayout()
            aux_layout.addWidget(QLabel(q.exercise))
            aux_layout.addWidget(selection_box)
            answer_layout.addLayout(aux_layout)
            
        answer.setLayout(answer_layout)
        return answer

    def show_answer(self):
        data_answers = self.data.options
        gui_answers: list[QLabel] = [label for label in self.answer.children() if type(label) == QLabel]
        gui_combobox: list[QComboBox] = [box for box in self.answer.children() if type(box) == QComboBox]
        for exc, answer in zip(gui_answers, gui_combobox):
            if data_answers[exc.text()].evaluate(answer.currentText()):
                exc.setStyleSheet("color: #009933")
            else:
                exc.setStyleSheet("color: #990033")
        self._set_correct(self.data.evaluate(dict(zip([x.text() for x in gui_answers], [x.currentText() for x in gui_combobox]))))
