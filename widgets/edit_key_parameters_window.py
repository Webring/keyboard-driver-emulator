from PyQt5.QtWidgets import QVBoxLayout, QComboBox, QLabel, QLineEdit, QTextEdit, QPushButton, QDoubleSpinBox, QDialog, \
    QHBoxLayout

from keyboard.basic_keyboard_keys import keyboard_keys, keyboard_modifiers
from widgets.utils import widget_with_layout


class EditKeyParametersWindow(QDialog):
    def __init__(self, key, parent=None):
        super().__init__(parent)
        self.key = key
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Редактирование кнопки')

        layout = QVBoxLayout()

        for value, text in keyboard_keys.items():
            if value == self.key.real_keycode:
                layout.addWidget(QLabel(f"<h1>Клавиша {text} ({self.key.real_keycode})</h1>"))
                break


        self.name_field = QLineEdit()
        self.name_field.setText(self.key.name)
        layout.addWidget(QLabel("Имя клавиши"))
        layout.addWidget(self.name_field)

        self.new_keycode_selector = QComboBox()
        for i, (value, text) in enumerate(keyboard_keys.items()):
            self.new_keycode_selector.addItem(text, value)
            if value == self.key.new_keycode:
                self.new_keycode_selector.setCurrentIndex(i)
        layout.addWidget(QLabel("Кейкод"))
        layout.addWidget(self.new_keycode_selector)

        self.modifier_selector = QComboBox()
        for i, (value, text) in enumerate(keyboard_modifiers.items()):
            self.modifier_selector.addItem(text, value)
            if value & self.key.modifiers:
                self.modifier_selector.setCurrentIndex(i)

        layout.addWidget(QLabel("Модификатор"))
        layout.addWidget(self.modifier_selector)

        # Положительное дробное число
        self.size_field = QDoubleSpinBox()
        self.size_field.setValue(self.key.size)
        self.size_field.setDecimals(2)
        self.size_field.setRange(1, 10)
        self.size_field.setSingleStep(0.25)

        layout.addWidget(QLabel('Размер кнопки'))
        layout.addWidget(self.size_field)

        # Редактор текста
        self.textEdit = QTextEdit()
        self.textEdit.setText(self.key.text_function)
        layout.addWidget(QLabel('Программа получения текста:'))
        layout.addWidget(self.textEdit)

        # Кнопка для закрытия окна
        self.buttons_layout = QHBoxLayout()
        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.accept)

        self.close_button = QPushButton('Выйти')
        self.close_button.clicked.connect(self.close)
        self.buttons_layout.addWidget(self.close_button)

        self.buttons_layout.addWidget(self.save_button)

        layout.addWidget(widget_with_layout(self.buttons_layout))

        self.setLayout(layout)

