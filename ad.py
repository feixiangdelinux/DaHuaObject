import json
import os
import time

import numpy as np
import pyautogui
from easyocr import easyocr
from pyopdll import OP

if __name__ == '__main__':
    print('开始')
    pyautogui.moveTo(175+(51*5), 393+(51*3))

    # img = pyautogui.screenshot(region=[0, 0, 955, 695])
    img = pyautogui.screenshot(region=[630, 439, 70, 18])
    img.save('1.png')
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    reader = easyocr.Reader(['ch_sim'], gpu=False)
    str1 = reader.readtext(np.asarray(pyautogui.screenshot(region=[630, 439, 70, 18])))
    for i in str1:
        print(i)

    # print('开始')
    # f = open('./2.txt', 'r', encoding="utf-8")
    # aa = f.read()
    # myClassReBuild = json.loads(aa)
    # os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    # reader = easyocr.Reader(['ch_sim'], gpu=False)
    # for k in range(2000):
    #     pyautogui.rightClick(175, 393, duration=0.1)
    #     time.sleep(0.2)
    #     str1 = reader.readtext(np.asarray(pyautogui.screenshot(region=[371, 329, 227, 31])))
    #     for i in str1:
    #         if '品' in i[-2]:
    #             if i[-2][-4:] not in myClassReBuild:
    #                 myClassReBuild.append(i[-2][-4:])
    #                 str = json.dumps(myClassReBuild).encode('utf-8').decode('unicode_escape')
    #                 with open('./2.txt', 'w', encoding='utf-8') as f:
    #                     f.write(str)
    # print('结束')

