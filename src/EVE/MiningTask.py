from EVETask import EVETask
import time
import random
from utils import *


class MiningTask(EVETask):
    haveChangedToMiningFilter = False
    def __init__(self, hwnd, index, mode=0):
        super().__init__(hwnd, index, mode=mode)

    def isSafe(self):
        if(self.mode==0):
            return super().isSafe()
        return True

    def passOre(self):
        if not (self.isSafe()):
            self.print("有海盗，蹲站")
            time.sleep(30)
            return
        wait(lambda: self.simulatorInstance.click_point(875, 180, True), 5)
        while self.isPlayerInSite() == "in" or self.isPlayerInSite() == "middle":
            time.sleep(5)
        time.sleep(15)
        wait(lambda: self.simulatorInstance.click_keyboard("`"), 6)
        wait(lambda: self.simulatorInstance.click_point(131, 186), 4)
        wait(lambda: self.simulatorInstance.click_point(204, 231), 4)
        time.sleep(15)
        while self.isPlayerInSite() == "out" or self.isPlayerInSite() == "middle":
            time.sleep(5)
        time.sleep(15)

        wait(lambda: self.simulatorInstance.click_keyboard("b"), 8)

        wait(lambda: self.simulatorInstance.click_point(102, 147), 4)

        wait(lambda: self.simulatorInstance.click_point(505, 138))
        wait(lambda: self.simulatorInstance.click_point(905, 93))
        wait(lambda: self.simulatorInstance.click_point(965, 141))
        wait(lambda: self.simulatorInstance.click_point(903, 70))
        wait(lambda: self.simulatorInstance.click_point(967, 245), 4)
        wait(lambda: self.simulatorInstance.click_keyboard("5"), 4)

        wait(lambda: self.simulatorInstance.click_point(961, 31))
        wait(lambda: self.simulatorInstance.click_point(961, 31))
        wait(lambda: self.simulatorInstance.click_point(961, 31))
        wait(lambda: self.simulatorInstance.click_point(961, 31))
        wait(lambda: self.simulatorInstance.click_point(961, 31))
        wait(lambda: self.simulatorInstance.click_point(961, 31))
        wait(lambda: self.simulatorInstance.click_point(961, 31))

        wait(lambda: self.simulatorInstance.click_keyboard("`"), 6)
        wait(lambda: self.simulatorInstance.click_point(131, 186))
        wait(lambda: self.simulatorInstance.click_point(204, 355), 5)
        wait(lambda: self.simulatorInstance.click_point(915, 456))

        time.sleep(15)
        while self.isPlayerInSite() == "out" or self.isPlayerInSite() == "middle":
            time.sleep(5)
        time.sleep(15)

        self.stockOre()
        time.sleep(10)

    def goOut(self):
        wait(lambda: self.simulatorInstance.click_point(1075, 226, True), 5)
        while self.isPlayerInSite() == "in" or self.isPlayerInSite() == "middle":
            time.sleep(5)
        time.sleep(10)
        if(not self.haveChangedToMiningFilter):
            wait(lambda: self.simulatorInstance.click_point(1197, 394), 4)
            wait(lambda: self.simulatorInstance.click_point(1048, 21, True), 4)
            wait(lambda: self.simulatorInstance.click_point(1051, 466), 4)
            self.haveChangedToMiningFilter = True
        if(self.mode==2):
            return self.minec70()
        else:
            return self.mineNormal()

    def minec70(self):
        return True
    
    def mineNormal(self):
        def checkGoHome():
            if self.isSafe() == False:
                self.syncBetweenUsers = True
                return True
        minerYDiff = 65
        oreSiteCalibrater = random.randint(-2, 2)
        while(oreSiteCalibrater==self.lastOreSiteCalibrater):
            oreSiteCalibrater = random.randint(-2, 2)
        if(self.mode==1):
            oreSiteCalibrater=-2
        if (checkGoHome()):
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
        wait(lambda: self.simulatorInstance.click_point(1064,644), 5)

        duration = 40 + random.randint(0, 5)
        while self.isSafe() and duration > 0:
            time.sleep(5)
            duration -= 5
        if (checkGoHome()):
            return

        # 上滑至顶
        times = 4
        # todo solve foreground scroll
        # while(times>0):
        #    wait(lambda: self.simulatorInstance.mouseWheel((1357,190), "up"),2)
        #    times=times-1
        wait(lambda: self.simulatorInstance.click_point(896, 389, True))
        wait(lambda: self.simulatorInstance.click_point(1197, 394), 4)

        wait(lambda: self.simulatorInstance.click_point(1051, 219, True), 2)
        wait(lambda: self.simulatorInstance.click_point(814, 300, True), 2)
        wait(lambda: self.simulatorInstance.click_point(896, 389, True))

        if (checkGoHome()):
            return

        wait(lambda: self.simulatorInstance.click_point(848,640), 1)
        wait(lambda: self.simulatorInstance.click_point(924,644), 1)
        wait(lambda: self.simulatorInstance.click_point(992,645), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("W"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("E"), 1)
        wait(lambda: self.simulatorInstance.click_keyboard("6"), 1)

    def startMiningTask(self):
        if self.syncBetweenUsers:
            self.print("账号差异化，等待x*60s")
            time.sleep(90 * self.index)
            self.syncBetweenUsers = not (self.syncBetweenUsers)
        self.print("新一轮开始了")
        if not (self.isSafe()):
            self.print("有海盗，蹲站")
            time.sleep(30 + random.randint(0, 5))
            return
        self.print("开始存货")
        self.stockOre()
        self.print("存货完毕")
        time.sleep(10)
        while True:
            if self.isSafe():
                self.print("安全，出发")
                self.goOut()
                self.print("到达，开采")
                break
            else:
                self.print("有海盗，蹲站")
                time.sleep(30 + random.randint(0, 5))
                continue
        self.print("采矿等待中")
        self.checkSafeForMinutes(11.2 + random.randint(0, 10) / 10)
        self.print("回家")
        self.goHome()
        self.print("到家")
        time.sleep(30 + random.randint(0, 30))