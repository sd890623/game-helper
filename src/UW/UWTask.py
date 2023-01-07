from FrontTask import FrontTask
from UW.Battle import Battle
from windows import *
from images import *
from utils import *
from Market import Market
from Sb import Sb
import time
import random
from constants import cityNames, routeLists, opponentNames,battleCity

#todo-list
#      healInjury   if(self.isPositionColorSimilarTo(447,68,(252,77,61))):
# change fleet             if(self.hasSingleLineWordsInArea("assign", A=[682,569,747,593])):
# useSkill         if("talker" in self.getSingleLineWordsInArea(A=[710,218,833,246])):

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

    simulatorInstance = None
    syncBetweenUsers = True
    currentCity = "ceuta"
    sbCity=None
    sbOptions=[]
    pickedUpShip=False
    tradeRouteBuyFin=False
    waitForCityTimeOut=800
    routeOption=0
    routeList=[]
    allCityList=cityNames
    battleMode="run"

    def testTask(self):
        # self.simulatorInstance.bringWindowToFront()
        self.gotoCity('banda',["banda"])
        self.restock()
        battle=Battle(self.simulatorInstance,self)
        battle.quickWaitForCity()

        self.currentCity = "banda"
        self.buyInCity('banda', products=["nutmeg"])
        self.sendNotification(f"You have reached {'mob'}")
        self.waitForCity()
        # self.buyBlackMarket('visby')

        # screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2()
        # self.saveImageToFile(screenshotBlob, relaPath="\\..\\..\\assets\\screenshots\\UW",filename="test.jpg")
        self.setCurrentCityFromScreen()
        self.checkReachCity()

        # self.buyBlackMarket('london')
        self.dumpCrew()
        # messager=Messager()
        # messager.sendMessage("reached A city")
        onionPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\products\\"+"onion"+".bmp")

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
                if(city in str.lower()):
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

            if(cityName in str.lower()):
                self.currentCity = cityName
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def setCurrentCityFromScreen(self):
        self.inCityList(self.allCityList)

    def setRouteOption(self,routeOption: int):
        self.routeOption=routeOption
        self.routeList=routeLists[routeOption]
        self.allCityList=cityNames
        for routeObject in self.routeList:
            self.allCityList+=routeObject["buyCities"]
            self.allCityList+=routeObject["supplyCities"]
            self.allCityList+=list(map(lambda x: x["name"], routeObject["sellCities"]))            

    def checkReachCity(self):
        with open('src/UW/reachCity.txt', 'r') as f:
            reachCity=f.readline()
        if(reachCity==self.currentCity):
            self.sendNotification(f"You have reached {reachCity}")
            with open('src/UW/reachCity.txt', 'w') as f:
                f.write('')
            self.print("reached city: "+reachCity)

    def playNotification(self):
        soundPath = os.path.abspath(__file__ + "\\..\\..\\assets\\alert1.mp3")
        #print(soundPath)
        # playsound("e:\\Workspaces\\Projects\\eveHelper2\\assets\\alert1.mp3")
        #playsound(soundPath)
        
    def findCityAndClick(self, cityName=None):
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
            self.selectCityFromMapAndMove(nextCityName)
        else:
            #click out any message
            wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),1)
            wait(lambda: self.simulatorInstance.clickPointV2(firstPosi[0],firstPosi[1]+int(index*58.3)),0.5)

        
    def goToHarbor(self):
        self.print("去码头")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,0)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(1245,257), lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),2,60)

    def restock(self):
        self.print("补给")
        okBtn=778,568
        firstLineArea=[1200,528,1362,552]
        firstLineArrowBtn=1401,540
        # Repair ship
        while(self.hasSingleLineWordsInArea("notenoughdura",A=[1202,560,1362,589])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1405,574),lambda: self.hasSingleLineWordsInArea("repair", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(1110,857),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1297,859),1)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*okBtn),3,1)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)            
        #Restore crew
        while(self.hasSingleLineWordsInArea("notenoughcrew",A=firstLineArea)):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*firstLineArrowBtn),lambda: self.hasSingleLineWordsInArea("recruit", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.longerClickPointV2(1350,526),2)
            wait(lambda: self.simulatorInstance.clickPointV2(*okBtn),2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*okBtn),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2,backupFunc=lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),timeout=10)
        #Remove extra crew
        if(self.hasSingleLineWordsInArea("maxcrew",A=firstLineArea)):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*firstLineArrowBtn),lambda: self.hasSingleLineWordsInArea("recruit", A=self.titleArea), 1,2)
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
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(517,435),lambda: self.hasSingleLineWordsInArea("managehold", A=[654,214,787,237]), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(964,664),1)#redistribute
            wait(lambda: self.simulatorInstance.clickPointV2(725,672),1)#ok
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)

    def inWater(self):
        return self.hasArrayStringInAreaSingleLineWords(["water","watar","law","wate"], A=self.outSeaWaterTitle)

    def depart(self):
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
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*departBtn), lambda: self.inWater(), 4,2, backupFunc=clickAndStockBackup)
        self.checkForDailyPopup(5)

    def selectNextCity(self):
        self.print("选城市")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,0)
        self.findCityAndClick()

    def selectCityFromMapAndMove(self,cityname):
        self.print("select city from map")
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1409,201), lambda: self.hasSingleLineWordsInArea("world", A=self.titleArea) or self.hasSingleLineWordsInArea("map", A=self.titleArea), 2,1,timeout=15)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(39,97),2,0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(141,78),2,0)
        wait(lambda: self.simulatorInstance.typewrite(cityname),0)
        wait(lambda: self.simulatorInstance.send_enter(),0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(114,109),2,1)
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(717,860), lambda: (self.inWater() or self.inCityList([cityname])),1,1,timeout=15)

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
            battle=Battle(self.simulatorInstance,self)
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

    def waitForCity(self,cityList=None,targetCity=None):
        self.print("航行中")
        def backupFunc():
            self.checkForDailyPopup()
            # if(self.hasSingleLineWordsInArea("notice",A=[452,292,546,316])):
            #     doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(813,436),5,10)
            # if(self.hasSingleLineWordsInArea("notice",A=[482,299,557,325])):
            #     doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(785,430),5,10)
            # #More checks
            # if(self.hasSingleLineWordsInArea("info",A=[452,292,546,316])):
            #     doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(813,436),5,10)
            if(self.hasSingleLineWordsInArea("ok", A=Battle.battleEnd["okBtn"]) or self.hasSingleLineWordsInArea("close", A=Battle.battleEnd["okBtn"])):
                battle=Battle(self.simulatorInstance,self)
                battle.suppressBattle()
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
        if(hour in [2,3]):
            time.sleep(delay)
            if(self.hasArrayStringInAreaSingleLineWords(['event'],A=[440,176,512,207])):
                wait(lambda: self.simulatorInstance.clickPointV2(1135,213),2)
                doMoreTimesWithWait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),4,5)

    # def checkForTreasure(self):
    #     chestCood=self.hasImageInScreen("chest",A=[173,48,1051,659])
    #     if(chestCood):
    #         doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(chestCood[0]+10,chestCood[1]+18),2,0,disableWait=True)

    def basicMarket(self):
        self.print("去超市")
        market=Market(self.simulatorInstance, self)

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
        market=Market(self.simulatorInstance, self)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1249,295), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

        #sell
        market.sellGoodsWithMargin(simple,types)
        time.sleep(3)
        def backup():
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1076,715),3, 2)
            time.sleep(5)
            self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(cityName), 3,2,backupFunc=backup)

    def buyInCity(self,cityList,products,buyStrategy=False,marketMode=0):
        self.print("去超市")
        market=Market(self.simulatorInstance, self,marketMode=marketMode)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1253,294), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

        #buy
        if(buyStrategy=="twice"):
            market.buyProductsInCityTwice(products)
        else:
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
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(cityList), 3,2,backupFunc=backup)

    def clickInMenu(self,menuItem,inTitle,infinite=False):
        wait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1)  

        area=[1232,251,1350,270]
        index=0
        while(index<150):
            yDiff=int(index%15*39)
            if(self.hasSingleLineWordsInArea(menuItem, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1241,261+yDiff), lambda: self.hasSingleLineWordsInArea(inTitle, A=self.titleArea),2,2)
                break
            index+=1
            if(not infinite and index==15):
                return False
        return True

    def buyBlackMarket(self,city):
        market=Market(self.simulatorInstance, self)
        if(market.shouldBuyBlackMarket(city)):
            self.print("去黑店")
            market.buyBlackMarket(city)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(city), 3,2)


    def shipBuilding(self,options=[0], city="faro", times=30):
        self.print("SB 开始")
        self.pickedUpShip=False
        sb=Sb(self.simulatorInstance, self)
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

    def startJourney(self):
        self.checkSB()
        self.goToHarbor()
        self.depart()
        self.selectNextCity()
        self.waitForCity()
        self.basicMarket()
        self.checkReachCity()
        self.buyBlackMarket(self.currentCity)
        time.sleep(random.randint(3,5))

    def getTime(self):
        try:
            timeOCR=self.getSingleLineWordsInArea(A=[1381,222,1422,236], ocrType=2)
            return int(timeOCR[0:2])
        except Exception as e:
            print(e)    
            return 12

    def healInjury(self,city):
        self.clickInMenu("tavern","tavern",infinite=True)
        # 4th button: 58,279 5th 60,342
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(60,342), lambda: self.hasSingleLineWordsInArea("managemate", A=self.titleArea),2,1)
        if(self.isPositionColorSimilarTo(447,68,(252,77,61))):
            # wait(lambda: self.simulatorInstance.clickPointV2(389,80),1)
            wait(lambda: self.simulatorInstance.clickPointV2(915,697),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1176,499),1)
            wait(lambda: self.simulatorInstance.clickPointV2(711,482),1)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(city),2,16)
    
    def changeFleet(self, fleetNo):
        if(not fleetNo):
            return
        for x in range(0,1):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.hasSingleLineWordsInArea("company", A=[156,22,227,39]),1,1)
            wait(lambda: self.simulatorInstance.clickPointV2(1165,111),1)#ship
            wait(lambda: self.simulatorInstance.clickPointV2(1069,90),1)#assign
            wait(lambda: self.simulatorInstance.clickPointV2(1022,138),1)#settings
            y=int(282+int(62*(fleetNo-1)))
            wait(lambda: self.simulatorInstance.clickPointV2(343,y),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1127,667),1)#apply
            wait(lambda: self.simulatorInstance.clickPointV2(769,534),1)#ok
            if(self.hasSingleLineWordsInArea("assign", A=[682,569,747,593])):
                wait(lambda: self.simulatorInstance.clickPointV2(718,584),1)#injury confirm
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(self.allCityList),1,15)
            
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.hasSingleLineWordsInArea("company", A=[151,19,227,37]),1,1)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1244,107), lambda: self.hasSingleLineWordsInArea("manage", A=self.titleArea),2,1)
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(1395,849), lambda: self.hasSingleLineWordsInArea("redistribute", A=[637,214,751,236]),1,15)#redistributeCrew
            wait(lambda: self.simulatorInstance.clickPointV2(456,663),1)#distributeMin
            wait(lambda: self.simulatorInstance.clickPointV2(1026,672),1)#apply
            wait(lambda: self.simulatorInstance.clickPointV2(780,566),1)#ok
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(self.allCityList),1,15)

    def dumpCrew(self):
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1274,22), lambda: self.hasSingleLineWordsInArea("company", A=[151,17,290,38]),2,1)
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
    def gotoCity(self,cityname,cityList,dumpCrew=False,useExtra=lambda: False):
        self.goToHarbor()
        self.depart()
        useExtra()
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,1)
        wait(lambda: self.findCityAndClick(cityname),2)
        #if(dumpCrew):
            #self.dumpCrew()
        self.waitForCity(cityList,targetCity=cityname)
        self.sendMessage("UW","reached city of "+cityname)
    
    def useTradeSkill(self):
        wait(lambda: self.simulatorInstance.clickPointV2(39,632),1)
        if("talker" in self.getSingleLineWordsInArea(A=[710,218,833,246])):
            wait(lambda: self.simulatorInstance.clickPointV2(782,385),1)
            wait(lambda: self.simulatorInstance.clickPointV2(717,479),1)
        
    def startTradeRoute(self):
        routeObjIndex=0
        routeObject=None
        self.setCurrentCityFromScreen()
        for index,obj in enumerate(self.routeList):
            if(self.currentCity in obj["buyCities"]):  #or self.currentCity in list(map(lambda x: x["name"], obj["sellCities"]))):
                routeObjIndex=index
                routeObject=obj
                break
        if(routeObject==None):
            self.print("没有在长途城市列表中，中断")
            wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint))
            time.sleep(5)
            return

        while(True):
            if(not(isWorkHour())):
                self.print("not working hour,sleep for 30mins")
                time.sleep(1800)
                continue

            self.changeFleet(routeObject.get('buyFleet'))
            self.tradeRouteBuyFin=False
            self.print("出发买东西城市")
            while(self.tradeRouteBuyFin==False and len(routeObject["buyCities"])>1):
                # goto buy cities
                deductedBuyBMCities=Market.deductBuyBMFromRouteObj(routeObject)
                for city in deductedBuyBMCities:
                    if(self.tradeRouteBuyFin==True):
                        break
                    self.gotoCity(city,self.allCityList)
                    if(self.getTime()>=0 and self.getTime()<6):
                        # no BM in buy if twice strategy
                        if(routeObject.get("buyStrategy")!= "twice"):
                            self.buyBlackMarket(city)
                    self.buyInCity(routeObject["buyCities"], products=routeObject["buyProducts"],buyStrategy=routeObject.get("buyStrategy"))
                    #special
                    self.checkSB()
                    if(routeObject.get("buyStrategy")!= "twice"):
                        self.buyBlackMarket(city)
                    self.checkReachCity()
                if(routeObject.get("buyStrategy")=="once"):
                    self.tradeRouteBuyFin=True
                #go to buy again if not full
                if(self.tradeRouteBuyFin!=True):
                    for city in routeObject["buySupplyCities"]:
                        self.gotoCity(city,self.allCityList)

            self.print("出发补给城市")
            #go to supply cities
            for index,city in enumerate(routeObject["supplyCities"]):
                self.gotoCity(city,self.allCityList,dumpCrew=(city in (routeObject.get('dumpCrewCities') if routeObject.get('dumpCrewCities') else [])))
                self.checkSB()
                if(index==0):
                    self.changeFleet(routeObject.get('sellFleet'))
                if(index in [0,1]):
                    self.buyInCity(routeObject["supplyCities"], products=routeObject["buyProducts"],buyStrategy=routeObject.get("buyStrategy"))
                self.buyBlackMarket(city)
                self.checkReachCity()

            self.print("出发卖货城市")
            # goto sell cities
            deductedSellBMCities=Market.deductSellBMFromCities(routeObject["sellCities"])
            for index,cityObject in enumerate(deductedSellBMCities):
                cityName=cityObject["name"]
                types=cityObject["types"]
                useSkill=self.useTradeSkill if (cityName==routeObject.get("useSkillCity")) else lambda:False
                self.gotoCity(cityName,self.allCityList,useExtra=useSkill)
                if(self.getTime()>=0 and self.getTime()<6):
                    self.buyBlackMarket(cityName)
                if(types!="BM"):
                    self.sellInCity(cityName,simple=True,types=types)
                self.buyBlackMarket(cityName)
                self.checkReachCity()

                # if(index==len(routeObject["sellCities"])-1):
                #     self.buyInCity(cityName, products=routeObject["buyProducts"])

            #swap to other route side
            routeObjIndex+=1
            routeObject=self.routeList[(routeObjIndex)%len(self.routeList)]

    def battleRoute(self):
        battle=Battle(self.simulatorInstance,self)
        while(True):
            if(not self.inWater()):
                battle.checkInPort(battleCity)
                battle.leavePort()
            self.checkForGiftAndReceive()
            foundOpponent=battle.findOpponentOrReturn(opponentNames,battleCity)
            if(not foundOpponent):
                continue
            battle.doBattle()
            if(not battle.checkStats(battleCity)):
                continue
            print("repeat battle")




