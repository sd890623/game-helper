from windows import *
from images import *
from utils import *
# from EveRunner import Runner
import guiUtils
import time
import random
import multiprocessing
import math

class EVETask:
    exclamationRedPlayerType = "EXCLAMATIONREDPLAYERTYPE"
    minusRedPlayerType = "MINUSREDPLAYERTYPE"
    whitePlayerType = "WHITEPLAYERTYPE"
    lastOreSiteCalibrater=0
    inSite=True

    hwnd = None
    simulatorInstance = None
    index = None
    syncBetweenUsers = True
    homeNameArea = [1038, 137, 1102, 157]
    stellarisArea=[109,14,245,46]
    closeFilterBtn=896,383
    openFilterBtn=1197, 394
    toggleFilterCategoryBtn=1048, 21

    def __init__(self, hwnd, index, childTitle="MuMuPlayer",eveRunners=[multiprocessing.Event(),multiprocessing.Queue()],mode=0):
        self.hwnd = hwnd
        self.index = index
        self.pauseEvent = eveRunners[0]
        self.queue=eveRunners[1]
        self.mode=mode
        childHwndObj = getChildHwndByTitleAndParentHwnd(childTitle, hwnd)
        self.simulatorInstance = guiUtils.win(childHwndObj["hwnd"], bor=True)

    def setInsite(self,val):
        self.inSite=val

    def testTask(self):
        self.isSafe()
        times = 1
        # todo solve foreground scroll
        while times > 0:
            # battle starts from 2nd one
            wait(lambda: self.simulatorInstance.click_point(1017,93))
            self.simulatorInstance.moveClickAndDrag((822,161),'up',150)
            times = times - 1
        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(64, 39), 20, 1)
    
    # a method to pause the process listening to self.statusObj
    def pause(self):
        while self.pauseEvent.is_set():
            time.sleep(1)

    def closeWindow(self):
        wait(lambda: self.simulatorInstance.click_point(44, 26))
        wait(lambda: self.simulatorInstance.click_point(531, 481))
        wait(lambda: self.simulatorInstance.click_keyboard("t"), 30)

    def print(self, text):
        self.queue.put(str(self.index) + "号玩家： " + text)
        print(getDateTimeString() + " " + str(self.index) + "号玩家： " + text)

    def findPlayerCountByType(self, type):
        count = 0
        playerTypeMarkImagePath = os.path.abspath(
            __file__ + "\\..\\..\\..\\assets\\clickOns\\" + type + ".bmp"
        )

        try:
            findPlayerCountLk.acquire()
            x, y = self.simulatorInstance.window_capture(
                playerTypeMarkImagePath, A=[4,555,214,580]
            )
            countOcrArea = [x + 18, y - 4, x + 33, y + 18]
            countImageBlob = self.simulatorInstance.output_window_screenshot(
                A=countOcrArea
            )
            # self.saveImageToFile(countImageBlob)
            ocrCount = getOCRfromImageBlob(countImageBlob, 2)
            # print(ocrCount)
            findPlayerCountLk.release()
        except Exception as e:
            findPlayerCountLk.release()
            raise e

        if x == 0 and y == 0:
            self.print("没打开人物列表？")
            return 1

        try:
            if len(ocrCount[0]) == 0:
                return 1
            count = int(ocrCount[0][0])
            return count
        except Exception as e:
            print(e)
            return 1

    def hasSingleLineWordsInArea(self, words, A, ocrType=3,debug=False):
        try:
            screenshotBlob = self.simulatorInstance.output_window_screenshot(A)
            if(debug):
                self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if len(ocrObj[0]) == 0:
                return False
            str = "".join(ocrObj[0])

            self.print(words + " in " + str)
            return words in str.lower()
        except Exception as e:
            print(e)
            return False
        
    def haveWords(self,A,ocrType=3):
        try:
            screenshotBlob = self.simulatorInstance.output_window_screenshot(A)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if len(ocrObj[0]) > 2 and '。' not in ocrObj[0] and ',' not in ocrObj[0] and '"' not in ocrObj[0]:
                str = "".join(ocrObj[0])
                self.print("ocr: "+str)
                return True
            return False
        except Exception as e:
            print(e)
            return False
        
    def getNumberFromSingleLineInArea(self, A=[0, 0, 0, 0], debug=False):
        try:
            screenshotBlob = self.simulatorInstance.output_window_screenshot(A)
            if (debug == True):
                self.saveImageToFile(screenshotBlob)
            num= getNumberfromImageBlob(screenshotBlob)
            if(num is None):
                return 0
            return num
        except Exception as e:
            print("fail to get number")
            return 0

    def isPositionColorSimilarTo(self, x, y, rgb):
        try:
            positionRGB = self.simulatorInstance.getColorV1(x, y)
            if (not (positionRGB)):
                return False
            d = math.sqrt((positionRGB[0] - rgb[0]) ** 2 +
                        (positionRGB[1] - rgb[1]) ** 2 + (positionRGB[2] - rgb[2]) ** 2)
            if (d < 20):
                return True
            else:
                return False
        except Exception as e:
            print("fail to get number")
            return False
        
    def isPlayerInSite(self):
        inCenter = self.hasSingleLineWordsInArea("活动", [1064,387,1116,421],4)
        isOut = self.getNumberFromSingleLineInArea([525,636,559,653])==100

        if inCenter:
            self.print("in")
            return "in"
        elif isOut and not(inCenter):
            self.print("out")
            return "out"
        else:
            return "middle"

    def goToStella(self,name,waitTime=40):
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.click_point(183,30),
            lambda: self.hasSingleLineWordsInArea("x", [1185,22,1213,54])
        )
        self.w(4)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.click_point(69,463),
            lambda: self.hasSingleLineWordsInArea("x", [423,70,452,98])
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.click_point(157,142),
            lambda: self.hasSingleLineWordsInArea("x", [1187,11,1222,52])
        )
        wait(lambda: self.simulatorInstance.click_point(224,28), 1)
        wait(lambda: self.simulatorInstance.typeWriteV1("9ke"),1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.click_point(1059,28),
            lambda: self.hasSingleLineWordsInArea("x", [423,70,452,98]),
            frequency=10
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.click_point(165,278),
            lambda: self.hasSingleLineWordsInArea(name, [1014,387,1112,413])
        )
        wait(lambda: self.simulatorInstance.click_point(1124,461))
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.click_point(1201,34),
            lambda: not self.hasSingleLineWordsInArea("x", [423,70,452,98])
        )
        def clickGo():
            wait(lambda: self.simulatorInstance.click_point(26,189))
            if(self.hasSingleLineWordsInArea("导航确认",[882,334,972,372],4)):
                wait(lambda: self.simulatorInstance.click_point(1135,536),10)
            if(self.hasSingleLineWordsInArea("保险提醒",[880,337,972,367],4)):
                wait(lambda: self.simulatorInstance.click_point(1135,536),10)
        doAndWaitUntilBy(clickGo,lambda: self.hasSingleLineWordsInArea(name, A=self.stellarisArea),waitTime,timeout=15)


    def checkEnemy(self):
        while True:
            if not self.isSafe():
                self.print("敌对，回站")
                time.sleep(2)
                self.goHome()
                self.pause()
            self.print("安全")
            self.pause()
            time.sleep(7)

    def w(self, sec=2):
        time.sleep(sec + random.random() * 0.5)

    def stockOre(self):
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.click_point(28,118),
            lambda: self.hasSingleLineWordsInArea("仓库", [138,23,213,70],4),
            timeout=15,
        )
        self.w(2)
        wait(lambda: self.simulatorInstance.click_point(118,533), 10)
        wait(lambda: self.simulatorInstance.click_point(924,644), 7)
        wait(lambda: self.simulatorInstance.click_point(174, 153, True), 9)
        wait(lambda: self.simulatorInstance.click_point(376, 154, True), 7)
        continueWithUntilBy(
            lambda: self.simulatorInstance.click_point(1198, 33),
            lambda: self.hasSingleLineWordsInArea("离站", A=[1144,208,1221,255],ocrType=4),
        )
        self.w()

    def isSafe(self):
        return (
            self.findPlayerCountByType(self.exclamationRedPlayerType) < 1
            and self.findPlayerCountByType(self.minusRedPlayerType) < 1
            and self.findPlayerCountByType(self.whitePlayerType) < 1
        )

    def checkSafeForMinutes(self, mins):
        frequency = 10
        totalSeconds = mins * 60
        # count=0
        while self.isSafe() and totalSeconds > 0:
            time.sleep(frequency)
            totalSeconds -= frequency
            # self.print("count:"+str(count))
            # count+=1
        if self.isSafe() == False:
            self.syncBetweenUsers = True

    def goHome(self,waitTime=60):
        def triggerGoHome():
            def backup():
                if self.hasSingleLineWordsInArea("x", A=[1186, 23, 1212, 55]):
                    doAndWaitUntilBy(
                        lambda: self.simulatorInstance.click_point(1199, 35),
                        lambda: not self.hasSingleLineWordsInArea(
                            "x", A=[1186, 23, 1212, 55]
                        ),
                    )
                wait(lambda: self.simulatorInstance.click_point(13,187))
            backup()
            if(self.mode!=2):
                doAndWaitUntilBy(
                    lambda: self.simulatorInstance.click_point(13,187),
                    lambda: self.hasSingleLineWordsInArea("x", A=[229,230,258,260]),
                    1,
                    1,
                    backupFunc=backup,
                    timeout=15
                )

            # homeRouteImgPath = os.path.abspath(__file__ + "\\..\\..\\..\\assets\\clickOns\\homeRoute.bmp")
            # homeRouteImgPath2 = os.path.abspath(__file__ + "\\..\\..\\..\\assets\\clickOns\\homeRoute2.bmp")

            # homeRouteImgX,homeRouteImgY = self.simulatorInstance.window_capture(homeRouteImgPath, A=[26,225,167,526])
            # if(homeRouteImgX==0 or homeRouteImgY==0):
            #     homeRouteImgX,homeRouteImgY = self.simulatorInstance.window_capture(homeRouteImgPath2, A=[26,221,171,531])

            # self.print("回家点击："+ str(homeRouteImgX+168) +", "+ str(homeRouteImgY+13))
            # wait(lambda: self.simulatorInstance.click_point(homeRouteImgX+168,homeRouteImgY+10),4)
            if(self.mode==2 or self.mode==3):
                point=(243,578)
            else:
                point=(240,532)
            wait(lambda: self.simulatorInstance.click_point(*point), 0.5,disableWait=True)
            self.simulatorInstance.click_point(13,187)
            self.simulatorInstance.click_point(1053,645)
            self.simulatorInstance.click_point(1128,644)
            self.simulatorInstance.click_point(1199,641)
            if(self.mode==0):
                wait(lambda: self.simulatorInstance.click_point(1216,580),1)
                self.simulatorInstance.click_point(1216,580)
            if(self.hasSingleLineWordsInArea("x", A=[229,230,258,260])):
                doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(242,242),lambda: not self.hasSingleLineWordsInArea("x", A=[229,230,258,260]))
            self.pause()

        doAndWaitUntilBy(
            lambda: triggerGoHome(),
            lambda: self.isPlayerInSite() == "in",
            waitTime,
            timeout=120,
        )

        while self.isPlayerInSite() == "out" or self.isPlayerInSite() == "middle":
            time.sleep(5)
        time.sleep(10)
        self.setInsite(True)

    def saveImageToFile(self, imageBlob):
        screenshotImgPath = os.path.abspath(
            __file__
            + "\\..\\..\\..\\assets\\screenshots\\"
            + str(self.index)
            + "\\players.bmp"
        )
        cv2.imwrite(screenshotImgPath, imageBlob)

    def clickOnTestPic(self):
        targetImgPath = os.path.abspath(
            __file__ + "\\..\\..\\..\\assets\\clickOns\\greenStars.bmp"
        )
        screenshotImgPath = os.path.abspath(
            __file__
            + "\\..\\..\\..\\assets\\screenshots\\"
            + str(self.index)
            + "\\players.bmp"
        )

        # x,y = self.simulatorInstance.window_capture(targetImgPath, A=[0,325,194,598])
