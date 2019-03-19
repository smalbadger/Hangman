import sys

from PySide2.QtWidgets import QApplication

from HangmanWindow import HangmanWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HangmanWindow()
    window.show()
    sys.exit(app.exec_())
