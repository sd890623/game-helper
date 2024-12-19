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
)
from images import getNumberFromString
import time
from UWTask import UWTask
from constants import blackListForBattle


# todo list
# checkStats
class Battle:
    randomPoint = 507, 783
    lastCallTime = 0
    haveSentBattleFinNotification = False
    battleEnd = {"okBtn": [685,649,765,669], "closeBtn": [685,649,765,669]}
    opentimeout = 0
    nameBoardInPrePanel = [57,147,141,171]
    sunk=False

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
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint), 3, 1)
        # use fast
        if self.uwtask.hasSingleLineWordsInArea("free", A=[77, 110, 106, 125]):
            self.instance.clickPointV2(101, 98)
        continueWithUntilBy(
            lambda: self.instance.rightClickPointV2(*self.randomPoint),
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
        times=0
        while self.uwtask.hasSingleLineWordsInArea("免费", A=[698,867,726,881]) and times<20:
            wait(lambda: self.instance.clickPointV2(715,865))
            times+=1
        if not self.uwtask.hasSingleLineWordsInArea(
            "使用", A=[699,868,743,883]
        ) and self.uwtask.hasSingleLineWordsInArea("快速", A=[700,856,738,870]):
            continueWithUntilBy(
                lambda: self.instance.clickPointV2(715,865),
                lambda: not self.uwtask.hasSingleLineWordsInArea(
                    "快速", A=[700,856,738,870]
                )
                or self.uwtask.isPositionColorSimilarTo(675, 856, (62,79,51)),
                timeout=10
            )
            if self.uwtask.hasSingleLineWordsInArea("购买", A=self.uwtask.noticeTitleArea):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(785,586), 2, 2)
                if self.haveSentBattleFinNotification == False:
                    self.uwtask.sendNotification(f"Battle finished")
                    self.haveSentBattleFinNotification = True

    def clickAuto(self):
        continueWithUntilBy(
            lambda: self.instance.clickPointV2(804 + randomInt(), 866 + randomInt()),
            lambda: not self.uwtask.isPositionColorSimilarTo(
                1304,34, (255,255,255)
            ),
            2,
        )
    def hasResultsBtn(self):
        return (
            self.uwtask.hasSingleLineWordsInArea("确定", A=self.battleEnd["okBtn"])
            or self.uwtask.hasSingleLineWordsInArea("close", A=self.battleEnd["okBtn"])
            or self.uwtask.hasSingleLineWordsInArea("discard", A=[679, 667, 757, 682])
        )

    def exitBattle(self):
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(723,657), 3, 2)
        if self.uwtask.hasSingleLineWordsInArea("ok", A=[756, 597, 804, 620]):
            wait(lambda: self.instance.clickPointV2(632, 566), 2)
            wait(lambda: self.instance.clickPointV2(777, 607), 2)

    def doBattle(self):
        x = 0
        continueWithUntilBy(
            lambda: self.instance.clickPointV2(27,144),
            lambda: not self.uwtask.isPositionColorSimilarTo(27,144, (255, 255, 255)),
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
                "托管", A=[786,860,831,882]
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

        centralPos = 712,457
        expressskill = 1232,858
        waitPos = 1399,798

        def getSkillPosByIndex(index):
            xDiff = 76.3
            yDiff = 75
            return (1161 + int(index % 4 * xDiff), 369 + int(index / 4) * yDiff)

        for x in range(6):
            while not self.uwtask.isPositionColorSimilarTo(
                29,112, (0,155,0)
            ):
                print("foe's turn, wait for 5s")
                time.sleep(5)
            # if self.uwtask.isPositionColorSimilarTo(1182, 830, (59, 59, 59)):
            #     wait(lambda: self.instance.clickPointV2(*waitPos), 3)
            #     continue
            number = self.uwtask.getNumberFromSingleLineInArea(A=[28,105,42,122])
            match number:
                case 1:
                    # No 1 melee Buff
                    wait(lambda: self.instance.longerClickPointV2(*expressskill), 0.5)

                    # wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    # wait(lambda: self.instance.clickPointV2(1260,332),0.5)
                    doMoreTimesWithWait(
                        lambda: self.instance.longerClickPointV2(*centralPos), 3, 0.5
                    )
                    time.sleep(5)
                case 2:
                    wait(lambda: self.instance.clickPointV2(*waitPos), 3)
                    # No 2
                    # wait(lambda: self.instance.clickPointV2(*expressskill), 0.5)
                    # doMoreTimesWithWait(
                    #     lambda: self.instance.longerClickPointV2(*centralPos), 2, 0.5
                    # )
                    # time.sleep(2)
                case 3:
                    # open skill #No3 ram buff
                    # wait(lambda: self.instance.clickPointV2(*waitPos),3)

                    wait(lambda: self.instance.clickPointV2(*expressskill), 0.5)
                    doMoreTimesWithWait(
                        lambda: self.instance.longerClickPointV2(*centralPos), 2, 0.5
                    )
                    time.sleep(2)

                case 4:
                    # wait(lambda: self.instance.clickPointV2(*expressskill), 0.5)
                    # doMoreTimesWithWait(
                    #     lambda: self.instance.longerClickPointV2(*centralPos), 2, 0.5
                    # )
                    # time.sleep(2)
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)

                case 5:
                    # 5  #CRI
                    # wait(lambda: self.instance.clickPointV2(*waitPos), 3)
                    wait(lambda: self.instance.clickPointV2(*expressskill),0.5)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    time.sleep(2)

                case 6:
                    # open skill
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)
                    # wait(lambda: self.instance.clickPointV2(*expressskill), 0.5)
                    # doMoreTimesWithWait(
                    #     lambda: self.instance.longerClickPointV2(*centralPos), 2, 0.5
                    # )
                    # time.sleep(2)

                case 7:
                    wait(lambda: self.instance.clickPointV2(*expressskill), 0.5)
                    doMoreTimesWithWait(
                        lambda: self.instance.longerClickPointV2(*centralPos), 2, 0.5
                    )
                    time.sleep(2)
                    #wait(lambda: self.instance.clickPointV2(*waitPos),3)
                case _:
                    wait(lambda: self.instance.clickPointV2(*waitPos), 3)

        self.clickAuto()
        time.sleep(15)
        # number = self.uwtask.getNumberFromSingleLineInArea(A=[1209, 96, 1237, 112])
        # if type(number) == int and number > 30:
        #     wait(
        #         lambda: self.instance.clickPointV2(
        #             825 + randomInt(), 863 + randomInt()
        #         ),
        #         0.5,
        #     )

        continueWithUntilBy(
            lambda: self.instance.rightClickPointV2(*self.randomPoint),
            lambda: self.hasResultsBtn(),
            5,
            timeout=480,
        )

        def backupFunc():
            self.exitBattle()
            if self.uwtask.hasSingleLineWordsInArea("defeat", A=[1078, 781, 1162, 807]):
                wait(lambda: self.instance.clickPointV2(1097, 798), 10)
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(859, 497), 2, 3)
                wait(lambda: self.instance.clickPointV2(781, 663), 60)
            self.uwtask.checkForDailyPopup()
            doMoreTimesWithWait(
                lambda: self.instance.clickPointV2(*self.randomPoint), 5, 3
            )
        if(self.uwtask.getNumberFromSingleLineInArea(A=[683,407,707,428])):
            self.sunk=True
        doAndWaitUntilBy(
            lambda: self.exitBattle(),
            lambda: self.uwtask.inWater() or self.uwtask.inCityList(self.uwtask.allCityList),
            5,
            2,
            backupFunc=backupFunc,
            timeout=30,
        )
        time.sleep(1)
        self.uwtask.checkForDailyPopup(4)
        if not self.uwtask.inWater():
            doAndWaitUntilBy(
                lambda: self.instance.rightClickPointV2(*self.randomPoint),
                lambda: self.uwtask.inWater(),
                1,
                1,
            )

    def checkStats(self, town):
        time.sleep(1)
        # 0 SHIP DOWN OR 0 SAILORS
        if self.sunk==True or self.uwtask.hasImageInScreen("shipSunk", A=[85,55,358,92]):
            self.goBackPort(town)
            self.sunk=False
            return False
        return True

    def checkInPort(self, town):
        now = datetime.now()
        if getTimeDiffInSeconds(self.lastCallTime, now) > 1800:
            if now.minute >= 30:
                self.uwtask.healInjury(town)
            # if(self.uwtask.tradeRouteBuyFin==False):
            #    self.uwtask.buyInCity([town], products=["agarwood","ylang-ylang","mace","chinesetea","gardenia","begonia","sweetolive","azalea","ginseng","doenjang","lris"],marketMode=1)
            self.lastCallTime = now

    def selectOpponentInList(self, opponentsInList):
        firstPosi = (1299,312)
        area = [1257,292,1376,314]
        # 8TH AREA
        # 1257,642,1378,663
        index = 0
        while index < 19:
            yDiff = int(index % 12 * 50)
            index += 1
            ocrName = self.uwtask.getSingleLineWordsInArea(
                A=[area[0], area[1] + yDiff, area[2], area[3] + yDiff], debug=False
            )
            hasName = hasOneArrayStringSimilarToString(
                ocrName, opponentsInList
            ) and not hasOneArrayStringSimilarToString(ocrName, blackListForBattle)

            if hasName:
                wait(
                    lambda: self.instance.fastClickPointV2(
                        firstPosi[0], firstPosi[1] + yDiff
                    ),
                    0.5,
                    disableWait=True,
                )
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
                lambda: self.instance.rightClickPointV2(*self.randomPoint), 4, 10
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
        secondLineArrowBtn = 1405,499
        okBtn = 785,591
        departBtn = 1368,646

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

            actualCrew = getNumberFromString(crewWords.split("/")[0])
            maxCrew = getNumberFromString(crewWords.split("/")[1])
            if actualCrew / maxCrew < 0.97:
                doAndWaitUntilBy(
                    lambda: self.instance.clickPointV2(*secondLineArrowBtn),
                    lambda: self.uwtask.hasSingleLineWordsInArea(
                        "招募", A=self.uwtask.titleArea
                    ),
                    1,
                    2,
                )
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(1370,367), 2, 0)
                def click():
                    wait(lambda: self.instance.longerClickPointV2(1318,471), 2)
                    doMoreTimesWithWait(lambda: self.instance.clickPointV2(*okBtn),2)
                doAndWaitUntilBy(
                    click,
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
        wait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2), 0)
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
            lambda: self.instance.rightClickPointV2(*self.randomPoint), 2, 1
        )
        self.uwtask.goToHarbor()
        self.depart()
        if (getHour() in [21, 22, 23, 24, 0, 1, 2] and self.uwtask.getDailyConfValByKey("dailyCheckedBattlePlaceLanding")):
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(43,716), 2, 4)

    def findOpponentOrReturn(self, opponentsInList, opponents, town):
        wait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint3), 0)
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
        combatScreenOpened = self.uwtask.hasSingleLineWordsInArea(
            "huamei", A=self.nameBoardInPrePanel,ocrType=1
        )
        if not combatScreenOpened:
            wait(lambda: False, 1)
        while timeout > 0 and not combatScreenOpened:
            if self.uwtask.hasSingleLineWordsInArea(
                "huamei", A=self.nameBoardInPrePanel,ocrType=1
            ):
                break
            if self.uwtask.checkStopped():
                return self.findOpponentOrReturn(opponentsInList, opponents, town)
            timeout -= 1
            wait(lambda: False, 1)
        if timeout == 0:
            wait(lambda: self.instance.clickPointV2(720, 862), 2)
            if self.uwtask.hasSingleLineWordsInArea(
                "huamei", A=self.nameBoardInPrePanel,ocrType=1
            ):
                doAndWaitUntilBy(
                    lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon),
                    lambda: self.uwtask.inWater(),
                    1,
                    1,
                )
            return self.findOpponentOrReturn(opponentsInList, opponents, town)

        def clickIntoBattle():
            self.instance.clickPointV2(682,833)
            # for small boss, enable only when required. Might cause stop of ship as 2nd click clicks after screen goes to sea.
            # self.instance.clickPointV2(726,820)

        if self.uwtask.hasArrayStringInSingleLineWords(
            opponents, A=[1215,115,1359,144]
        ):  # and not self.uwtask.hasSingleLineWordsInArea("pirate",A=[1187,129,1396,159])):
            self.uwtask.print("准备开战")
            return continueWithUntilBy(
                lambda: clickIntoBattle(),
                lambda: self.uwtask.hasSingleLineWordsInArea(
                    "战斗", A=[685,12,759,30]
                ),
                3,
                timeout=10,
            )
        continueWithUntilBy(
            lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon),
            lambda: self.uwtask.inWater(),
            1,
            30,
        )
        self.opentimeout += 1
        if self.opentimeout > 2:
            self.goBackPort(town)
            return False
        return self.findOpponentOrReturn(opponentsInList, opponents, town)
