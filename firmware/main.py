# Import board pins
import board

# KMK core imports
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

# Create keyboard instance
keyboard = KMKKeyboard()

# Add macro support
macros = Macros()
keyboard.modules.append(macros)

# Define GPIO pins based on your schematic (SW1–SW4)
PINS = [board.D3, board.D4, board.D2, board.D1]

# Tell KMK you're using a direct pin layout (not matrix)
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define macro functions for each button
keyboard.keymap = [
    [
        # SW1: Win+R, then type "wsl", then Enter
        KC.MACRO(
            Press(KC.LGUI),
            Tap(KC.R),
            Release(KC.LGUI),
            Tap(KC.W),
            Tap(KC.S),
            Tap(KC.L),
            Tap(KC.ENTER),
        ),

        # SW2: Type "git commit" + Enter
        KC.MACRO(
            Tap(KC.G),
            Tap(KC.I),
            Tap(KC.T),
            Tap(KC.SPACE),
            Tap(KC.C),
            Tap(KC.O),
            Tap(KC.M),
            Tap(KC.M),
            Tap(KC.I),
            Tap(KC.T),
            Tap(KC.ENTER),
        ),

        # SW3: Ctrl + S (Save)
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.S),
            Release(KC.LCTRL),
        ),

        # SW4: Ctrl + / (Toggle comment)
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.SLASH),
            Release(KC.LCTRL),
        ),
    ]
]

# Run the keyboard
if __name__ == '__main__':
    keyboard.go()

