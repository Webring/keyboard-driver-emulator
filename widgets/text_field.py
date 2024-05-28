from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QTextEdit, QApplication

from widgets.utils import check_modifiers


class TextField(QTextEdit):
    def __init__(self, parent=None):
        self.parent = parent
        self.pressed_keys = set()
        self.global_extra = dict()
        super().__init__(parent)

    def keyPressEvent(self, event):
        old_event = event

        scancode = event.nativeScanCode()

        other_modifiers = Qt.NoModifier
        for pressed_key_keycode in self.pressed_keys:
            pressed_key = self.parent.keys.get(pressed_key_keycode, None)
            other_modifiers |= pressed_key.modifier

        key = self.parent.keys.get(scancode, None)
        if key is not None:
            if event.key() != -1:
                self.pressed_keys.add(scancode)

            key.extra = self.global_extra

            modifiers = key.modifier | other_modifiers

            event = QKeyEvent(event.type(),
                              key.keycode,
                              modifiers,
                              key.get_text(modifiers))
            self.global_extra = key.extra
        else:
            print(f"Key {event.key()} not found")

        print(f"Event: ({scancode}) '{old_event}' -> '{event}'")
        print(f"Key: '{old_event.key()}' -> '{event.key()}'")
        print(f"Text: '{old_event.text()}' -> '{event.text()}'")
        print(
            f"Modifiers: '{check_modifiers(old_event.modifiers())}' -> '{check_modifiers(event.modifiers())}' ({check_modifiers(other_modifiers)})")
        print(f"\n")

        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        scancode = event.nativeScanCode()
        self.pressed_keys.discard(scancode)

    def emulate_key_press_function(self, scancode):
        def function():
            event = QKeyEvent(
                QEvent.KeyPress,
                -1,
                Qt.NoModifier,
                scancode,
                0x41,
                0x0,
                '',
                False,
                1
            )
            QApplication.postEvent(self, event)

        return function
