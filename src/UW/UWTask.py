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
    sami
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
    rightCatePoint1 = 1238, 94
    rightCatePoint2 = 1290, 90
    rightCatePoint3 = 1342, 88

    titleArea = [41,8,307,43]
    rightTopTownIcon = 1406,24
    leftTopBackBtn = 23, 26
    inTownCityNameArea = [108,15,236,41]
    inScreenConfirmYesButton = 1083, 794
    enterCityButton = 1202, 837
    outSeaWaterTitle = [72,14,175,42]
    randomPoint = 1084, 628
    mapIcon = 1411,173
    noticeTitleArea=[666,287,780,313]
    noticeOK=766,583
    hideNoticeTick=700,557
    # VM screen size: 1440x900

    syncBetweenUsers = True
    currentCity = "las"
    sbCity = None
    sbOptions = []
    pickedUpShip = False
    tradeRouteBuyFin = False
    hasStartedExtraBuy = False
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
        self.simulatorInstance.chineseTypeWrite("锦")
        self.gotoCity("杭州",express=True)
        # self.efficientHireInn=False
        # while(True):
        #     self.checkInn("santa")
        #     time.sleep(3600)
        self.click()
        self.initMarket()
        self.market.getBestPriceCity(samiRouteBase,samiRouteBase.get("sellCityOptions"))
        self.bartingTrade(yawuruRouteBase)
        self.getStockFromType("crafts")
        self.specialConfUpdate()
        self.market.barterInVillage({
            **sami
        })
        self.newLanding()
        self.startFocusedBartingTrade(1)
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
        while(True):
            wait(lambda: self.simulatorInstance.rightClickPointV2(1412,340), 5)

    def initMarket(self):
        self.market = importMarket()(self.simulatorInstance, self)

    def inCityList(self, cityList=None):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(
                A=self.inTownCityNameArea
            )
            # self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob,ocrType=4)
            if len(ocrObj[0]) == 0:
                return False
            str = "".join(ocrObj[0])
            if('water' in str.lower()):
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
            if self.liquorStock in [2,3, 4]:
                return 9
            else:
                return 14

    def setRouteOptionFromScreen(self):
        month = self.getSingleLineWordsInArea(A=[1330,200,1348,216],ocrType=2)
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
        self.allCityList += ["塞得港","cohasset"]
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

        # 8th city rea in 1253,585,1371,606
        # height between 51.8
        firstPosi = (1259,239)
        area = [1253,222,1360,245]
        index = 0
        found = False
        while not (found) and index < 8:
            yDiff = int(index * 51.8)
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
                        nextCityName, A=[658,831,787,850]
                    ),
                    3,
                    30,
                    1,
                )

    def goToHarbor(self):
        self.print("去码头")
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2), 2, 0
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1280,233),
            lambda: self.hasSingleLineWordsInArea("出港所", A=self.titleArea),
            2,
            60,
        )

    def restock(self):
        self.print("补给")
        okBtn = 752, 607
        firstLineArea = [1201, 490, 1380, 514]
        firstLineArrowBtn = 1405, 500
        # Repair ship
        while self.hasSingleLineWordsInArea(
            "notenoughdurability", A=[1202, 518, 1362, 543]
        ):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1403, 528),
                lambda: self.hasSingleLineWordsInArea("repair", A=self.titleArea),
                1,
                2,
            )
            wait(lambda: self.simulatorInstance.clickPointV2(1110, 857), 1)
            def click():
                wait(lambda: self.simulatorInstance.clickPointV2(1297, 859), 1)
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*okBtn),2)
            doAndWaitUntilBy(
                click,
                lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),
                1,
                2,
                timeout=10
            )
        # Restore crew
        while self.hasSingleLineWordsInArea("notenoughcrew", A=firstLineArea):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*firstLineArrowBtn),
                lambda: self.hasSingleLineWordsInArea("recruitcrew", A=self.titleArea),
                1,
                2,
            )
            def click2():
                wait(lambda: self.simulatorInstance.longerClickPointV2(1350, 526), 2)
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*okBtn),2)
            doAndWaitUntilBy(
                click2,
                lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),
                1,
                2,
            )
        # Remove extra crew
        if self.hasSingleLineWordsInArea("maxcrew", A=firstLineArea):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*firstLineArrowBtn),
                lambda: self.hasSingleLineWordsInArea("recruitcrew", A=self.titleArea),
                1,
                2,
            )
            wait(lambda: self.simulatorInstance.clickPointV2(252, 861), 2)
            def click3():
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1020, 671), 2, 1)                
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*okBtn),2)
            doAndWaitUntilBy(
                click3,
                lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),
                1,
                2,
            )
        # Destroy excess
        if self.hasSingleLineWordsInArea("discard", A=[1235, 652, 1306, 670]):
            wait(lambda: self.simulatorInstance.clickPointV2(1258, 657), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint), 1)
        # solve overload
        while self.hasSingleLineWordsInArea("overload", A=[1201, 393, 1284, 413]):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1402, 403),
                lambda: self.hasSingleLineWordsInArea("supply", A=self.titleArea),
                1,
                2,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(517, 435),
                lambda: self.hasSingleLineWordsInArea(
                    "managecargo", A=[651, 211, 787, 240]
                ),
                1,
                2,
            )
            wait(
                lambda: self.simulatorInstance.clickPointV2(964, 664), 1
            )  # redistribute
            wait(lambda: self.simulatorInstance.clickPointV2(725, 672), 1)  # ok
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),
                lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),
                1,
                2,
            )

    def inWater(self):
        return self.hasArrayStringEqualSingleLineWords(
            ["海域"],
            A=self.outSeaWaterTitle,
        )

    def depart(self, littleMove=True):
        departBtn = 1287, 655

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
            if self.hasSingleLineWordsInArea("harbor", A=self.titleArea):
                self.restock()
                self.simulatorInstance.clickPointV2(*departBtn)

        clickAndStock()
        self.print("出海")
        self.simulatorInstance.longerClickPointV2(*departBtn)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*departBtn),
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
                lambda: self.simulatorInstance.clickPointV2(39, 695),
                lambda: self.getNumberFromSingleLineInArea(A=[1174, 133, 1197, 150])
                == 0,
                3,
                firstWait=2,
            )  # leave map
            # doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(39,695),2,0)
            time.sleep(2)
        self.checkForDailyPopup(5)

    def selectNextCity(self):
        self.print("选城市")
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2), 2, 0
        )
        self.findCityAndClick()

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
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(35,83),
            lambda: self.hasSingleLineWordsInArea("搜索", A=[124,60,181,82]),
            2,
            1,
            timeout=15,
        )
        wait(lambda: self.simulatorInstance.clickPointV2(150,68), 1)
        wait(lambda: self.simulatorInstance.chineseTypeWrite(cityname), 0)
        wait(lambda: self.simulatorInstance.send_enter(), 0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(105,99), 2, 1)
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint), 1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(720,867),
            lambda: (
                self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea)
                or self.inWater()
                or self.inCityList([cityname])
            ),
            5,
            firstWait=15,
            backupFunc=mapBackup
        )
        if self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea):
            wait(lambda: self.simulatorInstance.clickPointV2(*self.hideNoticeTick), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(*self.noticeOK), 10)
            if self.hasSingleLineWordsInArea("通知", A=self.noticeTitleArea):
                wait(lambda: self.simulatorInstance.clickPointV2(*self.hideNoticeTick), 1)
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
            not self.hasSingleLineWordsInArea(cityname, A=[658,831,787,850])
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
            and self.getNumberFromSingleLineInArea(A=[1174, 133, 1197, 150]) == 0
        ):
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(1243, 259), 2, 0.5
            )

    def inJourneyTask(self):
        self.checkBattle()
        self.checkForGiftAndReceive()
        self.clickEnterCityButton()
        self.checkBeforeCity()

    def checkForBasicStuck(self):
        self.checkForDailyPopup()
        # Check for special purchase
        wait(lambda: self.simulatorInstance.clickPointV2(1029, 268), 1)
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
        if self.isPositionColorSimilarTo(1224,9, (253,72,54)):
            wait(lambda: self.simulatorInstance.clickPointV2(1207,27), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(436,636), 1)
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(*self.randomPoint), 2, 0.2
            )

    def checkForDailyPopup(self, delay=0):
        hour = dt.datetime.now().hour
        if hour in [1, 2, 3, 4]:
            time.sleep(delay)
            if self.hasArrayStringEqualSingleLineWords(
                ["attendance", "perk"], A=[241, 174, 367, 206]
            ):
                wait(lambda: self.simulatorInstance.clickPointV2(1135, 213), 2)
                doMoreTimesWithWait(
                    lambda: self.simulatorInstance.rightClickPointV2(
                        *self.enterCityButton
                    ),
                    4,
                    5,
                )
            wait(lambda: self.simulatorInstance.clickPointV2(1135, 213), 2)

    # def checkForTreasure(self):
    #     chestCood=self.hasImageInScreen("chest",A=[173,48,1051,659])
    #     if(chestCood):
    #         doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(chestCood[0]+10,chestCood[1]+18),2,0,disableWait=True)

    def basicMarket(self):
        self.print("去超市")
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2), 1, 1
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1283, 295),
            lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),
            2,
            2,
        )

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
    def sellInCity(self, cityName, simple=False, types=None):
        self.print("去超市")
        self.clickInMenu(["market"], ["market"])

        # sell
        self.market.sellGoodsWithMargin(simple, types)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(163, 674), 3, 1)
        time.sleep(3)

        def backup():
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(1076, 715), 3, 2
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
        self.clickInMenu(["market"], ["market"])
        # doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1253,294), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea) or self.hasSingleLineWordsInArea("skip", A=[1330,5,1384,39]),2,2)

        results = {}
        # buy
        match buyStrategy:
            case "twice":
                results = market.buyProductsInCityTwice(
                    products, returnResultsLambda=returnResultsLambda
                ) or {}
            case "useGem":
                market.buyProductsInCityTwiceWithGem(products)
            case _:
                market.buyProductsInMarket(products, buyNotProducts)
                if returnResultsLambda:
                    results = returnResultsLambda()

        time.sleep(3)

        def backup():
            def clickWithCheck():
                if self.hasSingleLineWordsInArea("no", A=[1006, 690, 1167, 743]):
                    wait(lambda: self.simulatorInstance.clickPointV2(1078, 715), 2, 2)

            clickWithCheck()
            time.sleep(5)
            clickWithCheck()
            self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)

        continueWithUntilByWithBackup(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList(cityList),
            3,
            30,
            backupFunc=backup,
        )
        if returnResultsLambda:
            return results

    def clickInMenu(self, menuArray, inTitleArray, infinite=False, startIndex=0, fallbackIndex=1):
        wait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2), 1)
        area = [1252,227,1347,245]
        index = startIndex
        def runFallback():
            yDiff = int(fallbackIndex % 15 * 35)
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1252, 240 + yDiff),
                lambda: self.hasArrayStringEqualSingleLineWords(
                    inTitleArray, A=self.titleArea
                ),
                2,
                2,
            )
        while index < 300:
            yDiff = int(index % 15 * 35)
            if self.hasArrayStringEqualSingleLineWords(
                menuArray, A=[area[0], area[1] + yDiff, area[2], area[3] + yDiff]
            ):
                doAndWaitUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(1252, 240  + yDiff),
                    lambda: self.hasArrayStringEqualSingleLineWords(
                        inTitleArray, A=self.titleArea
                    ),
                    2,
                    2,
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
        if not hasOneArrayStringSimilarToString(city,checkInnCities):
            return
        self.clickInMenu(["inn", "lnn", "nn"], ["lnn", "inn"], infinite=False,fallbackIndex=4)
        time.sleep(3)
        if not self.hasSingleLineWordsInArea("ailable", A=[8, 61, 90, 80]):
            self.sendNotification("found mate")
            time.sleep(100)
        if not self.isPositionColorSimilarTo(1407, 651, (179, 179, 179)):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(32, 143),
                lambda: self.hasSingleLineWordsInArea("party", A=self.titleArea),
                2,
                1,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(715, 854),
                lambda: self.hasSingleLineWordsInArea(
                    "parties", A=[722, 207, 795, 233]
                ),
                2,
                1,
                timeout=10,
            )
            if(self.efficientHireInn and self.isPositionColorSimilarTo(621,249, (211,185,78)) and self.isPositionColorSimilarTo(621,328, (211,185,78))):
                wait(lambda: self.simulatorInstance.clickPointV2(621,249))
                wait(lambda: self.simulatorInstance.clickPointV2(621,328))
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(714, 669), 3, 1
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
            timeOCR = self.getSingleLineWordsInArea(A=[1381, 222, 1422, 236], ocrType=2)
            return int(timeOCR[0:2])
        except Exception as e:
            print(e)
            return 12

    def healInjury(self, city):
        self.clickInMenu(["旅馆"],["旅馆"], infinite=True)
        # 4th button: 58,279 5th 84,341
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(46,246),
            lambda: self.hasSingleLineWordsInArea("航海士", A=self.titleArea),
            2,
            1,
        )
        if self.isPositionColorSimilarTo(449, 67, (253, 53, 51)):
            wait(lambda: self.simulatorInstance.clickPointV2(394, 84), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(1039, 861), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(1294, 522), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(746, 610), 1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList([city]),
            2,
            16,
        )

    def changeFleet(self, fleetNo, simple=False):
        if not fleetNo:
            return
        for x in range(0, 1):
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.hasSingleLineWordsInArea("company", A=[143,17,206,36]),
                2,
                15,
                firstWait=2,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1170, 188),
                lambda: self.hasSingleLineWordsInArea("placement", A=self.titleArea),
                1,
                1,
                timeout=10,
            )  # ship
            # doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1069,90),lambda: self.hasSingleLineWordsInArea("settings", A=[991,123,1058,145]),1,1,timeout=10)#assign
            # doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1022,138),lambda: self.hasSingleLineWordsInArea("placement", A=[637,215,735,237]),1,1,timeout=10)#settings
            y = int(118 + int(56 * (fleetNo - 1)))
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(116, y), 2, 1
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1306, 850),
                lambda: self.hasSingleLineWordsInArea("target", A=[661,328,779,352]),
                1,
                1,
                timeout=10,
            )  # apply
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(780,551),
                lambda: not self.hasSingleLineWordsInArea(
                    "target", A=[661,328,779,352]
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
                    lambda: self.hasSingleLineWordsInArea(
                        "company", A=[143,17,206,36]
                    ),
                    2,
                    1,
                    firstWait=2,
                )
                doAndWaitUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(1265,101),
                    lambda: self.hasSingleLineWordsInArea(
                        "managefleet", A=self.titleArea
                    ),
                    2,
                    1,
                )
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(1379,858),
                    lambda: self.hasSingleLineWordsInArea(
                        "redistribute", A=[644,238,797,258]
                    ),
                    1,
                    15,
                )  # redistributeCrew
                doMoreTimesWithWait(
                    lambda: self.simulatorInstance.clickPointV2(488,645), 3, 1
                )  # distributeMin
                wait(lambda: self.simulatorInstance.clickPointV2(1026, 672), 1)  # apply
                wait(lambda: self.simulatorInstance.clickPointV2(780,591), 1)  # ok
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                    lambda: self.inCityList(self.allCityList),
                    1,
                    15,
                )

    def dumpCrew(self):
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1274, 22),
            lambda: self.hasSingleLineWordsInArea("company", A=[151, 17, 290, 38]),
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
        return self.getNumberFromSingleLineInArea(A=[1194,120,1228,136]) == 0

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
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(824, 25), 2, 1)
        # 0: 78, 3: 184
        y = int(78 + int(35 * (element["route"] - 1)))
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(116, y), 3, 1)
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint), 1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(720,867),
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
            not self.hasSingleLineWordsInArea(city, A=[658,831,787,850])
            or self.checkStopped()
        ):
            backup()
        self.waitForCity(self.allCityList, targetCity=city, routeMode=True)
        self.sendMessage("UW", "reached city of " + city)

    def goToVillage(self, village, villageObject=None, fishing=False):
        def reachedVillage():
            return self.hasSingleLineWordsInArea("village", A=self.titleArea)

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
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(712, 27), 2, 1)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(35,83),
            lambda: self.hasSingleLineWordsInArea("搜索", A=[124,60,181,82]),
            2,
            1,
            timeout=15,
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(150,68), 2, 1)
        shortVillageName = None
        if villageObject and villageObject.get("shortVillageName"):
            shortVillageName = villageObject.get("shortVillageName")
        wait(
            lambda: self.simulatorInstance.chineseTypeWrite(
                shortVillageName if shortVillageName else village
            ),
            0,
        )
        wait(lambda: self.simulatorInstance.send_enter(), 0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(105,99), 3, 1)
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint), 1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(720,867),
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
        openButton = (48, 684) if inCity else (48, 636)
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*openButton),
            lambda: self.hasSingleLineWordsInArea("order", A=[735, 253, 801, 280]),
            2,
        )
        if self.hasArrayStringInSingleLineWords(
            ["talker", "seeker", "expertise"], A=[787, 317, 888, 340]
        ):
            wait(lambda: self.simulatorInstance.clickPointV2(831, 476), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(775, 612), 1)
        if self.hasArrayStringInSingleLineWords(["negotiator"], A=[671, 318, 766, 344]):
            wait(lambda: self.simulatorInstance.clickPointV2(739, 441), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(775, 612), 1)
        if self.hasArrayStringInSingleLineWords(["revival"], A=[497,321,555,338]):
            wait(lambda: self.simulatorInstance.clickPointV2(459,463), 1)
            wait(lambda: self.simulatorInstance.clickPointV2(775, 612), 1)
        if self.hasArrayStringInSingleLineWords(["negotiator"], A=[560, 320, 644, 337]):
            wait(lambda: self.simulatorInstance.clickPointV2(603, 513), 1)
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(775, 612), 2
            )
        if self.hasArrayStringInSingleLineWords(["sales"], A=[346, 320, 380, 337]):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(354, 515),
                lambda: self.hasSingleLineWordsInArea("notice", A=[681, 269, 760, 295]),
                2,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(784, 606),
                lambda: not self.hasSingleLineWordsInArea(
                    "notice", A=[681, 269, 760, 295]
                ),
                2,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*openButton),
                lambda: self.hasSingleLineWordsInArea("order", A=[735, 253, 801, 280]),
                2,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(600, 506),
                lambda: self.hasSingleLineWordsInArea("notice", A=[681, 269, 760, 295]),
                2,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(784, 606),
                lambda: not self.hasSingleLineWordsInArea(
                    "notice", A=[681, 269, 760, 295]
                ),
                2,
            )
        if(self.hasSingleLineWordsInArea("order", A=[735, 253, 801, 280])):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1084, 750),
                lambda: not self.hasSingleLineWordsInArea(
                    "order", A=[735, 253, 801, 280]
                ),
                2,
            )

    def shouldFinishTradeAndChangeFleet(self, routeObject):
        if routeObject.get("sellFleet"):
            if self.tradeRouteBuyFin and not self.hasStartedExtraBuy:
                self.changeFleet(routeObject.get("sellFleet"))
                self.tradeRouteBuyFin = False
                self.hasStartedExtraBuy = True
                self.buyInCity(
                    routeObject["buyCities"],
                    products=routeObject["buyProducts"],
                    buyStrategy=routeObject.get("buyStrategy"),
                )
                return False
            elif self.tradeRouteBuyFin and self.hasStartedExtraBuy:
                return True
            else:
                return False
        else:
            if self.tradeRouteBuyFin:
                return True

    def shouldFinishTradeSimple(self, routeObject):
        if routeObject.get("sellFleet"):
            if self.tradeRouteBuyFin and not self.hasStartedExtraBuy:
                return False
            elif self.tradeRouteBuyFin and self.hasStartedExtraBuy:
                return True
            else:
                return False
        else:
            if self.tradeRouteBuyFin:
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
            lambda: self.simulatorInstance.clickPointV2(24, 24),
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
            lambda: self.simulatorInstance.clickPointV2(61, 84),
            lambda: self.hasSingleLineWordsInArea("委托", A=self.titleArea),
            2,
            1,
        )

        firstPosi = (353,147)
        firstArea = [289,119,617,142]
        gotQuest = False

        x = 0
        # 5TH AREA
        # 288,471,489,490
        while x < 20:
            y = 0
            while y < 5:
                yDiff = int(y % 5 * 88)
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
                    doMoreTimesWithWait(
                        lambda: self.simulatorInstance.clickPointV2(
                            firstPosi[0], firstPosi[1] + yDiff
                        ),
                        3,
                        1,
                    )
                    doAndWaitUntilBy(
                        lambda: self.simulatorInstance.clickPointV2(1271,855),
                        lambda: self.hasSingleLineWordsInArea(
                            "通知", A=[700,291,740,308]
                        ),
                    )
                    doAndWaitUntilBy(
                        lambda: self.simulatorInstance.clickPointV2(778,592),
                        lambda: not self.hasSingleLineWordsInArea(
                            "通知", A=[700,291,740,308]
                        ),
                    )
                    gotQuest = True
                    break
            # if not self.hasSingleLineWordsInArea("accept", A=[992, 548, 1057, 570]):
            #     break
            if gotQuest:
                break
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1079,77),
                lambda: self.hasSingleLineWordsInArea(
                    "更新", A=[679,288,768,309]
                ),
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(773,594),
                lambda: not self.hasSingleLineWordsInArea(
                    "更新", A=[679,288,768,309]
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

    def report(self):
        self.changeFleet(dailyJobConf.get("landingFleet"), simple=True)
        self.clickInMenu(["estate"], ["estate"])
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(48, 151),
            lambda: self.hasSingleLineWordsInArea("report", A=self.titleArea),
            2,
            1,
        )
        chestLocation = self.hasImageInScreen("chestInReport", A=[196, 174, 1098, 468])
        if chestLocation:
            chestClick = chestLocation[0] + 5, chestLocation[1] + 5
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*chestClick),
                lambda: self.hasSingleLineWordsInArea("report", A=[645, 215, 710, 236]),
                2,
                1,
                timeout=10,
            )
            while (
                self.getNumberFromSingleLineInArea(A=[999, 278, 1064, 295]) > 20000
                or self.getNumberFromSingleLineInArea(A=[999, 278, 1064, 295]) < 1500
            ):
                doAndWaitUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(1021, 580),
                    lambda: self.hasSingleLineWordsInArea(
                        "number", A=[963, 279, 1039, 306]
                    ),
                    2,
                    1,
                    timeout=10,
                )
                wait(lambda: self.simulatorInstance.clickPointV2(951, 403), 1)
                doMoreTimesWithWait(
                    lambda: self.simulatorInstance.clickPointV2(878, 580), 2, 1
                )
                doAndWaitUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(1073, 556),
                    lambda: not self.hasSingleLineWordsInArea(
                        "number", A=[963, 279, 1039, 306]
                    ),
                    2,
                    1,
                    timeout=10,
                )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(796, 668),
                lambda: not self.hasSingleLineWordsInArea(
                    "report", A=[645, 215, 710, 236]
                ),
                2,
                1,
                timeout=10,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1284, 852),
                lambda: self.hasSingleLineWordsInArea("yes", A=[1047, 779, 1112, 812]),
                2,
                1,
                timeout=10,
            )
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(1085, 788), 2, 1
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

    def doLanding(self,isEverydayLanding=False):
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(103,687),
                lambda: self.hasSingleLineWordsInArea(
                    "探索", A=[1208,817,1281,835]
                ),
                2,
                1,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1279,852),
                lambda: self.hasSingleLineWordsInArea("探险", A=[231,851,270,871]),
                2,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(730 if isEverydayLanding else 266, 861),
                lambda: self.hasSingleLineWordsInArea(
                    "探险", A=[679,237,753,259]
                ),
                2,
                1,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(888,648),
                lambda: self.hasSingleLineWordsInArea(
                    "探险", A=[682,313,757,337]
                ),
                2,
                1,
            )
            if(isEverydayLanding):
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(784,565),2)
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(784,565),
                    lambda: self.hasSingleLineWordsInArea("结算", A=[660,236,773,262]),
                    3,
                    timeout=240,
                )
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                    lambda: self.inWater(),
                    2,
                )
    def newLanding(self):
        didEverydayLanding = False
        battleInstance = importBattle()(self.simulatorInstance, self)
        self.gotoCity(dailyJobConf.get("landingCity"), express=True)
        self.changeFleet(dailyJobConf.get("landingFleet"), simple=True)
        self.checkInn(dailyJobConf.get("landingCity"))
        self.goToHarbor()
        battleInstance.depart()
        self.goToVillage("bermuda", None)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(24, 24),
            lambda: (self.inWater()),
            2,
        )
        while not self.isPositionColorSimilarTo(
            109,689, (222,223,220)
        ):
            self.goToVillage("bermuda", None)
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(24, 24),
                lambda: (self.inWater()),
                2,
            )
        if not didEverydayLanding:
            self.doLanding(isEverydayLanding=True)
            didEverydayLanding = True
        timesOfLanding=dailyJobConf.get("landingRounds")
        for x in range(timesOfLanding):
            self.doLanding()
            def checkNum():
                num = self.getNumberFromSingleLineInArea(A=[1315,123,1347,143])
                return num and num > dailyJobConf.get("landingTimes")

            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(784,565),
                lambda: checkNum() or self.hasSingleLineWordsInArea("结算", A=[660,236,773,262]) or self.hasSingleLineWordsInArea("info", A=[693,207,741,230]),
                timeout=3900,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1329, 291),
                lambda: not self.hasSingleLineWordsInArea("stop", A=[1277,284,1318,305]),
                2,
                timeout=50,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.inWater(),
                2,
            )
            self.gotoCity(dailyJobConf.get("landingCity"), express=True)
            if(x<timesOfLanding-1):
                self.goToHarbor()
                battleInstance.depart()
                self.goToVillage("bermuda", None)
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(24, 24),
                    lambda: (self.inWater()),
                    2,
                )
        self.changeFleet(2)
        self.sellOverload()
        self.updateDailyConfVal("dailyLanding", True)


    def goLanding(self, mode=None):
        if self.getDailyConfValByKey("dailyLanding"):
            return
        battleInstance = importBattle()(self.simulatorInstance, self)
        # self.gotoCity(dailyJobConf.get("preLandingCity"), express=True)
        self.changeFleet(dailyJobConf.get("landingFleet"),simple=True)
        self.gotoCity(dailyJobConf.get("landingCity"), express=True)

        didEverydayLanding = False
        self.goToHarbor()
        battleInstance.depart()
        while not self.isPositionColorSimilarTo(
            109,689, (222,223,220)
        ):
            battleInstance.goBackPort(dailyJobConf.get("landingCity"))
            self.goToHarbor()
            battleInstance.depart()
        if not didEverydayLanding:
            self.doLanding(isEverydayLanding=True)
            didEverydayLanding = True
        timesOfLanding=dailyJobConf.get("landingRounds")

        for x in range(timesOfLanding):
            self.doLanding()
            def checkNum():
                num = self.getNumberFromSingleLineInArea(A=[1315,123,1347,143])
                return num and num > dailyJobConf.get("landingTimes")

            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(784,565),
                lambda: checkNum() or self.hasSingleLineWordsInArea("结算", A=[660,236,773,262]) or self.hasSingleLineWordsInArea("info", A=[693,207,741,230]),
                timeout=3900,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1329, 291),
                lambda: not self.hasSingleLineWordsInArea("stop", A=[1277,284,1318,305]),
                2,
                timeout=50,
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.inWater(),
                2,
            )
            battleInstance.goBackPort(dailyJobConf.get("landingCity"))
            if(x<timesOfLanding-1):
                self.goToHarbor()
                battleInstance.depart()
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(24, 24),
                    lambda: (self.inWater()),
                    2,
                )

        self.gotoCity(dailyJobConf.get("preLandingCity"), express=True)
        self.changeFleet(2)
        self.sellOverload()
        self.updateDailyConfVal("dailyLanding", True)

    def sellOverload(self):
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.hasSingleLineWordsInArea("company", A=[143,17,206,36]),
            2,
            15,
            firstWait=2,
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1385, 109),
            lambda: self.hasSingleLineWordsInArea("storage", A=self.titleArea),
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(55, 341), 2, 1)
        doMoreTimesWithWait(
            lambda: self.simulatorInstance.clickPointV2(1339, 153), 3, 1
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: (self.inCityList(self.allCityList)),
            2,
        )

    def getBuff(self):
        buffCity = dailyJobConf.get("buffCity")
        if buffCity:
            self.gotoCity(buffCity, express=True)
            self.clickInMenu(["sanctuary"], ["sanctuary"])
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(46, 146),
                lambda: self.hasSingleLineWordsInArea("donate", A=self.titleArea),
                2,
                1,
            )
            doAndWaitUntilBy(
                lambda: self.simulatorInstance.clickPointV2(806, 318),
                lambda: self.hasSingleLineWordsInArea("yes", A=[1007, 770, 1154, 816]),
                2,
                1,
                timeout=10,
            )
            doMoreTimesWithWait(
                lambda: self.simulatorInstance.clickPointV2(1075, 787), 3, 1
            )
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                lambda: self.inCityList([buffCity]),
                2,
                16,
            )
    # this includes landing
    def startDailyBattle(self, battleCity):
        if self.getDailyConfValByKey("dailyBattle"):
            return
        self.print("battle starts")
        self.changeFleet(dailyJobConf.get("battleFleet"))
        self.gotoCity(battleCity, express=True)
        # deactivate protection
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(42,222),
            lambda: self.hasSingleLineWordsInArea("保护", A=[622,299,806,318]),
            2,
            1,
            timeout=6,
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(780,604), 3, 1)
        self.battleRoute(battleCity)
        # activate protection
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(42,222),
            lambda: self.isPositionColorSimilarTo(39,232, (203,255,160)),
            5,
            timeout=10,
        )
        self.gotoCity(dailyJobConf.get("endBattleCity"))
        self.sellInCity(dailyJobConf.get("endBattleCity"), simple=True)
        self.updateDailyConfVal("dailyBattle", True)
        self.changeFleet(2,simple=True)
        self.sellOverload()

    def crossTunnel(self, goods=False):
        self.clickInMenu(["mmigration"], ["mmigration"])
        if goods:
            continueWithUntilBy(
                lambda: self.simulatorInstance.clickPointV2(1332, 579),
                lambda: self.isPositionColorSimilarTo(1188,582, (85,184,43)),
                2,
            )

        def backupFunc():
            self.simulatorInstance.clickPointV2(1332, 579)
            self.simulatorInstance.clickPointV2(1326, 643)

        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1326, 643),
            lambda: self.hasSingleLineWordsInArea("notice", A=[681, 314, 757, 337]),
            2,
            2,
            backupFunc=backupFunc,
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(776, 568),
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
        self.market.cleanupGoods(villageObject["buyProducts"], villageObject.get("leaveGoods"))
        self.sellOverload()
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList([self.currentCity]),
            2,
            16,
        )

    def startTradeRoute(self, routeObjIndex: int = 0):
        routeObject = self.routeList[routeObjIndex]
        while routeObjIndex is not len(self.routeList):
            if not (isWorkHour()):
                self.print("not working hour,sleep for 30mins")
                time.sleep(1800)
                continue
            self.changeFleet(routeObject.get("buyFleet"))
            (villageKey, villageObject) = self.getTargetVillageObject(routeObject)
            self.bartingTrade(routeObject)

            self.tradeRouteBuyFin = False
            self.hasStartedExtraBuy = False
            self.print("出发买东西城市")
            while (
                not self.shouldFinishTradeSimple(routeObject)
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
                    self.print("tradeRouteBuyFin:" + str(self.tradeRouteBuyFin))
                    self.print("hasStartedExtraBuy:" + str(self.hasStartedExtraBuy))
                    self.print("sellFleet no:" + str(routeObject.get("sellFleet")))

                    if self.shouldFinishTradeAndChangeFleet(routeObject):
                        break
                    if self.hasStartedExtraBuy and routeObject.get(
                        "buyProductsAfterSupply"
                    ):
                        break
                if routeObject.get("buyStrategy") == "once":
                    self.tradeRouteBuyFin = True

                if self.hasStartedExtraBuy and routeObject.get(
                    "buyProductsAfterSupply"
                ):
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
                if self.tradeRouteBuyFin != True:
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

    def getStockFromType(self,type):
        if(type=="crafts"):
            A=[1279,668,1308,695]
        elif(type=="liquor"):
            A=[1280,450,1309,476]
        stock=""
        if(self.hasImageInScreen("excessive", A,threshold=0.95)):
            stock="excessive"
        elif(self.hasImageInScreen("abundant", A,threshold=0.95)):
            stock="abundant"
        elif(self.hasImageInScreen("recommended", A,threshold=0.95)):
            stock="recommended"
        else:
            stock="insufficient"
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
            lambda: self.simulatorInstance.clickPointV2(35,83),
            lambda: self.hasSingleLineWordsInArea("搜索", A=[124,60,181,82]),
            2,
            1,
            timeout=15,
        )
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(150,68), 2, 1)
        wait(lambda: self.simulatorInstance.chineseTypeWrite("阿帕奇"), 0)
        wait(lambda: self.simulatorInstance.send_enter(), 0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(105,99), 2, 1)
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1191,141),
            lambda: (self.hasSingleLineWordsInArea("amity", A=[1149,188,1192,205])),
        )
        # right panel
        self.apacheFriendly = self.getNumberFromSingleLineInArea(
            A=[1292,189,1351,203]
        )
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(1366,142),
            lambda: (self.hasSingleLineWordsInArea("trade", A=[1177,169,1220,185])),
        )
        doMoreTimesWithWait(lambda:self.simulatorInstance.clickPointV2(1217,175),2)
        wampumQty = self.getNumberFromSingleLineInArea(A=[1198,622,1211,634])
        if wampumQty == 4:
            self.villageTradeList["apache"]["buys"][0]["targetNum"] = 500
            self.villageTradeList["apache"]["buys"][1]["targetNum"] = 500
            self.villageTradeList["apache"]["tradeObjects"] = [(0, 2), (1, 2),(2, 2)]
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
            lambda: self.simulatorInstance.clickPointV2(1335,174),
            lambda: (
                self.hasSingleLineWordsInArea("type", A=[1181,261,1222,281])
            ),
        )

        self.liquorStock = self.getStockFromType("liquor")
        self.craftStock = self.getStockFromType("crafts")

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
                        if(element.get("goToCityForTrade")):
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
        if(routeObject.get("onlySellTypes")):
            self.sellInCity(sellCity, types=routeObject.get("onlySellTypes"))
        else:
            self.sellInCity(sellCity, simple=True)
    def startFocusedBartingTrade(self, routeObjIndex: int = 0):
        routeObject = self.routeList[routeObjIndex]

        while routeObjIndex is not len(self.routeList):
            if not (isWorkHour()):
                self.print("not working hour,sleep for 30mins")
                time.sleep(1800)
                continue
            self.tradeRouteBuyFin = False
            if routeObject.get("mode"):
                if routeObject.get("mode") == "tunnel":
                    self.crossTunnel()
                elif routeObject.get("mode") == "landing":
                    self.goLanding(mode=routeObject.get("mode"))
                elif routeObject.get("mode") == "newlanding":
                    self.newLanding()
                elif routeObject.get("mode") == "battle":
                    self.startDailyBattle(self.battleCity)
                elif routeObject.get("mode") == "buff":
                    self.getBuff()
                elif routeObject.get("mode") == "merchantQuest":
                    self.startMerchantQuest()
                    self.lastExecuted = getCentralTime()
                elif routeObject.get("mode") == "reportAndAdvQuest":
                    self.reportAndAdvQuest()
                if routeObject.get("supplyCities"):
                    for city in routeObject.get("supplyCities"):
                        self.gotoCity(city, self.allCityList, express=True)
                        self.checkInn(city, routeObject)

            else:
                self.changeFleet(routeObject.get("buyFleet"))
                self.bartingTrade(routeObject)
                self.changeFleet(routeObject.get("sellFleet"))
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
                    elif(element=="tunnel"):
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
                        self.sellWithTypes(sellCity,routeObject)
                        self.checkInn(sellCity, routeObject)
                    else:
                        self.sellBySequencedConf(sellCity, element, routeObject)
                else:
                    sellCity = routeObject.get("sellCities")[2]["name"]
                    self.gotoCity(sellCity, self.allCityList, express=True)
                    self.changeFleet(6, simple=True)
                    self.sellWithTypes(sellCity,routeObject)
                self.changeFleet(routeObject.get("sellFleet"), simple=True)
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
            lambda: self.hasSingleLineWordsInArea("company", A=[143,17,206,36]),
            2,
            15,
            firstWait=2,
        )
        doAndWaitUntilBy(
            lambda: self.simulatorInstance.clickPointV2(170, 36),
            lambda: self.hasSingleLineWordsInArea("company", A=self.titleArea),
            1,
            1,
            timeout=10,
        )
        battleLeft = self.getNumberFromSingleLineInArea(A=[596, 325, 614, 344])
        continueWithUntilBy(
            lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
            lambda: self.inCityList([battleCity]),
            2,
            16,
        )
        if isinstance(battleLeft,int) and battleLeft < 1:
            return (False, now)
        else:
            return (True, now)

    def battleRoute(self, battleCity,battleOnMode=False):
        battle = importBattle()(self.simulatorInstance, self)
        lastCheckTime = None
        while True:
            if not self.inWater():
                if battle.utils.useSpecial("battle"):
                    battle.goBackPort(battleCity)
                # battle.checkInPort(battleCity)
                if(not battleOnMode):
                    checkResult = self.checkShouldBattle(lastCheckTime, battleCity) 
                    lastCheckTime = checkResult[1]
                    if not checkResult[0]:
                        break
                if not (isWorkHour()):
                    self.print("not working hour,sleep for 30mins")
                    time.sleep(1800)
                    continue
                if not self.getDailyConfValByKey("acceptedDailyBattleQuest"):
                    if dailyJobConf.get("battleQuest"):
                        self.acceptQuest(["完美", "战斗"])
                    self.updateDailyConfVal("acceptedDailyBattleQuest", True)
                battle.leavePort()
            self.checkForGiftAndReceive()
            # Special check of landing item in north pole
            if(not self.getDailyConfValByKey("dailyCheckedBattlePlaceLanding")):
                while not self.isPositionColorSimilarTo(
                    109,689, (222,223,220)
                ):
                    battle.goBackPort(battleCity)
                    self.goToHarbor()
                    battle.depart()
                self.doLanding()
                def checkNum():
                    num = self.getNumberFromSingleLineInArea(A=[1315,123,1347,143])
                    return num and num > 1
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(784,565),
                    lambda: checkNum() or self.hasSingleLineWordsInArea("结算", A=[660,236,773,262]) or self.hasSingleLineWordsInArea("info", A=[693,207,741,230]),
                    timeout=200,
                )
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(1345,266),
                    lambda: not self.hasSingleLineWordsInArea("终止", A=[1311,259,1383,279]),
                    2,
                    timeout=50,
                )
                continueWithUntilBy(
                    lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),
                    lambda: self.inWater(),
                    2,
                )
                self.updateDailyConfVal("dailyCheckedBattlePlaceLanding",True)
            foundOpponent = battle.findOpponentOrReturn(
                opponentsInList, opponentNames, battleCity
            )
            if not foundOpponent:
                continue
            battle.doBattle()
            if not battle.checkStats(battleCity):
                continue
            print("repeat battle")
