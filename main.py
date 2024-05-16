import sys

from PyQt5.QtWidgets import QApplication

from widgets.main_window import KeyboardDriverMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = KeyboardDriverMainWindow()
    widget.show()
    sys.exit(app.exec_())
