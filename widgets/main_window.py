import json
import os.path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QAction, QWidget, QHBoxLayout, QPushButton, QFileDialog, \
    QMessageBox, QLabel
from keyboard.button import KeyboardKey
from widgets.edit_key_parameters_window import EditKeyParametersWindow
from widgets.text_field import TextField
from widgets.utils import widget_with_layout


def create_keyboard_widget(placement, layout, click_function=None):
    keyboard_layout = QVBoxLayout()

    for line in placement:
        line_layout = QHBoxLayout()
        line_layout.setContentsMargins(0, 0, 0, 0)
        for i, (scancode, size) in enumerate(line):

            if scancode is None:
                line_layout.addWidget(QWidget())
            else:
                keyboard_key = layout.get(scancode, None)

                key_name = keyboard_key.name if keyboard_key is not None else f"SC{scancode}"

                push_button = QPushButton(key_name)
                push_button.setStyleSheet("QPushButton { padding: 10px; }")
                if keyboard_key is None or keyboard_key.keycode < 0:
                    push_button.setDisabled(True)
                if click_function is not None:
                    push_button.clicked.connect(click_function(scancode))
                line_layout.addWidget(push_button)

            line_layout.setStretch(i, int(size * 4))
        keyboard_layout.addWidget(widget_with_layout(line_layout))

    return widget_with_layout(keyboard_layout)


class KeyboardDriverMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.keys = {}
        self.keys_placement = []

        self.keyboard_widget = QLabel("Загрузите файл расположения и файл раскладки")

        self.initUI()

        self._load_placement(os.path.abspath("base_placement.kplc"))

        self.load_stylesheet("style.qss")


    def load_stylesheet(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print("Stylesheet file not found")

    def initUI(self):
        self.setWindowTitle('Keyboard driver emulator')

        self.setWindowIcon(QIcon('icon.ico'))

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('Файл')

        open_placement_action = QAction("Открыть расположение клавиш", self)
        open_placement_action.triggered.connect(self.load_placement)
        file_menu.addAction(open_placement_action)

        open_layout_action = QAction("Открыть раскладку", self)
        open_layout_action.triggered.connect(self.load_layout)
        file_menu.addAction(open_layout_action)

        save_layout_action = QAction("Сохранить раскладку", self)
        save_layout_action.triggered.connect(self.save_layout)

        file_menu.addAction(save_layout_action)

        self.base_layout = QVBoxLayout()
        self.textbox = TextField(self)
        self.base_layout.addWidget(self.textbox)
        self.base_layout.addWidget(self.keyboard_widget)

        self.setCentralWidget(widget_with_layout(self.base_layout))

    def open_key_param_editor(self, scancode):
        def function():
            key = self.keys[scancode]
            self.secondWindow = EditKeyParametersWindow(scancode, key, self)
            if self.secondWindow.exec_():
                name = self.secondWindow.name_field.text()
                keycode = self.secondWindow.new_keycode_selector.currentData()
                modifier = self.secondWindow.modifier_selector.currentData()
                text_function = self.secondWindow.textEdit.toPlainText()

                key.name = name
                key.keycode = keycode
                key.modifier = Qt.KeyboardModifier(modifier)
                key.text_function = text_function
                self.update_keyboard_widget()

        return function

    def load_placement(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Загрузить расположение', '', 'Конфигурация (*.kplc)')

        if not file_path:
            return

        self._load_placement(file_path)

    def _load_placement(self, file_path):
        try:
            with open(file_path, 'r') as file:
                keys_placement = json.load(file)
                for line in keys_placement:
                    for scancode, size in line:
                        pass

                self.keys_placement = keys_placement
            self.update_keyboard_widget()
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Ошибка открытия файла",
                                 f"При открытии файла \"{file_path}\" произошла ошибка!")

    def load_layout(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Загрузить раскладку', '', 'Конфигурация (*.klay)')

        if not file_path:
            return

        self._load_layout(file_path)

    def _load_layout(self, file_path):
        try:
            with open(file_path, 'r') as file:
                json_data = json.load(file)

                new_keys = dict()

                for scancode, key in json_data.items():
                    new_keys[int(scancode)] = KeyboardKey(key["name"],
                                                          key["keycode"],
                                                          key["modifier"],
                                                          key["text_function"])
                self.keys = new_keys
            self.update_keyboard_widget()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка открытия файла",
                                 f"При открытии файла \"{file_path}\" произошла ошибка!")

    def save_layout(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Сохранить раскладку', '', 'Конфигурация (*.klay)')

        if not file_path:
            return

        try:
            with open(file_path, 'w') as file:
                json.dump(self.keys, file, default=lambda o: o.__dict__())
        except Exception as e:
            QMessageBox.critical(self, "Ошибка сохранения файла",
                                 f"При сохранении файла \"{file_path}\" произошла ошибка!")

    def update_keyboard_widget(self):
        if not self.keys_placement:
            new_widget = QLabel("Откройте файл размещения")
        else:
            new_widget = create_keyboard_widget(self.keys_placement, self.keys, self.open_key_param_editor)
        self.base_layout.replaceWidget(self.keyboard_widget, new_widget)
        self.keyboard_widget.deleteLater()
        self.keyboard_widget = new_widget
