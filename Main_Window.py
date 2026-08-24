from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget


class Main_Window(QMainWindow):

    def __init__(self):
        super.__init__()

        #Creating an Blank Middle Man Widget
        TopWidget = QWidget()
        layout = QVBoxLayout()

        #Creating an Input Widget
        url_input = QLineEdit()
        play_button = QPushButton("Go")




