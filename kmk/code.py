print("Starting")

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.split import Split
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

split = Split(data_pin=keyboard.data_pin, use_pio=True)
# split = Split(data_pin=keyboard.data_pin, data_pin2=keyboard.data_pin2)

keyboard.modules.append(split)
keyboard.modules.append(Layers())

keyboard.keymap = [
    [
        KC.ESC,  KC.N1, KC.N2, KC.N3,    KC.N4,   KC.N5,       KC.N6,    KC.N7,   KC.N8,   KC.N9,  KC.N0,   KC.MINS,
        KC.TAB,  KC.Q,  KC.W,  KC.E,     KC.R,    KC.T,        KC.Y,     KC.U,    KC.I,    KC.O,   KC.P,    KC.LBRC,
        KC.BSLS, KC.A,  KC.S,  KC.D,     KC.F,    KC.G,        KC.H,     KC.J,    KC.K,    KC.L,   KC.SCLN, KC.QUOT,
        KC.NUBS, KC.Z,  KC.X,  KC.C,     KC.V,    KC.B,        KC.N,     KC.M,    KC.COMM, KC.DOT, KC.SLSH, KC.RBRC,
                               KC.MO(1), KC.SPC,  KC.BSPC,     KC.ENT,   KC.RSFT, KC.MO(2),
                                         KC.RGUI, KC.LCTRL,    KC.RCTRL, KC.LALT
    ],
    [
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,      KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,      KC.NLCK,  KC.P7,    KC.P8,    KC.P9,    KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,      KC.TRNS,  KC.P4,    KC.P5,    KC.P6,    KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,      KC.TRNS,  KC.P1,    KC.P2,    KC.P3,    KC.TRNS,  KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,      KC.TRNS,  KC.TRNS,  KC.TRNS,
                                                KC.TRNS,  KC.TRNS,      KC.TRNS,  KC.RALT
    ],
    [
        KC.F12,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,        KC.F6,    KC.F7,    KC.F8,      KC.F9,    KC.F10,   KC.F11,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,      KC.TRNS,  KC.TRNS,  KC.TRNS,    KC.TRNS,  KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,      KC.LEFT,  KC.DOWN,  KC.UP,      KC.RGHT,  KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,      KC.TRNS,  KC.TRNS,  KC.TRNS,    KC.TRNS,  KC.TRNS,  KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,      KC.TRNS,  KC.TRNS,  KC.TRNS,
                                                KC.TRNS,  KC.TRNS,      KC.TRNS,  KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()

