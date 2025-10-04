from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt, QUrl, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QListWidgetItem
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from ui_MainWindow import Ui_MainWindow
import pathlib
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        self.clips_path = ""
        self.reaction_time = 0
        self.category_map = {
        Qt.Key_1: "",
        Qt.Key_2: "",
        Qt.Key_3: "",
        Qt.Key_4: "",
        }
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
        self.player.mediaStatusChanged.connect(self.updateMediaStatus)

    def playClip(self, item):
        full_clip_object = item.data(Qt.UserRole)
        clip_url = QUrl.fromLocalFile(str(full_clip_object))
        self.player.setSource(clip_url)
        self.player.play()

    def updateClipsPath(self):
        self.clips_path = pathlib.Path(self.ui.clipsPathLineEdit.text())
        if self.clips_path.is_dir():
            self.ui.clipsListWidget.clear()
            for clip in self.clips_path.iterdir():
                if clip.suffix in [".mp4", ".avi", ".mov", ".mkv"]:
                    item = QListWidgetItem(clip.name)
                    item.setData(Qt.UserRole, clip) # Use data to store the full path (definitely will use ListView next time)
                    self.ui.clipsListWidget.addItem(item)
        else:
            QMessageBox.warning(self, "Invalid Path", "The specified clips path is not a valid directory.")
            self.ui.clipsListWidget.clear()

    def updateC1Path(self):
        self.category_map[Qt.Key_1] = pathlib.Path(self.ui.c1PathLineEdit.text())

    def updateC2Path(self):
        self.category_map[Qt.Key_2] = pathlib.Path(self.ui.c2PathLineEdit.text())

    def updateC3Path(self):
        self.category_map[Qt.Key_3] = pathlib.Path(self.ui.c3PathLineEdit.text())

    def updateC4Path(self):
        self.category_map[Qt.Key_4] = pathlib.Path(self.ui.c4PathLineEdit.text())

    def updateReactionTime(self):
        self.reaction_time = int(self.ui.timerFloatBox.value() * 1000)

    def updateMediaStatus(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.delayed = True
            self.playNextClip()

    def playNextClip(self):
        current_row = self.ui.clipsListWidget.currentRow()
        next_row = current_row + 1
        if next_row >= self.ui.clipsListWidget.count():
            self.player.stop()
            next_row = 0 
            return
        
        self.ui.clipsListWidget.setCurrentRow(next_row)
        self.next_item = self.ui.clipsListWidget.item(next_row)
        if self.reaction_time > 0 and self.delayed:
            self.reactionTimer.start(self.reaction_time)
        else:
            self.playClip(self.next_item)

    def delayedPlay(self):
        self.reactionTimer.stop()
        if self.next_item:
            self.playClip(self.next_item)

    def keyPressEvent(self, event):
        key = event.key()
        if isinstance(event, QKeyEvent):
            if key == Qt.Key_Space:
                if self.player.playbackState() == QMediaPlayer.PlayingState:
                    self.player.pause()
                else:
                    self.player.play()
            elif key == Qt.Key_S:
                self.player.stop()
            elif key in self.category_map:
                selected_item = self.ui.clipsListWidget.currentItem()
                if selected_item:
                    selected_filename = selected_item.text()
                    source_path = selected_item.data(Qt.UserRole)
                    target_dir = self.category_map[key]
                    target_path = target_dir / selected_filename
                    target_dir.mkdir(exist_ok=True)
                    try:
                        self.player.stop()
                        self.player.setSource(QUrl()) # Clear source to release file lock
                        source_path.rename(target_path)
                        selected_item.setData(Qt.UserRole, target_path)
                        self.playNextClip()
                    except Exception as e:
                        QMessageBox.critical(self, "Error", f"Failed to move file: {e}")
                else:
                    QMessageBox.information(self, "No Selection", "Please select a clip to categorize.")
            else:
                super().keyPressEvent(event)
        else:
            super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())