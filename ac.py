import pyautogui

if __name__ == '__main__':
    """
    清理当前物品栏
    """
    print('开始')
    for x in range(6):
        for y in range(4):
            pyautogui.leftClick(175 + (51 * x), 393 + (51 * y), duration=0.1)
            pyautogui.leftClick(x=539, y=315, duration=0.1)
            pyautogui.leftClick(x=430, y=240, duration=0.12)
    print('结束')
