from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QTextEdit

from widgets.utils import check_modifiers


class TextField(QTextEdit):
    def __init__(self, parent=None):
        self.parent = parent
        self.pressed_keys = set()
        super().__init__(parent)

    def keyPressEvent(self, event):
        old_event = event

        print(event.nativeScanCode())

        other_modifiers = Qt.NoModifier
        for pressed_key_keycode in self.pressed_keys:
            pressed_key = self.parent.keyboard_layout.buttons.get(pressed_key_keycode, None)
            other_modifiers |= pressed_key.modifiers

        key = self.parent.keyboard_layout.buttons.get(event.key(), None)
        if key is not None:
            self.pressed_keys.add(event.key())

            modifiers = key.modifiers | other_modifiers

            event = QKeyEvent(event.type(),
                              key.new_keycode,
                              modifiers,
                              key.get_text(modifiers))
        else:
            print(f"Key {event.key()} not found")

        print(f"Event: '{old_event}' -> '{event}'")
        print(f"Key: '{old_event.key()}' -> '{event.key()}'")
        print(f"Text: '{old_event.text()}' -> '{event.text()}'")
        print(f"Modifiers: '{check_modifiers(old_event.modifiers())}' -> '{check_modifiers(event.modifiers())}' ({check_modifiers(other_modifiers)})")
        print(f"\n")


        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        self.pressed_keys.discard(event.key())