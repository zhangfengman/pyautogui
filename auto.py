#-- coding:UTF-8 --
import pyautogui
from pywinauto.application import Application
import time
import cv2
import os
import pyperclip
import sys
def imgAutoCick(tempFile, whatDo, debug = False):
    pyautogui.screenshot('big.png') 
    # 读入背景图片
    gray = cv2.imread("big.png", 0)
    # 读入需要查找的图片 
    img_template = cv2.imread(tempFile, 0)
    # 得到图片的高和宽 
    w, h = img_template.shape[::-1]
    # 模板匹配操作 
    res = cv2.matchTemplate(gray, img_template, cv2.TM_SQDIFF)
    # 得到最大和最小值得位置 
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) 
    top = min_loc[0] 
    left = min_loc[1] 
    x = [top, left, w, h] 
    top_left = min_loc
    # 左上角的位置 
    bottom_right = (top_left[0] + w, top_left[1] + h)
    # 右下角的位# 先移动再操作， 进行点击动作， 可以修改为其他动作 
    pyautogui.moveTo(top + h / 2, left + w / 2) 
    print(x)
    whatDo(x) 
    '''
    if debug: 
        #读取原图 
        img = cv2.imread("big.png", 1)
        # 在原图上画矩形 
        cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
        # 调试显示 
        img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5, interpolation = cv2.INTER_NEAREST) 
        cv2.imshow("processed", img) 
        cv2.waitKey(0)
        # 销毁所有窗口 
        cv2.destroyAllWindows() 
        os.remove("big.png") 
    '''

app = Application(backend="uia").start(r'C:\Program Files (x86)\WXWork\WXWork.exe')
time.sleep(1)
path = sys.path[0]
# 点击联系人
imgAutoCick(path+'/search/1_lxr.png',pyautogui.click,True)
time.sleep(0.5)
# 打开视频号
imgAutoCick(path+'/search/2_sph.png',pyautogui.doubleClick,True)
time.sleep(3)
# 打开debug
imgAutoCick(path+'/search/3_dz.png',pyautogui.rightClick,True)
time.sleep(0.5)
curX,curY = pyautogui.position()
pyautogui.moveTo(curX+40,curY+10,0.2)
time.sleep(0.2)
pyautogui.click(curX+40,curY+10) 
# 选择console
time.sleep(1)
imgAutoCick(path+'/search/4_console.png',pyautogui.rightClick,True)

# 粘贴脚本
fd = open('docookie-min.js','r')
jstext = fd.read()
print(jstext)
pyperclip.copy(jstext)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')