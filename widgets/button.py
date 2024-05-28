from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.right_button_clicked()
        else:
            super(Button, self).mousePressEvent(event)

    def right_button_clicked(self):
        pass
