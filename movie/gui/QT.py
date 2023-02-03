from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, \
    QGridLayout, QLineEdit
import sys
import requests


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 350)
        self.setWindowTitle("Django App")
        self.layout = QGridLayout(self)
        self.button = QPushButton("Get json response from the server")
        self.button.clicked.connect(self.get_data)
        self.layout.addWidget(self.button, 0, 0)
        self.line_edit_url = QLineEdit("http://127.0.0.1:8000/movie/all/1")
        self.layout.addWidget(self.line_edit_url, 1, 0)

    def get_data(self):
        try:
            url = str(self.line_edit_url.text())
            response = requests.get(url=url)
            django_data = response.json()

            label = QLabel(str(django_data))
            label.setWordWrap(True)
            self.layout.addWidget(label)
        except Exception as ex:
            print('Error: ' + str(ex))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())