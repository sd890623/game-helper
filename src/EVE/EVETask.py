from windows import *
from images import *
from utils import *
import guiUtils
import time
import random

class EVETask:
    exclamationRedPlayerType = "EXCLAMATIONREDPLAYERTYPE"
    minusRedPlayerType = "MINUSREDPLAYERTYPE"
    whitePlayerType = "WHITEPLAYERTYPE"

    hwnd = None
    simulatorInstance = None
    index = None
    syncBetweenUsers = True
    homeNameArea=[1038,137,1102,157]
    def __init__(self, hwnd, index,childTitle):
        self.hwnd = hwnd
        self.index = index
        childHwndObj=getChildHwndByTitleAndParentHwnd(childTitle,hwnd)
        self.simulatorInstance = guiUtils.win(childHwndObj["hwnd"], bor= True)

    def testTask(self):
        times = 2
        #todo solve foreground scroll 
        while(times>0):
           wait(lambda: self.simulatorInstance.mouseWheel((1263,213), "up"),1)
           times=times-1
        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(64,39),20,1)
    
    def closeWindow(self):
        wait(lambda: self.simulatorInstance.click_point(44,26))
        wait(lambda: self.simulatorInstance.click_point(531,481))
        wait(lambda: self.simulatorInstance.click_keyboard("t"),30)

    def print(self,text):
        print(getDateTimeString()+" "+ str(self.index)+"号玩家： "+text)

    def findPlayerCountByType(self,type):
        count = 0
        playerTypeMarkImagePath = os.path.abspath(__file__ + "\\..\\..\\..\\assets\\clickOns\\"+type+".bmp")
        
        try:
            findPlayerCountLk.acquire()
            x,y = self.simulatorInstance.window_capture(playerTypeMarkImagePath, A=[6,562,205,584])
            countOcrArea = [x+18, y-4, x+33, y+18]
            countImageBlob = self.simulatorInstance.output_window_screenshot(A=countOcrArea)
            # self.saveImageToFile(countImageBlob)
            ocrCount = getOCRfromImageBlob(countImageBlob,2)
            # print(ocrCount)
            findPlayerCountLk.release()
        except Exception as e:
            findPlayerCountLk.release()
            raise e  

        if(x == 0 and y == 0):
            self.print("没打开人物列表？")
            return 1

        try:
            if(len(ocrCount[0]) == 0):
                return 0
            count = int(ocrCount[0][0])
            return count
        except Exception as e:
            print(e)
            return 1

    def hasSingleLineWordsInArea(self, words, A=[0,0,0,0], ocrType=3):
        try:
            screenshotBlob = self.simulatorInstance.output_window_screenshot(A)
            # self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if(len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])
            
            self.print(words +" in "+ str)
            return words in str.lower()
        except Exception as e:
            print(e)    
            return False      

    def isPlayerInSite(self):
        inCenter=self.hasSingleLineWordsInArea("b32-14",A=self.homeNameArea)
        minerImgPath = os.path.abspath(__file__ + "\\..\\..\\..\\assets\\clickOns\\miner.bmp")
        minerX,y = self.simulatorInstance.window_capture(minerImgPath, A=[808,608,878,678])

        if (inCenter):
            self.print("in")
            return "in"
        elif (minerX and not(inCenter)):
            self.print("out")
            return "out"
        else:
            return "middle"
        
    def checkEnemy(self):
        if(not(self.isSafe())):
            self.print("回家")
            self.goHome()
        time.sleep(7)
    def startMiningTask(self):
        if (self.syncBetweenUsers):
            self.print("账号差异化，等待x*60s")
            time.sleep(90*self.index)
            self.syncBetweenUsers = not(self.syncBetweenUsers)
        self.print("新一轮开始了")
        if(not(self.isSafe())):
            self.print("有海盗，蹲站")
            time.sleep(30+random.randint(0,5))
            return
        self.print("开始存货")
        self.stockOre()
        self.print("存货完毕")
        time.sleep(10)
        while(True):
            if(self.isSafe()):
                self.print("安全，出发")
                self.goOut()
                self.print("到达，开采")
                break
            else:
                self.print("有海盗，蹲站")
                time.sleep(30+random.randint(0,5))
                continue
        self.print("采矿等待中")
        self.checkSafeForMinutes(11.2+random.randint(0,10)/10)
        self.print("回家")
        self.goHome()
        self.print("到家")
        time.sleep(30+random.randint(0,30))

    def w(self,sec=2):
        time.sleep(sec+random.random()*0.5)
    def stockOre(self):
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_keyboard("B"), lambda: self.hasSingleLineWordsInArea("x",A=[1183,23,1217,56]),timeout=15)
        self.w(4)
        wait(lambda: self.simulatorInstance.click_point(118,533), 10)
        wait(lambda: self.simulatorInstance.click_keyboard("2"), 7)
        wait(lambda: self.simulatorInstance.click_point(174,153,True), 9)
        wait(lambda: self.simulatorInstance.click_point(376,154,True), 7)
        continueWithUntilBy(lambda: self.simulatorInstance.click_point(1198,33), lambda: self.hasSingleLineWordsInArea("b32-14",A=self.homeNameArea))
        self.w()

    def isSafe(self):
        return self.findPlayerCountByType(self.exclamationRedPlayerType) < 1 and self.findPlayerCountByType(self.minusRedPlayerType) < 1 and self.findPlayerCountByType(self.whitePlayerType) < 1
    
    def checkSafeForMinutes(self, mins):
        frequency = 10
        totalSeconds = mins*60
        # count=0
        while(self.isSafe() and totalSeconds > 0):
            time.sleep(frequency)
            totalSeconds -= frequency
            #self.print("count:"+str(count))
            #count+=1
        if(self.isSafe()==False):
            self.syncBetweenUsers = True

    def goOut(self):
        minerYDiff=44
        oreSiteCalibrater = random.randint(-2,2)
        wait(lambda: self.simulatorInstance.click_point(1075,226,True), 5)
        while(self.isPlayerInSite() == "in" or self.isPlayerInSite() == "middle"):
            time.sleep(5)
        time.sleep(10)
        wait(lambda: self.simulatorInstance.click_point(1197,394),4)
        wait(lambda: self.simulatorInstance.click_point(1048,21,True),4)
        wait(lambda: self.simulatorInstance.click_point(1051,466),4)
        self.print("点矿区y偏移量:"+str(oreSiteCalibrater))
        wait(lambda: self.simulatorInstance.click_point(1055,220+oreSiteCalibrater*minerYDiff),4)
        wait(lambda: self.simulatorInstance.click_point(819,299+oreSiteCalibrater*minerYDiff,4))
        #点平衡器
        wait(lambda: self.simulatorInstance.click_keyboard("4"), 5)

        duration = 40+random.randint(0,5)
        while(self.isSafe() and duration > 0):
            time.sleep(5)
            duration -= 5
        if(self.isSafe()==False):
            self.syncBetweenUsers = True
            return
        
        #上滑至顶
        times = 4
        #todo solve foreground scroll 
        # while(times>0):
        #    wait(lambda: self.simulatorInstance.mouseWheel((1357,190), "up"),2)
        #    times=times-1
        wait(lambda: self.simulatorInstance.click_point(896,389,True))
        wait(lambda: self.simulatorInstance.click_point(1197,394),4)


        wait(lambda: self.simulatorInstance.click_point(1051,219,True),2)
        wait(lambda: self.simulatorInstance.click_point(814,300,True),2)
        wait(lambda: self.simulatorInstance.click_point(896,389,True))

        wait(lambda: self.simulatorInstance.click_keyboard("1"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("2"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("3"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("W"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("E"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("6"), 1)


    def goHome(self):
        wait(lambda: self.simulatorInstance.click_keyboard("`"),4)

        # homeRouteImgPath = os.path.abspath(__file__ + "\\..\\..\\..\\assets\\clickOns\\homeRoute.bmp")
        # homeRouteImgPath2 = os.path.abspath(__file__ + "\\..\\..\\..\\assets\\clickOns\\homeRoute2.bmp")

        # homeRouteImgX,homeRouteImgY = self.simulatorInstance.window_capture(homeRouteImgPath, A=[26,225,167,526])
        # if(homeRouteImgX==0 or homeRouteImgY==0):
        #     homeRouteImgX,homeRouteImgY = self.simulatorInstance.window_capture(homeRouteImgPath2, A=[26,221,171,531])
        
        # self.print("回家点击："+ str(homeRouteImgX+168) +", "+ str(homeRouteImgY+13))
        # wait(lambda: self.simulatorInstance.click_point(homeRouteImgX+168,homeRouteImgY+10),4)
        wait(lambda: self.simulatorInstance.click_point(245,599),4)
        wait(lambda: self.simulatorInstance.click_keyboard("4"),2)
        wait(lambda: self.simulatorInstance.click_keyboard("5"), 2)

        while(self.isPlayerInSite() == "out" or self.isPlayerInSite() == "middle"):
             time.sleep(5)
        time.sleep(10)

    def passOre(self):
        if(not(self.isSafe())):
            self.print("有海盗，蹲站")
            time.sleep(30)
            return
        wait(lambda: self.simulatorInstance.click_point(875,180,True), 5)
        while(self.isPlayerInSite() == "in" or self.isPlayerInSite() == "middle"):
            time.sleep(5)
        time.sleep(15)
        wait(lambda: self.simulatorInstance.click_keyboard("`"),6)
        wait(lambda: self.simulatorInstance.click_point(131,186),4)
        wait(lambda: self.simulatorInstance.click_point(204,231),4)
        time.sleep(15)
        while(self.isPlayerInSite() == "out" or self.isPlayerInSite() == "middle"):
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
        while(self.isPlayerInSite() == "out" or self.isPlayerInSite() == "middle"):
             time.sleep(5)
        time.sleep(15)

        self.stockOre()
        time.sleep(10)


    def saveImageToFile(self,imageBlob):
        screenshotImgPath = os.path.abspath(__file__ + "\\..\\..\\..\\assets\\screenshots\\"+str(self.index)+"\\players.bmp")
        cv2.imwrite(screenshotImgPath, imageBlob)  


    def clickOnTestPic(self):
        targetImgPath = os.path.abspath(__file__ + "\\..\\..\\..\\assets\\clickOns\\greenStars.bmp")
        screenshotImgPath = os.path.abspath(__file__ + "\\..\\..\\..\\assets\\screenshots\\"+str(self.index)+"\\players.bmp")

        #x,y = self.simulatorInstance.window_capture(targetImgPath, A=[0,325,194,598])
    
