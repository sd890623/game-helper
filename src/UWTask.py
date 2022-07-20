from windows import *
from images import *
from utils import *
import guiUtils
import time
import random
import cv2

cityNames = ["syracuse", "naples", "pisa", "genoa", "marseille", "montpellier", "palma", "valencia", "algiers", "sassari", "cagliari", "tunis", "tripoli", "benghazi"]

class UWTask:

    #window size: 1495,860 chrome remote content window

    hwnd = None
    simulatorInstance = None
    syncBetweenUsers = True
    currentCity = "syracuse"
    def __init__(self, hwnd, index):
        self.hwnd = hwnd
        self.index = index
        hwndObject = getWindowSubObjectById(hwnd)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"], bor= True)

    def runTask(self):        
        playerTypeMarkImagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"anchor"+".bmp")
        screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2()
        self.saveImageToFile(screenshotBlob)
        print(self.simulatorInstance.window_capture_v2(playerTypeMarkImagePath))

    def hasImageInScreen(self, imageName, A=[0,0,0,0]):
        imagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+imageName+".bmp")
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            self.saveImageToFile(screenshotBlob)
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
            #print(position[0]+int(targetWidth/2), position[1]+int(targetHeigh/2))
            wait(lambda: self.simulatorInstance.click_point(position[0]+int(targetWidth/2), position[1]+int(targetHeigh/2)), 2)

    def hasSingleLineWordsInArea(self, words, A=[0,0,0,0]):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob)
            if(len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])
            
            print(words +" in "+ str)
            return words in str.lower()
        except Exception as e:
            print(e)    
            return False         

    def inCityList(self):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A=[110,25,236,52])
            #self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob)
            if(len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])
            print(" ocred city: "+ str)
            for city in cityNames:
                if(city in str.lower()):
                    self.currentCity = city
                    return True
            return False
        except Exception as e:
            print(e)    
            return False      

    def findNextCityAndClick(self):
        index=cityNames.index(self.currentCity)
        nextCityName = None
        if((index+1)>len(cityNames)-1):
            nextCityName=cityNames[0]
        else:
            nextCityName = cityNames[index+1]
        print(nextCityName)

        #firstCityPosi in list 1314,231,1364,249
        #height between 47.4
        firstPosi = (1328,239)
        area=[1316,231,1407,249]
        index=0
        found=False
        while(not(found)):
            time.sleep(1)
            yDiff=int(index%10*52.7)
            if(self.hasSingleLineWordsInArea(nextCityName, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                found=True
                break
            index+=1

        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(firstPosi[0],firstPosi[1]+int(index%10*52.7)), 2)
            

    # 1318,90, 1st point
    # 1366,91, 2nd point
    # 110,25,236,52 in harbor city name area
    # 54,17,142,55 title area, Harbor/Supply,etc
    def goToHarbor(self):
        self.print("去码头")
        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(1366,91),2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(1310,234), lambda: self.hasSingleLineWordsInArea("harbor", A=[54,17,142,55]))
    
    def restock(self):
        self.print("补给")
        wait(lambda: self.simulatorInstance.click_point(1465,385),1)
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(1465,385), lambda: self.hasSingleLineWordsInArea("supply", A=[54,17,142,55]),1)
        # Destroy excess
        # wait(lambda: self.simulatorInstance.click_point(662,398))
        # wait(lambda: self.simulatorInstance.click_point(1132,750))
        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(1058,396), 3)

    def depart(self):
        self.print("出海")
        wait(lambda: self.simulatorInstance.click_point(1370,620),2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(1370,620), lambda: self.hasSingleLineWordsInArea("waters", A=[68,24,238,53]))

    def selectCity(self):
        self.print("选城市")
        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(1364,91),2)
        #2nd city
        self.findNextCityAndClick()

    def inJourneyTask(self):
        self.checkForGiftAndReceive()
        self.simulatorInstance.click_point(1310,786)
        #self.checkForBottleAndClick()

    def waitForCity(self):
        self.print("航行中")
        #click on "move immediately continusly"
        continueWithUntilBy(lambda: self.inJourneyTask(), lambda: self.inCityList(), 9)

    def checkForGiftAndReceive(self):
        if(self.hasImageInScreen("redDot", A=[1329,13,1355,31])):
            wait(lambda: self.simulatorInstance.click_point(1324,33),2)
            wait(lambda: self.simulatorInstance.click_point(470,626),2)

    ## Not use
    def checkForBottleAndClick(self):
        position=self.hasImageInScreen("flowBottle")
        if(position):
            wait(lambda: self.simulatorInstance.click_point(position[0], position[1]))
                 
    def bargin(self):
        if(self.hasSingleLineWordsInArea("yes", A=[1094,736,1145,764])):
            #click yes
            wait(lambda: self.simulatorInstance.click_point(1126,752),10)
            #wait for dialog, click no regardless of successful.
            doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(1116,668),2)

    def market(self):
        self.print("去超市")
        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(1366,91),2)  
        wait(lambda: self.simulatorInstance.click_point(1329,268),1)      
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(1329,268), lambda: self.hasSingleLineWordsInArea("market", A=[54,17,142,55]))
        
        coinPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"coinInBuy"+".bmp")

        #sell
        wait(lambda: self.simulatorInstance.click_point(40,146),0.2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(40,146), lambda: self.hasSingleLineWordsInArea("sel", A=[54,17,142,55]), 1)
          
        count=7
        while(count>0):
            position=self.simulatorInstance.window_capture_v2(coinPath, A=[172,99,1192,370])
            if(self.hasSingleLineWordsInArea("noitemtosell", A=[623,444,737,469])):
                break
            else:
                print("sell item x")
                count-=1
                wait(lambda: self.simulatorInstance.click_point(position[0], position[1]),0.2)
                if(self.hasSingleLineWordsInArea("-", A=[1401,761,1469,782])):
                    self.clickWithImage("crossInSell", A=[1203,94,1274,131])
                    continue  
                wait(lambda: self.simulatorInstance.click_point(1398,808),1)
                wait(lambda: self.simulatorInstance.click_point(809,658))
                self.bargin()
                doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(809,658),3,1) 
                

        #buy
        wait(lambda: self.simulatorInstance.click_point(54,88),0.2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(54,88), lambda: self.hasSingleLineWordsInArea("purch", A=[54,17,142,55]), 1)        
        while(True):
            if(self.hasSingleLineWordsInArea("max", A=[1212,126,1265,139])):
                break
            position=self.simulatorInstance.window_capture_v2(coinPath, A=[172,99,1192,370])

            if(position):
                print("buy item x")
                wait(lambda: self.simulatorInstance.click_point(position[0], position[1]),0.2)  
                wait(lambda: self.simulatorInstance.click_point(1398,808),1)
                wait(lambda: self.simulatorInstance.click_point(809,658))
                self.bargin()
                doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(809,658),3,1) 
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(1470,34), lambda: self.inCityList())        


    def print(self,text):
        print(getDateTimeString()+"： "+text)

    def startJourney(self):
        self.goToHarbor()
        self.restock()
        self.depart()
        self.selectCity()
        self.waitForCity()
        self.market()
        time.sleep(random.randint(1,5))

    def saveImageToFile(self,imageBlob):
        screenshotImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\screenshots\\"+str(self.index)+"\\players.bmp")
        cv2.imwrite(screenshotImgPath, imageBlob)  