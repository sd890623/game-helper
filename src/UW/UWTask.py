import sys
import os
import json

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

from images import getOCRfromImageBlob
from utils import *
from FrontTask import FrontTask

import time
import datetime as dt
import random
import os
from constants import villageTradeList, cityNames,dailyJobConf, routeLists, opponentNames,monthToRoute,opponentsInList,maticBarterTrade

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
    rightCatePoint1=1238,94
    rightCatePoint2=1290,90
    rightCatePoint3=1342,88

    titleArea=[46,8,238,49]
    rightTopTownIcon=1402,25
    leftTopBackBtn=23,26
    inTownCityNameArea=[121,20,262,46]
    inScreenConfirmYesButton=1083,794
    enterCityButton=1202,837
    outSeaWaterTitle=[79,17,268,47]
    randomPoint=1084,628
    #VM screen size: 1440x900

    syncBetweenUsers = True
    currentCity = "las"
    sbCity=None
    sbOptions=[]
    pickedUpShip=False
    tradeRouteBuyFin=False
    hasStartedExtraBuy=False
    waitForCityTimeOut=800
    hasSelectedMap=0
    routeOption=4
    routeList=[]
    allCityList=cityNames
    battleMode="run"
    goBM=True
    initialRun=True
    dailyConfFile = os.path.abspath(__file__ + "\\..\\dailyConfFile.json")

    def testTask(self):
        self.startMerchantQuest()
        self.startDailyBattle("sierra")
        dailyBattleInstance=importBattle()(self.simulatorInstance,self)
        self.goLanding(dailyBattleInstance)
        dailyBattleInstance.doBattle()
        self.checkInn('manila',{
                "checkInnCities": ['manila','hanyang','hangzhou','hobe']
        })
        # market.cleanupGoods(["oil"])
        print(hasOneArrayStringSimilarToString("lawlsswata", ["lawlesswaters","dangerouswaters","safewaters"]))
        self.changeFleet(2)
        self.checkForDailyPopup()

        if(self.hasSingleLineWordsInArea("ok",A=[757,597,811,616])):
            wait(lambda: self.simulatorInstance.clickPointV2(632,566),2)
            wait(lambda: self.simulatorInstance.clickPointV2(777,607),2)
        wait(lambda: self.simulatorInstance.clickPointV2(725,681),2)
        if(self.hasSingleLineWordsInArea("yes",A=[1041,779,1118,811])):
            wait(lambda: self.simulatorInstance.clickPointV2(1072,789),2)
        if(self.hasSingleLineWordsInArea("fast",A=[79,83,129,106])):
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(106,104), lambda: not self.isPositionColorSimilarTo(79,103,(0,30,37)),3,10)
            if(self.hasSingleLineWordsInArea("purchase",A=[667,279,767,308])):
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(776,593),4,5)

        # screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2()
        # self.saveImageToFile(screenshotBlob, relaPath="\\..\\..\\assets\\screenshots\\UW",filename="test.jpg")
        self.setCurrentCityFromScreen()
        self.checkReachCity()

        self.dumpCrew()
        wait(lambda: self.clickWithImage("tourmaline", A=[187,99,949,395],imagePrefix="products"),1)
        #print(self.simulatorInstance.window_capture_v2(playerTypeMarkImagePath, A=[512, 200, 622, 235]))

    def inCityList(self,cityList=None):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A=self.inTownCityNameArea)
            # self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob)
            if(len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])
            self.print(" ocred city: "+ str)
            if(cityList==None):
                cityList=cityNames
            for city in cityList:
                if(isStringSameOrSimilar(city,str.lower())):
                    self.currentCity = city
                    return True
            return False
        except Exception as e:
            print(e)    
            return False      

    def inCity(self,cityName):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A=self.inTownCityNameArea)
            # self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob)
            if(len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])
            self.print(" ocred city: "+ str)

            if(isStringSameOrSimilar(cityName,str.lower())):
                self.currentCity = cityName
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def setCurrentCityFromScreen(self):
        self.inCityList(self.allCityList)

    def setRouteOptionFromScreen(self):
        month=self.getSingleLineWordsInArea(A=[1322,220,1357,239])
        if month and monthToRoute.get(month):
            self.routeOption=monthToRoute.get(month)

    def setRouteOption(self,routeOption: int=False):
        if(routeOption):
            self.routeOption=routeOption
        else:
            self.setRouteOptionFromScreen()
        self.routeList=routeLists[self.routeOption]
        self.allCityList=cityNames
        self.allCityList+=villageTradeList.get("svear").get("buyCities")
        self.allCityList+=["visby","bergen","bremen","narvik"]
        self.allCityList+=[dailyJobConf["merchatQuestCity"]]
        for routeObject in self.routeList:
            self.allCityList+=routeObject["buyCities"]
            self.allCityList+=routeObject["supplyCities"]
            if routeObject.get("buyProductsAfterSupplyCities"):
                self.allCityList+=routeObject["buyProductsAfterSupplyCities"]
            self.allCityList+=list(map(lambda x: x["name"], routeObject["sellCities"]))            

    def checkReachCity(self):
        with open(os.path.abspath(__file__ + "\\..\\reachCity.txt"), 'r') as f:
            reachCity=f.readline()
        if(reachCity==self.currentCity):
            self.sendNotification(f"You have reached {reachCity}")
            with open(os.path.abspath(__file__ + "\\..\\reachCity.txt"), 'w') as f:
                f.write('')
            self.print("reached city: "+reachCity)            
            time.sleep(1200)

    def playNotification(self):
        soundPath = os.path.abspath(__file__ + "\\..\\..\\assets\\alert1.mp3")
        #print(soundPath)
        # playsound("e:\\Workspaces\\Projects\\eveHelper2\\assets\\alert1.mp3")
        #playsound(soundPath)
        
    def findCityAndClick(self, cityName=None, noExpect=None):
        if(cityName==None):
            index=cityNames.index(self.currentCity)
            nextCityName = None
            if((index+1)>len(cityNames)-1):
                nextCityName=cityNames[0]
            else:
                nextCityName = cityNames[index+1]
        else:
            nextCityName=cityName
        self.print(nextCityName)

        #firstCityarea in list 1231,245,1333,270
        #7th city rea in 1231,595,1333,621
        #height between 58.33
        firstPosi = (1259,260)
        area=[1231,245,1333,270]
        index=0
        found=False
        while(not(found) and index<8):
            yDiff=int(index*58.3)
            if(self.hasSingleLineWordsInArea(nextCityName, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                found=True
                break
            index+=1

        if(index==8):
            self.hasSelectedMap=0
            self.selectCityFromMapAndMove(nextCityName)
        else:
            #click out any message
            wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),0)
            if(noExpect):
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(firstPosi[0],firstPosi[1]+int(index*58.3)),3,1)
            else:
                continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(firstPosi[0],firstPosi[1]+int(index*58.3)),lambda: self.hasSingleLineWordsInArea(nextCityName,A=[647,823,791,845]),3,30,1)
        
    def goToHarbor(self):
        self.print("去码头")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,0)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(1245,257), lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),2,60)

    def restock(self):
        self.print("补给")
        okBtn=752,607
        firstLineArea=[1201,490,1380,514]
        firstLineArrowBtn=1405,500
        # Repair ship
        while(self.hasSingleLineWordsInArea("notenoughdurability",A=[1202,518,1362,543])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1403,528),lambda: self.hasSingleLineWordsInArea("repair", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(1110,857),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1297,859),1)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*okBtn),3,1)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)            
        #Restore crew
        while(self.hasSingleLineWordsInArea("notenoughcrew",A=firstLineArea)):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*firstLineArrowBtn),lambda: self.hasSingleLineWordsInArea("recruitcrew", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.longerClickPointV2(1350,526),2)
            wait(lambda: self.simulatorInstance.clickPointV2(*okBtn),2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)
        #Remove extra crew
        if(self.hasSingleLineWordsInArea("maxcrew",A=firstLineArea)):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*firstLineArrowBtn),lambda: self.hasSingleLineWordsInArea("recruitcrew", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(252,861),2)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1020,671),2,1)
            wait(lambda: self.simulatorInstance.clickPointV2(*okBtn),2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)
        # Destroy excess
        if(self.hasSingleLineWordsInArea("discard", A=[1235,652,1306,670])):
            wait(lambda: self.simulatorInstance.clickPointV2(1258,657),1)
            wait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),1)
        #solve overload
        while(self.hasSingleLineWordsInArea("overload", A=[1201,393,1284,413])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1402,403),lambda: self.hasSingleLineWordsInArea("supply", A=self.titleArea), 1,2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(517,435),lambda: self.hasSingleLineWordsInArea("managecargo", A=[651,211,787,240]), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(964,664),1)#redistribute
            wait(lambda: self.simulatorInstance.clickPointV2(725,672),1)#ok
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)

    def inWater(self):
        return self.hasArrayStringEqualSingleLineWords(["lawlesswaters","dangerouswaters","safewaters","lawless"], A=self.outSeaWaterTitle)

    def depart(self, littleMove=True):
        departBtn=1287,655
        def clickAndStock():
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),2,0.2)
            self.restock()

        def clickAndStockBackup():
            self.checkForDailyPopup()
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),2,0.2)
            if(self.hasSingleLineWordsInArea("harbor", A=self.titleArea)):
                self.restock()
                self.simulatorInstance.clickPointV2(*departBtn)

        clickAndStock()
        self.print("出海")
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*departBtn), lambda: self.inWater(), 4,1, backupFunc=clickAndStockBackup)
        time.sleep(2)
        if(littleMove):
            # Stop the ship on rare case it goes back town
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(39,695),lambda: self.getNumberFromSingleLineInArea(A=[1174,133,1197,150])==0, 3, firstWait=2)#leave map
            # doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(39,695),2,0)
            time.sleep(2)
        self.checkForDailyPopup(5)

    def selectNextCity(self):
        self.print("选城市")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,0)
        self.findCityAndClick()

    def selectCityFromMapAndMove(self,cityname):
        def backup():
            self.print("cant move, map again")
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),lambda: (self.inWater() or self.inCityList(self.allCityList)),2)#leave map
            
            self.checkForBasicStuck()
            if(self.hasSelectedMap<5):
                self.hasSelectedMap+=1
                self.selectCityFromMapAndMove(cityname)
        self.print("select city from map")
        if not doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1409,201), lambda: self.hasSingleLineWordsInArea("worldmap", A=self.titleArea), 2,1,timeout=15):
            return
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(39,97), lambda: self.hasSingleLineWordsInArea("search", A=[131,68,203,90]), 2,1,timeout=15)

        wait(lambda: self.simulatorInstance.clickPointV2(39,97),1)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(156,76),3,1)
        wait(lambda: self.simulatorInstance.typewrite(cityname),0)
        wait(lambda: self.simulatorInstance.send_enter(),0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(114,109),3,1)
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),1)
        # wait(lambda: self.simulatorInstance.clickPointV2(717,860),1)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(717,860),lambda: (self.hasSingleLineWordsInArea("notice",A=[683,278,756,304]) or self.inWater() or self.inCityList(self.allCityList)),5,firstWait=3)

        if(self.hasSingleLineWordsInArea("notice",A=[683,278,756,304])):
            wait(lambda: self.simulatorInstance.clickPointV2(794,599),1)
        if not doAndWaitUntilBy(lambda: False, lambda: (self.inWater() or self.inCityList(self.allCityList) or self.inCityList([cityname])),1,1,timeout=10,backupFunc=backup):
            return
        if(self.inWater() and not self.hasSingleLineWordsInArea(cityname,A=[647,823,791,845])):
            if(self.hasSelectedMap<3):
                self.hasSelectedMap+=1
                self.selectCityFromMapAndMove(cityname)
    
    # def checkForDisaster(self):
    #     #click disaster icon
    #     wait(lambda: self.simulatorInstance.clickPointV2(637,345),1)
    #     if(self.hasSingleLineWordsInArea("miracle",A=[1076,602,1144,626])):
    #         #click use tool
    #         wait(lambda: self.simulatorInstance.clickPointV2(1094,547),2)
    #         #click yes
    #         wait(lambda: self.simulatorInstance.clickPointV2(*self.inScreenConfirmYesButton),2)

    def checkBattle(self):
        if(self.hasSingleLineWordsInArea("retreat",A=[756,549,848,577])):
            battle=importBattle()(self.simulatorInstance,self)
            if(self.battleMode=="run"):
                battle.suppressBattle()
            elif(self.battleMode=="battle"):
                battle.doBattle()

    def clickEnterCityButton(self):
        doMoreTimesWithWait(lambda: self.simulatorInstance.rightClickPointV2(*self.enterCityButton),2,0.5)
    
    def checkBeforeCity(self):
        if(self.hasSingleLineWordsInArea("adjacent",A=[1360,273,1430,293]) and self.getNumberFromSingleLineInArea(A=[1174,133,1197,150])==0):
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1243,259),2,0.5)
    
    def inJourneyTask(self):
        self.checkBattle()
        self.checkForGiftAndReceive()
        self.clickEnterCityButton()
        self.checkBeforeCity()

    def checkForBasicStuck(self):
        self.checkForDailyPopup()
        #Check for special purchase
        wait(lambda: self.simulatorInstance.clickPointV2(1029,268),1)
        if(self.hasSingleLineWordsInArea("notice",A=[555,379,600,401])):
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(859,507),5,10)
        if(self.hasSingleLineWordsInArea("notice",A=[684,282,755,305])):
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(713,595),5,10)
        if(self.hasSingleLineWordsInArea("info",A=[452,292,546,316])):
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(813,436),5,10)
        if(self.hasSingleLineWordsInArea("auto",A=[139,82,192,102]) or self.hasSingleLineWordsInArea("ok", A=importBattle().battleEnd["okBtn"]) or self.hasSingleLineWordsInArea("close", A=importBattle().battleEnd["okBtn"])):
            battle=importBattle()(self.simulatorInstance,self)
            battle.suppressBattle()

    def waitForCity(self,cityList=None,targetCity=None):
        self.print("航行中")
        def backupFunc():
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),lambda: (self.inWater() or self.inCityList(cityList)),2)
            self.checkForBasicStuck()
            time.sleep(10)
            wait(lambda: self.findCityAndClick(targetCity),40)
            doMoreTimesWithWait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),4,5)
        
        continueWithUntilByWithBackup(lambda: self.inJourneyTask(), lambda: self.inCityList(cityList), 8, timeout=self.waitForCityTimeOut,notifyFunc=lambda: self.print("not found, wait for 8s"),backupFunc=backupFunc)
        self.print("click twice")
        self.clickEnterCityButton()

    def checkForGiftAndReceive(self):
        if(self.isPositionColorSimilarTo(1201,10,(251,61,52))):
            wait(lambda: self.simulatorInstance.clickPointV2(1183,25),1)
            wait(lambda: self.simulatorInstance.clickPointV2(398,661),1)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),2,0.2)

    def checkForDailyPopup(self,delay=0):
        hour=dt.datetime.now().hour
        if(hour in [1,2]):
            time.sleep(delay)
            if(self.hasArrayStringEqualSingleLineWords(['attendance','perk'],A=[241,174,367,206])):
                wait(lambda: self.simulatorInstance.clickPointV2(1135,213),2)
                doMoreTimesWithWait(lambda: self.simulatorInstance.rightClickPointV2(*self.enterCityButton),4,5)
            wait(lambda: self.simulatorInstance.clickPointV2(1135,213),2)

    # def checkForTreasure(self):
    #     chestCood=self.hasImageInScreen("chest",A=[173,48,1051,659])
    #     if(chestCood):
    #         doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(chestCood[0]+10,chestCood[1]+18),2,0,disableWait=True)

    def basicMarket(self):
        self.print("去超市")
        market=importMarket()(self.simulatorInstance, self)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)  
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1283,295), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

        #sell
        market.sellGoodsWithMargin()
        time.sleep(3)
                
        #buy
        market.buyExpensive()

        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(), 3,2)

    #need to provide a city list
    def sellInCity(self,cityName,simple=False,types=None):
        self.print("去超市")
        market=importMarket()(self.simulatorInstance, self)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1249,295), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

        #sell
        market.sellGoodsWithMargin(simple,types)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(163,674),3,1)
        time.sleep(3)
        def backup():
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1076,715),3, 2)
            time.sleep(5)
            self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(cityName), 3,2,backupFunc=backup)

    def buyInCity(self,cityList,products,buyStrategy=False,marketMode=0):
        self.print("去超市")
        market=importMarket()(self.simulatorInstance, self,marketMode=marketMode)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)
        self.clickInMenu('market', ['market'])
        # doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1253,294), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea) or self.hasSingleLineWordsInArea("skip", A=[1330,5,1384,39]),2,2)

        #buy
        match buyStrategy:
            case "twice":
                market.buyProductsInCityTwice(products)
            case "useGem":
                market.buyProductsInCityTwiceWithGem(products)
            case _:
                market.buyProductsInMarket(products)

        time.sleep(3)
        def backup():
            def clickWithCheck():
                if(self.hasSingleLineWordsInArea("no", A=[1006,690,1167,743])):
                    wait(lambda: self.simulatorInstance.clickPointV2(1078,715),2,2)
            clickWithCheck()
            time.sleep(5)
            clickWithCheck()
            self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)
        continueWithUntilByWithBackup(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(cityList),3,30,backupFunc=backup)

    def clickInMenu(self,menuItem,inTitleArray,infinite=False,startIndex=0):
        wait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1)  

        area=[1232,251,1350,270]
        index=startIndex
        while(index<1250):
            yDiff=int(index%15*39)
            if(self.hasSingleLineWordsInArea(menuItem, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1241,261+yDiff), lambda: self.hasArrayStringEqualSingleLineWords(inTitleArray, A=self.titleArea),2,2)
                break
            index+=1
            if(not infinite and index==30):
                return False
        return True

    def buyBlackMarket(self,city):
        if(not self.goBM):
            self.print("不去黑店")
            return
        market=importMarket()(self.simulatorInstance, self)
        if(market.shouldBuyBlackMarket(city)):
            self.print("去黑店")
            market.buyBlackMarket(city)
            def backup():
                self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)
                if(self.hasSingleLineWordsInArea("notice",[685,281,755,305])):
                    self.simulatorInstance.clickPointV2(784,595)
            continueWithUntilByWithBackup(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(city),2,15,backupFunc=backup)

    def shipBuilding(self,options=[0], city="faro", times=30):
        self.print("SB 开始")
        self.pickedUpShip=False
        sb=importSB()(self.simulatorInstance, self)
        timeout=times*1400   
        while(timeout>0):
            sb.gotoShipyard()
            for option in options:
                sb.pickup()
            for index, option in enumerate(options):
                sb.dismantle(index)
            for option in options:
                sb.build(option)
            sb.goBackTown(city)
            timeout-=1400
            if(times != 1):
                time.sleep(1400)
                self.print("一轮完成，开始等23分")

    def enableSB(self,cityName, options):
        self.sbCity=cityName
        self.sbOptions=options
    def checkSB(self):
        if(self.sbCity and self.currentCity==self.sbCity):
            self.shipBuilding(self.sbOptions, self.sbCity, 1)

    def checkInn(self, city, routeObject):
        if(not routeObject.get("checkInnCities")):
            return
        if(city not in routeObject.get("checkInnCities")):
            return
        self.clickInMenu("inn",["lnn","inn"],infinite=True)
        if(not self.hasSingleLineWordsInArea("ailable", A=[8,61,90,80])):
            self.sendNotification("found mate")
            time.sleep(1200)

        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(32,143), lambda: self.hasSingleLineWordsInArea("party", A=self.titleArea),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(715,854), lambda: self.hasSingleLineWordsInArea("parties", A=[722,207,795,233]),2,1,timeout=10)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(714,669),3,1)

        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(city),2,16)
    
    def startJourney(self):
        # self.buyBlackMarket(self.currentCity)
        # self.checkSB()
        self.goToHarbor()
        self.depart()
        self.selectNextCity()
        self.waitForCity()
        self.basicMarket()
        self.checkReachCity()
        time.sleep(random.randint(3,5))

    def getTime(self):
        try:
            timeOCR=self.getSingleLineWordsInArea(A=[1381,222,1422,236], ocrType=2)
            return int(timeOCR[0:2])
        except Exception as e:
            print(e)    
            return 12

    def healInjury(self,city):
        self.clickInMenu("inn",["lnn","inn"],infinite=True)
        # 4th button: 58,279 5th 84,341
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(58,279), lambda: self.hasSingleLineWordsInArea("managemate", A=self.titleArea),2,1)
        if(self.isPositionColorSimilarTo(449,67,(253,53,51))):
            wait(lambda: self.simulatorInstance.clickPointV2(394,84),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1039,861),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1294,522),1)
            wait(lambda: self.simulatorInstance.clickPointV2(746,610),1)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(city),2,16)
    
    def changeFleet(self, fleetNo, simple=False):
        if(not fleetNo):
            return
        for x in range(0,1):
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.hasSingleLineWordsInArea("company", A=[156,22,227,39]),2,15,firstWait=2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1170,188),lambda: self.hasSingleLineWordsInArea("placement", A=self.titleArea),1,1,timeout=10)#ship
            # doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1069,90),lambda: self.hasSingleLineWordsInArea("settings", A=[991,123,1058,145]),1,1,timeout=10)#assign
            # doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1022,138),lambda: self.hasSingleLineWordsInArea("placement", A=[637,215,735,237]),1,1,timeout=10)#settings
            y=int(152+int(62*(fleetNo-1)))
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(116,y),2,1)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1306,850),lambda: self.hasSingleLineWordsInArea("target", A=[718,328,782,353]),1,1,timeout=10)#apply
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(780,554),lambda: not self.hasSingleLineWordsInArea("target", A=[718,328,782,353]),1,1,timeout=10)#ok
            # No more check, can change fleet with injured
            # if(self.hasSingleLineWordsInArea("assign", A=[748,655,813,678])):
            #     doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(785,666),lambda: not self.hasSingleLineWordsInArea("ship", A=[703,431,758,449]),1,1,timeout=10)#injury confirm
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(self.allCityList),1,15)
            if(not simple):
                continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.hasSingleLineWordsInArea("company", A=[151,19,227,37]),2,1,firstWait=2)
                doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1244,107), lambda: self.hasSingleLineWordsInArea("managefleet", A=self.titleArea),2,1)
                continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(1344,850), lambda: self.hasSingleLineWordsInArea("redistribute", A=[637,214,751,236]),1,15)#redistributeCrew
                wait(lambda: self.simulatorInstance.clickPointV2(456,663),1)#distributeMin
                wait(lambda: self.simulatorInstance.clickPointV2(1026,672),1)#apply
                wait(lambda: self.simulatorInstance.clickPointV2(778,609),1)#ok
                continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(self.allCityList),1,15)

    def dumpCrew(self):
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1274,22), lambda: self.hasSingleLineWordsInArea("company", A=[151,17,290,38]),2,1,firstWait=2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1124,110), lambda: self.hasSingleLineWordsInArea("manage", A=self.titleArea),2,1)
        wait(lambda: self.simulatorInstance.clickPointV2(1220,688),1)
        for looper in [0,1,2,3,4]:
            while(True):
                currentCrew = self.getSingleLineWordsInArea(A=[753,202+looper*79,772,219+looper*79], ocrType=2)
                try:
                    if(currentCrew and int(currentCrew) <38):
                        break
                except:
                    print("int conversation failed")
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(584,211+looper*79),3,0,disableWait=True)
        for looper in [0,1,2,3,4]:
            while(True):
                currentCrew = self.getSingleLineWordsInArea(A=[753,202+looper*79,772,219+looper*79], ocrType=2)
                try:
                    if(currentCrew and int(currentCrew) <34):
                        break
                except:
                    print("int conversation failed")
                wait(lambda: self.simulatorInstance.clickPointV2(584,211+looper*79),0,disableWait=True)
                
        wait(lambda: self.simulatorInstance.clickPointV2(950,580),1)
        wait(lambda: self.simulatorInstance.clickPointV2(721,486),1)
        
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inWater(), 1,30)

    #cityList is an array to contain the target city
    def gotoCity(self,cityname,cityList=None,dumpCrew=False,useExtra=lambda: False):
        self.goToHarbor()
        self.depart()
        useExtra()
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,1)
        wait(lambda: self.findCityAndClick(cityname),2)
        #if(dumpCrew):
            #self.dumpCrew()
        self.waitForCity(cityList if cityList else [cityname],targetCity=cityname)
        self.sendMessage("UW","reached city of "+cityname)
    
    def goToVillage(self,village, villageObject=None):
        def backup():
            self.print("cant move, map again")
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),lambda: (self.inWater()),2)#leave map
            self.checkForBasicStuck()
            if(self.hasSelectedMap<3):
                self.hasSelectedMap+=1
                self.goToVillage(village, villageObject)

        self.print("select village from map")
        if not doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1409,201), lambda: self.hasSingleLineWordsInArea("worldmap", A=self.titleArea), 2,1,timeout=15):
            return
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(712,27),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(39,97), lambda: self.hasSingleLineWordsInArea("search", A=[131,68,203,90]), 2,1,timeout=15)
        wait(lambda: self.simulatorInstance.clickPointV2(39,97),1)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(156,76),3,1)
        shortVillageName=None
        if(villageObject and villageObject.get("shortVillageName")):
            shortVillageName=villageObject.get("shortVillageName")
        wait(lambda: self.simulatorInstance.typewrite(shortVillageName if shortVillageName else village),0)
        wait(lambda: self.simulatorInstance.send_enter(),0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(114,109),3,1)
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),1)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(717,860),lambda: (self.hasSingleLineWordsInArea("notice",A=[683,278,756,304]) or self.inWater() or self.inCityList(self.allCityList)),5,firstWait=3)
        if(self.hasSingleLineWordsInArea("notice",A=[683,278,756,304])):
            wait(lambda: self.simulatorInstance.clickPointV2(634,568),1)
            wait(lambda: self.simulatorInstance.clickPointV2(794,599),1)
        if not doAndWaitUntilBy(lambda: False, lambda: (self.inWater() or self.inCityList(self.allCityList) or self.inCityList([village])),1,1,timeout=10,backupFunc=backup):
            return
        self.print("航行中")
        def reachedVillage():
            return self.hasSingleLineWordsInArea("village", A=self.titleArea)
        continueWithUntilByWithBackup(lambda: self.inJourneyTask(), lambda: reachedVillage(), 8, timeout=self.waitForCityTimeOut,notifyFunc=lambda: self.print("not found, wait for 8s"),backupFunc=backup)
        self.print("到达村庄")

    def useTradeSkill(self):
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(39,632),lambda: self.hasSingleLineWordsInArea("order", A=[735,253,801,280]), 2)
        if(self.hasArrayStringInSingleLineWords(["talker","seeker","expertise"],A=[787,317,888,340])):
            wait(lambda: self.simulatorInstance.clickPointV2(831,476),1)
            wait(lambda: self.simulatorInstance.clickPointV2(775,612),1)
        if(self.hasArrayStringInSingleLineWords(["negotiator"],A=[671,318,766,344])):
            wait(lambda: self.simulatorInstance.clickPointV2(739,441),1)
            wait(lambda: self.simulatorInstance.clickPointV2(775,612),1)
        if(self.hasArrayStringInSingleLineWords(["negotiator"],A=[560,320,644,337])):
            wait(lambda: self.simulatorInstance.clickPointV2(603,513),1)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(775,612),2)
        if(self.hasArrayStringInSingleLineWords(["sales"],A=[346,320,380,337])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(354,515),lambda: self.hasSingleLineWordsInArea("notice", A=[681,269,760,295]), 2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(784,606),lambda: not self.hasSingleLineWordsInArea("notice", A=[681,269,760,295]), 2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(39,632),lambda: self.hasSingleLineWordsInArea("order", A=[735,253,801,280]), 2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(600,506),lambda: self.hasSingleLineWordsInArea("notice", A=[681,269,760,295]), 2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(784,606),lambda: not self.hasSingleLineWordsInArea("notice", A=[681,269,760,295]), 2)

    
    def shouldFinishTradeAndChangeFleet(self,routeObject):
        if(routeObject.get("sellFleet")):
            if(self.tradeRouteBuyFin and not self.hasStartedExtraBuy):
                self.changeFleet(routeObject.get('sellFleet'))
                self.tradeRouteBuyFin=False
                self.hasStartedExtraBuy=True
                self.buyInCity(routeObject["buyCities"], products=routeObject["buyProducts"],buyStrategy=routeObject.get("buyStrategy"))
                return False
            elif(self.tradeRouteBuyFin and self.hasStartedExtraBuy):
                return True
            else:
                return False
        else:
            if(self.tradeRouteBuyFin):
                return True
    def shouldFinishTradeSimple(self,routeObject):
        if(routeObject.get("sellFleet")):
            if(self.tradeRouteBuyFin and not self.hasStartedExtraBuy):
                return False
            elif(self.tradeRouteBuyFin and self.hasStartedExtraBuy):
                return True
            else:
                return False
        else:
            if(self.tradeRouteBuyFin):
                return True
    def getDailyConfValByKey(self,key):
        with open(self.dailyConfFile, 'r') as f:
            dailyConf = json.load(f)
            return dailyConf.get(key)
        
    def updateDailyConfVal(self,key,val):
        with open(self.dailyConfFile, 'r') as f:
            dailyConf = json.load(f)
            dailyConf[key]=val
            with open(self.dailyConfFile, 'w') as f:
                json.dump(dailyConf, f)

    def doVillageTrade(self,villageObject):
        village=villageObject.get("villageName")
        self.print("do village trade to "+village)
        self.goToVillage(village, villageObject)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(44,343), lambda: self.hasSingleLineWordsInArea("barter", A=self.titleArea),2,1)
        market=importMarket()(self.simulatorInstance, self)
        market.barterInVillage(villageObject)
        self.updateDailyConfVal(village,True)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(24,24),lambda: (self.inWater()),2)

    def getTargetVillageObject(self,routeObject):
        if(routeObject.get("enableVillageTrade")):
            for village in routeObject.get("villages"):
                if(village in villageTradeList.keys() and not self.getDailyConfValByKey(village)):
                    return villageTradeList.get(village)
        return None
    
    def getInitialRouteIndex(self):
        self.setCurrentCityFromScreen()
        self.setRouteOption()
        routeObjIndex=0
        for index,obj in enumerate(self.routeList):
            if(self.currentCity in obj["buyCities"]):  #or self.currentCity in list(map(lambda x: x["name"], obj["sellCities"]))):
                routeObjIndex=index
                return routeObjIndex
        if(not routeObjIndex):
            self.print("没有在长途城市列表中，中断")
            wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint))
            time.sleep(5)
            return False

    def acceptQuest(self, questNames):
        self.clickInMenu('union', ['union'])
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(61,84), lambda: self.hasSingleLineWordsInArea("requests", A=self.titleArea),2,1)

        firstPosi=(400,165)
        firstArea=[319,133,594,161]
        gotQuest=False

        x=0
        #5TH AREA
        # 321,521,500,549
        while(x<20):
            y=0
            while(y<5):
                yDiff=int(y%5*97)
                y+=1
                if(self.hasArrayStringEqualSingleLineWords(questNames, A=[firstArea[0], firstArea[1]+yDiff, firstArea[2], firstArea[3]+yDiff])):
                    doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(firstPosi[0],firstPosi[1]+yDiff),3,1)
                    doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1248,847),lambda: self.hasSingleLineWordsInArea("notice",A=[683,270,763,297]))
                    doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(778,608),lambda: not self.hasSingleLineWordsInArea("notice",A=[683,270,763,297]))
                    gotQuest=True
                    break
            if(gotQuest):
                break
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1042,87),lambda: self.hasSingleLineWordsInArea("refresh",A=[662,270,741,295]))
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(780,614),lambda: not self.hasSingleLineWordsInArea("refresh",A=[662,270,741,295]))
            x+=1
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon),lambda: self.inCityList(self.allCityList),2)

    def startMerchantQuest(self):
        if(not self.getDailyConfValByKey("merchantQuest")):
            print("go merchant request, TBC")
            self.changeFleet(4)
            self.gotoCity(dailyJobConf.get("merchatQuestCity"))
            self.acceptQuest(["exchange"])
            self.bartingTrade(maticBarterTrade)
            self.updateDailyConfVal("merchantQuest", True)

    def goLanding(self,battleInstance):
        self.changeFleet(dailyJobConf.get("landingFleet"))
        self.gotoCity(dailyJobConf.get("landingCity"))
        self.goToHarbor()
        self.depart(littleMove=False)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(113,671), lambda: self.hasSingleLineWordsInArea("explore", A=[1183,808,1241,828]),2,1)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(1246,836), lambda: self.hasSingleLineWordsInArea("land", A=[662,847,711,865]),2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(714,855), lambda: self.hasSingleLineWordsInArea("exploration", A=[645,212,755,239]),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(921,664), lambda: self.hasSingleLineWordsInArea("exploration", A=[722,303,825,326]),2,1)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(694,579), lambda: self.hasSingleLineWordsInArea("report", A=[794,215,859,236]),2,timeout=150)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inWater(),2)
        battleInstance.goBackPort(dailyJobConf.get("landingCity"))

    def startDailyBattle(self,battleCity):
        if(self.getDailyConfValByKey("dailyBattle")):
            return
        buffCity=dailyJobConf.get("buffCity")
        if(buffCity):
            self.gotoCity(buffCity)
            self.clickInMenu('sanctuary', ['sanctuary'])
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(46,146), lambda: self.hasSingleLineWordsInArea("donate", A=self.titleArea),2,1)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(806,318), lambda: self.hasSingleLineWordsInArea("yes", A=[1007,770,1154,816]),2,1,timeout=10)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1075,787),3,1)
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(buffCity),2,16)

        self.print("landing starts")
        dailyBattleInstance=importBattle()(self.simulatorInstance,self)
        self.goLanding(dailyBattleInstance)
        self.print("battle starts")
        # deactivate protection
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(38,205), lambda: self.hasSingleLineWordsInArea("protection", A=[699,258,799,280]),2,1,timeout=6)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(789,626),3,1)

        self.changeFleet(dailyJobConf.get("battleFleet"))
        self.battleRoute(battleCity)

        # activate protection
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(38,205), lambda: self.isPositionColorSimilarTo(38,205,(162,255,113)),5,timeout=10)

        self.updateDailyConfVal("dailyBattle", True)

    def bartingTrade(self, routeObject):
        # 换货
        villageObject=self.getTargetVillageObject(routeObject)
        if(villageObject):
            for city in villageObject.get("buyCities"):
                self.gotoCity(city,self.allCityList)
                self.checkInn(city, routeObject)
                self.checkReachCity()
                buyStrategy=None
                if(villageObject.get("buyStrategy")=="useGem" and city in villageObject.get("useGemCities")):
                    buyStrategy="useGem"
                self.buyInCity(villageObject["buyCities"], products=villageObject["buyProducts"],buyStrategy=buyStrategy)
            for city in villageObject.get("supplyCities"):
                self.gotoCity(city,self.allCityList)
            if(villageObject.get("barterFleet")):
                self.changeFleet(villageObject.get("barterFleet"))

            self.doVillageTrade(villageObject)
            for city in villageObject.get("supplyCities"):
                wait(lambda: self.findCityAndClick(city),2)
                self.waitForCity(self.allCityList,targetCity=city)
            market=importMarket()(self.simulatorInstance, self)
            market.cleanupGoods(villageObject["buyProducts"])
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(self.currentCity),2,16)
            self.changeFleet(routeObject.get('buyFleet'))

    def startTradeRoute(self, routeObjIndex:int =0):
        routeObject=self.routeList[routeObjIndex]
        while(routeObjIndex is not len(self.routeList)):
            if(not(isWorkHour())):
                self.print("not working hour,sleep for 30mins")
                time.sleep(1800)
                continue
            market=importMarket()(self.simulatorInstance, self)
            self.changeFleet(routeObject.get('buyFleet'))
            villageObject=self.getTargetVillageObject(routeObject)
            self.bartingTrade(routeObject)

            self.tradeRouteBuyFin=False
            self.hasStartedExtraBuy=False
            self.print("出发买东西城市")
            while(not self.shouldFinishTradeSimple(routeObject) and len(routeObject["buyCities"])>1):
                # goto buy cities
                deductedBuyBMCities=market.deductBuyBMFromRouteObj(routeObject)
                for city in deductedBuyBMCities:
                    self.gotoCity(city,self.allCityList)
                    if(self.getTime()>=0 and self.getTime()<6):
                        # no BM in buy if twice strategy
                        if(routeObject.get("buyStrategy")!= "twice"):
                            self.buyBlackMarket(city)
                    self.buyInCity(routeObject["buyCities"], products=routeObject["buyProducts"],buyStrategy=routeObject.get("buyStrategy"))
                    #special
                    self.checkInn(city, routeObject)
                    self.checkSB()
                    if(routeObject.get("buyStrategy")!= "twice"):
                        self.buyBlackMarket(city)
                    self.print("tradeRouteBuyFin:"+str(self.tradeRouteBuyFin))
                    self.print("hasStartedExtraBuy:"+str(self.hasStartedExtraBuy))
                    self.print("sellFleet no:"+str(routeObject.get("sellFleet")))

                    if(self.shouldFinishTradeAndChangeFleet(routeObject)):
                        break
                    if(self.hasStartedExtraBuy and routeObject.get("buyProductsAfterSupply")): 
                        break
                    self.checkReachCity()
                if(routeObject.get("buyStrategy")=="once"):
                    self.tradeRouteBuyFin=True

                if(self.hasStartedExtraBuy and routeObject.get("buyProductsAfterSupply")):
                    for city in routeObject.get("buyProductsAfterSupplyCities"):
                        self.gotoCity(city,self.allCityList)
                        if(self.getTime()>=0 and self.getTime()<6):
                            self.buyBlackMarket(city)
                        self.buyInCity(routeObject["buyProductsAfterSupplyCities"], products=routeObject["buyProductsAfterSupply"],buyStrategy="once")
                        self.buyBlackMarket(city)
                        if(self.shouldFinishTradeAndChangeFleet(routeObject)):
                            break
                        self.checkReachCity()

                #go to buy again if not full
                if(self.tradeRouteBuyFin!=True):
                    for city in routeObject["buySupplyCities"]:
                        self.gotoCity(city,self.allCityList)

            self.print("出发补给城市")
            #go to supply cities
            for index,city in enumerate(routeObject["supplyCities"]):
                self.gotoCity(city,self.allCityList,dumpCrew=(city in (routeObject.get('dumpCrewCities') if routeObject.get('dumpCrewCities') else [])))
                self.checkInn(city, routeObject)
                self.checkSB()
                if(self.getTime()>=0 and self.getTime()<6):
                    self.buyBlackMarket(city)
                self.buyBlackMarket(city)
                self.checkReachCity()

            self.print("出发卖货城市")
            # goto sell cities
            deductedSellBMCities=importMarket().deductSellBMFromCities(routeObject["sellCities"])
            for index,cityObject in enumerate(deductedSellBMCities):
                cityName=cityObject["name"]
                types=cityObject["types"]
                def useSkill():
                    if(villageObject):
                        return cityName=="yanyun"
                    if(self.getDailyConfValByKey("svea")):
                        return cityName=="beck"
                    else:
                        return cityName=="yanyun"
                useSkill=self.useTradeSkill if useSkill() else lambda:False
                self.gotoCity(cityName,self.allCityList,useExtra=useSkill)
                if(self.getTime()>=0 and self.getTime()<6):
                    self.buyBlackMarket(cityName)
                if(types!="BM" and types!="supply"):
                    self.changeFleet(6,simple=True)
                    self.sellInCity(cityName,simple=True,types=types)
                    self.changeFleet(2,simple=True)
                self.buyBlackMarket(cityName)
                self.checkReachCity()
        
                # if(index==len(routeObject["sellCities"])-1):
                #     self.buyInCity(cityName, products=routeObject["buyProducts"])

            #swap to other route side
            time.sleep(10+random.randint(1,10))
            routeObjIndex+=1
            routeObject=self.routeList[(routeObjIndex)%len(self.routeList)]

    # will update lastCheckTime if hourly check is done
    def checkShouldBattle(self, lastCheckTime,battleCity):
        currentTime=datetime.now()
        if(lastCheckTime and currentTime-lastCheckTime<3600):
            return True
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.hasSingleLineWordsInArea("company", A=[156,22,227,39]),2,15,firstWait=2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(170,36),lambda: self.hasSingleLineWordsInArea("company", A=self.titleArea),1,1,timeout=10)
        battleLeft=self.getNumberFromSingleLineInArea(A=[596,325,614,344])
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(battleCity),2,16)
        finishedFirstBattle=self.getDailyConfValByKey("finishedFirstBattle")
        lastCheckTime=datetime.now()
        if(battleLeft<10 and finishedFirstBattle):
            return False
        else:
            return True
        
    def battleRoute(self,battleCity):
        battle=importBattle()(self.simulatorInstance,self)
        battleFinished=False
        lastCheckTime=None
        while(not battleFinished):
            if(not self.inWater()):
                battle.checkInPort(battleCity)
                if(not self.checkShouldBattle(lastCheckTime,battleCity)):
                    battleFinished=True
                    continue
                if(not(isWorkHour())):
                    self.print("not working hour,sleep for 30mins")
                    time.sleep(1800)
                    continue
                if(not self.getDailyConfValByKey("acceptedDailyBattleQuest")):
                    self.acceptQuest(["perfect","fighting"])
                    self.updateDailyConfVal("acceptedDailyBattleQuest", True)
                battle.leavePort()
            self.checkForGiftAndReceive()
            foundOpponent=battle.findOpponentOrReturn(opponentsInList,opponentNames,battleCity)
            if(not foundOpponent):
                continue
            battle.doBattle()
            self.updateDailyConfVal("finishedFirstBattle", True)
            if(not battle.checkStats(battleCity)):
                continue
            print("repeat battle")




