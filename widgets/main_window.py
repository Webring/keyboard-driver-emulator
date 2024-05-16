from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QAction
from keyboard.button import KeyboardKey
from keyboard.layout import KeyboardLayout
from widgets.text_field import TextField
from widgets.utils import widget_with_layout

buttons = [
    [KeyboardKey("Esc", 27, 27, 1, Qt.NoModifier, "value='Esc'"),
     KeyboardKey("F1", 16777264, 16777264, 1, Qt.NoModifier, "value='F1'"),
     KeyboardKey("F2", 16777265, 16777265, 1, Qt.NoModifier, "value='F2'"),
     KeyboardKey("F3", 16777266, 16777266, 1, Qt.NoModifier, "value='F3'"),
     KeyboardKey("F4", 16777267, 16777267, 1, Qt.NoModifier, "value='F4'"),
     KeyboardKey("F5", 16777268, 16777268, 1, Qt.NoModifier, "value='F5'"),
     KeyboardKey("F6", 16777269, 16777269, 1, Qt.NoModifier, "value='F6'"),
     KeyboardKey("F7", 16777270, 16777270, 1, Qt.NoModifier, "value='F7'"),
     KeyboardKey("F8", 16777271, 16777271, 1, Qt.NoModifier, "value='F8'"),
     KeyboardKey("F9", 16777272, 16777272, 1, Qt.NoModifier, "value='F9'"),
     KeyboardKey("F10", 16777273, 16777273, 1, Qt.NoModifier, "value='F10'"),
     KeyboardKey("F11", 16777274, 16777274, 1, Qt.NoModifier, "value='F11'"),
     KeyboardKey("F12", 16777275, 16777275, 1, Qt.NoModifier, "value='F12'")],
    [KeyboardKey("`", 96, 96, 1, Qt.NoModifier, "value='`'"),
     KeyboardKey("1", 49, 49, 1, Qt.NoModifier, "value='1'"),
     KeyboardKey("2", 50, 50, 1, Qt.NoModifier, "value='2'"),
     KeyboardKey("3", 51, 51, 1, Qt.NoModifier, "value='3'"),
     KeyboardKey("4", 52, 52, 1, Qt.NoModifier, "value='4'"),
     KeyboardKey("5", 53, 53, 1, Qt.NoModifier, "value='5'"),
     KeyboardKey("6", 54, 54, 1, Qt.NoModifier, "value='6'"),
     KeyboardKey("7", 55, 55, 1, Qt.NoModifier, "value='7'"),
     KeyboardKey("8", 56, 56, 1, Qt.NoModifier, "value='8'"),
     KeyboardKey("9", 57, 57, 1, Qt.NoModifier, "value='9'"),
     KeyboardKey("0", 48, 48, 1, Qt.NoModifier, "value='0'"),
     KeyboardKey("-", 45, 45, 1, Qt.NoModifier, "value='-'"),
     KeyboardKey("=", 61, 61, 1, Qt.NoModifier, "value='='"),
     KeyboardKey("Backspace", 16777219, 16777219, 2, Qt.NoModifier, "value=''")],
    [KeyboardKey("Tab", 16777217, 16777217, 1.5, Qt.NoModifier, "value='\t'"),
     KeyboardKey("Q", 81, 81, 1, Qt.NoModifier, "value='Q' if shift_pressed else 'q'"),
     KeyboardKey("W", 87, 87, 1, Qt.NoModifier, "value='W' if shift_pressed else 'w'"),
     KeyboardKey("E", 69, 69, 1, Qt.NoModifier, "value='E' if shift_pressed else 'e'"),
     KeyboardKey("R", 82, 82, 1, Qt.NoModifier, "value='R' if shift_pressed else 'r'"),
     KeyboardKey("T", 84, 84, 1, Qt.NoModifier, "value='T' if shift_pressed else 't'"),
     KeyboardKey("Y", 89, 89, 1, Qt.NoModifier, "value='Y' if shift_pressed else 'y'"),
     KeyboardKey("U", 85, 85, 1, Qt.NoModifier, "value='U' if shift_pressed else 'u'"),
     KeyboardKey("I", 73, 73, 1, Qt.NoModifier, "value='I' if shift_pressed else 'i'"),
     KeyboardKey("O", 79, 79, 1, Qt.NoModifier, "value='O' if shift_pressed else 'o'"),
     KeyboardKey("P", 80, 80, 1, Qt.NoModifier, "value='P' if shift_pressed else 'p'"),
     KeyboardKey("[", 91, 91, 1, Qt.NoModifier, "value='['"),
     KeyboardKey("]", 93, 93, 1, Qt.NoModifier, "value=']'"),
     KeyboardKey("\\", 92, 92, 1.75, Qt.NoModifier, "value='\\'")],
    [KeyboardKey("Caps Lock", 16777252, 16777252, 1.75, Qt.NoModifier, "value=''"),
     KeyboardKey("A", 65, 65, 1, Qt.NoModifier, "value='A' if shift_pressed else 'a'"),
     KeyboardKey("S", 83, 83, 1, Qt.NoModifier, "value='S' if shift_pressed else 's'"),
     KeyboardKey("D", 68, 68, 1, Qt.NoModifier, "value='D' if shift_pressed else 'd'"),
     KeyboardKey("F", 70, 70, 1, Qt.NoModifier, "value='F' if shift_pressed else 'f'"),
     KeyboardKey("G", 71, 71, 1, Qt.NoModifier, "value='G' if shift_pressed else 'g'"),
     KeyboardKey("H", 72, 72, 1, Qt.NoModifier, "value='H' if shift_pressed else 'h'"),
     KeyboardKey("J", 74, 74, 1, Qt.NoModifier, "value='J' if shift_pressed else 'j'"),
     KeyboardKey("K", 75, 75, 1, Qt.NoModifier, "value='K' if shift_pressed else 'k'"),
     KeyboardKey("L", 76, 76, 1, Qt.NoModifier, "value='L' if shift_pressed else 'l'"),
     KeyboardKey(";", 59, 59, 1, Qt.NoModifier, "value=';'"),
     KeyboardKey("'", 39, 39, 1, Qt.NoModifier, "value='''"),
     KeyboardKey("Enter", 16777220, 16777220, 2.5, Qt.NoModifier, "value=''")],
    [KeyboardKey("Shift", 16777248, 16777248, 2.25, Qt.ShiftModifier, "value=''"),
     KeyboardKey("Z", 90, 90, 1, Qt.NoModifier, "value='Z' if shift_pressed else 'z'"),
     KeyboardKey("X", 88, 88, 1, Qt.NoModifier, "value='X' if shift_pressed else 'x'"),
     KeyboardKey("C", 67, 67, 1, Qt.NoModifier, "value='C' if shift_pressed else 'c'"),
     KeyboardKey("V", 86, 86, 1, Qt.NoModifier, "value='V' if shift_pressed else 'v'"),
     KeyboardKey("B", 66, 66, 1, Qt.NoModifier, "value='B' if shift_pressed else 'b'"),
     KeyboardKey("N", 78, 78, 1, Qt.NoModifier, "value='N' if shift_pressed else 'n'"),
     KeyboardKey("M", 77, 77, 1, Qt.NoModifier, "value='M' if shift_pressed else 'm'"),
     KeyboardKey(",", 44, 44, 1, Qt.NoModifier, "value=','"),
     KeyboardKey(".", 46, 46, 1, Qt.NoModifier, "value='.'"),
     KeyboardKey("/", 47, 47, 1, Qt.NoModifier, "value='/'"),
     KeyboardKey("Shift", 16777248, 16777248, 2.75, Qt.ShiftModifier, "value=''")],
    [KeyboardKey("Ctrl", 16777249, 16777249, 1, Qt.ControlModifier, "value=''"),
     KeyboardKey("Win", 16777250, 16777250, 1, Qt.MetaModifier, "value=''"),
     KeyboardKey("Alt", 16777251, 16777251, 1, Qt.AltModifier, "value=''"),
     KeyboardKey("Space", 32, 32, 7, Qt.NoModifier, "value=' '"),
     KeyboardKey("Alt", 16777251, 16777251, 1, Qt.AltModifier, "value=''"),
     KeyboardKey("Menu", 16777253, 16777253, 1, Qt.NoModifier, "value=''"),
     KeyboardKey("Ctrl", 16777249, 16777249, 1, Qt.ControlModifier, "value=''")]
]


class KeyboardDriverMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.keyboard_layout = KeyboardLayout(buttons)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Keyboard driver emulator')

        self.setWindowIcon(QIcon('icon.png'))

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('Раскладка')

        open_layout_action = QAction("Открыть", self)
        # open_layout_action.triggered.connect()
        file_menu.addAction(open_layout_action)

        save_layout_action = QAction("Сохранить", self)
        file_menu.addAction(save_layout_action)

        base_layout = QVBoxLayout()

        self.textbox = TextField(self)

        base_layout.addWidget(self.textbox)

        base_layout.addWidget(self.keyboard_layout.widget)

        self.setCentralWidget(widget_with_layout(base_layout))

    def save_layout(self):
        pass
