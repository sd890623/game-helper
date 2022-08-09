from FrontTask import FrontTask
from windows import *
from images import *
from utils import *
from Market import Market
from Sb import Sb
import guiUtils
import time
import random
from playsound import playsound

# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","dover","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]

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

    def __init__(self, hwnd, index):
        FrontTask.__init__(self,hwnd,index)
        hwndObject = getChildHwndByTitleAndParentHwnd("Chrome Legacy Window",hwnd)
        parentWindow = guiUtils.win(hwnd, bor= True)
        parentWindow.moveWindow(10,10,1327,779)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"], bor= True)

    def testTask(self):        
        self.market()
        playerTypeMarkImagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"redLock"+".bmp")
        screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2()
        self.saveImageToFile(screenshotBlob)
        wait(lambda: self.simulatorInstance.rightClickPointV2(43,51),1)
        #print(self.simulatorInstance.window_capture_v2(playerTypeMarkImagePath, A=[512, 200, 622, 235]))

    def inCityList(self):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A=self.inTownCityNameArea)
            # self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob)
            if(len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])
            self.print(" ocred city: "+ str)
            for city in cityNames:
                if(city in str.lower()):
                    self.currentCity = city
                    return True
            return False
        except Exception as e:
            print(e)    
            return False      

    def setCurrentCityFromScreen(self):
        self.inCityList()

    def checkReachingPlace(self):
        if(self.targetCity==self.currentCity):
            self.playNotification()
            time.sleep(300)

    def playNotification(self):
        soundPath = os.path.abspath(__file__ + "\\..\\..\\assets\\alert1.mp3")
        #print(soundPath)
        # playsound("e:\\Workspaces\\Projects\\eveHelper2\\assets\\alert1.mp3")
        #playsound(soundPath)
        
    def findNextCityAndClick(self):
        index=cityNames.index(self.currentCity)
        nextCityName = None
        if((index+1)>len(cityNames)-1):
            nextCityName=cityNames[0]
        else:
            nextCityName = cityNames[index+1]
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
            time.sleep(1)
            timeout-=1
            yDiff=int(index%8*58.8)
            if(self.hasSingleLineWordsInArea(nextCityName, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                found=True
                break
            index+=1

        if(timeout<=0):
            self.selectCityFromMapAndMove(nextCityName)
            
        else:
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(firstPosi[0],firstPosi[1]+int(index%9*58)), 2,0.2)

        
    def goToHarbor(self):
        self.print("去码头")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1143,251), lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea),2,2)
        time.sleep(2)

    def restock(self):
        self.print("补给")
        # use emergency stock
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(57,85), lambda: self.hasSingleLineWordsInArea("supply", A=self.titleArea),1,2)

        if(self.hasSingleLineWordsInArea("o", A=[922,417,938,436])):
            doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(26,25),lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea), 1,2)
            return
        # Destroy excess
        # wait(lambda: self.simulatorInstance.click_point(662,398))
        # wait(lambda: self.simulatorInstance.click_point(1132,750))
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1005,424), 2,2)

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

    def selectCity(self):
        self.print("选城市")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2,1)
        self.findNextCityAndClick()

    def selectCityFromMapAndMove(self,cityname):
        self.print("select city from map")
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1277,193), lambda: self.hasSingleLineWordsInArea("world", A=self.titleArea), 2,2)
        wait(lambda: self.simulatorInstance.clickPointV2(38,89),2)
        wait(lambda: self.simulatorInstance.clickPointV2(86,77),2)
        self.simulatorInstance.typewrite(cityname)
        wait(lambda: self.simulatorInstance.clickPointV2(114,107),2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(651,699), lambda: self.hasSingleLineWordsInArea("waters", A=[74,15,256,46]),2,2)        


    def inJourneyTask(self):
        self.checkForGiftAndReceive()
        self.simulatorInstance.clickPointV2(*self.enterCityButton)
        #self.checkForBottleAndClick()

    def waitForCity(self):
        self.print("航行中")
        #click on "move immediately continusly"
        def backupFunc():
            wait(self.selectCity, 15)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.enterCityButton),3,15)
        continueWithUntilByWithBackup(lambda: self.inJourneyTask(), lambda: self.inCityList(), 6, timeout=420, backupFunc=backupFunc)
        time.sleep(random.randint(1,3))
        print("click twice")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.enterCityButton),2,1)


    #todo
    def checkForGiftAndReceive(self):
        if(self.hasImageInScreen("redDot", A=[1106,2,1128,22], greyMode=True)):
            wait(lambda: self.simulatorInstance.clickPointV2(1100,21),2)
            wait(lambda: self.simulatorInstance.clickPointV2(332,588),2)

    ## Not use
    def checkForBottleAndClick(self):
        position=self.hasImageInScreen("flowBottle")
        if(position):
            wait(lambda: self.simulatorInstance.clickPointV2(position[0], position[1]))

    def market(self):
        self.print("去超市")
        #mem overflow?
        market=Market(self.simulatorInstance, self)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),1, 1)  
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1140,281), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea),2,2)

        #sell
        market.sellV3()
        time.sleep(3)
                
        #buy
        market.buyV2()

        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(*self.rightTopTownIcon), lambda: self.inCityList(), 3,2)   

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
        if(self.currentCity==self.sbCity):
            self.shipBuilding(self.sbOptions, self.sbCity, 1)

    def startJourney(self):
        self.goToHarbor()
        # self.restock()
        self.depart()
        self.selectCity()
        self.waitForCity()
        self.market()
        self.checkReachingPlace()
        self.checkSB()
        time.sleep(random.randint(3,5))
