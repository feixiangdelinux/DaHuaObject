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
    hwnd = op.FindWindow("", "书剑西游   八神庵 ID:98154")
    op.BindWindow(hwnd, 'gdi', 'normal', 'windows', 0)
    # op.SetDict(0, './pic/1.txt')
    op.MoveWindow(hwnd, 0, 0)
    # op.Capture(0, 0, 950, 670, '1.png')
    img = pyautogui.screenshot(region=[0, 0, 1024, 768])
    # img.save('./pic/1.png')
    img.save('1.png')
    # os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    # reader = easyocr.Reader(['ch_sim'], gpu=False)
    # str1 = reader.readtext(np.asarray(pyautogui.screenshot(region=[431, 224, 129, 22])))


