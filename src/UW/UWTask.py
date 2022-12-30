from FrontTask import FrontTask
from UW.Battle import Battle
from windows import *
from images import *
from utils import *
from Market import Market
from Sb import Sb
import guiUtils
import time
import random
from constants import cityNames, routeLists, opponentNames,battleCity

class UWTask(FrontTask):
    rightCatePoint1=1119,92
    rightCatePoint2=1171,88
    rightCatePoint3=1214,88

    titleArea=[49,8,220,50]
    rightTopTownIcon=1285,25
    leftTopBackBtn=27,23
    inTownCityNameArea=[119,18,265,48]
    inScreenConfirmYesButton=977,639
    enterCityButton=1075,671
    outSeaWaterTitle=[74,15,260,46]
    randomPoint=874,666
    noticeTitleArea=[619,234,688,259]
    noticeOK=708,482
    #client screen size: 1280x720
    #remote control setup size:

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
    allCityList=[]
    battleMode="run"

    def __init__(self, hwnd, index):
        FrontTask.__init__(self,hwnd,index)
        hwndObject = getChildHwndByTitleAndParentHwnd("Chrome Legacy Window",hwnd)
        parentWindow = guiUtils.win(hwnd, bor= True)
        parentWindow.moveWindow(10,10,1327,858)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"], bor= True)

    def testTask(self):
        self.gotoCity('constantinopl',['constantinopl'])

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

        #firstCityarea in list 1088,234,1183,258
        #9th city rea in 1088,698,1194,723
        #height between 47.4
        firstPosi = (1138,256)
        area=[1113,240,1211,266]
        timeout=8
        index=0
        found=False
        while(not(found) and timeout>0):
            timeout-=1
            yDiff=int(index%8*58.8)
            if(self.hasSingleLineWordsInArea(nextCityName, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                found=True
                break
            index+=1

        if(timeout<=0):
            self.selectCityFromMapAndMove(nextCityName)
            
        else:
            #click out any message
            wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),1)
            wait(lambda: self.simulatorInstance.clickPointV2(firstPosi[0],firstPosi[1]+int(index%8*58.8)),0.5)

        
    def goToHarbor(self):
        self.print("去码头")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,0)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(1143,251), lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),2,60)

    def restock(self):
        self.print("补给")
        # Repair ship
        while(self.hasSingleLineWordsInArea("notenoughdura",A=[1078,486,1205,506])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1164,495),lambda: self.hasSingleLineWordsInArea("repair", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(986,692),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1149,701),1)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(715,480),3,1)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(26,25),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)            
        #Restore crew
        while(self.hasSingleLineWordsInArea("notenoughcrew",A=[1078,450,1205,470])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1164,464),lambda: self.hasSingleLineWordsInArea("recruit", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.longerClickPointV2(1240,509),2)
            wait(lambda: self.simulatorInstance.clickPointV2(714,483),2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(714,483),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2,backupFunc=lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),timeout=10)
        #Remove extra crew
        if(self.hasSingleLineWordsInArea("maxcrew",A=[1078,450,1205,470])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1164,464),lambda: self.hasSingleLineWordsInArea("recruit", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(259,697),2)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(940,578),2,1)
            wait(lambda: self.simulatorInstance.clickPointV2(712,485),2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(24,21),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)
        # Destroy excess
        if(self.hasSingleLineWordsInArea("discard", A=[1138,558,1208,574])):
            wait(lambda: self.simulatorInstance.clickPointV2(1172,573),1)
            wait(lambda: self.simulatorInstance.clickPointV2(722,516),1)
        #solve overload
        if(self.hasSingleLineWordsInArea("overload", A=[1076,307,1160,334])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1272,324),lambda: self.hasSingleLineWordsInArea("supply", A=self.titleArea), 1,2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(460,427),lambda: self.hasSingleLineWordsInArea("managehold", A=[591,137,718,161]), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(890,577),1)#redistribute
            wait(lambda: self.simulatorInstance.clickPointV2(657,582),1)#ok
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.leftTopBackBtn),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)

    def inWater(self):
        return self.hasArrayStringInAreaSingleLineWords(["water","watar","law","wate"], A=self.outSeaWaterTitle)

    def depart(self):
        def clickAndStock():
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(979,538),2,0.2)
            self.restock()

        def clickAndStockBackup():
            self.checkForDailyPopup()
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(979,538),2,0.2)
            if(self.hasSingleLineWordsInArea("harbor", A=self.titleArea)):
                self.restock()
                self.simulatorInstance.clickPointV2(1183,568)

        clickAndStock()
        self.print("出海")
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1183,568), lambda: self.inWater(), 4,2, backupFunc=clickAndStockBackup)
        self.checkForDailyPopup(5)

    def selectNextCity(self):
        self.print("选城市")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,0)
        self.findCityAndClick()

    def selectCityFromMapAndMove(self,cityname):
        self.print("select city from map")
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1277,193), lambda: self.hasSingleLineWordsInArea("world", A=self.titleArea) or self.hasSingleLineWordsInArea("map", A=self.titleArea), 2,1,timeout=15)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(38,89),2,0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(86,77),2,0)
        wait(lambda: self.simulatorInstance.typewrite(cityname),0)
        wait(lambda: self.simulatorInstance.send_enter(),0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(114,107),2,1)
        wait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(651,699), lambda: (self.inWater() or self.inCityList([cityname])),1,1,timeout=15)

    def checkForDisaster(self):
        #click disaster icon
        wait(lambda: self.simulatorInstance.clickPointV2(637,345),1)
        if(self.hasSingleLineWordsInArea("miracle",A=[1076,602,1144,626])):
            #click use tool
            wait(lambda: self.simulatorInstance.clickPointV2(1094,547),2)
            #click yes
            wait(lambda: self.simulatorInstance.clickPointV2(*self.inScreenConfirmYesButton),2)

    def checkBattle(self):
        if(self.hasSingleLineWordsInArea("retreat",A=[756,549,848,577])):
            battle=Battle(self.simulatorInstance,self)
            if(self.battleMode=="run"):
                battle.suppressBattle()
            elif(self.battleMode=="battle"):
                battle.doBattle()

    def clickEnterCityButton(self):
        doMoreTimesWithWait(lambda: self.simulatorInstance.rightClickPointV2(655,330),2,0.5)
    
    def checkBeforeCity(self):
        if(self.hasSingleLineWordsInArea("adjacent",A=[1225,264,1297,289]) and self.getNumberFromSingleLineInArea(A=[1049,132,1085,146])==0):
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1169,258),2,0.5)
    
    def inJourneyTask(self):
        # self.checkForDisaster()
        self.checkBattle()
        self.checkForGiftAndReceive()
        self.clickEnterCityButton()
        self.checkBeforeCity()

    def waitForCity(self,cityList=None,targetCity=None):
        self.print("航行中")
        def backupFunc():
            self.checkForDailyPopup()
            if(self.hasSingleLineWordsInArea("notice",A=[452,292,546,316])):
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(813,436),5,10)
            if(self.hasSingleLineWordsInArea("notice",A=[482,299,557,325])):
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(785,430),5,10)
            #More checks
            if(self.hasSingleLineWordsInArea("info",A=[452,292,546,316])):
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(813,436),5,10)
            if(self.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.hasSingleLineWordsInArea("close", A=[632,691,680,714])):
                battle=Battle(self.simulatorInstance,self)
                battle.suppressBattle()
            time.sleep(10)
            wait(lambda: self.findCityAndClick(targetCity),40)
            doMoreTimesWithWait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),4,5)
        
        continueWithUntilByWithBackup(lambda: self.inJourneyTask(), lambda: self.inCityList(cityList), 8, timeout=self.waitForCityTimeOut,notifyFunc=lambda: self.print("not found, wait for 8s"),backupFunc=backupFunc)
        self.print("click twice")
        self.clickEnterCityButton()

    def checkForGiftAndReceive(self):
        if(self.isPositionColorSimilarTo(1078,9,(245, 70, 60))):
            wait(lambda: self.simulatorInstance.clickPointV2(1068,25),1)
            wait(lambda: self.simulatorInstance.clickPointV2(346,572),1)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),2,0.2)

    def checkForDailyPopup(self,delay=0):
        hour=dt.datetime.now().hour
        if(hour in [2,3]):
            time.sleep(delay)
            if(self.hasArrayStringInAreaSingleLineWords(['event'],A=[381,101,452,130])):
                wait(lambda: self.simulatorInstance.clickPointV2(1068,137),2)
                doMoreTimesWithWait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),4,5)

    def checkForTreasure(self):
        chestCood=self.hasImageInScreen("chest",A=[173,48,1051,659])
        if(chestCood):
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(chestCood[0]+10,chestCood[1]+18),2,0,disableWait=True)

    def basicMarket(self):
        self.print("去超市")
        #mem overflow?
        market=Market(self.simulatorInstance, self)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)  
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1140,281), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

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
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1140,281), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

        #sell
        market.sellGoodsWithMargin(simple,types)
        time.sleep(3)
        def backup():
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(895,570),3, 2)
            time.sleep(5)
            self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(895,570),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(cityName), 3,2,backupFunc=backup)

    def buyInCity(self,cityList,products,buyStrategy=False,marketMode=0):
        self.print("去超市")
        market=Market(self.simulatorInstance, self,marketMode=marketMode)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1140,281), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

        #buy
        if(buyStrategy=="twice"):
            market.buyProductsInCityTwice(products)
        else:
            market.buyProductsInMarket(products)
        time.sleep(3)
        def backup():
            def clickWithCheck():
                if(self.hasSingleLineWordsInArea("no", A=[948,549,1015,581])):
                    wait(lambda: self.simulatorInstance.clickPointV2(895,570),2,2)
            clickWithCheck()
            time.sleep(5)
            clickWithCheck()
            self.simulatorInstance.clickPointV2(*self.rightTopTownIcon)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(cityList), 3,2,backupFunc=backup)

    def clickInMenu(self,menuItem,inTitle,infinite=False):
        wait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1)  

        area=[1111,242,1195,265]
        index=0
        while(index<150):
            yDiff=int(index%13*37.8)
            if(self.hasSingleLineWordsInArea(menuItem, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1127,252+yDiff), lambda: self.hasSingleLineWordsInArea(inTitle, A=self.titleArea),2,2)
                break
            index+=1
            if(not infinite and index==14):
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
        self.goToHarbor()
        # self.restock()
        self.depart()
        self.selectNextCity()
        self.waitForCity()
        self.basicMarket()
        self.checkReachCity()
        self.checkSB()
        self.buyBlackMarket(self.currentCity)
        time.sleep(random.randint(3,5))

    def getTime(self):
        try:
            timeOCR=self.getSingleLineWordsInArea(A=[1253,214,1297,230], ocrType=2)
            return int(timeOCR[0:2])
        except Exception as e:
            print(e)    
            return 12

    def healInjury(self,city):
        self.clickInMenu("tavern","tavern",infinite=True)
        # 4th button: 91,276 5th 60,332
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(91,276), lambda: self.hasSingleLineWordsInArea("managemate", A=self.titleArea),2,1)
        if(self.isPositionColorSimilarTo(437,66,(252,77,61))):
            wait(lambda: self.simulatorInstance.clickPointV2(389,80),1)
            wait(lambda: self.simulatorInstance.clickPointV2(915,697),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1176,499),1)
            wait(lambda: self.simulatorInstance.clickPointV2(711,482),1)
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(city),2,16)
    
    def changeFleet(self, fleetNo):
        if(not fleetNo):
            return
        for x in range(0,1):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.hasSingleLineWordsInArea("company", A=[151,19,227,37]),1,1)
            wait(lambda: self.simulatorInstance.clickPointV2(1046,103),1)#ship
            wait(lambda: self.simulatorInstance.clickPointV2(950,86),1)#assign
            wait(lambda: self.simulatorInstance.clickPointV2(896,133),1)#settings
            y=int(198+int(62.25*(fleetNo-1)))
            wait(lambda: self.simulatorInstance.clickPointV2(295,y),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1039,579),1)#apply
            wait(lambda: self.simulatorInstance.clickPointV2(725,459),1)#ok
            if(self.hasSingleLineWordsInArea("assign", A=[682,569,747,593])):
                wait(lambda: self.simulatorInstance.clickPointV2(718,584),1)#injury confirm
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(self.allCityList),1,15)
            
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.hasSingleLineWordsInArea("company", A=[151,19,227,37]),1,1)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1124,110), lambda: self.hasSingleLineWordsInArea("manage", A=self.titleArea),2,1)
            continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(1264,683), lambda: self.hasSingleLineWordsInArea("redistribute", A=[575,137,685,158]),1,15)#redistributeCrew
            wait(lambda: self.simulatorInstance.clickPointV2(402,578),1)#distributeMin
            wait(lambda: self.simulatorInstance.clickPointV2(958,578),1)#apply
            wait(lambda: self.simulatorInstance.clickPointV2(721,486),1)#ok
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
        wait(lambda: self.simulatorInstance.clickPointV2(37,480),1)
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
                deductedBuyBMCities=Market.deductBuyBMFromCities(routeObject["buyCities"])
                for city in deductedBuyBMCities:
                    if(self.tradeRouteBuyFin==True):
                        break
                    self.gotoCity(city,self.allCityList)
                    if(self.getTime()>=0 and self.getTime()<5):
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
                useSkill=self.useTradeSkill if (city==routeObject.get("useSkillCity")) else lambda:False
                self.gotoCity(city,self.allCityList,dumpCrew=(city in (routeObject.get('dumpCrewCities') if routeObject.get('dumpCrewCities') else [])),useExtra=useSkill)
                self.checkSB()
                if(index==0):
                    self.changeFleet(routeObject.get('sellFleet'))
                    self.buyInCity(routeObject["supplyCities"], products=routeObject["buyProducts"],buyStrategy=routeObject.get("buyStrategy"))
                self.buyBlackMarket(city)
                self.checkReachCity()

            self.print("出发卖货城市")
            # goto sell cities
            deductedSellBMCities=Market.deductSellBMFromCities(routeObject["sellCities"])
            for index,cityObject in enumerate(deductedSellBMCities):
                cityName=cityObject["name"]
                types=cityObject["types"]
                self.gotoCity(cityName,self.allCityList)
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




