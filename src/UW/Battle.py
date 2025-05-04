import sys
import os

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

from guiUtils import win
from datetime import datetime
from utils import (
    Utils,
    randomInt,
    wait,
    doMoreTimesWithWait,
    continueWithUntilBy,
    doAndWaitUntilBy,
    continueWithUntilByWithBackup,
    getTimeDiffInSeconds,
    getHour,
    hasOneArrayStringSimilarToString,
    while_with_timeout
)
from images import getNumberFromString
import time
from UWTask import UWTask
from constants import blackListForBattle


# todo list
# checkStats
class Battle:
    lastCallTime = 0
    haveSentBattleFinNotification = False
    battleEnd = {"okBtn": [685,639,763,661], "closeBtn": [685,639,763,661]}
    opentimeout = 0
    nameBoardInPrePanel = [49,136,162,165]
    sunk=False
    skillShip=[1,3,4,5,6,7]
    clickFastBtn=717,864
    clickAutoBtn=797,864
    supplyNoToCheckAuto=[1240,80,1265,96]

    def __init__(self, instance: win, uwtask: UWTask) -> None:
        self.instance = instance
        self.uwtask = uwtask
        self.lastCallTime = datetime(2021, 1, 1, 1, 1, 1)
        self.utils = Utils(uwtask, self)

    def suppressBattle(self):
        # runAway
        # wait(lambda: self.instance.clickPointV2(800,560),10)
        if self.uwtask.inWater():
            self.uwtask.print("retreated from battle")
            return

        print("in battle")
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.randomPoint), 3, 1)
        # use fast
        if self.uwtask.hasSingleLineWordsInArea("free", A=[77, 110, 106, 125]):
            self.instance.clickPointV2(101, 98)
        continueWithUntilBy(
            lambda: self.instance.rightClickPointV2(*self.uwtask.randomPoint),
            lambda: self.uwtask.hasSingleLineWordsInArea(
                "ok", A=self.battleEnd["okBtn"]
            )
            or self.uwtask.hasSingleLineWordsInArea("close", A=self.battleEnd["okBtn"])
            or self.uwtask.inCityList(self.uwtask.allCityList),
            10,
            timeout=240,
        )
        time.sleep(3)

        def exitBattle():
            wait(lambda: self.instance.clickPointV2(725, 681), 2)
            if self.uwtask.hasSingleLineWordsInArea("yes", A=[1041, 779, 1118, 811]):
                wait(lambda: self.instance.clickPointV2(1072, 789), 2)

        doAndWaitUntilBy(lambda: exitBattle(), lambda: self.uwtask.inWater(), 5, 2)

    def useFast(self):
        #first line
        fastWordsArea=702,856,745,872
        #second line
        usingArea=697,868,746,882
        times=0
        while self.uwtask.hasSingleLineWordsInArea("免费", A=fastWordsArea,looseCheckName=True) and times<20:
            wait(lambda: self.instance.clickPointV2(*self.clickFastBtn))
            times+=1
        if not self.uwtask.hasSingleLineWordsInArea(
            "使用", A=usingArea,looseCheckName=True
        ) and self.uwtask.hasSingleLineWordsInArea("快速", A=fastWordsArea, looseCheckName=True):
            continueWithUntilBy(
                lambda: self.instance.clickPointV2(*self.clickFastBtn),
                lambda: self.uwtask.hasSingleLineWordsInArea(
                    "使用", A=usingArea,looseCheckName=True
                ) or self.uwtask.hasSingleLineWordsInArea("购买", A=self.uwtask.noticeTitleArea),
                timeout=10
            )
            if self.uwtask.hasSingleLineWordsInArea("购买", A=self.uwtask.noticeTitleArea):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(770,584), 2, 2)
                if self.haveSentBattleFinNotification == False:
                    self.uwtask.sendNotification(f"Battle finished")
                    self.haveSentBattleFinNotification = True

    def clickAuto(self):
        continueWithUntilBy(
            lambda: self.instance.clickPointV2(self.clickAutoBtn[0] + randomInt(), self.clickAutoBtn[1] + randomInt()),
            self.checkSupplyNoForAutoEnabled,
            2,
        )
    def hasResultsBtn(self):
        return (
            self.uwtask.hasSingleLineWordsInArea("确定", A=self.battleEnd["okBtn"])
            or self.uwtask.hasSingleLineWordsInArea("丢弃", A=self.battleEnd["okBtn"])
        )

    def exitBattle(self):
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(725,651), 3, 2)
        if self.uwtask.hasSingleLineWordsInArea("ok", A=[756, 597, 804, 620]):
            wait(lambda: self.instance.clickPointV2(632, 566), 2)
            wait(lambda: self.instance.clickPointV2(777, 607), 2)

    def checkSupplyNoForAutoEnabled(self):
        number = self.uwtask.getNumberFromSingleLineInArea(A=self.supplyNoToCheckAuto)
        if (type(number) == int and number > 5):
            return False
        else:
            return True
    def doBattle(self):
        shipsDone = []
        x = 0
        continueWithUntilBy(
            lambda: self.instance.clickPointV2(38, 145),
            lambda: not self.uwtask.isPositionColorSimilarTo(48,151, (244, 244, 243)),
            1,
            10,
        )
        while x < 4:
            wait(lambda: self.instance.clickPointV2(1074, 797), 0.6)
            wait(lambda: self.instance.clickPointV2(654, 588), 0.6)
            x += 1

        def backup():
            if self.uwtask.hasSingleLineWordsInArea("notice", A=[682, 268, 755, 294]):
                wait(lambda: self.instance.clickPointV2(571, 568))
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(780, 600), 4, 5)
                if self.haveSentBattleFinNotification == False:
                    self.uwtask.sendNotification(f"Battle finished")
                    self.haveSentBattleFinNotification = True

        doAndWaitUntilBy(
            lambda: False,
            lambda: self.uwtask.hasSingleLineWordsInArea(
                "托管", A=[783,858,827,882]
            ),
            1,
            1,
            timeout=15,
            backupFunc=backup,
        )

        if self.uwtask.inWater():
            return
        print("in battle")
        self.useFast()

        centralPos = 724,448
        expressskill = 1240,857
        waitPos = 1400,801
        admiralSkillCostArea=[1399,747,1415,760]

        def useSkill(shipNo):
            def compareAdmiralCost():
                num=self.uwtask.getNumberFromSingleLineInArea(A=admiralSkillCostArea)
                return num and num<55
            if shipNo in self.skillShip:
                if(shipNo==1 and compareAdmiralCost()):
                    wait(lambda: self.instance.longerClickPointV2(1401,735), 0.5)
                    doMoreTimesWithWait(
                        lambda: self.instance.longerClickPointV2(*centralPos), 2, 0.5
                    )
                    time.sleep(3)
                wait(lambda: self.instance.longerClickPointV2(*expressskill), 0.5)
                doMoreTimesWithWait(
                    lambda: self.instance.longerClickPointV2(*centralPos), 2, 0.5
                )
                time.sleep(3)
            else:
                wait(lambda: self.instance.clickPointV2(*waitPos), 2)
            shipsDone.append(shipNo)

        for x in range(7):
            while True:
                def condition():
                    return not self.uwtask.isPositionColorSimilarTo(28, 107, (0, 155, 0))
                while_with_timeout(condition_func=condition, max_attempts=50, interval=5)

                number = self.uwtask.getNumberFromSingleLineInArea(A=[29,102,40,116])
                print("shipsDone", shipsDone)
                if number in shipsDone:
                    print(
                        "2nd same ship, rerun current iter after wait->so run next ship in current index"
                    )
                    wait(lambda: self.instance.clickPointV2(*waitPos), 2)
                    continue
                print("ship no", number)
                print("index", x)
                useSkill(number)
                break

        self.clickAuto()
        time.sleep(15)
        if(not self.checkSupplyNoForAutoEnabled()):
            self.clickAuto()

        continueWithUntilBy(
            lambda: self.instance.rightClickPointV2(*self.uwtask.randomPoint),
            lambda: self.hasResultsBtn(),
            5,
            timeout=400,
        )

        def backupFunc():
            self.exitBattle()
            if self.uwtask.hasSingleLineWordsInArea("战败", A=[1014,782,1161,816]):
                wait(lambda: self.instance.clickPointV2(1088,799), 10)
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(856,540), 2, 3)
                wait(lambda: self.instance.clickPointV2(777,643), 40)
            self.uwtask.checkForDailyPopup()
            doMoreTimesWithWait(
                lambda: self.instance.clickPointV2(*self.uwtask.randomPoint), 5, 3
            )
        if(self.uwtask.getNumberFromSingleLineInArea(A=[687,416,709,434]) or self.uwtask.getNumberFromSingleLineInArea(A=[685,513,712,536])):
            self.sunk=True
        continueWithUntilBy(
            lambda: self.exitBattle(),
            lambda: self.uwtask.inWater() or self.uwtask.inCityList(self.uwtask.allCityList),
            5,
            backupFunc=backupFunc,
            timeout=30,
        )
        time.sleep(1)
        self.uwtask.checkForDailyPopup(4)
        # if not self.uwtask.inWater():
        #     doAndWaitUntilBy(
        #         lambda: self.instance.rightClickPointV2(*self.uwtask.randomPoint),
        #         lambda: self.uwtask.inWater(),
        #         1,
        #         1,
        #     )

    def checkStats(self, town):
        time.sleep(1)
        # 0 SHIP DOWN OR 0 SAILORS
        if self.sunk==True or self.uwtask.hasImageInScreen("shipSunk", A=[131,50,299,81]):
            self.goBackPort(town)
            # set sunk false after in inn healing
            return False
        return True

    def checkInPort(self, town):
        if(self.sunk):
            self.uwtask.healInjury(town)
            self.sunk=False
        self.sunk=False
        now = datetime.now()
        if getTimeDiffInSeconds(self.lastCallTime, now) > 1800:
            if now.minute >= 30:
                self.uwtask.healInjury(town)
                self.uwtask.sellInCity(town, simple=True,negoTimes=False)
            # if(self.uwtask.firstBuyFin==False):
            #    self.uwtask.buyInCity([town], products=["agarwood","ylang-ylang","mace","chinesetea","gardenia","begonia","sweetolive","azalea","ginseng","doenjang","lris"],marketMode=1)
            self.lastCallTime = now

    def selectOpponentInList(self, opponentsInList):
        firstPosi = (1415,297)
        area = [1264,278,1396,297]
        # 8TH AREA
        # 1257,642,1378,663
        index = 0
        while index < 19:
            yDiff = int(index % 13 * 46)
            index += 1
            ocrName = self.uwtask.getSingleLineWordsInArea(
                A=[area[0], area[1] + yDiff, area[2], area[3] + yDiff], debug=False
            )
            hasName = hasOneArrayStringSimilarToString(
                ocrName, opponentsInList
            ) and not hasOneArrayStringSimilarToString(ocrName, blackListForBattle)

            if hasName:
                wait(lambda: self.instance.clickPointV2(
                        firstPosi[0], firstPosi[1] + yDiff
                    ))

                # if not self.uwtask.hasArrayStringInSingleLineWords(
                #     opponentsInList, A=[1215,115,1359,144]
                # ):
                #     continueWithUntilBy(
                #         lambda: self.instance.clickPointV2(
                #             *self.uwtask.rightTopTownIcon
                #         ),
                #         lambda: self.uwtask.inWater(),
                #         1,
                #         30,
                #     )
                #     continue
                # else:
                return True
        return False

    def quickWaitForCity(self, cityList=None, targetCity=None):
        self.uwtask.print("航行中")

        def inJourneyTask():
            self.uwtask.clickEnterCityButton()

        def backupFunc():
            self.utils.useSpecial("battle")
            self.uwtask.checkForDailyPopup(5)
            if self.uwtask.hasSingleLineWordsInArea("huamei", A=self.nameBoardInPrePanel,ocrType=1):
                continueWithUntilBy(
                    lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon),
                    lambda: self.uwtask.inWater(),
                    1,
                    30,
                )
            self.uwtask.checkForBasicStuck()
            time.sleep(10)
            wait(lambda: self.uwtask.findCityAndClick(targetCity), 40)
            doMoreTimesWithWait(
                lambda: self.instance.rightClickPointV2(*self.uwtask.randomPoint), 4, 10
            )

        continueWithUntilByWithBackup(
            lambda: inJourneyTask(),
            lambda: self.uwtask.inCityList(cityList),
            1,
            timeout=60,
            notifyFunc=lambda: self.uwtask.print("not found, wait for 4s"),
            backupFunc=backupFunc,
        )
        self.uwtask.print("click twice")
        self.uwtask.clickEnterCityButton()

    def depart(self):
        departBtn = self.uwtask.departBtn

        def clickAndStock():
            wait(lambda: self.instance.clickPointV2(*self.uwtask.randomPoint), 0.2)
            self.uwtask.restock()

        def clickAndStockBackup():
            self.uwtask.checkForDailyPopup()
            wait(lambda: self.instance.clickPointV2(*self.uwtask.randomPoint), 0.2)
            if self.uwtask.hasSingleLineWordsInArea("出港所", A=self.uwtask.titleArea):
                self.uwtask.restock()
                self.instance.clickPointV2(*departBtn)

        clickAndStock()
        if self.uwtask.hasSingleLineWordsInArea("船员", A=[1225,490,1286,508]):
            crewWords = self.uwtask.getSingleLineWordsInArea(
                A=[1286,490,1386,510], ocrType=2
            )
            if(len(crewWords.split("/")) > 1):
                actualCrew = getNumberFromString(crewWords.split("/")[0])
                maxCrew = getNumberFromString(crewWords.split("/")[1])
                if actualCrew / maxCrew < 0.97:
                    doAndWaitUntilBy(
                        lambda: self.instance.clickPointV2(*self.uwtask.departSecondArrowBtn),
                        lambda: self.uwtask.hasSingleLineWordsInArea("船员", A=self.uwtask.titleArea),
                    )
                    doMoreTimesWithWait(lambda: self.instance.clickPointV2(1359,352), 2, 0)
                    def click2():
                        wait(lambda: self.instance.longerClickPointV2(1296, 451), 2)
                        doMoreTimesWithWait(
                            lambda: self.instance.clickPointV2(*self.uwtask.departRestockOkBtn), 2
                        )
                    doAndWaitUntilBy(
                        click2,
                        lambda: self.uwtask.hasSingleLineWordsInArea(
                            "出港所", A=self.uwtask.titleArea
                        ),
                        1,
                        2,
                        backupFunc=lambda: self.instance.clickPointV2(
                            *self.uwtask.leftTopBackBtn
                        ),
                        timeout=10,
                    )

        self.uwtask.print("出海")
        self.instance.longerClickPointV2(*departBtn)
        doAndWaitUntilBy(
            lambda: self.instance.clickPointV2(*departBtn),
            lambda: self.uwtask.inWater(),
            4,
            2,
            backupFunc=clickAndStockBackup,
            timeout=120,
        )
        time.sleep(2)
        self.uwtask.checkForDailyPopup(3)

    def backupFromDashboardToSea(self):
        wait(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), 1)
        self.uwtask.checkForBasicStuck()

    def goBackPort(self, town):
        def backup():
            self.utils.useSpecial("battle")
            self.uwtask.simulatorInstance.clickPointV2(*self.uwtask.mapIcon)

        if self.uwtask.hasSingleLineWordsInArea("huamei", A=self.nameBoardInPrePanel,ocrType=1):
            doAndWaitUntilBy(
                lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon),
                lambda: self.uwtask.inWater(),
                1,
                1,
            )
        doAndWaitUntilBy(
            lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),
            lambda: self.uwtask.inWater(),
            1,
            1,
            backupFunc=self.backupFromDashboardToSea,
            timeout=10,
        )
        wait(
            lambda: self.uwtask.findCityAndClick(town, noExpect=True, backup=backup), 0
        )
        self.quickWaitForCity([town], targetCity=town)
        self.opentimeout = 0

    def leavePort(self):
        doMoreTimesWithWait(
            lambda: self.instance.rightClickPointV2(*self.uwtask.randomPoint), 2, 1
        )
        self.uwtask.goToHarbor()
        self.depart()
        if (getHour() in [21, 22, 23, 24, 0, 1, 2] and self.uwtask.getDailyConfValByKey("dailyCheckedBattlePlaceLanding")):
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(36,721), 2, 4)

    def findOpponentOrReturn(self, opponentsInList, opponents, town):
        doAndWaitUntilBy(
            lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint3),
            lambda: self.uwtask.inWater(),
            1,
            1,
            backupFunc=self.backupFromDashboardToSea,
            timeout=10,
        )
        clickedOpponentInList = self.selectOpponentInList(opponentsInList)
        if not clickedOpponentInList:
            self.uwtask.print("no foe,return port")
            self.goBackPort(town)
            return False
        timeout = 20

        # combatScreenOpened = self.uwtask.hasSingleLineWordsInArea(
        #     "huamei", A=self.nameBoardInPrePanel,ocrType=1
        # )
        # if not combatScreenOpened:
        #     wait(lambda: False, 1)
        # while timeout > 0 and not combatScreenOpened:
        #     if self.uwtask.hasSingleLineWordsInArea(
        #         "huamei", A=self.nameBoardInPrePanel,ocrType=1
        #     ):
        #         break
        #     if self.uwtask.checkStopped():
        #         return self.findOpponentOrReturn(opponentsInList, opponents, town)
        #     timeout -= 1
        #     wait(lambda: False, 1)
        # if timeout == 0:
        #     wait(lambda: self.instance.clickPointV2(720, 862), 2)
        #     if self.uwtask.hasSingleLineWordsInArea(
        #         "huamei", A=self.nameBoardInPrePanel,ocrType=1
        #     ):
        #         doAndWaitUntilBy(
        #             lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon),
        #             lambda: self.uwtask.inWater(),
        #             1,
        #             1,
        #         )
        #     return self.findOpponentOrReturn(opponentsInList, opponents, town)
        wrongShipErrorTitle=[689,291,753,320]
        while timeout > 0:
            if self.uwtask.hasSingleLineWordsInArea(
                    "战斗", A=[683,3,760,29]
                ):
                break
            if self.uwtask.hasSingleLineWordsInArea("LiHuamei", A=[54,142,208,163]):
                continueWithUntilBy(
                    lambda: self.instance.clickPointV2(676,852),
                    lambda: self.uwtask.hasSingleLineWordsInArea(
                        "战斗", A=[683,3,760,29]
                    ),
                    1,
                    timeout=10,
                )
                break
            # clicked into wrong ship
            if(self.uwtask.hasSingleLineWordsInArea(
                    "通知", A=wrongShipErrorTitle
                )):
                doAndWaitUntilBy(
                    lambda: self.instance.clickPointV2(123,123),
                    lambda: not self.uwtask.hasSingleLineWordsInArea(
                    "通知", A=wrongShipErrorTitle)
                )
                return self.findOpponentOrReturn(opponentsInList, opponents, town)
            if self.uwtask.checkStopped():
                return self.findOpponentOrReturn(opponentsInList, opponents, town)
            timeout -= 1
            wait(lambda: False, 1)
        if timeout == 0:
            return self.findOpponentOrReturn(opponentsInList, opponents, town)
        return True


        # if self.uwtask.hasArrayStringInSingleLineWords(
        #     opponents, A=[1215,115,1359,144]
        # ):  # and not self.uwtask.hasSingleLineWordsInArea("pirate",A=[1187,129,1396,159])):
        #     self.uwtask.print("准备开战")
        #     return continueWithUntilBy(
        #         lambda: clickIntoBattle(),
        #         lambda: self.uwtask.hasSingleLineWordsInArea(
        #             "战斗", A=[685,12,759,30]
        #         ),
        #         1,
        #         timeout=10,
        #     )
        # continueWithUntilBy(
        #     lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon),
        #     lambda: self.uwtask.inWater(),
        #     1,
        #     30,
        # )
        # self.opentimeout += 1
        # if self.opentimeout > 2:
        #     self.goBackPort(town)
        #     return False
        # return self.findOpponentOrReturn(opponentsInList, opponents, town)
