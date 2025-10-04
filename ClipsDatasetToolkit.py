from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from ui_MainWindow import Ui_MainWindow
import pathlib
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        self.clips_path = ""
        self.reaction_time = 0
        self.c2_path = ""
        self.c3_path = ""
        self.c4_path = ""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()
        self.playerAudio = QAudioOutput()
        self.reactionTimer = QTimer()
        self.initSlots()

    def initSlots(self):
        self.ui.clipsListWidget.itemActivated.connect(self.playClip)
        self.ui.clipsPathLineEdit.editingFinished.connect(self.updateClipsPath)
        self.ui.c1PathLineEdit.editingFinished.connect(self.updateC1Path)
        self.ui.c2PathLineEdit.editingFinished.connect(self.updateC2Path)
        self.ui.c3PathLineEdit.editingFinished.connect(self.updateC3Path)
        self.ui.c4PathLineEdit.editingFinished.connect(self.updateC4Path)
        self.ui.timerFloatBox.valueChanged.connect(self.updateReactionTime)
        self.reactionTimer.timeout.connect(self.delayedPlay)
        self.player.setVideoOutput(self.ui.playerWidget)
        self.player.setAudioOutput(self.playerAudio)
        

    def playClip(self, item):
        selected_filename = item.text()
        full_clip_object = self.clips_path / selected_filename
        clip_url = QUrl.fromLocalFile(str(full_clip_object))
        self.player.setSource(clip_url)
        
        self.player.play()

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
    def updateReactionTime(self):
        self.reaction_time = int(self.ui.timerFloatBox.value() * 1000)

    def playNextClip(self):
        current_row = self.ui.clipsListWidget.currentRow()
        next_row = current_row + 1
        if next_row >= self.ui.clipsListWidget.count():
            self.player.stop()
            next_row = 0 
            return
        
        self.ui.clipsListWidget.setCurrentRow(next_row)
        self.next_item = self.ui.clipsListWidget.item(next_row)
        if self.reaction_time > 0:
            self.reactionTimer.start(self.reaction_time)
        else:
            self.playClip(self.next_item)

    def delayedPlay(self):
        self.reactionTimer.stop()
        if self.next_item:
            self.playClip(self.next_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())