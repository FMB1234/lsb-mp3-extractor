import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox

class LSBMP3ExtractorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('LSB MP3 Extractor')

        layout = QVBoxLayout()
        self.label = QLabel('Choose an action:')
        layout.addWidget(self.label)

        self.extractButton = QPushButton('Extract LSB from MP3')
        self.extractButton.clicked.connect(self.extractLSB)
        layout.addWidget(self.extractButton)

        self.encodeButton = QPushButton('Encode Message into MP3')
        self.encodeButton.clicked.connect(self.encodeMessage)
        layout.addWidget(self.encodeButton)

        self.setLayout(layout)

    def extractLSB(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open MP3 File', '', 'MP3 Files (*.mp3);;All Files (*)', options=options)
        if fileName:
            # Add LSB extraction logic here
            QMessageBox.information(self, 'Info', f'Extracted LSB from {fileName}')  # Placeholder message

    def encodeMessage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open MP3 File', '', 'MP3 Files (*.mp3);;All Files (*)', options=options)
        if fileName:
            # Add message encoding logic here
            QMessageBox.information(self, 'Info', f'Encoded message into {fileName}')  # Placeholder message

if __name__ == '__main__':
    app = QApplication(sys.argv)
    extractor = LSBMP3ExtractorApp()
    extractor.resize(300, 200)
    extractor.show()
    sys.exit(app.exec_())