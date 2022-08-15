from FrontTask import FrontTask
from windows import *
from images import *
from utils import *
from Market import Market
from Sb import Sb
import guiUtils
import time
import random
from constants import cityNames, routeList

allCityList=cityNames+routeList[0]["buyCities"]+routeList[1]["buyCities"]+routeList[0]["supplyCities"]+routeList[1]["supplyCities"]

class UWTask(FrontTask):
    rightCatePoint1=1119,92
    rightCatePoint2=1171,88
    titleArea=[49,8,187,45]
    rightTopTownIcon=1285,25
    inTownCityNameArea=[119,18,265,48]
    inScreenConfirmYesButton=977,639
    enterCityButton=1075,671
    #client screen size: 1280x720
    #remote control setup size:

    simulatorInstance = None
    syncBetweenUsers = True
    currentCity = "ceuta"
    targetCity=None
    sbCity=None
    sbOptions=[]
    shipBeingBuilt=False
    fastStock=False
    tradeRouteBuyFin=False

    def __init__(self, hwnd, index):
        FrontTask.__init__(self,hwnd,index)
        hwndObject = getChildHwndByTitleAndParentHwnd("Chrome Legacy Window",hwnd)
        parentWindow = guiUtils.win(hwnd, bor= True)
        parentWindow.moveWindow(10,10,1327,779)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"], bor= True)

    def testTask(self):        
        # messager=Messager()
        # messager.sendMessage("reached A city")
        onionPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\products\\"+"onion"+".bmp")
        # screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2()
        # self.saveImageToFile(screenshotBlob)
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
                    self.sendMessage("UW","reached city of "+city)
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
        self.inCityList(allCityList)

    def checkReachingPlace(self):
        if(self.targetCity==self.currentCity):
            self.playNotification()
            time.sleep(300)

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
        area=[1113,240,1198,266]
        timeout=16
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
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(firstPosi[0],firstPosi[1]+int(index%8*58.8)), 2,0.2)

        
    def goToHarbor(self):
        self.print("去码头")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1143,251), lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),2,2)

    def restock(self):
        self.print("补给")
        # use emergency stock
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(57,85), lambda: self.hasSingleLineWordsInArea("supply", A=self.titleArea),1,2)

        if(self.hasSingleLineWordsInArea("0", A=[922,417,938,436],ocrType=2) and len(self.getSingleLineWordsInArea(A=[922,417,958,437],ocrType=2))==1):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(26,25),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)
            return
        # Destroy excess
        # wait(lambda: self.simulatorInstance.click_point(662,398))
        # wait(lambda: self.simulatorInstance.click_point(1132,750))
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1005,424), 2,2)
        #Restore crew
        if(self.hasSingleLineWordsInArea("notenough",A=[1078,449,1167,471])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1164,464),lambda: self.hasSingleLineWordsInArea("recruit", A=self.titleArea), 1,2)
            wait(lambda: self.simulatorInstance.clickPointV2(1240,509),2)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(714,483),2,2)
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(26,25),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)



    def depart(self):
        def clickAndStock():
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(979,538),2,1)
            if(not(self.fastStock)):
                self.restock()
            else:
                wait(lambda: self.simulatorInstance.clickPointV2(1183,568),1)
                wait(lambda: self.simulatorInstance.clickPointV2(716,485),1)

        clickAndStock()
        self.print("出海")

        # wait(lambda: self.simulatorInstance.clickPointV2(1183,568),2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1183,568), lambda: self.hasSingleLineWordsInArea("waters", A=[74,15,256,46]), 15,2, backupFunc=clickAndStock)
        time.sleep(4)

    def selectNextCity(self):
        self.print("选城市")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,1)
        self.findCityAndClick()

    def selectCityFromMapAndMove(self,cityname):
        self.print("select city from map")
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1277,193), lambda: self.hasSingleLineWordsInArea("world", A=self.titleArea), 2,2)
        wait(lambda: self.simulatorInstance.clickPointV2(38,89),2)
        wait(lambda: self.simulatorInstance.clickPointV2(86,77),2)
        self.simulatorInstance.typewrite(cityname)
        self.simulatorInstance.send_enter()
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(114,107),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.doubleClickPointV2(651,699), lambda: self.hasSingleLineWordsInArea("waters", A=[74,15,260,46]),2,2)

    def checkForDisaster(self):
        #click disaster icon
        wait(lambda: self.simulatorInstance.clickPointV2(637,388),1)
        if(self.hasSingleLineWordsInArea("miracle",A=[1076,602,1144,626])):
            #click use tool
            wait(lambda: self.simulatorInstance.clickPointV2(1094,547),2)
            #click yes
            wait(lambda: self.simulatorInstance.clickPointV2(*self.inScreenConfirmYesButton),2)

    def clickEnterCityButton(self):
        for x in range(2):
            if(self.hasSingleLineWordsInArea("move",A=[1089,660,1159,685])):
                wait(lambda: self.simulatorInstance.clickPointV2(970,674),0.5)
            else:
                wait(lambda: self.simulatorInstance.clickPointV2(*self.enterCityButton),0.5)

    def inJourneyTask(self):
        self.checkForDisaster()
        self.checkForGiftAndReceive()
        self.clickEnterCityButton()

    def waitForCity(self,cityList=None,targetCity=None):
        self.print("航行中")
        #click on "move immediately continusly"
        def backupFunc():
            wait(lambda: self.findCityAndClick(targetCity), 15)   
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.enterCityButton),3,15)
        continueWithUntilByWithBackup(lambda: self.inJourneyTask(), lambda: self.inCityList(cityList), 8, timeout=420, backupFunc=backupFunc)
        print("click twice")
        self.clickEnterCityButton()

    def checkForGiftAndReceive(self):
        if(self.hasImageInScreen("redDot", A=[1084,6,1099,14], greyMode=True)):
            wait(lambda: self.simulatorInstance.clickPointV2(1068,25),1)
            wait(lambda: self.simulatorInstance.clickPointV2(346,572),1)
            self.clickEnterCityButton()

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
    def sellInCity(self,cityName):
        self.print("去超市")
        market=Market(self.simulatorInstance, self)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1140,281), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

        #sell
        market.sellGoodsWithMargin()
        time.sleep(3)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(cityName), 3,2)

    def buyInCity(self,cityName,products):
        self.print("去超市")
        market=Market(self.simulatorInstance, self)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1140,281), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

        #buy
        market.buyProductsInCity(products)
        time.sleep(3)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCity(cityName), 3,2)

    def shipBuilding(self,options=[0], city="faro", times=30):
        self.print("SB 开始")
        self.shipBeingBuilt=False
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
        self.checkReachingPlace()
        self.checkSB()
        time.sleep(random.randint(3,5))

    #cityList is an array to contain the target city
    def gotoCity(self,cityname,cityList):
        self.goToHarbor()
        self.depart()
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,1)
        self.findCityAndClick(cityname)
        self.waitForCity(cityList,targetCity=cityname)

    def startTradeRoute(self):
        #Long journey, disable fast stock
        self.fastStock=False
        routeObjIndex=0
        routeObject=None
        self.setCurrentCityFromScreen()
        for index,obj in enumerate(routeList):
            if(self.currentCity in obj["buyCities"]):
                routeObjIndex=index
                routeObject=obj
        if(routeObject==None):
            self.print("没有在长途城市列表中，中断")
            return

        while(True):
            self.print("出发卖货城市")
            # goto sell city
            self.gotoCity(routeObject["sellCity"],allCityList)
            self.sellInCity(routeObject["sellCity"])

            self.print("出发买东西城市")
            # goto buy cities
            self.tradeRouteBuyFin=False
            for city in routeObject["buyCities"]:
                if(self.tradeRouteBuyFin==True):
                    break
                self.gotoCity(city,allCityList)
                self.buyInCity(city, products=routeObject["buyProducts"])
            #go to buy again if not full
            if(self.tradeRouteBuyFin!=True):
                for city in routeObject["buySupplyCities"]:
                    self.gotoCity(city,allCityList)
            # time.sleep(1200)
            for city in routeObject["buyCities"]:
                if(self.tradeRouteBuyFin==True):
                    break
                self.gotoCity(city,allCityList)
                self.buyInCity(city, products=routeObject["buyProducts"])            

            self.print("出发补给城市")
            #go to supply cities
            for city in routeObject["supplyCities"]:
                self.gotoCity(city,allCityList)
                self.checkSB()

            #swap to other route side
            routeObjIndex+=1
            routeObject=routeList[(routeObjIndex)%2]








