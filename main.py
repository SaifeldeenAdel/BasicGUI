import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from src.ui.mainwindow_ui import Ui_MainWindow as View
from src.logic.task1 import Task1
from src.logic.task2 import Task2

class MyGUI(QMainWindow, View):
    def __init__(self, parent=None):
        super(MyGUI, self).__init__(parent)
        self.setupUi(self)

        task1 = Task1()
        self.tabWidget.addTab(task1, "My Task")

        task2 = Task2()
        self.tabWidget.addTab(task2, "Task 2!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyGUI()
    w.show()
    app.exec()
