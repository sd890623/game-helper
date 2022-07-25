from windows import *
from images import *
from utils import *
from Market import Market
from Sb import Sb
import guiUtils
import time
import random
import cv2
from playsound import playsound


cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "palma", "valencia", "malaga", "seville", "faro", "lisbon", "ceuta", "algiers", "cagliari","sassari"]


class UWTask:
    rightCatePoint1=1095,88
    rightCatePoint2=1144,85
    titleArea=[54,8,201,47]
    rightTopTownIcon=1249,26
    inTownCityNameArea=[116,18,222,44]
    inScreenConfirmYesButton=978,673
    #window size: 1280x768, vmware inside window size

    hwnd = None
    simulatorInstance = None
    syncBetweenUsers = True
    currentCity = "palma"
    targetCity=None
    def __init__(self, hwnd, index):
        self.hwnd = hwnd
        self.index = index
        hwndObject = getChildHwndByTitleAndParentHwnd("MKSWindow#0",hwnd)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"], bor= True)

    def runTask(self):        
        playerTypeMarkImagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"redLock"+".bmp")
        screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2()
        self.saveImageToFile(screenshotBlob)

        wait(lambda: self.simulatorInstance.rightClickPointV2(43,51),1)

        #print(self.simulatorInstance.window_capture_v2(playerTypeMarkImagePath, A=[512, 200, 622, 235]))

    def hasImageInScreen(self, imageName, A=[0,0,0,0]):
        imagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+imageName+".bmp")
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            #self.saveImageToFile(screenshotBlob)
            x,y = getCoordinateByScreenshotTarget(screenshotBlob, imagePath)

            if(x and y):
                print(x+A[0],y+A[1])
                return (x+A[0],y+A[1])
            else:
                return False
        except Exception as e:
            print(e)    
            return False  

    def clickWithImage(self, imageName, A=[0,0,0,0]):
        imagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+imageName+".bmp")
        targetImage = cv2.imread(imagePath)
        targetHeigh, targetWidth, channel = targetImage.shape
        position=self.simulatorInstance.window_capture_v2(imagePath, A)
        if(position):
            #self.print(position[0]+int(targetWidth/2), position[1]+int(targetHeigh/2))
            wait(lambda: self.simulatorInstance.clickPointV2(position[0]+int(targetWidth/2), position[1]+int(targetHeigh/2)), 2)

    def hasSingleLineWordsInArea(self, words, A=[0,0,0,0], ocrType=1):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            #self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if(len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])
            
            self.print(words +" in "+ str)
            return words in str.lower()
        except Exception as e:
            print(e)    
            return False      
    
    def getNumberFromSingleLineInArea(self, A=[0,0,0,0]):
        screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
        #self.saveImageToFile(screenshotBlob)
        return getNumberfromImageBlob(screenshotBlob)

    def inCityList(self):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A=self.inTownCityNameArea)
            #self.saveImageToFile(screenshotBlob)
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

    def bringWindowToFront(self):
        self.simulatorInstance.outputWindowScreenshotV2()

    def findNextCityAndClick(self):
        index=cityNames.index(self.currentCity)
        nextCityName = None
        if((index+1)>len(cityNames)-1):
            nextCityName=cityNames[0]
        else:
            nextCityName = cityNames[index+1]
        self.print(nextCityName)

        #firstCityPosi in list 1314,231,1364,249
        #height between 47.4
        firstPosi = (1328,239)
        area=[1316,231,1407,249]
        index=0
        found=False
        while(not(found)):
            # time.sleep(1)
            yDiff=int(index%10*52.7)
            if(self.hasSingleLineWordsInArea(nextCityName, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                found=True
                break
            index+=1

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(firstPosi[0],firstPosi[1]+int(index%10*52.7)), 2)
    
        
    def goToHarbor(self):
        self.print("去码头")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(*self.rightCatePoint2),2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1104,244), lambda: self.hasSingleLineWordsInArea("harbor", A=self.titleArea))
    
    def restock(self):
        self.print("补给")
        wait(lambda: self.simulatorInstance.clickPointV2(1465,385),1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1465,385), lambda: self.hasSingleLineWordsInArea("supply", A=self.titleArea),1)

        if(self.hasSingleLineWordsInArea("o", A=[990,394,1003,408])):
            wait(lambda: self.simulatorInstance.clickPointV2(23,27),1)
            return
        # Destroy excess
        # wait(lambda: self.simulatorInstance.click_point(662,398))
        # wait(lambda: self.simulatorInstance.click_point(1132,750))
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1058,396), 3)

    def depart(self):
        self.print("出海")
        wait(lambda: self.simulatorInstance.clickPointV2(1370,620),2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1370,620), lambda: self.hasSingleLineWordsInArea("waters", A=[68,24,238,53]))

    def selectCity(self):
        self.print("选城市")
        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1364,91),2,1)
        #2nd city
        self.findNextCityAndClick()

    def inJourneyTask(self):
        self.checkForGiftAndReceive()
        self.simulatorInstance.clickPointV2(1310,786)
        #self.checkForBottleAndClick()

    def waitForCity(self):
        self.print("航行中")
        #click on "move immediately continusly"
        def backupFunc():
            wait(self.selectCity, 15)
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1310,786),3,15)
        continueWithUntilByWithBackup(lambda: self.inJourneyTask(), lambda: self.inCityList(), 9, timeout=240, backupFunc=backupFunc)

    def checkForGiftAndReceive(self):
        if(self.hasImageInScreen("redDot", A=[1333,13,1350,26])):
            wait(lambda: self.simulatorInstance.clickPointV2(1324,33),2)
            wait(lambda: self.simulatorInstance.clickPointV2(470,626),2)

    ## Not use
    def checkForBottleAndClick(self):
        position=self.hasImageInScreen("flowBottle")
        if(position):
            wait(lambda: self.simulatorInstance.clickPointV2(position[0], position[1]))
                 
    def bargin(self):
        if(self.hasSingleLineWordsInArea("yes", A=[1094,736,1145,764])):
            #click yes
            wait(lambda: self.simulatorInstance.clickPointV2(1126,752),10)
            #wait for dialog, click no regardless of successful.
            doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1116,668),2)

    def market(self):
        self.print("去超市")
        #mem overflow?
        market=Market(self.simulatorInstance, self)

        doMoreTimesWithWait(lambda: self.simulatorInstance.clickPointV2(1366,91),2)  
        wait(lambda: self.simulatorInstance.clickPointV2(1329,268),1)      
        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1329,268), lambda: self.hasSingleLineWordsInArea("market", A=self.titleArea))

        #sell
        market.sellV3()
        time.sleep(2)
                
        #buy
        market.buyV2()

        doAndWaitUntilBy(lambda: self.simulatorInstance.clickPointV2(1470,34), lambda: self.inCityList())        

    def shipBuilding(self,options=[0], city="faro"):
        self.print("SB 开始")
        sb=Sb(self.simulatorInstance, self)
        timeout=45000      
        while(timeout>0):
            sb.pickup()
            sb.dismantle()
            for option in options:
                sb.build(option)
            sb.goBackTown(city)
            timeout-=1500
            self.print("一轮完成，开始等25分")
            time.sleep(1500)


    def print(self,text):
        print(getDateTimeString()+"： "+text)

    def startJourney(self):
        self.goToHarbor()
        self.restock()
        self.depart()
        self.selectCity()
        self.waitForCity()
        self.market()
        self.checkReachingPlace()
        time.sleep(random.randint(1,5))

    def saveImageToFile(self,imageBlob):
        screenshotImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\screenshots\\"+str(self.index)+"\\players.bmp")
        cv2.imwrite(screenshotImgPath, imageBlob)  