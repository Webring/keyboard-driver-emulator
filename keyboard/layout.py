from typing import Dict

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

from keyboard.button import KeyboardKey
from widgets.edit_key_parameters_window import EditKeyParametersWindow
from widgets.utils import widget_with_layout


class KeyboardLayout:
    def __init__(self, keyboard):
        self.buttons: Dict[KeyboardKey] = dict()
        self.widget = self.get_widget(keyboard)

    def change_key_event(self, key_event: QKeyEvent):

        button = self.buttons.get(key_event.key(), None)
        if button is not None:
            print(bool(button.modifiers & Qt.ShiftModifier))
            key_event = QKeyEvent(key_event.type(),
                                  button.new_keycode,
                                  button.modifiers | key_event.modifiers(),
                                  button.get_text(key_event.modifiers()))

        return key_event

    def get_widget(self, keyboard):
        keyboard_layout = QVBoxLayout()

        for keyboard_line in keyboard:
            keyboard_line_layout = QHBoxLayout()
            keyboard_line_layout.setContentsMargins(0, 0, 0, 0)
            for i, button in enumerate(keyboard_line):
                self.buttons[button.real_keycode] = button
                new_button = QPushButton(button.name)
                new_button.setStyleSheet("QPushButton { padding: 10px; }")
                new_button.clicked.connect(self.change_button(button))
                keyboard_line_layout.addWidget(new_button)
                keyboard_line_layout.setStretch(i, button.scratch_factor())

            keyboard_layout.addWidget(widget_with_layout(keyboard_line_layout))

        return widget_with_layout(keyboard_layout)

    def change_button(self, button):

        def function():
            key = self.buttons[button.real_keycode]
            self.secondWindow = EditKeyParametersWindow(key)
            if self.secondWindow.exec_():
                name = self.secondWindow.name_field.text()
                new_keycode = self.secondWindow.new_keycode_selector.currentData()
                modifier = self.secondWindow.modifier_selector.currentData()
                size = self.secondWindow.size_field.value()
                text_function = self.secondWindow.textEdit.toPlainText()

                key.name = name
                key.new_keycode = new_keycode
                key.modifiers = Qt.KeyboardModifier(modifier)
                key.size = size
                key.text_function = text_function

        return function
