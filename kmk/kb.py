import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import SplitSide
from digitalio import DigitalInOut, Direction

sided_pin = DigitalInOut(board.GP7)
sided_pin.direction = Direction.INPUT

class KMKKeyboard(_KMKKeyboard):
    debug_enabled = False
    col_pins = (
        board.GP20, 
        board.GP21, 
        board.GP22, 
        board.GP26, 
        board.GP27, 
        board.GP28
    )
    row_pins = (
        board.GP2, 
        board.GP3, 
        board.GP4, 
        board.GP5, 
        board.GP6
    )
    diode_orientation = DiodeOrientation.ROW2COL
    data_pin = board.GP1
    data_pin2 = board.GP0
    side = SplitSide.LEFT if sided_pin.value else SplitSide.RIGHT

    coord_mapping = [
         0,  1,  2,  3,  4,  5,   35, 34, 33, 32, 31, 30,
         6,  7,  8,  9, 10, 11,   41, 40, 39, 38, 37, 36,
        12, 13, 14, 15, 16, 17,   47, 46, 45, 44, 43, 42,
        18, 19, 20, 21, 22, 23,   53, 52, 51, 50, 49, 48,
                    27, 28, 25,   55, 58, 57, 
                        29, 26,   56, 59
    ]
