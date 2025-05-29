import sys
import os
import json
import copy

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

from images import getOCRfromImageBlob
from utils import *
from FrontTask import FrontTask

import time
import datetime as dt
import random
import os
from constants import (
    villageTradeList,
    cityNames,
    dailyJobConf,
    yawuruRouteBase,
    routeLists,
    opponentNames,
    monthToRoute,
    bartingMonthToRoute,
    opponentsInList,
    maticBarterTrade,
    checkInnCities,
    samiRouteBase,
    sami,
)


def importBattle():
    from Battle import Battle

    return Battle


def importMarket():
    from Market import Market

    return Market


def importSB():
    from Sb import Sb

    return Sb


class UWTask(FrontTask):
    rightCatePoint1 = 1266, 81
    rightCatePoint2 = 1306, 74
    rightCatePoint3 = 1358, 79

    titleArea = [39, 6, 176, 41]
    rightTopTownIcon = 1407, 22
    leftTopBackBtn = 24, 16
    inTownCityNameArea = [105, 14, 208, 40]
    inScreenConfirmYesButton = 1071, 800
    enterCityButton = 1316, 845
    outSeaWaterTitle = [64, 12, 193, 41]
    randomPoint = 1115, 586
    mapIcon = 1412, 172
    noticeTitleArea = [684, 303, 763, 325]
    largerNoticeTitleArea = [664, 282, 776, 342]
    noticeOK = 767, 574
    hideNoticeTick = 667, 552
    searchClick = 191,64
    openSearchBar = 33, 74
    searchBarTextArea = [73, 57, 230, 84]
    menuCompany = [182, 13, 252, 38]
    depotClick = 1393, 95
    cargoClick = 32, 291
    cargoTag = [1330, 87, 1400, 112]
    sailToCityArea = [676, 833, 770, 853]
    firstCityClickInMap = 102, 90
    redistributeTitle = [656, 242, 779, 274]
    shipSpeedArea = [1206, 117, 1219, 129]
    gotocityClickInMap = 721, 861
    bargainNoBtn = 1070, 723
    landingClickBtn = 98, 699
    startAdvClickInPage = 782, 563
    advCheckoutTitle = [670, 241, 768, 271]
    inAdvRoundCount = [1319,119,1347,135]
    clickIntoCharProfile = 123, 36
    clickToggleProtection = 40, 223
    checkLandingBtnTuple=(104, 698, (220, 219, 215))
    endDiggingBtn=1351,248
    dialogueYesArea=1028,780,1112,824
    dialogueYesClick=1064,807
    departSecondLineArea = [1237, 486, 1370, 505]
    departSecondArrowBtn = 1411, 493
    departBtn = 1317, 623
    departRestockOkBtn = 777, 589


    # VM screen size: 1440x900 @ 90%

    syncBetweenUsers = True
    currentCity = "拉斯帕尔"
    sbCity = None
    sbOptions = []
    pickedUpShip = False
    firstBuyFin = False
    secondBuyFin = False
    justStartsSecondBuy = False
    # 860=14mins
    waitForCityTimeOut = 960
    hasSelectedMap = 0
    routeOption = 4
    routeList = []
    allCityList = cityNames
    battleMode = "run"
    battleCity = ""
    goBM = True
    initialRun = True
    lastExecuted = None
    focusedBarterTrade = False
    apacheFriendly = None
    liquorStock = None
    craftStock = None
    dailyConfFile = os.path.abspath(__file__ + "\\..\\dailyConfFile.json")
    villageTradeList = copy.copy(villageTradeList)
    efficientHireInn = False
    dailyCheckedBattlePlaceLanding = False

    def testTask(self):
        self.click()
        self.report()
        self.initMarket()
        self.bartingTrade(yawuruRouteBase)
        self.getStockFromType("crafts")
        self.specialConfUpdate()
        self.market.barterInVillage({**sami})
        self.startTradeByConfs(1)
        battle = importBattle()(self.simulatorInstance, self)
        self.goToRoute({"route": 2, "target": "杭州"})
        print(
            hasOneArrayStringSimilarToString(
                "lawlsswata", ["lawlesswaters", "dangerouswaters", "safewaters"]
            )
        )
        self.changeFleet(2)
        self.checkForDailyPopup()
        # screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2()
        # self.saveImageToFile(screenshotBlob, relaPath="\\..\\..\\assets\\screenshots\\UW",filename="test.jpg")
        self.setCurrentCityFromScreen()
        self.checkReachCity()

        self.dumpCrew()
        wait(
            lambda: self.clickWithImage(
                "tourmaline", A=[187, 99, 949, 395], imagePrefix="products"
            ),
            1,
        )

    def click(self):
        while True:
            wait(lambda: self.simulatorInstance.rightClickPointV2(1418, 310), 5)

    def initMarket(self):
        self.market = importMarket()(self.simulatorInstance, self)

    def inCityList(self, cityList=None):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(
                A=self.inTownCityNameArea
            )
            # self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType=4)
            if len(ocrObj[0]) == 0:
                return False
            str = "".join(ocrObj[0])
            if "water" in str.lower():
                return False
            self.print(" ocred city: " + str)
            if cityList == None:
                cityList = cityNames
            for city in cityList:
                if isStringSameOrSimilar(city, str.lower()):
                    self.currentCity = city
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def setCurrentCityFromScreen(self):
        self.inCityList(self.allCityList)

    def getRouteNoFromApacheStats(self):
        if self.apacheFriendly > 90000:
            if self.craftStock in [2, 3, 4]:
                return 14
                # return 14
            # elif self.liquorStock in [1, 2, 3, 4]:
            #     return 9
            else:
                return 14
        else:
            if self.liquorStock in [2, 3, 4]:
                return 9
            else:
                return 14

    def setRouteOptionFromScreen(self):
        month = self.getSingleLineWordsInArea(A=[1339, 192, 1355, 205], ocrType=2)
        if self.focusedBarterTrade:
            mapping = bartingMonthToRoute
            if self.apacheFriendly:
                for month in mapping.keys():
                    mapping[month] = self.getRouteNoFromApacheStats()
        else:
            mapping = monthToRoute
        if month and mapping.get(month):
            self.routeOption = mapping.get(month)

    def setRouteOption(self, routeOption: int = False):
        if routeOption:
            self.routeOption = routeOption
        else:
            self.setRouteOptionFromScreen()
        self.routeList = routeLists[self.routeOption]
        self.allCityList = cityNames
        for key, value in self.villageTradeList.items():
            if value.get("buyCities"):
                addNonExistArrayToArray(self.allCityList, value.get("buyCities"))
            if value.get("supplyCities"):
                addNonExistArrayToArray(self.allCityList, value.get("supplyCities"))
            if value.get("afterVillageSupplyCities"):
                addNonExistArrayToArray(
                    self.allCityList, value.get("afterVillageSupplyCities")
                )
            if value.get("afterVillageBuyCities"):
                addNonExistArrayToArray(
                    self.allCityList, value.get("afterVillageBuyCities")
                )
        addNonExistArrayToArray(self.allCityList, ["塞得港", "科哈塞特", "苏伊士"])
        self.allCityList += [
            dailyJobConf["merchatQuestCity"],
            dailyJobConf["buffCity"],
            dailyJobConf["landingCity"],
            dailyJobConf["endBattleCity"],
            dailyJobConf["reportAndAdvQuestCity"],
            self.battleCity,
        ]
        for routeObject in self.routeList:
            if routeObject.get("buyCities"):
                addNonExistArrayToArray(self.allCityList, routeObject.get("buyCities"))
            if routeObject.get("supplyCities"):
                addNonExistArrayToArray(
                    self.allCityList, routeObject.get("supplyCities")
                )
            if routeObject.get("sellCityOptions"):
                addNonExistArrayToArray(
                    self.allCityList, routeObject.get("sellCityOptions")
                )
            if routeObject.get("buyProductsAfterSupplyCities"):
                addNonExistArrayToArray(
                    self.allCityList, routeObject.get("buyProductsAfterSupplyCities")
                )
            if routeObject.get("afterSellCities"):
                addNonExistArrayToArray(
                    self.allCityList, routeObject.get("afterSellCities")
                )
            if routeObject.get("sellCities"):
                self.allCityList += list(
                    map(lambda x: x["name"], routeObject["sellCities"])
                )
            if routeObject.get("secondSellOptions"):
                for element in routeObject.get("secondSellOptions"):
                    addNonExistArrayToArray(self.allCityList, element.get("cities"))

    def checkReachCity(self):
        with open(os.path.abspath(__file__ + "\\..\\reachCity.txt"), "r") as f:
            reachCity = f.readline()
        if reachCity == self.currentCity:
            self.sendNotification(f"You have reached {reachCity}")
            with open(os.path.abspath(__file__ + "\\..\\reachCity.txt"), "w") as f:
                f.write("")
            self.print("reached city: " + reachCity)
            time.sleep(1200)

    def playNotification(self):
        soundPath = os.path.abspath(__file__ + "\\..\\..\\assets\\alert1.mp3")
        # print(soundPath)
        # playsound("e:\\Workspaces\\Projects\\eveHelper2\\assets\\alert1.mp3")
        # playsound(soundPath)

    def findCityAndClick(self, cityName=None, noExpect=None, backup=None):
        if cityName == None:
            index = cityNames.index(self.currentCity)
            nextCityName = None
            if (index + 1) > len(cityNames) - 1:
                nextCityName = cityNames[0]
            else:
                nextCityName = cityNames[index + 1]
        else:
            nextCityName = cityName
        self.print(nextCityName)

        # height between 47
        firstPosi = (1253, 228)
        area = [1262, 211, 1355, 233]
        index = 0
        found = False
        while not (found) and index < 8:
            yDiff = int(index * 47)
            if self.hasSingleLineWordsInArea(
                nextCityName, A=[area[0], area[1] + yDiff, area[2], area[3] + yDiff]
            ):
                found = True
                break
            index += 1

        if index == 8:
            self.hasSelectedMap = 0
            self.selectCityFromMapAndMove(nextCityName, backup)
        else:
            # click out any message
            wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint), 0)
            if noExpect:
                doMoreTimesWithWait(
                    lambda: self.simulatorInstance.clickPointV2(
                        firstPosi[0], firstPosi[1] + int(index * 58.3)
                    ),
                    3,
                    1,
                )
            else:
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(
                        firstPosi[0], firstPosi[1] + int(index * 51.8)
                    ),
                    lambda: self.hasSingleLineWordsInArea(
                        nextCityName, A=self.sailToCityArea
                    ),
                    3,
                    30,
                    1,
                )

    def goToHarbor(self):
        self.print("去码头")
        self.clickInMenu(["出港所"], ["出港所"])

    def restock(self):
        self.print("补给")
        firstLineArea = [1234, 398, 1343, 422]
        firstArrowBtn = 1410, 409

        thirdLineArea = [1216, 511, 1373, 530]
        thirdArrowBtn = 1409, 521
        # Repair ship
        while self.hasSingleLineWordsInArea("不足", A=thirdLineArea):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*thirdArrowBtn),
                lambda: self.hasSingleLineWordsInArea("修理", A=self.titleArea),
            )
            wait(lambda: self.simulatorInstance.clickPointV2(1156, 862), 1)

            def click():
                wait(lambda: self.simulatorInstance.clickPointV2(1298, 867), 1)
                doMoreTimesWithWait(
                    lambda: self.simulatorInstance.clickPointV2(*self.departRestockOkBtn), 2
                )

            doAndWaitUntilBy(
                click, lambda: self.hasSingleLineWordsInArea("出港所", A=self.titleArea)
            )
        # Restore crew
        while self.hasSingleLineWordsInArea("不足", A=self.departSecondLineArea):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.departSecondArrowBtn),
                lambda: self.hasSingleLineWordsInArea("船员", A=self.titleArea),
            )

            def click2():
                wait(lambda: self.simulatorInstance.longerClickPointV2(1296, 451), 2)
                doMoreTimesWithWait(
                    lambda: self.simulatorInstance.clickPointV2(*self.departRestockOkBtn), 2
                )

            doAndWaitUntilBy(
                click2,
                lambda: self.hasSingleLineWordsInArea("出港所", A=self.titleArea),
                1,
                2,
            )
        # Remove extra crew
        if self.hasSingleLineWordsInArea("超员", A=self.departSecondLineArea):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.departSecondArrowBtn),
                lambda: self.hasSingleLineWordsInArea("船员", A=self.titleArea),
                1,
                2,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(228, 862),
                lambda: self.hasArrayStringEqualMultiLineWords(
                    ["通知"], A=self.largerNoticeTitleArea
                ),
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),
                lambda: self.hasSingleLineWordsInArea("分配", A=self.redistributeTitle),
            )
            self.redistributeMinimum()
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),
                lambda: self.hasSingleLineWordsInArea("出港所", A=self.titleArea),
                1,
                2,
            )
        # Destroy excess
        if self.hasSingleLineWordsInArea("超载出售", A=[1283, 600, 1342, 625]):
            wait(lambda: self.simulatorInstance.clickPointV2(1299, 612), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint), 1)
        # solve overload
        while self.hasSingleLineWordsInArea("发生超载", A=firstLineArea):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*firstArrowBtn),
                lambda: self.hasSingleLineWordsInArea("补给", A=self.titleArea),
                1,
                1,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(537, 374),
                lambda: self.hasSingleLineWordsInArea(
                    "货舱管理", A=[682, 242, 763, 269]
                ),
            )
            wait(lambda: self.simulatorInstance.clickPointV2(930, 639), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(712, 638), 1)  # ok
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),
                lambda: self.hasSingleLineWordsInArea("出港所", A=self.titleArea),
                1,
                2,
            )

    def inWater(self):
        return self.hasSingleLineWordsInArea(
            "海",
            A=self.outSeaWaterTitle
        )

    def depart(self, littleMove=True):
        def clickAndStock():
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.randomPoint), 2, 0.2
            )
            self.restock()

        def clickAndStockBackup():
            self.checkForDailyPopup()
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.randomPoint), 2, 0.2
            )
            if self.hasSingleLineWordsInArea("出港所", A=self.titleArea):
                self.restock()
                self.simulatorInstance.clickPointV2(*self.departBtn)

        clickAndStock()
        self.print("出海")
        self.simulatorInstance.longerClickPointV2(*self.departBtn)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.departBtn),
            lambda: self.inWater(),
            4,
            1,
            backupFunc=clickAndStockBackup,
            timeout=30,
        )
        time.sleep(2)
        if littleMove:
            # Stop the ship on rare case it goes back town
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(41, 673),
                lambda: self.checkStopped(),
                3,
                firstWait=2,
            )
            time.sleep(2)
        self.checkForDailyPopup(5)

    def selectNextCity(self):
        self.print("选城市")
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2), 2, 0
        )
        self.findCityAndClick()

    def clearSearch(self):
        wait(lambda: self.simulatorInstance.clickPointV2(*self.searchClick), 1)
        self.simulatorInstance.send_backspaces()

    def selectCityFromMapAndMove(self, cityname, backup=None):
        def mapBackup():
            self.print("cant move, map again")
            if backup:
                backup()
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: (self.inWater() or self.inCityList(self.allCityList)),
                2,
            )
            self.checkForBasicStuck()
            if self.hasSelectedMap < 5:
                self.hasSelectedMap += 1
                self.selectCityFromMapAndMove(cityname)

        self.print("select city from map")
        # if not doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1409,201), lambda: self.hasSingleLineWordsInArea("地图", A=self.titleArea), 2,1,timeout=15):
        #     return
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.mapIcon),
            lambda: self.hasSingleLineWordsInArea("地图", A=self.titleArea),
            2,
            1,
            timeout=8,
            backupFunc=backup,
        )
        self.simulatorInstance.warmTyping(cityname)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.openSearchBar),
            lambda: self.hasArrayStringEqualSingleLineWords(
                ["搜", cityname], A=self.searchBarTextArea
            ),
            2,
            1,
            timeout=6,
            backupFunc=self.clearSearch,
        )

        def input():
            wait(lambda: self.simulatorInstance.clickPointV2(*self.searchClick), 1)
            wait(lambda: self.simulatorInstance.chineseTypeWrite(cityname), 0)

        doAndWaitUntilBy(
            input,
            lambda: self.hasSingleLineWordsInArea(
                cityname, A=self.searchBarTextArea, looseCheckName=True
            ),
            timeout=5,
        )
        wait(lambda: self.simulatorInstance.send_enter(), 0)
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(*self.firstCityClickInMap), 2, 1
        )
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint), 1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.gotocityClickInMap),
            lambda: (
                self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea)
                or self.inWater()
                or self.inCityList([cityname])
            ),
            5,
            firstWait=15,
            backupFunc=mapBackup,
        )
        if self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea):
            wait(lambda: self.simulatorInstance.clickPointV2(*self.hideNoticeTick), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(*self.noticeOK), 10)
            if self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea):
                wait(
                    lambda: self.simulatorInstance.clickPointV2(*self.hideNoticeTick), 1
                )
                wait(lambda: self.simulatorInstance.clickPointV2(*self.noticeOK), 10)
        if not doAndWaitUntilBy(
            lambda: False,
            lambda: (self.inWater() or self.inCityList([cityname])),
            1,
            1,
            timeout=30,
            backupFunc=mapBackup,
        ):
            return
        if self.inWater() and (
            not self.hasSingleLineWordsInArea(cityname, A=self.sailToCityArea)
            or self.checkStopped()
        ):
            mapBackup()

    # def checkForDisaster(self):
    #     #click disaster icon
    #     wait(lambda: self.simulatorInstance.clickPointV2(637,345),1)
    #     if(self.hasSingleLineWordsInArea("miracle",A=[1076,602,1144,626])):
    #         #click use tool
    #         wait(lambda: self.simulatorInstance.clickPointV2(1094,547),2)
    #         #click yes
    #         wait(lambda: self.simulatorInstance.clickPointV2(*self.inScreenConfirmYesButton),2)

    def checkBattle(self):
        if self.hasSingleLineWordsInArea("retreat", A=[756, 549, 848, 577]):
            battle = importBattle()(self.simulatorInstance, self)
            if self.battleMode == "run":
                battle.suppressBattle()
            elif self.battleMode == "battle":
                battle.doBattle()

    def clickEnterCityButton(self):
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.rightClickPointV2(*self.enterCityButton),
            2,
            0.5,
        )

    def checkBeforeCity(self):
        if (
            self.hasSingleLineWordsInArea("adjacent", A=[1360, 273, 1430, 293])
            and self.checkStopped()
        ):
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(1243, 259), 2, 0.5
            )

    def inJourneyTask(self):
        self.checkBattle()
        self.checkForGiftAndReceive()
        self.clickEnterCityButton()
        # self.checkBeforeCity()

    def checkForBasicStuck(self):
        self.checkForDailyPopup()
        # Check for special purchase
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(994, 290), 2)
        if self.hasSingleLineWordsInArea("notice", A=[555, 379, 600, 401]):
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(859, 507), 5, 10
            )
        if self.hasSingleLineWordsInArea("notice", A=[684, 282, 755, 305]):
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(713, 595), 5, 10
            )
        if self.hasSingleLineWordsInArea("info", A=[452, 292, 546, 316]):
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(813, 436), 5, 10
            )
        if (
            self.hasSingleLineWordsInArea("auto", A=[139, 82, 192, 102])
            or self.hasSingleLineWordsInArea("ok", A=importBattle().battleEnd["okBtn"])
            or self.hasSingleLineWordsInArea(
                "close", A=importBattle().battleEnd["okBtn"]
            )
        ):
            battle = importBattle()(self.simulatorInstance, self)
            battle.suppressBattle()

    def fishing(self):
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(288, 792),
            lambda: self.hasSingleLineWordsInArea("fishing", A=[709, 218, 780, 246]),
            2,
            2,
        )
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(1004, 575), 2, 1
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(785, 663),
            lambda: not self.hasSingleLineWordsInArea(
                "fishing", A=[709, 218, 780, 246]
            ),
            2,
            2,
        )

    def waitForCity(
        self, cityList=None, targetCity=None, routeMode=False, fishing=False
    ):
        self.print("航行中")

        def backupFunc():
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: (self.inWater() or self.inCityList(cityList)),
                2,
            )
            self.checkForBasicStuck()
            time.sleep(10)
            wait(lambda: self.findCityAndClick(targetCity), 40)
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),
                4,
                5,
            )

        if fishing:
            self.fishing()
            time.sleep(240)
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1381, 423),
                lambda: self.hasSingleLineWordsInArea("notice", A=[685, 270, 761, 299]),
                2,
                2,
                timeout=10,
            )
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(780, 610), 3
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: (self.inWater() or self.inCityList(cityList)),
                2,
            )
        if routeMode:
            continueWithUntilByWithBackup(
                lambda: self.inJourneyTask(),
                lambda: self.inCityList(cityList),
                8,
                timeout=4500,
                notifyFunc=lambda: self.print("route city not found, wait for 8s"),
            )
        else:
            continueWithUntilByWithBackup(
                lambda: self.inJourneyTask(),
                lambda: self.inCityList(cityList),
                8,
                timeout=self.waitForCityTimeOut,
                notifyFunc=lambda: self.print("not found, wait for 8s"),
                backupFunc=backupFunc,
            )
        self.hasSelectedMap = 0
        self.print("click twice")
        self.clickEnterCityButton()

    def checkForGiftAndReceive(self):
        if self.isPositionColorSimilarTo(1234, 8, (253, 72, 54)):
            wait(lambda: self.simulatorInstance.clickPointV2(1215, 20), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(448, 633), 1)
            if self.hasArrayStringEqualMultiLineWords(
                ["通知"], A=self.largerNoticeTitleArea
            ):
                wait(lambda: self.simulatorInstance.clickPointV2(753, 578))
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),
                2,
                0.2,
            )

    def checkForDailyPopup(self, delay=0):
        hour = dt.datetime.now().hour
        if hour in [1, 2, 3, 4]:
            time.sleep(delay)
            if self.hasSingleLineWordsInArea("活动", A=[487, 216, 533, 239]):
                wait(lambda: self.simulatorInstance.clickPointV2(1082, 248), 2)
                doMoreTimesWithWait(
                    lambda: self.simulatorInstance.rightClickPointV2(
                        *self.enterCityButton
                    )
                )
            wait(lambda: self.simulatorInstance.clickPointV2(1082, 248), 2)

    # def checkForTreasure(self):
    #     chestCood=self.hasImageInScreen("chest",A=[173,48,1051,659])
    #     if(chestCood):
    #         doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(chestCood[0]+10,chestCood[1]+18),2,0,disableWait=True)

    def basicMarket(self):
        self.print("去超市")
        self.clickInMenu(["交易所"], ["交易所"])
        # sell
        self.market.sellGoodsWithMargin()
        time.sleep(3)

        # buy
        self.market.buyExpensive()

        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList(),
            3,
            2,
        )

    # need to provide a city list
    def sellInCity(self, cityName, simple=False, types=None, negoTimes=True):
        self.print("去超市")
        self.clickInMenu(["交易所"], ["交易所"])

        # sell
        self.market.sellGoodsWithMargin(simple, types, negoTimes)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(132,705), 2, 1)
        time.sleep(3)

        def backup():
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.bargainNoBtn), 3, 2
            )
            time.sleep(5)
            self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.randomPoint), 2, 1
            )

        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList([cityName]),
            3,
            2,
            backupFunc=backup,
        )

    def buyInCity(
        self,
        cityList,
        products,
        buyStrategy=False,
        marketMode=0,
        returnResultsLambda=None,
        buyNotProducts=[],
    ):
        self.print("去超市")
        market = importMarket()(self.simulatorInstance, self, marketMode=marketMode)

        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2), 1, 1
        )
        self.clickInMenu(["交易所"], ["交易所"])
        # doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1253,294), lambda: self.hasSingleLineWordsInArea("交易所", A=self.titleArea) or self.hasSingleLineWordsInArea("skip", A=[1330,5,1384,39]),2,2)

        results = {}
        # buy
        match buyStrategy:
            case "twice":
                results = (
                    market.buyProductsInCityTwice(
                        products, returnResultsLambda=returnResultsLambda
                    )
                    or {}
                )
            case "useGem":
                market.buyProductsInCityTwiceWithGem(products)
            case _:
                market.buyProductsInMarket(products, buyNotProducts)
                if returnResultsLambda:
                    results = returnResultsLambda()

        time.sleep(3)

        def backup():
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.bargainNoBtn), 3, 2
            )
            time.sleep(5)
            self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.randomPoint), 2, 1
            )

        continueWithUntilByWithBackup(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList(cityList),
            3,
            30,
            backupFunc=backup,
        )
        if returnResultsLambda:
            return results

    def clickInMenu(
        self, menuArray, inTitleArray, infinite=False, startIndex=0, fallbackIndex=1
    ):
        wait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2), 1)
        area = [1262, 214, 1340, 235]
        index = startIndex

        def runFallback():
            yDiff = int(fallbackIndex % 15 * 34)
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1252, 225 + yDiff),
                lambda: self.hasArrayStringEqualSingleLineWords(
                    inTitleArray, A=self.titleArea
                ),
            )

        while index < 300:
            yDiff = int(index % 15 * 34)
            if self.hasArrayStringEqualSingleLineWords(
                menuArray, A=[area[0], area[1] + yDiff, area[2], area[3] + yDiff]
            ):
                doAndWaitUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(1252, 225 + yDiff),
                    lambda: self.hasArrayStringEqualSingleLineWords(
                        inTitleArray, A=self.titleArea
                    ),
                )
                return True
            index += 1
            if not infinite and index == 30:
                runFallback()
                return False
            time.sleep(0.1)
        runFallback()
        return False

    def buyBlackMarket(self, city):
        if not self.goBM:
            self.print("不去黑店")
            return
        if self.market.shouldBuyBlackMarket(city):
            self.print("去黑店")
            self.market.buyBlackMarket(city)

            def backup():
                self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)
                if self.hasSingleLineWordsInArea("notice", [685, 281, 755, 305]):
                    self.simulatorInstance.clickPointV2(784, 595)

            continueWithUntilByWithBackup(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.inCityList([city]),
                2,
                15,
                backupFunc=backup,
            )

    def shipBuilding(self, options=[0], city="faro", times=30):
        self.print("SB 开始")
        self.pickedUpShip = False
        sb = importSB()(self.simulatorInstance, self)
        timeout = times * 1400
        while timeout > 0:
            sb.gotoShipyard()
            for option in options:
                sb.pickup()
            for index, option in enumerate(options):
                sb.dismantle(index)
            for option in options:
                sb.build(option)
            sb.goBackTown(city)
            timeout -= 1400
            if times != 1:
                time.sleep(1400)
                self.print("一轮完成，开始等23分")

    def enableSB(self, cityName, options):
        self.sbCity = cityName
        self.sbOptions = options

    def checkSB(self):
        if self.sbCity and self.currentCity == self.sbCity:
            self.shipBuilding(self.sbOptions, self.sbCity, 1)

    def checkInn(self, city, routeObject=None):
        if routeObject and not routeObject.get("checkInnCities"):
            return
        if not hasOneArrayStringSimilarToString(city, checkInnCities):
            return
        self.clickInMenu(["旅馆"], ["旅馆"], infinite=False, fallbackIndex=4)
        time.sleep(3)
        if not self.hasSingleLineWordsInArea("无法", A=[8, 54, 57, 70]):
            self.sendNotification("找到人了")
            time.sleep(100)
        if not self.isPositionColorSimilarTo(1320, 612, (177, 177, 177)):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(34, 130),
                lambda: self.hasSingleLineWordsInArea("聚餐", A=self.titleArea),
                2,
                1,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(720, 860),
                lambda: self.hasSingleLineWordsInArea(
                    "一键聚餐", A=[681, 237, 754, 266]
                ),
                2,
                1,
                timeout=10,
            )
            if (
                self.efficientHireInn
                and self.isPositionColorSimilarTo(637, 276, (211, 185, 78))
                and self.isPositionColorSimilarTo(638, 345, (211, 185, 78))
            ):
                wait(lambda: self.simulatorInstance.clickPointV2(637, 276))
                wait(lambda: self.simulatorInstance.clickPointV2(638, 345))
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(742, 643), 3, 1
            )

        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList([city]),
            2,
            16,
        )

    def startJourney(self):
        # self.buyBlackMarket(self.currentCity)
        # self.checkSB()
        self.goToHarbor()
        self.depart()
        self.selectNextCity()
        self.waitForCity()
        self.basicMarket()
        self.checkReachCity()
        time.sleep(random.randint(3, 5))

    def getTime(self):
        try:
            timeOCR = self.getSingleLineWordsInArea(A=[1382, 190, 1428, 205], ocrType=2)
            return int(timeOCR[0:2])
        except Exception as e:
            print(e)
            return 12

    def healInjury(self, city):
        self.clickInMenu(["旅馆"], ["旅馆"], infinite=True)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(56,232),
            lambda: self.hasSingleLineWordsInArea("航海士", A=self.titleArea),
            2,
            1,
        )
        if self.isPositionColorSimilarTo(386, 58, (253, 53, 51)):
            wait(lambda: self.simulatorInstance.clickPointV2(354, 65), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(1090, 868), 1)
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1299, 444),
                lambda: self.hasArrayStringEqualMultiLineWords(
                    ["通知"], A=self.largerNoticeTitleArea
                ),
            )
            wait(lambda: self.simulatorInstance.clickPointV2(775, 587), 1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList([city]),
        )

    def redistributeMinimum(self):
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(499, 639), 2, 1)
        wait(lambda: self.simulatorInstance.clickPointV2(975, 642), 1)  # apply
        wait(lambda: self.simulatorInstance.clickPointV2(782, 591), 1)  # ok

    def changeFleet(self, fleetNo, simple=False):
        if not fleetNo:
            return
        for x in range(0, 1):
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.hasSingleLineWordsInArea("船队", A=self.menuCompany),
                2,
                15,
                firstWait=2,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1209, 152),
                lambda: self.hasSingleLineWordsInArea("分配", A=self.titleArea),
                1,
                1,
                timeout=10,
            )  # ship
            # doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1069,90),lambda: self.hasSingleLineWordsInArea("settings", A=[991,123,1058,145]),1,1,timeout=10)#assign
            # doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1022,138),lambda: self.hasSingleLineWordsInArea("分配", A=[637,215,735,237]),1,1,timeout=10)#settings
            y = int(129 + int(54 * (fleetNo - 1)))
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(99, y), 2, 1
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1309, 859),
                lambda: self.hasSingleLineWordsInArea("对象", A=[656, 345, 785, 369]),
                1,
                1,
                timeout=10,
            )  # apply
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(754, 540),
                lambda: not self.hasSingleLineWordsInArea(
                    "对象", A=[656, 345, 785, 369]
                ),
                1,
                1,
                timeout=10,
            )  # ok
            # No more check, can change fleet with injured
            # if(self.hasSingleLineWordsInArea("assign", A=[748,655,813,678])):
            #     doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(785,666),lambda: not self.hasSingleLineWordsInArea("ship", A=[703,431,758,449]),1,1,timeout=10)#injury confirm
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.inCityList(self.allCityList),
                1,
                15,
            )
            if not simple:
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                    lambda: self.hasSingleLineWordsInArea("船队", A=self.menuCompany),
                    2,
                    1,
                    firstWait=2,
                )
                doAndWaitUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(1273, 93),
                    lambda: self.hasSingleLineWordsInArea("舰队", A=self.titleArea),
                    2,
                    1,
                )
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(1357, 854),
                    lambda: self.hasSingleLineWordsInArea(
                        "分配", A=self.redistributeTitle
                    ),
                )
                self.redistributeMinimum()
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                    lambda: self.inCityList(self.allCityList),
                )

    def dumpCrew(self):
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1274, 22),
            lambda: self.hasSingleLineWordsInArea("舰队", A=self.titleArea),
            2,
            1,
            firstWait=2,
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1124, 110),
            lambda: self.hasSingleLineWordsInArea("manage", A=self.titleArea),
            2,
            1,
        )
        wait(lambda: self.simulatorInstance.clickPointV2(1220, 688), 1)
        for looper in [0, 1, 2, 3, 4]:
            while True:
                currentCrew = self.getSingleLineWordsInArea(
                    A=[753, 202 + looper * 79, 772, 219 + looper * 79], ocrType=2
                )
                try:
                    if currentCrew and int(currentCrew) < 38:
                        break
                except:
                    print("int conversation failed")
                doMoreTimesWithWait(
                    lambda: self.simulatorInstance.clickPointV2(584, 211 + looper * 79),
                    3,
                    0,
                    disableWait=True,
                )
        for looper in [0, 1, 2, 3, 4]:
            while True:
                currentCrew = self.getSingleLineWordsInArea(
                    A=[753, 202 + looper * 79, 772, 219 + looper * 79], ocrType=2
                )
                try:
                    if currentCrew and int(currentCrew) < 34:
                        break
                except:
                    print("int conversation failed")
                wait(
                    lambda: self.simulatorInstance.clickPointV2(584, 211 + looper * 79),
                    0,
                    disableWait=True,
                )

        wait(lambda: self.simulatorInstance.clickPointV2(950, 580), 1)
        wait(lambda: self.simulatorInstance.clickPointV2(721, 486), 1)

        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inWater(),
            1,
            30,
        )

    # cityList is an array to contain the target city
    def gotoCity(
        self,
        cityname,
        cityList=None,
        dumpCrew=False,
        useExtra=lambda: False,
        express=False,
        fishing=False,
    ):
        if express:
            self.selectCityFromMapAndMove(cityname)
            self.waitForCity(
                cityList if cityList else [cityname],
                targetCity=cityname,
                fishing=fishing,
            )
        else:
            self.goToHarbor()
            self.depart()
            useExtra()
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2), 2, 1
            )
            wait(lambda: self.findCityAndClick(cityname), 2)
            # if(dumpCrew):
            # self.dumpCrew()
            self.waitForCity(
                cityList if cityList else [cityname],
                targetCity=cityname,
                fishing=fishing,
            )
        self.checkReachCity()
        self.sendMessage("UW", "reached city of " + cityname)

    def checkStopped(self):
        return self.getNumberFromSingleLineInArea(self.shipSpeedArea) == 0

    def goToRoute(self, element):
        def backup():
            self.print("cant move, map again")
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: (self.inWater() or self.inCityList(self.allCityList)),
                2,
            )
            self.checkForBasicStuck()
            if self.hasSelectedMap < 5:
                self.hasSelectedMap += 1
                self.goToRoute(element)

        # element: {"route":3,"target":"杜法尔"}
        city = element["target"]
        self.print("select route from map")
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.mapIcon),
            lambda: self.hasSingleLineWordsInArea("地图", A=self.titleArea),
            2,
            1,
            timeout=15,
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(805, 19), 2, 1)
        # 28,70 ->5th 27,194
        y = int(69 + int(29 * (element["route"] - 1)))
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(127, y), 2)
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint), 1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.gotocityClickInMap),
            lambda: (
                self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea)
                or self.inWater()
                or self.inCityList(self.allCityList)
            ),
            5,
            firstWait=15,
        )
        if self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea):
            wait(lambda: self.simulatorInstance.clickPointV2(*self.hideNoticeTick), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(*self.noticeOK), 10)
        if not doAndWaitUntilBy(
            lambda: False,
            lambda: self.inWater(),
            1,
            1,
            timeout=30,
            backupFunc=backup,
        ):
            return
        if self.inWater() and (
            not self.hasSingleLineWordsInArea(city, A=self.sailToCityArea)
            or self.checkStopped()
        ):
            backup()
        self.waitForCity(self.allCityList, targetCity=city, routeMode=True)
        self.sendMessage("UW", "reached city of " + city)

    def goToVillage(self, village, villageObject=None, fishing=False):
        def reachedVillage():
            return self.hasSingleLineWordsInArea("村庄", A=self.titleArea)

        def backup():
            self.print("cant move, map again")
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: (self.inWater()),
                2,
            )
            self.checkForBasicStuck()
            if self.hasSelectedMap < 3:
                self.hasSelectedMap += 1
                self.goToVillage(village, villageObject, fishing=fishing)

        self.print("select village from map")
        # if not doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1409,201), lambda: self.hasSingleLineWordsInArea("地图", A=self.titleArea), 2,1,timeout=15):
        #     return
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.mapIcon),
            lambda: self.hasSingleLineWordsInArea("地图", A=self.titleArea),
            2,
            1,
            timeout=15,
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(715, 24), 2, 1)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.openSearchBar),
            lambda: self.hasSingleLineWordsInArea("搜", A=self.searchBarTextArea),
            2,
            1,
            timeout=15,
        )
        shortVillageName = None
        if villageObject and villageObject.get("shortVillageName"):
            shortVillageName = villageObject.get("shortVillageName")

        def input():
            wait(lambda: self.simulatorInstance.clickPointV2(*self.searchClick))
            wait(
                lambda: self.simulatorInstance.chineseTypeWrite(
                    shortVillageName if shortVillageName else village
                ),
                0,
            )

        doAndWaitUntilBy(
            input,
            lambda: self.hasArrayStringEqualSingleLineWords(
                [shortVillageName if shortVillageName else village],
                A=self.searchBarTextArea,
            ),
            timeout=5,
        )
        wait(lambda: self.simulatorInstance.send_enter(), 0)
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(*self.firstCityClickInMap), 3, 1
        )
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint), 1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.gotocityClickInMap),
            lambda: (
                self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea)
                or self.inWater()
                or self.inCityList(self.allCityList)
            ),
            5,
            firstWait=15,
        )
        if self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea):
            wait(lambda: self.simulatorInstance.clickPointV2(*self.hideNoticeTick), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(*self.noticeOK), 10)
        if not doAndWaitUntilBy(
            lambda: False,
            lambda: (
                self.inWater() or self.inCityList(self.allCityList) or reachedVillage()
            ),
            1,
            1,
            timeout=30,
            backupFunc=backup,
        ):
            return
        if self.inWater() and self.checkStopped():
            backup()
        self.print("航行中")
        if fishing:
            self.fishing()
        continueWithUntilByWithBackup(
            lambda: self.inJourneyTask(),
            lambda: reachedVillage(),
            8,
            timeout=self.waitForCityTimeOut,
            notifyFunc=lambda: self.print("not found, wait for 8s"),
            backupFunc=backup,
        )
        self.print("到达村庄")

    def useTradeSkill(self, inCity=False):
        skillMenuArea = (676,282,759,305) if inCity else [678, 275, 762, 312]
        openButton = (40, 717) if inCity else (41, 670)
        okBtn = 768, 583
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*openButton),
            lambda: self.hasSingleLineWordsInArea("命令", A=skillMenuArea),
            1,
        )
        if self.hasArrayStringInSingleLineWords(["话术"], A=[785, 336, 862, 353]):
            wait(lambda: self.simulatorInstance.clickPointV2(853, 492), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(*okBtn), 1)
        if self.hasArrayStringInSingleLineWords(["谈判"], A=[692, 332, 748, 352]):
            wait(lambda: self.simulatorInstance.clickPointV2(734, 492), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(*okBtn), 1)
        if self.hasArrayStringInSingleLineWords(["复兴"], A=[466, 332, 563, 356]):
            # avoid the skill is in cd and the ok click is on other skill and get stuck
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(520, 490),
                lambda: self.hasArrayStringEqualMultiLineWords(
                    ["通知"], A=self.largerNoticeTitleArea
                ),
                timeout=5,
            )
            if self.hasArrayStringEqualMultiLineWords(
                ["通知"], A=self.largerNoticeTitleArea
            ):
                wait(lambda: self.simulatorInstance.clickPointV2(*okBtn), 1)
        if self.hasArrayStringInSingleLineWords(["谈判"], A=[582, 325, 645, 353]):
            wait(lambda: self.simulatorInstance.clickPointV2(597, 464), 1)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*okBtn), 1)
        if self.hasArrayStringInSingleLineWords(["今井"], A=[367, 336, 455, 353]):
            # doAndWaitUntilBy(
            #     lambda: self.simulatorInstance.clickPointV2(401,502),
            #     lambda: self.hasArrayStringEqualMultiLineWords(
            #         ["通知"], A=self.largerNoticeTitleArea
            #     ),
            #     1,
            # )
            # doAndWaitUntilBy(
            #     lambda: self.simulatorInstance.clickPointV2(*okBtn),
            #     lambda: not self.hasArrayStringEqualMultiLineWords(
            #         ["通知"], A=self.largerNoticeTitleArea
            #     ),
            #     1,
            # )
            # doAndWaitUntilBy(
            #     lambda: self.simulatorInstance.clickPointV2(*openButton),
            #     lambda: self.hasSingleLineWordsInArea("命令", A=skillMenuArea),
            #     1,
            # )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(624, 494),
                lambda: self.hasArrayStringEqualMultiLineWords(
                    ["通知"], A=self.largerNoticeTitleArea
                ),
                1,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*okBtn),
                lambda: not self.hasArrayStringEqualMultiLineWords(
                    ["通知"], A=self.largerNoticeTitleArea
                ),
            )
        if self.hasSingleLineWordsInArea("命令", A=skillMenuArea):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.enterCityButton),
                lambda: not self.hasSingleLineWordsInArea("命令", A=skillMenuArea),
                1,
            )

    def shouldFinishTradeAndChangeFleet(self, routeObject):
        if routeObject.get("buyStrategy") == "twice":
            if self.justStartsSecondBuy:
                self.changeFleet(routeObject.get("transportFleet"))
                self.justStartsSecondBuy = False
                if routeObject.get("onlyUseBuyFleetBuy"):
                    self.secondBuyFin = True
                    return True
                self.buyInCity(
                    routeObject["buyCities"],
                    products=routeObject["buyProducts"],
                    buyStrategy=routeObject.get("buyStrategy"),
                )
                return False
            if self.firstBuyFin and not self.secondBuyFin:
                return False
            elif self.firstBuyFin and self.secondBuyFin:
                return True
            else:
                return False
        else:
            if self.firstBuyFin:
                return True

    def getDailyConfValByKey(self, key):
        with open(self.dailyConfFile, "r") as f:
            dailyConf = json.load(f)
            return dailyConf.get(key)

    def updateDailyConfVal(self, key, val):
        with open(self.dailyConfFile, "r") as f:
            dailyConf = json.load(f)
            dailyConf[key] = val
            with open(self.dailyConfFile, "w") as f:
                json.dump(dailyConf, f)

    def doVillageTrade(self, villageKey, villageObject):
        village = villageObject.get("villageName")
        self.print("do village trade to " + village)
        self.goToVillage(
            village, villageObject, fishing=villageObject.get("useFishing")
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(44, 343),
            lambda: self.hasSingleLineWordsInArea("barter", A=self.titleArea),
            2,
            1,
            timeout=10,
        )
        time.sleep(90)
        self.market.barterInVillage(villageObject)
        self.updateDailyConfVal(villageKey, True)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),
            lambda: (self.inWater()),
            2,
        )

    def getTargetVillageObject(self, routeObject):
        if routeObject.get("enableVillageTrade"):
            for village in routeObject.get("villages"):
                # todo disable for new routes, break old route
                # if(village in villageTradeList.keys() and not self.getDailyConfValByKey(village)):
                if village in self.villageTradeList.keys():
                    return (village, self.villageTradeList.get(village))
        return (None, None)

    def getInitialRouteIndex(self):
        self.setCurrentCityFromScreen()
        self.setRouteOption()
        routeObjIndex = 0
        for index, obj in enumerate(self.routeList):
            if obj.get("buyCities") and self.currentCity in obj["buyCities"]:
                routeObjIndex = index
                return routeObjIndex
        if not routeObjIndex:
            self.print("没有在长途城市列表中，中断")
            wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint))
            time.sleep(5)
            return False

    def acceptQuest(self, questNames):
        self.clickInMenu(["公会"], ["公会"])
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(23, 73),
            lambda: self.hasSingleLineWordsInArea("委托", A=self.titleArea),
            2,
            1,
        )

        firstPosi = (1082, 150)
        firstArea = [276, 116, 436, 138]
        gotQuest = False

        x = 0
        while x < 20:
            y = 0
            while y < 5:
                yDiff = int(y % 5 * 84)
                y += 1
                if self.hasArrayStringEqualSingleLineWords(
                    questNames,
                    A=[
                        firstArea[0],
                        firstArea[1] + yDiff,
                        firstArea[2],
                        firstArea[3] + yDiff,
                    ],
                ):
                    doAndWaitUntilBy(
                        lambda: self.simulatorInstance.clickPointV2(
                            firstPosi[0], firstPosi[1] + yDiff
                        ),
                        lambda: self.hasArrayStringEqualMultiLineWords(
                            ["通知"], A=self.largerNoticeTitleArea
                        ),
                    )
                    doAndWaitUntilBy(
                        lambda: self.simulatorInstance.clickPointV2(772, 589),
                        lambda: not self.hasArrayStringEqualMultiLineWords(
                            ["通知"], A=self.largerNoticeTitleArea
                        ),
                    )
                    gotQuest = True
                    break
            # if not self.hasSingleLineWordsInArea("accept", A=[992, 548, 1057, 570]):
            #     break
            if gotQuest:
                break
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1102, 77),
                lambda: self.hasSingleLineWordsInArea("更新", A=[678, 292, 757, 317]),
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(765, 586),
                lambda: not self.hasSingleLineWordsInArea(
                    "更新", A=[678, 292, 757, 317]
                ),
            )
            x += 1
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList(self.allCityList),
            2,
        )
        return gotQuest

    def startMerchantQuest(self):
        if not self.getDailyConfValByKey("merchantQuest"):
            print("go merchant request, TBC")
            self.gotoCity(dailyJobConf.get("merchatQuestCity"))
            if self.acceptQuest(["exchange"]):
                self.changeFleet(4)
                self.bartingTrade(maticBarterTrade)
            self.gotoCity(maticBarterTrade.get("sellCity"), express=True)
            self.changeFleet(6, simple=True)
            self.sellInCity(maticBarterTrade.get("sellCity"), simple=True)
            self.crossTunnel()
            self.changeFleet(2)
            self.updateDailyConfVal("merchantQuest", True)

    def inputNumber(self, inputNumber, triggerXY):
        area = [902, 300, 978, 331]
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*triggerXY),
            lambda: self.hasSingleLineWordsInArea("输入", A=area),
        )

        def getPosition(number):
            if number == 0:
                return 851, 561
            # 定义参考位置
            x_start, y_start = 853, 403  # 1 的位置
            x_end, y_end = 967, 512  # 9 的位置

            # 计算每行和每列的步长
            x_step = (x_end - x_start) // 2  # 每列间距
            y_step = (y_end - y_start) // 2  # 每行间距

            # 确定数字的行号和列号
            row = (number - 1) // 3  # 行号（0, 1, 2）
            col = (number - 1) % 3  # 列号（0, 1, 2）

            # 计算 x, y 坐标
            x = x_start + col * x_step
            y = y_start + row * y_step

            return x, y

        digits = [int(digit) for digit in str(inputNumber)]
        for digit in digits:
            wait(
                lambda: self.simulatorInstance.clickPointV2(*getPosition(digit)),
                seconds=0,
                disableWait=True,
            )
        if self.getNumberFromSingleLineInArea(A=[906, 343, 1052, 365]) != inputNumber:
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),
                lambda: not self.hasSingleLineWordsInArea("输入", A=area),
            )
            self.inputNumber(inputNumber, triggerXY)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1026, 542),
            lambda: not self.hasSingleLineWordsInArea("输入", A=area),
        )

    def report(self):
        reportTitleArea=[672,241,777,270]
        # todo
        # self.changeFleet(dailyJobConf.get("landingFleet"), simple=True)
        self.clickInMenu(["住宅"], ["住宅"])
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(46, 131),
            lambda: self.hasSingleLineWordsInArea("报告", A=self.titleArea),
            2,
            1,
        )
        chestLocation = self.hasImageInScreen("chestInReport", A=[155,207,1144,443])
        if chestLocation:
            chestClick = chestLocation[0] + 5, chestLocation[1] + 5
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*chestClick),
                lambda: self.hasSingleLineWordsInArea("报告", A=reportTitleArea),
            )
            while self.getNumberFromSingleLineInArea(A=[842,553,877,571]) > 200:
                self.inputNumber(200, (981,558))
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(769,636),
                lambda: not self.hasSingleLineWordsInArea(
                    "报告", A=reportTitleArea
                ),
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1229,862),
                lambda: self.hasSingleLineWordsInArea("是", A=self.dialogueYesArea),
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.dialogueYesClick),
                lambda: not self.hasSingleLineWordsInArea(
                    "是", A=self.dialogueYesArea
                ),
            )

        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList(self.allCityList),
            2,
            16,
        )
        self.checkInn(dailyJobConf.get("reportAndAdvQuestCity"))
        self.changeFleet(dailyJobConf.get("basicFleet"))

    def reportAndAdvQuest(self):
        if not self.getDailyConfValByKey("reportAndAdvQuest"):
            self.gotoCity(dailyJobConf.get("reportAndAdvQuestCity"), express=True)
            self.report()

    def doLanding(self, isEverydayLanding=False):
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.landingClickBtn),
            lambda: self.hasSingleLineWordsInArea("探索陆地", A=[1219, 818, 1272, 834]),
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1272, 842),
            lambda: self.hasSingleLineWordsInArea("探险", A=[223, 853, 276, 875]),
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(
                711 if isEverydayLanding else 253, 863
            ),
            lambda: self.hasSingleLineWordsInArea("探险信息", A=self.advCheckoutTitle),
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(894, 632),
            lambda: self.hasSingleLineWordsInArea("连续探险", A=[684, 322, 761, 345]),
        )
        if isEverydayLanding:
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.startAdvClickInPage),
                lambda: self.hasSingleLineWordsInArea("结算", A=self.advCheckoutTitle),
                3,
                timeout=240,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.inWater(),
                2,
            )

    def newLanding(self, routeObject):
        didEverydayLanding = False
        battleInstance = importBattle()(self.simulatorInstance, self)
        self.changeFleet(dailyJobConf.get("landingFleet"), simple=True)
        if routeObject.get("titleNo"):
            self.changeTitle(routeObject.get("titleNo"))
        if routeObject.get("beforeCities"):
            for city in routeObject.get("beforeCities"):
                self.gotoCity(city, self.allCityList, express=True)
                self.checkInn(city, routeObject)
        else:
            self.gotoCity(dailyJobConf.get("landingCity"), express=True)
        self.goToHarbor()
        battleInstance.depart()
        self.goToVillage("百慕大", None)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),
            lambda: (self.inWater()),
            2,
        )
        while not self.isPositionColorSimilarTo(*self.checkLandingBtnTuple):
            self.goToVillage("百慕大", None)
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),
                lambda: (self.inWater()),
                2,
            )
        if not didEverydayLanding:
            self.doLanding(isEverydayLanding=True)
            didEverydayLanding = True
        timesOfLanding = dailyJobConf.get("landingRounds")
        for x in range(timesOfLanding):
            self.doLanding()

            def checkNum(number=None):
                num = self.getNumberFromSingleLineInArea(A=self.inAdvRoundCount)
                if(number):
                    return num and num > number
                return num and num > dailyJobConf.get("landingTimes")

            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(
                    *self.startAdvClickInPage
                ),
                lambda: checkNum(1)
            )
            continueWithUntilBy(
                lambda: None,
                lambda: checkNum()
                or self.hasSingleLineWordsInArea("结算", A=self.advCheckoutTitle),
                timeout=3900,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.endDiggingBtn),
                lambda: self.hasSingleLineWordsInArea("结算", A=self.advCheckoutTitle)
                or self.hasSingleLineWordsInArea("探险信息", A=self.advCheckoutTitle),
                10,
                timeout=50,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.inWater(),
                2,
            )
            self.gotoCity(dailyJobConf.get("landingCity"), express=True)
            if x < timesOfLanding - 1:
                self.goToHarbor()
                battleInstance.depart()
                self.goToVillage("百慕大", None)
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),
                    lambda: (self.inWater()),
                    2,
                )
        self.changeFleet(2)
        self.sellOverload()
        self.updateDailyConfVal("dailyLanding", True)

    def goLanding(self, routeObject):
        battleInstance = importBattle()(self.simulatorInstance, self)
        self.changeFleet(dailyJobConf.get("landingFleet"), simple=True)
        if routeObject.get("titleNo"):
            self.changeTitle(routeObject.get("titleNo"))
        if routeObject.get("beforeCities"):
            for city in routeObject.get("beforeCities"):
                self.gotoCity(city, self.allCityList, express=True)
                self.checkInn(city, routeObject)
        else:
            self.gotoCity(dailyJobConf.get("landingCity"), express=True)
        didEverydayLanding = False

        def goPortAndLeaveWithAdvConfidence():
            self.goToHarbor()
            battleInstance.depart()
            while not self.isPositionColorSimilarTo(*self.checkLandingBtnTuple):
                battleInstance.goBackPort(dailyJobConf.get("landingCity"))
                self.goToHarbor()
                battleInstance.depart()

        goPortAndLeaveWithAdvConfidence()
        if not didEverydayLanding:
            self.doLanding(isEverydayLanding=True)
            didEverydayLanding = True
        timesOfLanding = dailyJobConf.get("landingRounds")

        for x in range(timesOfLanding):
            self.doLanding()

            def checkNum(number=None):
                num = self.getNumberFromSingleLineInArea(A=self.inAdvRoundCount)
                if(number):
                    return num and num > number
                return num and num > dailyJobConf.get("landingTimes")

            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(
                    *self.startAdvClickInPage
                ),
                lambda: checkNum(1)
            )
            continueWithUntilBy(
                lambda: None,
                lambda: checkNum()
                or self.hasSingleLineWordsInArea("结算", A=self.advCheckoutTitle),
                timeout=3900,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.endDiggingBtn),
                lambda: self.hasSingleLineWordsInArea("结算", A=self.advCheckoutTitle)
                or self.hasSingleLineWordsInArea("探险信息", A=self.advCheckoutTitle),
                10,
                timeout=50,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.inWater(),
                2,
            )
            battleInstance.goBackPort(dailyJobConf.get("landingCity"))
            if x < timesOfLanding - 1:
                goPortAndLeaveWithAdvConfidence()
                # continueWithUntilBy(
                #     lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),
                #     lambda: (self.inWater()),
                #     2,
                # )
        if routeObject.get("afterCities"):
            for city in routeObject.get("afterCities"):
                self.gotoCity(city, self.allCityList, express=True)
                self.checkInn(city, routeObject)
        else:
            self.gotoCity(dailyJobConf.get("preLandingCity"), express=True)
        self.changeFleet(dailyJobConf.get("basicFleet"))
        self.sellOverload()
        self.updateDailyConfVal("dailyLanding", True)

    def changeTitle(self, titleNo):
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.hasSingleLineWordsInArea("船队", A=self.menuCompany),
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.clickIntoCharProfile),
            lambda: self.hasSingleLineWordsInArea("船队管理", A=self.titleArea),
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(28, 397),
            lambda: self.hasSingleLineWordsInArea("称号", A=[1260,57,1312,82]),
        )
        # 289,214 xDiff 189.7 yDiff 169
        #
        #
        index = titleNo - 1
        xDiff = int(index % 5 * 194)
        yDiff = int(index / 5) * 172
        # Loop through and find title
        firstClick = (284, 181)
        firstColorCheck = (360, 100)
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(
                firstClick[0] + xDiff, firstClick[1] + yDiff
            ),
            2,
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1285, 449),
            lambda: self.isPositionColorSimilarTo(
                firstColorCheck[0] + xDiff, firstColorCheck[1] + yDiff, (31,224,0)
            ),
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList(self.allCityList),
        )

    def sellOverload(self):
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.hasSingleLineWordsInArea("船队", A=self.menuCompany),
            2,
            15,
            firstWait=2,
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.depotClick),
            lambda: self.hasSingleLineWordsInArea("仓库", A=self.titleArea),
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.cargoClick),
            lambda: self.hasSingleLineWordsInArea("货舱管理", A=self.cargoTag),
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1358, 134), 2)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: (self.inCityList(self.allCityList)),
            2,
        )

    # todo
    def getBuff(self):
        buffCity = dailyJobConf.get("buffCity")
        if buffCity:
            self.gotoCity(buffCity, express=True)
            self.clickInMenu(["圣院"], ["圣院"])
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(32,120),
                lambda: self.hasSingleLineWordsInArea("捐赠", A=self.titleArea),
                2,
                1,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(788,301),
                lambda: self.hasSingleLineWordsInArea("是", A=self.dialogueYesArea),
                2,
                1,
                timeout=10,
            )
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.dialogueYesClick), 2, 1
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.inCityList([buffCity]),
                2,
                16,
            )

    def startDailyBattle(self, battleCity, routeObject):
        self.print("battle starts")
        self.changeFleet(dailyJobConf.get("battleFleet"))
        if routeObject.get("titleNo"):
            self.changeTitle(routeObject.get("titleNo"))
        if routeObject.get("beforeCities"):
            for city in routeObject.get("beforeCities"):
                self.gotoCity(city, self.allCityList, express=True)
                self.checkInn(city, routeObject)
        else:
            self.gotoCity(battleCity, express=True)
        # deactivate protection
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.clickToggleProtection),
            lambda: self.hasArrayStringEqualMultiLineWords(
                ["保护"], A=self.largerNoticeTitleArea
            ),
            2,
            1,
            timeout=5,
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(770, 594), 2, 1)
        self.battleRoute(battleCity)
        # activate protection

        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.clickToggleProtection),
            lambda: self.isPositionColorSimilarTo(
                *self.clickToggleProtection, (148, 255, 106)
            ),
            firstWait=5,
            timeout=10,
        )
        if routeObject.get("afterCities"):
            for city in routeObject.get("afterCities"):
                self.gotoCity(city, self.allCityList, express=True)
                self.checkInn(city, routeObject)
        else:
            self.gotoCity(dailyJobConf.get("endBattleCity"), express=True)
        self.sellInCity(dailyJobConf.get("endBattleCity"), simple=True)
        self.updateDailyConfVal("dailyBattle", True)
        self.changeFleet(2, simple=True)
        self.sellOverload()
        self.healInjury(dailyJobConf.get("endBattleCity"))

    # todo
    def crossTunnel(self, goods=False):
        clickForGoods=1293,565
        self.clickInMenu(["出境"], ["出境"])
        if goods:
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*clickForGoods),
                lambda: self.isPositionColorSimilarTo(1223,565, (89,219,33)),
                2,
            )

        def backupFunc():
            self.simulatorInstance.clickPointV2(*clickForGoods)
            self.simulatorInstance.clickPointV2(1305, 624)

        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1329,619),
            lambda: self.hasArrayStringEqualMultiLineWords(
                ["通知"], A=[673,326,767,358]
            ),
            backupFunc=backupFunc,
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(767,549),
            lambda: self.inCityList(self.allCityList),
            5,
            timeout=60,
        )

    def bartingTrade(self, routeObject):
        # 换货
        (villageKey, villageObject) = self.getTargetVillageObject(routeObject)
        if not villageObject:
            return
        if villageObject.get("buys"):
            self.print("complex buy until reach certain amount")
            self.market.buyUntilByConf(villageObject, routeObject)
        else:
            for city in villageObject.get("buyCities"):
                self.gotoCity(city, self.allCityList, express=True)
                self.checkInn(city, villageObject)
                buyStrategy = None
                if villageObject.get(
                    "buyStrategy"
                ) == "useGem" and city in villageObject.get("useGemCities"):
                    buyStrategy = "useGem"
                self.buyInCity(
                    villageObject["buyCities"],
                    products=villageObject["buyProducts"],
                    buyStrategy=buyStrategy,
                    buyNotProducts=villageObject.get("buyNotProducts"),
                )
        if villageObject.get("supplyFleet"):
            self.changeFleet(villageObject.get("supplyFleet"))
        for city in villageObject.get("supplyCities"):
            self.gotoCity(
                city,
                self.allCityList,
                express=True,
                fishing=(
                    routeObject.get("useFishingCities") is not None
                    and city in routeObject.get("useFishingCities")
                ),
            )
            self.checkInn(city, villageObject)
        if villageObject.get("barterFleet"):
            self.changeFleet(villageObject.get("barterFleet"))
        self.sellOverload()
        self.doVillageTrade(villageKey, villageObject)
        afterVillageSupplyCities = (
            villageObject.get("afterVillageSupplyCities")
            if villageObject.get("afterVillageSupplyCities")
            else villageObject.get("supplyCities")
        )
        for city in afterVillageSupplyCities:
            self.gotoCity(city, self.allCityList, express=True)
        self.market.cleanupGoods(
            villageObject["buyProducts"], villageObject.get("leaveGoods")
        )
        self.sellOverload()
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList([self.currentCity]),
            2,
            16,
        )

    def startTradeRouteOld(self, routeObjIndex: int = 0):
        routeObject = self.routeList[routeObjIndex]
        while routeObjIndex is not len(self.routeList):
            self.changeFleet(routeObject.get("buyFleet"))

            villageObject = self.getTargetVillageObject(routeObject)
            if villageObject:
                for city in villageObject.get("buyCities"):
                    self.gotoCity(city, self.allCityList)
                    self.checkInn(city, routeObject)
                    self.checkReachCity()
                    buyStrategy = None
                    if villageObject.get(
                        "buyStrategy"
                    ) == "useGem" and city in villageObject.get("useGemCities"):
                        buyStrategy = "useGem"
                    self.buyInCity(
                        villageObject["buyCities"],
                        products=villageObject["buyProducts"],
                        buyStrategy=buyStrategy,
                    )
                for city in villageObject.get("supplyCities"):
                    self.gotoCity(city, self.allCityList)
                if villageObject.get("barterFleet"):
                    self.changeFleet(villageObject.get("barterFleet"))

                self.doVillageTrade(villageObject)
                for city in villageObject.get("supplyCities"):
                    wait(lambda: self.findCityAndClick(city), 2)
                    self.waitForCity(self.allCityList, targetCity=city)
                market = importMarket()(self.simulatorInstance, self)
                market.cleanupGoods(villageObject["buyProducts"])
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                    lambda: self.inCity(self.currentCity),
                    2,
                    16,
                )
                self.changeFleet(routeObject.get("buyFleet"))

            self.firstBuyFin = False
            self.secondBuyFin = False
            self.print("出发买东西城市")
            while (
                not self.shouldFinishTradeAndChangeFleet(routeObject)
                and len(routeObject["buyCities"]) > 1
            ):
                # goto buy cities
                deductedBuyBMCities = self.market.deductBuyBMFromRouteObj(routeObject)
                for city in deductedBuyBMCities:
                    self.gotoCity(city, self.allCityList)
                    if self.getTime() >= 0 and self.getTime() < 6:
                        # no BM in buy if twice strategy
                        if routeObject.get("buyStrategy") != "twice":
                            self.buyBlackMarket(city)
                    self.buyInCity(
                        routeObject["buyCities"],
                        products=routeObject["buyProducts"],
                        buyStrategy=routeObject.get("buyStrategy"),
                    )
                    # special
                    self.checkInn(city, routeObject)
                    self.checkSB()
                    if routeObject.get("buyStrategy") != "twice":
                        self.buyBlackMarket(city)
                    self.print("firstBuyFin:" + str(self.firstBuyFin))
                    self.print("secondBuyFin:" + str(self.secondBuyFin))
                    self.print(
                        "transportFleet no:" + str(routeObject.get("transportFleet"))
                    )

                    if self.shouldFinishTradeAndChangeFleet(routeObject):
                        break
                    if self.secondBuyFin and routeObject.get("buyProductsAfterSupply"):
                        break
                if routeObject.get("buyStrategy") == "once":
                    self.firstBuyFin = True

                if self.secondBuyFin and routeObject.get("buyProductsAfterSupply"):
                    for city in routeObject.get("buyProductsAfterSupplyCities"):
                        self.gotoCity(city, self.allCityList)
                        if self.getTime() >= 0 and self.getTime() < 6:
                            self.buyBlackMarket(city)
                        self.buyInCity(
                            routeObject["buyProductsAfterSupplyCities"],
                            products=routeObject["buyProductsAfterSupply"],
                            buyStrategy="once",
                        )
                        self.buyBlackMarket(city)
                        if self.shouldFinishTradeAndChangeFleet(routeObject):
                            break

                # go to buy again if not full
                if self.firstBuyFin != True:
                    for city in routeObject["buySupplyCities"]:
                        self.gotoCity(city, self.allCityList)

            self.print("出发补给城市")
            # go to supply cities
            for index, city in enumerate(routeObject["supplyCities"]):
                self.gotoCity(
                    city,
                    self.allCityList,
                    dumpCrew=(
                        city
                        in (
                            routeObject.get("dumpCrewCities")
                            if routeObject.get("dumpCrewCities")
                            else []
                        )
                    ),
                )
                self.checkInn(city, routeObject)
                self.checkSB()
                if self.getTime() >= 0 and self.getTime() < 6:
                    self.buyBlackMarket(city)
                self.buyBlackMarket(city)

            self.print("出发卖货城市")
            # goto sell cities
            deductedSellBMCities = importMarket().deductSellBMFromCities(
                routeObject["sellCities"]
            )
            for index, cityObject in enumerate(deductedSellBMCities):
                cityName = cityObject["name"]
                types = cityObject["types"]

                def useSkill():
                    if villageObject:
                        return cityName == "燕云"
                    if self.getDailyConfValByKey("svea"):
                        return cityName == "beck"
                    else:
                        return cityName == "燕云"

                useSkill = self.useTradeSkill if useSkill() else lambda: False
                self.gotoCity(cityName, self.allCityList, useExtra=useSkill)
                if self.getTime() >= 0 and self.getTime() < 6:
                    self.buyBlackMarket(cityName)
                if types != "BM" and types != "supply":
                    self.changeFleet(6, simple=True)
                    self.sellInCity(cityName, simple=True, types=types)
                    self.changeFleet(2, simple=True)
                self.buyBlackMarket(cityName)

                # if(index==len(routeObject["sellCities"])-1):
                #     self.buyInCity(cityName, products=routeObject["buyProducts"])

            # swap to other route side
            time.sleep(10 + random.randint(1, 10))
            routeObjIndex += 1
            routeObject = self.routeList[(routeObjIndex) % len(self.routeList)]

    def startTradeRouteSingle(self, routeObject):
        self.changeFleet(routeObject.get("buyFleet"))
        if routeObject.get("buyTitleNo"):
            self.changeTitle(routeObject.get("buyTitleNo"))
        self.firstBuyFin = False
        self.secondBuyFin = False
        self.print("出发买东西城市")
        while (
            not self.shouldFinishTradeAndChangeFleet(routeObject)
            and len(routeObject["buyCities"]) > 1
        ):
            # goto buy cities
            for city in routeObject["buyCities"]:
                self.gotoCity(city, self.allCityList, express=True)
                self.buyInCity(
                    routeObject["buyCities"],
                    products=routeObject["buyProducts"],
                    buyStrategy=routeObject.get("buyStrategy"),
                )
                # special
                self.print("firstBuyFin:" + str(self.firstBuyFin))
                self.print("secondBuyFin:" + str(self.secondBuyFin))
                self.print("sellFleet no:" + str(routeObject.get("sellFleet")))

                if self.shouldFinishTradeAndChangeFleet(routeObject):
                    break
                # if(self.secondBuyFin and routeObject.get("buyProductsAfterSupply")):
                #     break

        self.print("出发补给城市")
        if routeObject.get("normalTitleNo"):
            self.changeTitle(routeObject.get("normalTitleNo"))
        # go to supply cities
        for element in routeObject.get("supplyCities"):
            if isinstance(element, collections.abc.Mapping):
                self.goToRoute(element)
            elif element == "tunnel":
                self.crossTunnel(True)
            else:
                self.gotoCity(
                    element,
                    self.allCityList,
                    express=True,
                    fishing=(
                        routeObject.get("useFishingCities") is not None
                        and element in routeObject.get("useFishingCities")
                    ),
                )
                self.checkInn(element, routeObject)

        self.print("出发卖货城市")
        # goto sell cities
        if routeObject.get("forceUseSequenceOptions"):
            self.sellBySequencedConf(
                routeObject.get("secondSellOptions")[0].get("cities")[0],
                routeObject.get("secondSellOptions")[0],
                routeObject,
            )
        elif routeObject.get("sellCityOptions"):
            # (sellCity,element), element is obj in secondSellOptions or None
            (sellCity, element) = self.getSellCity(routeObject)
            if element is None:
                self.gotoCity(sellCity, self.allCityList, express=True)
                if routeObject.get("useSkillCity"):
                    self.useTradeSkill(inCity=True)
                self.changeFleet(6, simple=True)
                self.sellWithTypes(sellCity, routeObject)
                self.checkInn(sellCity, routeObject)
            else:
                self.sellBySequencedConf(sellCity, element, routeObject)
        else:
            sellCity = routeObject.get("sellCities")[2]["name"]
            self.gotoCity(sellCity, self.allCityList, express=True)
            self.changeFleet(6, simple=True)
            self.sellWithTypes(sellCity, routeObject)

    def startTradeRoute(self, routeObjIndex: int = 0):
        routeObject = self.routeList[routeObjIndex]
        for index, obj in enumerate(self.routeList):
            if (
                self.currentCity in obj["buyCities"]
            ):  # or self.currentCity in list(map(lambda x: x["name"], obj["sellCities"]))):
                routeObjIndex = index
                routeObject = obj
                break
        if routeObject is None:
            self.print("没有在长途城市列表中，中断")
            wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint))
            time.sleep(5)
            return

        while True:
            if not (isWorkHour()):
                self.print("not working hour,sleep for 30mins")
                time.sleep(1000)
                continue
            self.startTradeRouteSingle(routeObject)
            # swap to other route side
            time.sleep(10 + random.randint(1, 10))
            routeObjIndex += 1
            routeObject = self.routeList[(routeObjIndex) % len(self.routeList)]

    def getStockFromType(self, type):
        if type == "crafts":
            A = [1279, 668, 1308, 695]
        elif type == "liquor":
            A = [1277, 634, 1311, 667]
        stock = ""
        if self.hasImageInScreen("excessive", A, threshold=0.95):
            stock = "excessive"
        elif self.hasImageInScreen("abundant", A, threshold=0.95):
            stock = "abundant"
        elif self.hasImageInScreen("recommended", A, threshold=0.95):
            stock = "recommended"
        else:
            stock = "insufficient"
        return getStockIdFromString(stock)

    def specialConfUpdate(self):
        self.print("check today's barting")
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.mapIcon),
            lambda: self.hasSingleLineWordsInArea("地图", A=self.titleArea),
            2,
            1,
            timeout=15,
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(712, 27), 2, 1)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.openSearchBar),
            lambda: self.hasSingleLineWordsInArea("搜", A=self.searchBarTextArea),
            2,
            1,
            timeout=15,
        )

        def input():
            wait(lambda: self.simulatorInstance.clickPointV2(*self.searchClick))
            wait(lambda: self.simulatorInstance.chineseTypeWrite("阿帕奇"), 0)

        doAndWaitUntilBy(
            input,
            lambda: self.hasArrayStringEqualSingleLineWords(
                ["阿帕奇"], A=self.searchBarTextArea
            ),
            timeout=5,
        )
        wait(lambda: self.simulatorInstance.send_enter(), 0)
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(*self.firstCityClickInMap), 2, 1
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1191, 141),
            lambda: (self.hasSingleLineWordsInArea("友好", A=[1150, 186, 1197, 206])),
        )
        # right panel
        self.apacheFriendly = self.getNumberFromSingleLineInArea(
            A=[1292, 189, 1351, 203]
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1366, 135),
            lambda: (
                self.hasSingleLineWordsInArea("兑换列表", A=[1179, 166, 1241, 187])
            ),
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1212, 179), 2)
        wampumQty = self.getNumberFromSingleLineInArea(A=[1199, 619, 1211, 636])
        if wampumQty == 4:
            self.villageTradeList["apache"]["buys"][0]["targetNum"] = 500
            self.villageTradeList["apache"]["buys"][1]["targetNum"] = 500
            self.villageTradeList["apache"]["tradeObjects"] = [(0, 2), (1, 2), (2, 2)]
            self.villageTradeList["apache"]["cleanupIndex"] = 1

            self.routeList.insert(1, self.routeList[0])
            self.routeList[1]["villages"] = "apach"

        # if(wampumQty==3):
        # self.villageTradeList["apache"]["buys"][0]["targetNum"]=400
        # self.villageTradeList["apache"]["buys"][1]["targetNum"]=500

        if wampumQty == 2:
            print("should restore")
            self.villageTradeList = copy.copy(villageTradeList)

        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1346, 174),
            lambda: (self.hasSingleLineWordsInArea("种类", A=[1180, 262, 1221, 280])),
        )

        self.liquorStock = self.getStockFromType("liquor")
        self.craftStock = self.getStockFromType("liquor")

        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList(self.allCityList),
            3,
        )

    def getSellCity(self, routeObject):
        if routeObject.get("waitForFashion"):
            waitHour = (
                routeObject.get("waitHour") + 1 if routeObject.get("waitHour") else 3
            )
            shouldWaitForFashion = self.market.shouldWaitForFashion(
                routeObject.get("fashions"),
                routeObject.get("sellCityOptions"),
                waitHour,
            )
            if shouldWaitForFashion:
                self.print(f"find fashion in {waitHour} hours, wait")
                extraMinutes = self.market.fashion.getExtraMinutesByCity(
                    routeObject.get("sellCityOptions")[0]
                )
                waitUntilClockByHour(shouldWaitForFashion, extraMinutes)
            elif routeObject.get("secondSellOptions"):
                for element in routeObject.get("secondSellOptions"):
                    shouldWaitForFashion = self.market.shouldWaitForFashion(
                        routeObject.get("fashions"), element.get("cities"), 2
                    )
                    if shouldWaitForFashion:
                        if element.get("goToCityForTrade"):
                            self.gotoCity(element.get("goToCityForTrade"), express=True)
                        self.print("find fashion in 1 hours, wait")

                        extraMinutes = self.market.fashion.getExtraMinutesByCity(
                            element.get("cities")[0]
                        )
                        waitUntilClockByHour(shouldWaitForFashion, extraMinutes)
                        sellCity = self.market.getBestPriceCity(
                            routeObject, element.get("cities")
                        )
                        return (sellCity, element)
        sellCity = self.market.getBestPriceCity(
            routeObject, routeObject.get("sellCityOptions")
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList(self.allCityList),
            3,
            2,
        )
        return (sellCity, None)

    def sellBySequencedConf(self, sellCity, option, routeObject):
        for seq in option.get("seqs"):
            if seq.get("type") == "go":
                self.gotoCity(seq.get("val"), [seq.get("val")], express=True)
                self.checkInn(seq.get("val"), routeObject)
            if seq.get("type") == "goSellCity":
                self.gotoCity(sellCity, [sellCity], express=True)
            if seq.get("type") == "tunnel":
                self.crossTunnel(goods=seq.get("val"))
            if seq.get("type") == "getBestPriceCity":
                sellCity = self.getSellCity(routeObject)[0]
            if seq.get("type") == "sell":
                if routeObject.get("useSkillCity"):
                    self.useTradeSkill(inCity=True)
                self.changeFleet(6, simple=True)
                self.sellWithTypes(sellCity, routeObject)
                self.checkInn(sellCity, routeObject)

    def sellWithTypes(self, sellCity, routeObject):
        if routeObject.get("onlySellTypes"):
            self.sellInCity(sellCity, types=routeObject.get("onlySellTypes"))
        else:
            self.sellInCity(sellCity, simple=True)

    def startTradeByConfs(self, routeObjIndex: int = 0):
        routeObject = self.routeList[routeObjIndex]
        while routeObjIndex is not len(self.routeList):
            if not (isWorkHour()):
                self.print("not working hour,sleep for 30mins")
                time.sleep(1800)
                continue
            self.firstBuyFin = False
            if routeObject.get("mode"):
                if routeObject.get("mode") == "tunnel":
                    self.crossTunnel()
                elif routeObject.get("mode") == "landing":
                    self.goLanding(routeObject)
                elif routeObject.get("mode") == "newlanding":
                    self.newLanding(routeObject)
                elif routeObject.get("mode") == "battle":
                    self.startDailyBattle(self.battleCity, routeObject)
                elif routeObject.get("mode") == "buff":
                    self.getBuff()
                elif routeObject.get("mode") == "merchantQuest":
                    self.startMerchantQuest()
                    self.lastExecuted = getCentralTime()
                elif routeObject.get("mode") == "reportAndAdvQuest":
                    self.reportAndAdvQuest()
                elif routeObject.get("mode") == "changeTitle":
                    self.changeTitle(routeObject.get("param"))
                if (
                    routeObject.get("supplyCities")
                    and routeObject.get("mode") != "plainTrade"
                ):
                    for city in routeObject.get("supplyCities"):
                        self.gotoCity(city, self.allCityList, express=True)
                        self.checkInn(city, routeObject)
                if routeObject.get("mode") == "plainTrade":
                    self.startTradeRouteSingle(routeObject)
            else:
                self.changeFleet(routeObject.get("buyFleet"))
                self.bartingTrade(routeObject)
                self.changeFleet(routeObject.get("transportFleet"))
                if routeObject.get("afterVillageBuyCities"):
                    self.changeFleet(routeObject.get("buyFleet"), simple=True)
                    for city in routeObject["afterVillageBuyCities"]:
                        self.gotoCity(city, self.allCityList, express=True)
                        self.buyInCity(
                            self.allCityList, products=routeObject["buyProducts"]
                        )
                for element in routeObject.get("supplyCities"):
                    if isinstance(element, collections.abc.Mapping):
                        self.goToRoute(element)
                    elif element == "tunnel":
                        self.crossTunnel(True)
                    else:
                        self.gotoCity(
                            element,
                            self.allCityList,
                            express=True,
                            fishing=(
                                routeObject.get("useFishingCities") is not None
                                and element in routeObject.get("useFishingCities")
                            ),
                        )
                        self.checkInn(element, routeObject)
                if routeObject.get("forceUseSequenceOptions"):
                    self.sellBySequencedConf(
                        routeObject.get("secondSellOptions")[0].get("cities")[0],
                        routeObject.get("secondSellOptions")[0],
                        routeObject,
                    )
                elif routeObject.get("sellCityOptions"):
                    # (sellCity,element), element is obj in secondSellOptions or None
                    (sellCity, element) = self.getSellCity(routeObject)
                    if element is None:
                        self.gotoCity(sellCity, self.allCityList, express=True)
                        if routeObject.get("useSkillCity"):
                            self.useTradeSkill(inCity=True)
                        self.changeFleet(6, simple=True)
                        self.sellWithTypes(sellCity, routeObject)
                        self.checkInn(sellCity, routeObject)
                    else:
                        self.sellBySequencedConf(sellCity, element, routeObject)
                else:
                    sellCity = routeObject.get("sellCities")[2]["name"]
                    self.gotoCity(sellCity, self.allCityList, express=True)
                    self.changeFleet(6, simple=True)
                    self.sellWithTypes(sellCity, routeObject)
                self.changeFleet(routeObject.get("transportFleet"), simple=True)
                if routeObject.get("afterSellCities"):
                    for element in routeObject.get("afterSellCities"):
                        if isinstance(element, collections.abc.Mapping):
                            self.goToRoute(element)
                        else:
                            self.gotoCity(element, self.allCityList, express=True)
                            self.checkInn(element, routeObject)

            time.sleep(random.randint(1, 10))
            routeObjIndex += 1
            routeObject = self.routeList[(routeObjIndex) % len(self.routeList)]

    # will update lastCheckTime if hourly check is done
    # Return tuple (Boolean, updated/original time)
    def checkShouldBattle(self, lastCheckTime, battleCity):
        now = datetime.now()
        if lastCheckTime and getTimeDiffInSeconds(lastCheckTime, now) < 900:
            return (True, lastCheckTime)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.hasSingleLineWordsInArea("船队", A=self.menuCompany),
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.clickIntoCharProfile),
            lambda: self.hasSingleLineWordsInArea("船队管理", A=self.titleArea),
        )
        battleLeft = self.getNumberFromSingleLineInArea(A=[612, 281, 631, 296])
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList([battleCity]),
            2,
            16,
        )
        if isinstance(battleLeft, int) and battleLeft < 1:
            return (False, now)
        else:
            return (True, now)

    def battleRoute(self, battleCity, battleOnMode=False):
        battle = importBattle()(self.simulatorInstance, self)
        lastCheckTime = None
        while True:
            if not self.inWater():
                if battle.utils.useSpecial("battle"):
                    battle.goBackPort(battleCity)
                battle.checkInPort(battleCity)
                if not battleOnMode:
                    checkResult = self.checkShouldBattle(lastCheckTime, battleCity)
                    lastCheckTime = checkResult[1]
                    if not checkResult[0]:
                        self.healInjury(battleCity)
                        battle.leavePort()
                        battle.goBackPort(battleCity)
                        break
                if not (isWorkHour()):
                    self.print("not working hour,sleep for 30mins")
                    time.sleep(1800)
                    continue
                if not self.getDailyConfValByKey("acceptedDailyBattleQuest"):
                    if dailyJobConf.get("battleQuest"):
                        self.acceptQuest(["完美", "讨伐海盗"])
                    self.updateDailyConfVal("acceptedDailyBattleQuest", True)
                battle.leavePort()
            self.checkForGiftAndReceive()
            # Special check of landing item in north pole
            if not self.getDailyConfValByKey("dailyCheckedBattlePlaceLanding"):
                while not self.isPositionColorSimilarTo(*self.checkLandingBtnTuple):
                    battle.goBackPort(battleCity)
                    self.goToHarbor()
                    battle.depart()
                self.doLanding()

                def checkNum():
                    num = self.getNumberFromSingleLineInArea(A=self.inAdvRoundCount)
                    return num and num > 1

                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(
                        *self.startAdvClickInPage
                    ),
                    lambda: checkNum()
                    or self.hasSingleLineWordsInArea("结算", A=self.advCheckoutTitle),
                    timeout=200
                )

                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(*self.endDiggingBtn),
                    lambda: self.hasSingleLineWordsInArea(
                        "结算", A=self.advCheckoutTitle
                    ) or self.hasSingleLineWordsInArea("探险信息", A=self.advCheckoutTitle),
                    10,
                    timeout=50,
                )
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                    lambda: self.inWater(),
                    2,
                )
                self.updateDailyConfVal("dailyCheckedBattlePlaceLanding", True)
            foundOpponent = battle.findOpponentOrReturn(
                opponentsInList, opponentNames, battleCity
            )
            if not foundOpponent:
                continue
            battle.doBattle()
            if not battle.checkStats(battleCity):
                continue
            print("repeat battle")
