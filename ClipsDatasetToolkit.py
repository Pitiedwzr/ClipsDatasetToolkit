from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from ui_MainWindow import Ui_MainWindow
import pathlib
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        self.clips_path = ""
        self.c1_path = ""
        self.c2_path = ""
        self.c3_path = ""
        self.c4_path = ""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()
        self.initSlots()

    def initSlots(self):
        self.ui.clipsListWidget.itemActivated.connect(self.playClip)
        self.ui.clipsPathLineEdit.editingFinished.connect(self.updateClipsPath)
        self.ui.c1PathLineEdit.editingFinished.connect(self.updateC1Path)
        self.ui.c2PathLineEdit.editingFinished.connect(self.updateC2Path)
        self.ui.c3PathLineEdit.editingFinished.connect(self.updateC3Path)
        self.ui.c4PathLineEdit.editingFinished.connect(self.updateC4Path)
    def updateClipsPath(self):
        self.clips_path = pathlib.Path(self.ui.clipsPathLineEdit.text())
        if self.clips_path.is_dir():
            self.ui.clipsListWidget.clear()
            for clip in self.clips_path.iterdir():
                if clip.suffix in [".mp4", ".avi", ".mov", ".mkv"]:
                    self.ui.clipsListWidget.addItem(clip.name)
        else:
            QMessageBox.warning(self, "Invalid Path", "The specified clips path is not a valid directory.")
            self.ui.clipsListWidget.clear()

    def updateC1Path(self):
        self.c1_path = pathlib.Path(self.ui.c1PathLineEdit.text())

    def updateC2Path(self):
        self.c2_path = pathlib.Path(self.ui.c2PathLineEdit.text())

    def updateC3Path(self):
        self.c3_path = pathlib.Path(self.ui.c3PathLineEdit.text())

    def updateC4Path(self):
        self.c4_path = pathlib.Path(self.ui.c4PathLineEdit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())