import json
import os
import time

import numpy as np
import pyautogui
from easyocr import easyocr
from pyopdll import OP




if __name__ == '__main__':
    print('开始')
    # img = pyautogui.screenshot(region=[0, 0, 955, 695])
    # img.save('./pic/1.png')
    # img.save('1.png')
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    reader = easyocr.Reader(['ch_sim'], gpu=False)
    str1 = reader.readtext(np.asarray(pyautogui.screenshot(region=[0, 0, 955, 695])))
    for i in str1:
        print(i)



