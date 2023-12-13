from PySide6.QtWidgets import QWidget
from src.ui.task1_ui import Ui_Form as View

class Task1(QWidget, View):
    def __init__(self, parent=None):
        super(Task1, self).__init__(parent)
        self.setupUi(self)

        self.changeButton.clicked.connect(self.changeText)
    
    def changeText(self):
        self.textLabel.setText("Changed")

