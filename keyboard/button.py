from PyQt5.QtCore import Qt


class KeyboardKey:
    def __init__(self,
                 name: str,
                 keycode,
                 modifier,
                 text_function: str = "value = ''"):
        self.name = name
        self.keycode = keycode
        self.modifier = Qt.KeyboardModifier(modifier)
        self.text_function = text_function
        self.extra = dict()

    def get_text(self, modifiers):
        exec_dict = {'alt_pressed': modifiers & Qt.AltModifier,
                     'ctrl_pressed': modifiers & Qt.ControlModifier,
                     'shift_pressed': modifiers & Qt.ShiftModifier}

        exec_dict.update({"extra": self.extra})

        try:
            exec(self.text_function, {}, exec_dict)
            self.extra = exec_dict.get("extra", dict())
            return exec_dict.get("value", "")
        except Exception as e:
            print("Get text error:", e)
            return ""

    def __dict__(self) -> dict:
        return {
            'name': self.name,
            'keycode': self.keycode,
            'modifier': self.modifier,
            'text_function': self.text_function
        }
