from EVETask import EVETask
import time
import random
from utils import *


class MiningTask(EVETask):
    haveChangedToMiningFilter = False
    minedRows = []
    otherStellaRows = {"EZC": []}
    havePirate = False

    def __init__(self, hwnd, index, mode=0):
        super().__init__(hwnd, index, mode=mode)

    def isSafe(self):
        if self.mode == 0:
            return super().isSafe()
        elif self.mode == 1:
            return True
        else:
            if (
                not self.inSite and self.isPositionColorSimilarTo(774, 27, (36, 36, 39))
            ) or self.hasSingleLineWordsInArea("探测", [203, 162, 236, 182], 4):
                wait(lambda: self.simulatorInstance.click_point(26, 189), 1)
                self.havePirate = True
                return False
            if self.havePirate:
                return False
            return True

    def goOut(self):
        wait(lambda: self.simulatorInstance.click_point(1075, 226, True), 5)
        while self.isPlayerInSite() == "in" or self.isPlayerInSite() == "middle":
            time.sleep(5)
        self.setInsite(False)
        time.sleep(10)
        if not self.haveChangedToMiningFilter:
            wait(lambda: self.simulatorInstance.click_point(1197, 394), 4)
            wait(lambda: self.simulatorInstance.click_point(1048, 21, True), 4)
            wait(lambda: self.simulatorInstance.click_point(1051, 466), 4)
            self.haveChangedToMiningFilter = True
        else:
            wait(lambda: self.simulatorInstance.click_point(1197, 394), 4)

        if self.mode == 2:
            return self.minec70()
        else:
            return self.mineNormal()

    def c70GoOut(self):
        if len(self.minedRows) == 6:
            self.goToStella("ezc")
            self.minec70()
        else:
            self.goOut()

    def recordMined(self, row):
        if len(self.minedRows) == 6:
            self.otherStellaRows["EZC"].append(row)
        else:
            self.minedRows.append(row)

    def minec70(self):
        def checkGoHome():
            if self.isSafe() == False:
                self.syncBetweenUsers = True
                return True

        yDiff = 68

        def getCurrentRow():
            for row in range(6):
                if row not in (
                    self.otherStellaRows["EZC"]
                    if len(self.minedRows) == 6
                    else self.minedRows
                ):
                    return row

        wait(
            lambda: self.simulatorInstance.click_point(1202, 395),
            4,
        )
        row = getCurrentRow()
        wait(
            lambda: self.simulatorInstance.click_point(1069, 70 + row * yDiff),
            4,
        )
        wait(
            lambda: self.simulatorInstance.click_point(814, 163 + row * yDiff),
            4,
        )
        time.sleep(15)
        if checkGoHome():
            return
        wait(lambda: self.simulatorInstance.click_point(896, 389, True))
        wait(lambda: self.simulatorInstance.click_point(1197, 394), 4)
        if self.getNumberFromSingleLineInArea([1071, 359, 1093, 376]) == 70:
            wait(
                lambda: self.simulatorInstance.click_point(1056, 351),
                1,
            )
            wait(
                lambda: self.simulatorInstance.click_point(823, 361),
                1,
            )
            wait(
                lambda: self.simulatorInstance.click_point(1062, 362),
                1,
            )
            wait(
                lambda: self.simulatorInstance.click_point(824, 433),
                1,
            )
            wait(
                lambda: self.simulatorInstance.click_point(1199, 647),
                20,
            )
            if checkGoHome():
                return
            wait(lambda: self.simulatorInstance.click_point(848, 640), 1)
            wait(lambda: self.simulatorInstance.click_point(924, 644), 1)
            wait(lambda: self.simulatorInstance.click_point(992, 645), 1)
            wait(lambda: self.simulatorInstance.click_point(1199, 647))
        else:
            self.recordMined(row)
        return True

    def mineNormal(self):
        def checkGoHome():
            if self.isSafe() == False:
                self.syncBetweenUsers = True
                return True

        minerYDiff = 65
        oreSiteCalibrater = random.randint(-2, 2)
        while oreSiteCalibrater == self.lastOreSiteCalibrater:
            oreSiteCalibrater = random.randint(-2, 2)
        if self.mode == 1:
            oreSiteCalibrater = -2
        if checkGoHome():
            return
        self.print("点矿区y偏移量:" + str(oreSiteCalibrater))
        wait(
            lambda: self.simulatorInstance.click_point(
                1055, 220 + oreSiteCalibrater * minerYDiff
            ),
            4,
        )
        wait(
            lambda: self.simulatorInstance.click_point(
                819, 299 + oreSiteCalibrater * minerYDiff, 4
            )
        )
        # 点平衡器
        wait(lambda: self.simulatorInstance.click_point(1064, 644), 5)

        duration = 40 + random.randint(0, 5)
        while self.isSafe() and duration > 0:
            time.sleep(5)
            duration -= 5
        if checkGoHome():
            return

        wait(lambda: self.simulatorInstance.click_point(896, 389, True))
        wait(lambda: self.simulatorInstance.click_point(1197, 394), 4)

        wait(lambda: self.simulatorInstance.click_point(1051, 219, True), 2)
        wait(lambda: self.simulatorInstance.click_point(814, 300, True), 2)
        wait(lambda: self.simulatorInstance.click_point(896, 389, True))

        if checkGoHome():
            return

        wait(lambda: self.simulatorInstance.click_point(848, 640), 1)
        wait(lambda: self.simulatorInstance.click_point(924, 644), 1)
        wait(lambda: self.simulatorInstance.click_point(992, 645), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("W"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("E"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("6"), 1)

    def waitForOreFinish(self):
        if self.mode == 2:
            frequency = 5
            totalSeconds = 30 * 60
            # count=0
            while (
                self.hasSingleLineWordsInArea("富勒体", [844, 104, 887, 122], 4)
                and totalSeconds > 0
                and self.isSafe()
            ):
                time.sleep(frequency)
                totalSeconds -= frequency
                # self.print("count:"+str(count))
                # count+=1
            return
        else:
            self.checkSafeForMinutes(11.2 + random.randint(0, 10) / 10)

    def startMiningTask(self):
        if self.syncBetweenUsers:
            self.print("账号差异化，等待x*60s")
            time.sleep(90 * self.index)
            self.syncBetweenUsers = not (self.syncBetweenUsers)
        self.print("新一轮开始了")
        if not (self.isSafe()):
            self.print("有海盗，蹲站")
            time.sleep(1800)
            self.havePirate = False
            return
        self.print("开始存货")
        self.stockOre()
        self.print("存货完毕")
        time.sleep(10)
        while True:
            if self.isSafe():
                self.print("安全，出发")
                if self.mode == 2:
                    self.c70GoOut()
                else:
                    self.goOut()
                self.print("到达，开采")
                break
            else:
                self.print("有海盗，蹲站")
                time.sleep(30 + random.randint(0, 5))
                continue
        self.print("采矿等待中")
        self.waitForOreFinish()
        self.print("回家")
        self.goHome()
        self.print("到家")
        time.sleep(30 + random.randint(0, 30))
        if len(self.minedRows) == 6 and len(self.otherStellaRows["EZC"]) == 6:
            self.print("已经采集完成,sleep for 1hr")
            time.sleep(3600)
            self.minedRows = []
            self.otherStellaRows["EZC"] = []
