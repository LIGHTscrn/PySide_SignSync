from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget

from PySide6.QtWebEngineWidgets import QWebEngineView

from PySide6.QtCore import QUrl


class Main_Window(QMainWindow):

    def __init__(self):
        super().__init__()

        #Creating an Blank Middle Man Widget
        topWidget = QWidget()
        layout = QVBoxLayout()


        #Creating an Input Widget
        url_input = QLineEdit()
        play_button = QPushButton("Go")

        #Creating a WebEngineView
        self.youtubePlayer = QWebEngineView()
        layout.addWidget(self.youtubePlayer)

        youtubeIframe = '''
        <iframe width="560" height="315" src="https://www.youtube.com/embed/oe1ySIpWZgo?si=xxmvHJfvC7Q7beIa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen> </iframe>
        '''
        self.youtubePlayer.setHtml(youtubeIframe, QUrl("https://www.youtube.com"))
        
        layout.addWidget(url_input)
        layout.addWidget(play_button)

        topWidget.setLayout(layout)
        self.setCentralWidget(topWidget)


app = QApplication()
window = Main_Window()
window.show()
app.exec()



