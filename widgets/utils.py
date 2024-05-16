from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

all_modifiers = [
    Qt.ShiftModifier,
    Qt.ControlModifier,
    Qt.AltModifier,
    Qt.MetaModifier,
    Qt.KeypadModifier,
    Qt.GroupSwitchModifier
]

# Вывести их имена
modifier_names = {
    Qt.ShiftModifier: "Shift",
    Qt.ControlModifier: "Ctrl",
    Qt.AltModifier: "Alt",
    Qt.MetaModifier: "Meta",
    Qt.KeypadModifier: "Keypad",
    Qt.GroupSwitchModifier: "GroupSwitch"
}


def widget_with_layout(layout):
    new_widget = QWidget()
    new_widget.setLayout(layout)
    return new_widget


# Проверить комбинацию модификаторов
def check_modifiers(modifiers):
    pressed_modifiers = [modifier for modifier in all_modifiers if modifiers & modifier]
    if pressed_modifiers:
        return ", ".join(modifier_names[modifier] for modifier in pressed_modifiers)
    else:
        return ""
