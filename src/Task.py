from windows import *
from images import *
from utils import *
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
    syncBetweenUsers = True
    def __init__(self, hwnd, index):
        self.hwnd = hwnd
        self.index = index
        hwndObject = getWindowHwndObjectById(hwnd)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"])

    def runTask(self):
        count = 1
        playerTypeMarkImagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\"+self.exclamationRedPlayerType+".bmp")
        while(count>0):
            x,y = self.simulatorInstance.window_capture(playerTypeMarkImagePath, A=[5,463,167,489])
            print(str(count)+" times and x="+str(x))
            time.sleep(0.1)
            count+=1
    
    def closeWindow(self):
        wait(lambda: self.simulatorInstance.click_point(76,32))
        wait(lambda: self.simulatorInstance.click_point(537,488))
        wait(lambda: self.simulatorInstance.click_keyboard("t"),30)

    def print(self,text):
        print(getDateTimeString()+" "+ str(self.index)+"号玩家： "+text)


    def findPlayerCountByType(self,type):
        count = 0
        iconWitdhHeight = 11
        playerTypeMarkImagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\"+type+".bmp")
        findPlayerCountLk.acquire()
        try:
            x,y = self.simulatorInstance.window_capture(playerTypeMarkImagePath, A=[5,463,167,489])
        except:
            findPlayerCountLk.release()
            raise Exception("error")
        if(x == 0 and y == 0):
            self.print("没打开人物列表？")
            return 0
        countOcrArea = [x+iconWitdhHeight+3, y, x+iconWitdhHeight+1+14+15, y+iconWitdhHeight+5]
        countImageBlob = self.simulatorInstance.output_window_screenshot(A=countOcrArea)
        ocrCount = getOCRfromImageBlob(countImageBlob)
        findPlayerCountLk.release()

        try:
            if(len(ocrCount[0]) == 0):
                return 0
            count = int(ocrCount[0][0])
            return count
        except:
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
        else:
            return True
        

    def startMiningTask(self):
        if (self.syncBetweenUsers):
            self.print("账号差异化，等待x*60s")
            time.sleep(60*self.index)
            self.syncBetweenUsers = not(self.syncBetweenUsers)
        self.print("新一轮开始了")
        if(not(self.isSafe())):
            self.print("有海盗，蹲站")
            time.sleep(60+random.randint(0,5))
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
        time.sleep(30+random.randint(0,10))



    def stockOre(self):
        wait(lambda: self.simulatorInstance.click_keyboard("B"), 15)
        wait(lambda: self.simulatorInstance.click_point(86,430,True), 8)
        wait(lambda: self.simulatorInstance.click_keyboard("E"), 4)
        wait(lambda: self.simulatorInstance.click_point(98,129,True), 9)
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
        if(self.isSafe()==False):
            self.syncBetweenUsers = True


    def goOut(self):
        oreSiteCalibrater = random.randint(-70,70)
        wait(lambda: self.simulatorInstance.click_point(875,180,True), 5)
        while(self.isPlayerInSite()):
            time.sleep(5)
        time.sleep(25)
        wait(lambda: self.simulatorInstance.click_point(961,350))
        wait(lambda: self.simulatorInstance.click_point(847,17,True))
        wait(lambda: self.simulatorInstance.click_point(878,376))
        self.print("点矿区y偏移量："+str(oreSiteCalibrater))
        wait(lambda: self.simulatorInstance.click_point(891,172+oreSiteCalibrater))
        wait(lambda: self.simulatorInstance.click_point(685,237+oreSiteCalibrater))
        #点平衡器
        wait(lambda: self.simulatorInstance.click_keyboard("4"), 55)
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
        homeRouteImgX,homeRouteImgY = self.simulatorInstance.window_capture(homeRouteImgPath, A=[0,201,179,556])
        self.print("回家点击："+ str(homeRouteImgX+168) +", "+ str(homeRouteImgY+10))
        wait(lambda: self.simulatorInstance.click_point(homeRouteImgX+168,homeRouteImgY+10),4)
        wait(lambda: self.simulatorInstance.click_keyboard("4"), 6)
        wait(lambda: self.simulatorInstance.click_point(206,182))

        while(not(self.isPlayerInSite())):
             time.sleep(5)


    def passOre(self):
        if(not(self.isSafe())):
            self.print("有海盗，蹲站")
            time.sleep(30)
            return
        wait(lambda: self.simulatorInstance.click_point(875,180,True), 5)
        while(self.isPlayerInSite()):
            time.sleep(5)
        time.sleep(15)
        wait(lambda: self.simulatorInstance.click_keyboard("`"),6)
        wait(lambda: self.simulatorInstance.click_point(131,186),4)
        wait(lambda: self.simulatorInstance.click_point(204,231),4)
        time.sleep(15)
        while(not(self.isPlayerInSite())):
             time.sleep(5)
        time.sleep(15)

        wait(lambda: self.simulatorInstance.click_keyboard("b"),8)

        wait(lambda: self.simulatorInstance.click_point(102,147),4)

        wait(lambda: self.simulatorInstance.click_point(505,138))
        wait(lambda: self.simulatorInstance.click_point(905,93))
        wait(lambda: self.simulatorInstance.click_point(965,141))
        wait(lambda: self.simulatorInstance.click_point(903,70))
        wait(lambda: self.simulatorInstance.click_point(967,245),4)
        wait(lambda: self.simulatorInstance.click_keyboard("5"),4)
        
        wait(lambda: self.simulatorInstance.click_point(961,31))
        wait(lambda: self.simulatorInstance.click_point(961,31))
        wait(lambda: self.simulatorInstance.click_point(961,31))
        wait(lambda: self.simulatorInstance.click_point(961,31))
        wait(lambda: self.simulatorInstance.click_point(961,31))
        wait(lambda: self.simulatorInstance.click_point(961,31))
        wait(lambda: self.simulatorInstance.click_point(961,31))


        wait(lambda: self.simulatorInstance.click_keyboard("`"),6)
        wait(lambda: self.simulatorInstance.click_point(131,186))
        wait(lambda: self.simulatorInstance.click_point(204,355),5)
        wait(lambda: self.simulatorInstance.click_point(915,456))

        time.sleep(15)
        while(not(self.isPlayerInSite())):
             time.sleep(5)
        time.sleep(15)

        self.stockOre()
        time.sleep(10)



        







        




    def clickOnTestPic(self):
        targetImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\greenStars.bmp")
        screenshotImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\screenshots\\"+str(self.index)+"\\players.bmp")

        #x,y = self.simulatorInstance.window_capture(targetImgPath, A=[0,325,194,598])
    
