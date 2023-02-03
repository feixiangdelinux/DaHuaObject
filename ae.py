import json
import os
import time

import numpy as np
import pyautogui
from easyocr import easyocr

if __name__ == '__main__':
    '''
    把炼化的属性保存到2.txt中
    '''
    print('开始')
    # 护身符炼化属性表
    # file = './1.txt'
    # 仙器武器炼化属性表
    # file = './2.txt'
    # 仙器衣服炼化属性表
    file = './3.txt'
    f = open(file, 'r', encoding="utf-8")
    aa = f.read()
    myClassReBuild = json.loads(aa)
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    reader = easyocr.Reader(['ch_sim'], gpu=False)
    str1 = reader.readtext(np.asarray(pyautogui.screenshot(region=[0, 0, 955, 695])))
    for i in str1:
        if '新炼化属性' == i[-2]:
            for k in range(500):
                str2 = reader.readtext(np.asarray(pyautogui.screenshot(region=[i[0][0][0] - 23, i[0][0][-1] + 30, 135, 180])))
                for j in str2:
                    if j[-2] not in myClassReBuild:
                        myClassReBuild.append(j[-2])
                        json_str = json.dumps(myClassReBuild).encode('utf-8').decode('unicode_escape')
                        with open(file, 'w', encoding='utf-8') as f:
                            f.write(json_str)
                pyautogui.leftClick(x=i[0][0][0] + 120, y=i[0][0][-1] - 20, duration=0.2)
                time.sleep(1)
    print('结束')
