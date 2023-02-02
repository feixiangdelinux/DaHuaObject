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
    # os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    # reader = easyocr.Reader(['ch_sim'], gpu=False)
    # str1 = reader.readtext(np.asarray(pyautogui.screenshot(region=[0, 0, 955, 695])))
    # for i in str1:
    #     if '新炼化属性' == i[-2]:
    #         # pyautogui.moveTo()
    #         print(i)
    #         print(i[0][0])
    #         print(i[0][0][0])
    #         print(i[0][0][-1])


    img = pyautogui.screenshot(region=[451-23, 163+30, 135, 180])
    img.save('1.png')
