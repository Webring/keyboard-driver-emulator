from PyQt5.QtCore import Qt


class KeyboardKey:
    def __init__(self, name: str,
                 scancode: int,
                 keycode,
                 size: float,
                 modifiers,
                 text_function: str = "value = ''"):
        self.name = name
        self.real_keycode = scancode
        self.new_keycode = keycode
        self.size = size
        self.modifiers = modifiers
        self.text_function = text_function

    def scratch_factor(self):
        return int(self.size * 4)

    def get_text(self, modifiers):
        exec_dict = {'alt_pressed': modifiers & Qt.AltModifier,
                     'ctrl_pressed': modifiers & Qt.ControlModifier,
                     'shift_pressed': modifiers & Qt.ShiftModifier}
        exec(self.text_function, {}, exec_dict)
        return exec_dict.get("value", "")

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'real_keycode': self.real_keycode,
            'new_keycode': self.new_keycode,
            'size': self.size,
            'modifiers': self.modifiers,
            'text_function': self.text_function
        }
