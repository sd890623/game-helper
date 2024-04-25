from windows import *
from images import *
from utils import *
# from EveRunner import Runner
import guiUtils
import time
import random
import multiprocessing

class EVETask:
    exclamationRedPlayerType = "EXCLAMATIONREDPLAYERTYPE"
    minusRedPlayerType = "MINUSREDPLAYERTYPE"
    whitePlayerType = "WHITEPLAYERTYPE"
    lastOreSiteCalibrater=0

    hwnd = None
    simulatorInstance = None
    index = None
    syncBetweenUsers = True
    homeNameArea = [1038, 137, 1102, 157]

    def __init__(self, hwnd, index, childTitle="MuMuPlayer",eveRunners=[multiprocessing.Event(),multiprocessing.Queue()],mode=0):
        self.hwnd = hwnd
        self.index = index
        self.pauseEvent = eveRunners[0]
        self.queue=eveRunners[1]
        self.mode=mode
        childHwndObj = getChildHwndByTitleAndParentHwnd(childTitle, hwnd)
        self.simulatorInstance = guiUtils.win(childHwndObj["hwnd"], bor=True)

    def testTask(self):
        times = 2
        # todo solve foreground scroll
        while times > 0:
            wait(lambda: self.simulatorInstance.mouseWheel((1263, 213), "up"), 1)
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

    def hasSingleLineWordsInArea(self, words, A, ocrType=3):
        try:
            screenshotBlob = self.simulatorInstance.output_window_screenshot(A)
            # self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if len(ocrObj[0]) == 0:
                return False
            str = "".join(ocrObj[0])

            self.print(words + " in " + str)
            return words in str.lower()
        except Exception as e:
            print(e)
            return False
        
    def getNumberFromSingleLineInArea(self, A=[0, 0, 0, 0], debug=False):
        try:
            screenshotBlob = self.simulatorInstance.output_window_screenshot(A)
            if (debug == True):
                self.saveImageToFile(screenshotBlob)
            return getNumberfromImageBlob(screenshotBlob)
        except Exception as e:
            print("fail to get number")
            return 0

    def isPlayerInSite(self):
        inCenter = self.hasSingleLineWordsInArea("活动", [1064,387,1116,421],4)
        isOut = self.getNumberFromSingleLineInArea([482,589,511,605])==100

        if inCenter:
            self.print("in")
            return "in"
        elif isOut and not(inCenter):
            self.print("out")
            return "out"
        else:
            return "middle"

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

    def goHome(self):
        def triggerGoHome():
            def backup():
                if self.hasSingleLineWordsInArea("x", A=[1186, 23, 1212, 55]):
                    doAndWaitUntilBy(
                        lambda: self.simulatorInstance.click_point(1199, 35),
                        lambda: not self.hasSingleLineWordsInArea(
                            "x", A=[1186, 23, 1212, 55]
                        ),
                    )
                wait(lambda: self.simulatorInstance.click_point(26,192))

            doAndWaitUntilBy(
                lambda: self.simulatorInstance.click_point(26,189),
                lambda: self.hasSingleLineWordsInArea("x", A=[229,230,258,260]),
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
            if(self.mode==2):
                point=(243,578)
            else:
                point=(240,532)
            wait(lambda: self.simulatorInstance.click_point(*point), 4)
            wait(lambda: self.simulatorInstance.click_point(1128,644), 2)
            self.pause()

        doAndWaitUntilBy(
            lambda: triggerGoHome(),
            lambda: self.isPlayerInSite() == "in",
            60,
            timeout=60,
        )

        while self.isPlayerInSite() == "out" or self.isPlayerInSite() == "middle":
            time.sleep(5)
        time.sleep(10)

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
