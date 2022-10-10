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
from constants import cityNames, routeLists

class UWTask(FrontTask):
    rightCatePoint1=1119,92
    rightCatePoint2=1171,88
    titleArea=[49,8,220,50]
    rightTopTownIcon=1285,25
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
    waitForCityTimeOut=820
    routeOption=0
    routeList=[]
    allCityList=[]
    battleMode="run"

    def __init__(self, hwnd, index):
        FrontTask.__init__(self,hwnd,index)
        hwndObject = getChildHwndByTitleAndParentHwnd("Chrome Legacy Window",hwnd)
        parentWindow = guiUtils.win(hwnd, bor= True)
        parentWindow.moveWindow(10,10,1327,779)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"], bor= True)

    def testTask(self):
        # screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2()
        # self.saveImageToFile(screenshotBlob, relaPath="\\..\\..\\assets\\screenshots\\UW",filename="test.jpg")
        self.setCurrentCityFromScreen()
        self.checkReachCity()

        # self.buyBlackMarket('london')
        self.buyBlackMarket('visby')
        self.waitForCity(['constantinopl'],'constantinopl')
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
        self.allCityList=cityNames+self.routeList[0]["buyCities"]+self.routeList[1]["buyCities"]+self.routeList[0]["supplyCities"]+self.routeList[1]["supplyCities"]+list(map(lambda x: x["name"], self.routeList[0]["sellCities"]))+list(map(lambda x: x["name"],self.routeList[1]["sellCities"]))

    def checkReachCity(self):
        with open('src/UW/reachCity.txt', 'r') as f:
            reachCity=f.readline()
        if(reachCity==self.currentCity):
            self.print("reached city: "+reachCity)
            # self.playNotification()
            #Need to add break point here for wait
            with open('src/UW/reachCity.txt', 'w') as f:
                f.write('')

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
        continueWithUntilBy(lambda: self.simulatorInstance.clickPointV2(1143,251), lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),5,60)

    def restock(self):
        self.print("补给")
        # Repair ship
        while(self.hasSingleLineWordsInArea("notenough",A=[1078,486,1165,506])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1164,495),lambda: self.hasSingleLineWordsInArea("repair", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(399,130),1)
            wait(lambda: self.simulatorInstance.clickPointV2(1232,703),1)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.inScreenConfirmYesButton),3,1)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(26,25),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)            
        #Restore crew
        if(self.hasSingleLineWordsInArea("notenoughcrew",A=[1078,450,1205,470])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1164,464),lambda: self.hasSingleLineWordsInArea("recruit", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(1240,509),2)
            wait(lambda: self.simulatorInstance.clickPointV2(714,483),2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(714,483),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)


        # Destroy excess

        if(self.hasSingleLineWordsInArea("discard", A=[1138,558,1208,574])):
            wait(lambda: self.simulatorInstance.clickPointV2(1172,573),1)
            wait(lambda: self.simulatorInstance.clickPointV2(722,516),1)
        wait(lambda: self.simulatorInstance.clickPointV2(1183,577),1)

    def inWater(self):
        return self.hasSingleLineWordsInArea("water", A=self.outSeaWaterTitle) or self.hasSingleLineWordsInArea("watar", A=self.outSeaWaterTitle) or self.hasSingleLineWordsInArea("lawle", A=self.outSeaWaterTitle)
    def depart(self):
        def clickAndStock():
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(979,538),2,0.2)
            self.restock()

        clickAndStock()
        self.print("出海")
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1183,568), lambda: self.inWater(), 8,2, backupFunc=clickAndStock)

    def selectNextCity(self):
        self.print("选城市")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,0)
        self.findCityAndClick()

    def selectCityFromMapAndMove(self,cityname):
        self.print("select city from map")
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1277,193), lambda: self.hasSingleLineWordsInArea("world", A=self.titleArea) or self.hasSingleLineWordsInArea("map", A=self.titleArea), 2,1)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(38,89),2,0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(86,77),2,0)
        wait(lambda: self.simulatorInstance.typewrite(cityname),0)
        wait(lambda: self.simulatorInstance.send_enter(),0)
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(114,107),2,1)
        wait(lambda: self.simulatorInstance.rightClickPointV2(651,699),1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(651,699), lambda: (self.inWater() or self.inCityList([cityname])),1,1)

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
        # for x in range(2):
        #     if(self.hasSingleLineWordsInArea("move",A=[1117,668,1195,688])):
        #         wait(lambda: self.simulatorInstance.clickPointV2(1006,680),0.5)
        #     else:
        #         wait(lambda: self.simulatorInstance.clickPointV2(*self.enterCityButton),0.5)
    
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
            if(self.hasSingleLineWordsInArea("notice",A=[452,292,546,316])):
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(813,436),5,10)
            #More checks
            if(self.hasSingleLineWordsInArea("info",A=[452,292,546,316])):
                doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(813,436),5,10)
            if(self.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.hasSingleLineWordsInArea("close", A=[632,691,680,714])):
                battle=Battle(self.simulatorInstance,self)
                battle.suppressBattle()
            #For everyday login click-out
            doMoreTimesWithWait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),4,5)
            time.sleep(10)
            wait(lambda: self.findCityAndClick(targetCity),300)
            doMoreTimesWithWait(lambda: self.simulatorInstance.rightClickPointV2(*self.randomPoint),4,10)
        
        continueWithUntilByWithBackup(lambda: self.inJourneyTask(), lambda: self.inCityList(cityList), 8, timeout=self.waitForCityTimeOut,notifyFunc=lambda: self.print("not found, wait for 8s"),backupFunc=backupFunc)
        self.print("click twice")
        self.clickEnterCityButton()

    def checkForGiftAndReceive(self):
        if(self.isPositionColorSimilarTo(1078,9,(245, 70, 60))):
            wait(lambda: self.simulatorInstance.clickPointV2(1068,25),1)
            wait(lambda: self.simulatorInstance.clickPointV2(346,572),1)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.randomPoint),2,0.2)

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
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(895,570),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(cityName), 3,2,backupFunc=backup)

    def buyInCity(self,cityList,products,buyStrategy=False):
        self.print("去超市")
        market=Market(self.simulatorInstance, self)

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
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(cityList), 3,2,backupFunc=backup)

    def clickInMenu(self,menuItem,inTitle):
        wait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1)  

        area=[1111,242,1195,265]
        index=0
        while(index<13):
            yDiff=int(index*37.8)
            if(self.hasSingleLineWordsInArea(menuItem, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1127,252+yDiff), lambda: self.hasSingleLineWordsInArea(inTitle, A=self.titleArea),2,2)
                break
            index+=1
        if(index==13):
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
        time.sleep(random.randint(3,5))

    def getTime(self):
        try:
            timeOCR=self.getSingleLineWordsInArea(A=[1255,213,1296,232], ocrType=2)
            return int(timeOCR[0:2])
        except Exception as e:
            print(e)    
            return 12

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
    def gotoCity(self,cityname,cityList,dumpCrew=False):
        self.goToHarbor()
        self.depart()
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,1)
        wait(lambda: self.findCityAndClick(cityname),2)
        if(dumpCrew):
            self.dumpCrew()
        self.waitForCity(cityList,targetCity=cityname)
        self.sendMessage("UW","reached city of "+cityname)

    def startTradeRoute(self):
        routeObjIndex=0
        routeObject=None
        self.setCurrentCityFromScreen()
        for index,obj in enumerate(self.routeList):
            if(self.currentCity in obj["buyCities"] or self.currentCity in list(map(lambda x: x["name"], obj["sellCities"]))):
                routeObjIndex=index
                routeObject=obj
        if(routeObject==None):
            self.print("没有在长途城市列表中，中断")
            return

        while(True):
            if(not(isWorkHour())):
                self.print("not working hour,sleep for 30mins")
                time.sleep(1800)
                continue

            self.tradeRouteBuyFin=False
            self.print("出发买东西城市")
            self.tradeRouteBuyFin=False
            while(self.tradeRouteBuyFin==False):
                # goto buy cities
                for city in routeObject["buyCities"]:
                    if(self.tradeRouteBuyFin==True):
                        break
                    self.gotoCity(city,self.allCityList)
                    self.checkReachCity()
                    if(self.getTime()>=0 and self.getTime()<5):
                        self.buyBlackMarket(city)
                    self.buyInCity(routeObject["buyCities"], products=routeObject["buyProducts"],buyStrategy=routeObject.get("buyStrategy"))
                    #special
                    self.checkSB()
                    self.buyBlackMarket(city)
                if(routeObject.get("buyStrategy")=="once"):
                    self.tradeRouteBuyFin=True
                #go to buy again if not full
                if(self.tradeRouteBuyFin!=True):
                    for city in routeObject["buySupplyCities"]:
                        self.gotoCity(city,self.allCityList)

            self.print("出发补给城市")
            #go to supply cities
            for city in routeObject["supplyCities"]:
                self.gotoCity(city,self.allCityList,dumpCrew=(city in (routeObject.get('dumpCrewCities') if routeObject.get('dumpCrewCities') else [])))
                self.checkReachCity()
                self.checkSB()
                self.buyBlackMarket(city)

            self.print("出发卖货城市")
            # goto sell cities
            for index,cityObject in enumerate(routeObject["sellCities"]):
                cityName=cityObject["name"]
                types=cityObject["types"]
                self.gotoCity(cityName,self.allCityList)
                self.checkReachCity()
                if(self.getTime()>=0 and self.getTime()<5):
                    self.buyBlackMarket(cityName)
                self.sellInCity(cityName,simple=True,types=types)
                self.buyBlackMarket(cityName)
                # if(index==len(routeObject["sellCities"])-1):
                #     self.buyInCity(cityName, products=routeObject["buyProducts"])

            #swap to other route side
            routeObjIndex+=1
            routeObject=self.routeList[(routeObjIndex)%2]








