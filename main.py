import sys
from PyQt6 import QtCore, QtMultimedia
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from piano import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for button in [self.w1, self.w2, self.w3, self.w4, self.w5, self.w6, self.w7,
                       self.b1, self.b2, self.b3, self.b4, self.b5, self.b6]:
            button.clicked.connect(self.funct)

    def funct(self):
        self.load_mp3(f'music/{self.sender().objectName()}.mp3')

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        self._audio_output = QtMultimedia.QAudioOutput()
        self._player = QtMultimedia.QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(50)
        self._player.setSource(media)
        self._player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())