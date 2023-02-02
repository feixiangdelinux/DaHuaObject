import json
import os
import time

import numpy as np
import pyautogui
from easyocr import easyocr

if __name__ == '__main__':
    '''
    洗护身符
    '''
    print('开始')
    f = open('./1.txt', 'r', encoding="utf-8")
    aa = f.read()
    myClassReBuild = json.loads(aa)
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    reader = easyocr.Reader(['ch_sim'], gpu=False)
    str1 = reader.readtext(np.asarray(pyautogui.screenshot(region=[0, 0, 955, 695])))
    for i in str1:
        if '新炼化属性' == i[-2]:
            while True:
                str2 = reader.readtext(np.asarray(pyautogui.screenshot(region=[i[0][0][0] - 23, i[0][0][-1] + 30, 135, 180])))
                if len(str2) > 3:
                    # 敏魔强抽
                    length1 = 0
                    # 火仙
                    length2 = 0
                    # 风仙
                    length3 = 0
                    # 水仙
                    length4 = 0
                    # 雷仙
                    length5 = 0
                    # 沧波龙
                    length6 = 0
                    # 扶摇龙
                    length7 = 0
                    # 霹雳龙
                    length8 = 0
                    # 鬼火鬼
                    length9 = 0
                    # 回血鬼
                    length10 = 0
                    # 强冰人
                    length11 = 0
                    # 强混人
                    length12 = 0
                    # 强睡人
                    length13 = 0
                    # 强毒人
                    length14 = 0
                    # 附混
                    length15 = 0
                    for j in str2:
                        if j[-2] not in myClassReBuild:
                            myClassReBuild.append(j[-2])
                            str = json.dumps(myClassReBuild).encode('utf-8').decode('unicode_escape')
                            with open('./1.txt', 'w', encoding='utf-8') as f:
                                f.write(str)
                        if j[-2] in ['忽视抗震慑', '加强震慑_', '加强震慑', '强力克火']:
                            length1 = length1 + 1
                        if j[-2] in ['忽视抗火', '火法狂暴几率', '加强火', '强力克火', '火法狂暴几幸']:
                            length2 = length2 + 1
                        if j[-2] in ['忽视抗风', '风法狂暴几率', '加强风', '强力克火', '风法狂暴几幸']:
                            length3 = length3 + 1
                        if j[-2] in ['忽视抗水', '水法狂暴几率', '加强水', '强力克火', '水法狂暴几幸']:
                            length4 = length4 + 1
                        if j[-2] in ['忽视抗雷', '雷法狂暴几率', '加强雷', '强力克火', '雷法狂暴几幸']:
                            length5 = length5 + 1
                        if j[-2] in ['加强苍波效果', '强力克火']:
                            length6 = length6 + 1
                        if j[-2] in ['加强扶摇效果', '强力克火']:
                            length7 = length7 + 1
                        if j[-2] in ['加强霹雳效果', '强力克火']:
                            length8 = length8 + 1
                        if j[-2] in ['忽视抗鬼火', '鬼火狂暴几率', '鬼火狂暴程度', '加强鬼火', '强力克火']:
                            length9 = length9 + 1
                        if j[-2] in ['强三尸虫', '三尸虫狂暴程度', '加强三尸虫回血程', '三尸虫狂暴几率', '三尺虫狂暴程度', '加强二尸虫回血程', '强力克火']:
                            length10 = length10 + 1
                        if j[-2] in ['忽视抗封', '加强封印', '强力克火']:
                            length11 = length11 + 1
                        if j[-2] in ['忽视抗混', '加强混乱', '强力克火']:
                            length12 = length12 + 1
                        if j[-2] in ['忽视抗睡', '加强昏睡', '强力克火']:
                            length13 = length13 + 1
                        if j[-2] in ['强毒伤', '忽视抗中毒', '加强毒伤害', '强力克火']:
                            length14 = length14 + 1
                        if j[-2] in ['附加混乱攻击', '附加混乱击', '附加混乱斑击', '附加混乱;击', '附加混乱又击']:
                            length15 = length15 + 1
                    if length1 > 3 or length2 > 3 or length3 > 3 or length4 > 3 or length5 > 3 or length6 > 3 or length7 > 3 or length8 > 3 or length9 > 3 or length10 > 3 or length11 > 3 or length12 > 3 or length13 > 3 or length14 > 3 or length15 > 3:
                        print('大于两条')
                        break
                pyautogui.leftClick(x=451 + 120, y=163 - 20, duration=0.2)
                time.sleep(0.7)
    print('结束')
