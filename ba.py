import json
import os
import time

import numpy as np
import pyautogui
from easyocr import easyocr
from pyopdll import OP




if __name__ == '__main__':
    print('开始')
    op = OP()
    # hwnd = op.FindWindow("", "书剑西游   八神庵 ID:98154")
    # hwnd = op.FindWindow("", "书剑西游   草薙京 ID:98155")
    hwnd = op.FindWindow("", "书剑西游   莉安娜 ID:98157")
    # hwnd = op.FindWindow("", "书剑西游   不知火舞 ID:98158")
    # hwnd = op.FindWindow("", "书剑西游   山崎龙二 ID:98160")
    op.BindWindow(hwnd, 'dx.d3d11', 'windows', 'windows', 1)
    op.MoveWindow(hwnd, 0, 0)
    # op.LeftClick
    op.MoveTo(175 , 370)
    op.RightClick()
