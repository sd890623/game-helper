from windows import *
from images import *
from utils import wait
import guiUtils
import time
import random

class Task:
    exclamationRedPlayerType = "EXCLAMATIONREDPLAYERTYPE"
    minusRedPlayerType = "MINUSREDPLAYERTYPE"
    whitePlayerType = "WHITEPLAYERTYPE"

    hwnd = None
    simulatorInstance = None
    index = None
    def __init__(self, hwnd, index):
        self.hwnd = hwnd
        self.index = index
        hwndObject = getWindowHwndObjectById(hwnd)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"])

    def runTask(self):
        self.checkSafeForMinutes(0.1)
        self.print("回家")
        self.goHome()

    def print(self,text):
        print(str(self.index)+"号玩家： "+text)


    def findPlayerCountByType(self,type):
        count = 0
        iconWitdhHeight = 11
        playerTypeMarkImagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\"+type+".bmp")
        x,y = self.simulatorInstance.window_capture(playerTypeMarkImagePath, A=[5,463,167,489])
        countOcrArea = [x+iconWitdhHeight+3, y, x+iconWitdhHeight+1+14+15, y+iconWitdhHeight+5]
        countImageBlob = self.simulatorInstance.output_window_screenshot(A=countOcrArea)
        ocrCount = getOCRfromImageBlob(countImageBlob)
        try:
            if(len(ocrCount[0]) == 0):
                return 0
            count = int(ocrCount[0][0])
            return count
        except e:
            return 1

    def isPlayerInSite(self):
        leaveSiteImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\cloneCenter.bmp")
        minerImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\miner.bmp")
        cloneCenterX,y = self.simulatorInstance.window_capture(leaveSiteImgPath, A=[910,385,988,477])
        minerX,y = self.simulatorInstance.window_capture(minerImgPath, A=[927,525,996,593])

        if (cloneCenterX and not(minerX)):
            return True
        elif (minerX and not(cloneCenterX)):
            return False

    def startMiningTask(self):
        self.print("新一轮开始了")
        time.sleep(20+random.randint(0,25))
        if(not(self.isSafe())):
            self.print("有海盗，蹲站")
            return
        self.print("开始存货")
        self.stockOre()
        self.print("存货完毕")
        time.sleep(10)
        if(self.isSafe()):
            self.print("安全，出发")
            self.goOut()
            self.print("到达，开采")
        else:
            self.print("有海盗，蹲站")
            return
        self.print("采矿等待中")
        self.checkSafeForMinutes(13.2)
        self.print("回家")
        self.goHome()
        self.print("到家")

    def stockOre(self):
        wait(lambda: self.simulatorInstance.click_keyboard("B"), 7)
        wait(lambda: self.simulatorInstance.click_point(86,430,True), 4)
        wait(lambda: self.simulatorInstance.click_keyboard("E"), 2)
        wait(lambda: self.simulatorInstance.click_point(98,129,True), 2)
        wait(lambda: self.simulatorInstance.click_point(380,136,True), 7)
        wait(lambda: self.simulatorInstance.click_point(961,31), 2)
        wait(lambda: self.simulatorInstance.click_point(961,31), 2)

    def isSafe(self):
        return self.findPlayerCountByType(self.exclamationRedPlayerType) < 1 and self.findPlayerCountByType(self.minusRedPlayerType) < 1 and self.findPlayerCountByType(self.whitePlayerType) < 1
    
    def checkSafeForMinutes(self, mins):
        frequency = 10
        totalSeconds = mins*60
        while(self.isSafe() and totalSeconds > 0):
            time.sleep(frequency)
            totalSeconds -= frequency


    def goOut(self):
        oreSiteCalibrater = random.randint(-70,70)
        wait(lambda: self.simulatorInstance.click_point(875,180,True), 5)
        while(self.isPlayerInSite()):
            time.sleep(5)
        time.sleep(15)
        wait(lambda: self.simulatorInstance.click_point(961,350))
        wait(lambda: self.simulatorInstance.click_point(928,19,True))
        wait(lambda: self.simulatorInstance.click_point(878,376))
        self.print("点矿区y偏移量："+str(oreSiteCalibrater))
        wait(lambda: self.simulatorInstance.click_point(891,172+oreSiteCalibrater))
        wait(lambda: self.simulatorInstance.click_point(685,237+oreSiteCalibrater))
        #点平衡器
        wait(lambda: self.simulatorInstance.click_keyboard("4"), 45)
        #上滑至顶
        times = 25
        #todo solve foreground scroll 
        #while(times>0):
        #    wait(lambda: self.simulatorInstance.mouseWheel((893,121), "up"),1)
        #    times=times-1

        wait(lambda: self.simulatorInstance.click_point(898,121,True))
        wait(lambda: self.simulatorInstance.click_point(703,186,True))
        wait(lambda: self.simulatorInstance.click_keyboard("q"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("r"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("t"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("y"), 1)

    def goHome(self):
        wait(lambda: self.simulatorInstance.click_keyboard("`"),6)

        homeRouteImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\homeRoute.bmp")
        homeRouteImgX,homeRouteImgY = self.simulatorInstance.window_capture(homeRouteImgPath, A=[0,203,178,601])
        wait(lambda: self.simulatorInstance.click_point(homeRouteImgX+168,homeRouteImgY+6),4)
        wait(lambda: self.simulatorInstance.click_keyboard("4"), 6)
        wait(lambda: self.simulatorInstance.click_point(206,182))

        while(not(self.isPlayerInSite())):
             time.sleep(5)

        







        




    def clickOnTestPic(self):
        targetImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\greenStars.bmp")
        screenshotImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\screenshots\\"+str(self.index)+"\\players.bmp")

        #x,y = self.simulatorInstance.window_capture(targetImgPath, A=[0,325,194,598])
    
