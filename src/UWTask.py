from windows import *
from images import *
from utils import *
import guiUtils
import time
import random
import cv2

cityNames = ["thessaloniki", "athens", "candia", "syracuse", "naples", "pisa", "genoa", "marseille", "montpellier", "palma", "valencia", "algiers", "sassari", "cagliari", "tunis", "tripoli", "benghazi"]
class UWTask:

    #window size: 1495,860 chrome remote content window

    hwnd = None
    simulatorInstance = None
    index = None
    syncBetweenUsers = True
    currentCity = "genoa"
    def __init__(self, hwnd, index):
        self.hwnd = hwnd
        self.index = index
        hwndObject = getWindowSubObjectById(hwnd)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"], bor= True)

    def clickByImage(self, imageName, A =[0 ,0 ,0 ,0 ]):
        imagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+imageName+".bmp")
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            #self.saveImageToFile(screenshotBlob)
            x,y = getCoordinateByScreenshotTarget(screenshotBlob, imagePath)
            #print(x,y)
            if(not(x)):
                return
            self.simulatorInstance.click_point(x,y)
        except Exception as e:
            raise(e)

    def runTask(self):
        self.clickByImage("townsiteIcon")
#        self.simulatorInstance.click_point(40,85)

    def hasImageInScreen(self, imageName, A=[0,0,0,0]):
        imagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+imageName+".bmp")
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            self.saveImageToFile(screenshotBlob)
            x,y = getCoordinateByScreenshotTarget(screenshotBlob, imagePath)
            print(x,y)

            if(x and y):
                return (x,y)
            else:
                return False
        except Exception as e:
            print(e)    
            return False  

    def hasSingleLineWordsInArea(self, words, A=[0,0,0,0]):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            #self.saveImageToFile(screenshotBlob)
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
        nextCityName = cityNames[index+1]
        print(nextCityName)
        firstPosi = (1328,239)
        area=[1316,231,1407,249]
        index=0
        found=False
        while(not(found)):
            time.sleep(2)
            yDiff=int(index%10*52.7)
            print([area[0], area[1]+yDiff, area[2], area[3]+yDiff])
            if(self.hasSingleLineWordsInArea(nextCityName, A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])):
                found=True
                break
            index+=1

        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(firstPosi[0],firstPosi[1]+int(index%10*47.4)), 2)

        
            
        #firstCityPosi in list 1314,231,1364,249
        #height between 47.4
        

    # 1318,90, 1st point
    # 1366,91, 2nd point
    # 110,25,236,52 in harbor city name area
    # 54,17,142,55 title area, Harbor/Supply,etc
    def goToHarbor(self):
        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(1366,91),2)
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(1310,234), lambda: self.hasSingleLineWordsInArea("harbor", A=[54,17,142,55]))
    def restock(self):
        wait(lambda: self.simulatorInstance.click_point(1465,385))
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(1465,385), lambda: self.hasSingleLineWordsInArea("supply", A=[54,17,142,55]))
        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(1058,396), 3)

    def depart(self):
        wait(lambda: self.simulatorInstance.click_point(1370,620))
        doAndWaitUntilBy(lambda: self.simulatorInstance.click_point(1370,620), lambda: self.hasSingleLineWordsInArea("waters", A=[68,24,238,53]))

    def selectCity(self):
        doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(1364,91),2)
        #2nd city
        self.findNextCityAndClick()
        #doMoreTimesWithWait(lambda: self.simulatorInstance.click_point(1359,297), 2)

    def inJourneyTask(self):
        self.simulatorInstance.click_point(1310,786)
        self.checkForGiftAndReceive()
        #self.checkForBottleAndClick()

    def waitForCity(self):
        #click on "move immediately continusly"
        continueWithUntilBy(lambda: self.inJourneyTask(), lambda: self.inCityList())
        #wait(lambda: self.simulatorInstance.click_point(1319,94))
        #wait(lambda: self.simulatorInstance.click_point(1319,94))

    def checkForGiftAndReceive(self):
        if(self.hasImageInScreen("redDot", A=[1331,11,1348,27])):
            wait(lambda: self.simulatorInstance.click_point(1324,33),2)
            wait(lambda: self.simulatorInstance.click_point(470,626),2)

    def checkForBottleAndClick(self):
        position=self.hasImageInScreen("flowBottle")
        if(position):
            wait(lambda: self.simulatorInstance.click_point(position[0], position[1]))
                 
    def closeWindow(self):
        wait(lambda: self.simulatorInstance.click_point(76,32))
        wait(lambda: self.simulatorInstance.click_point(537,488))
        wait(lambda: self.simulatorInstance.click_keyboard("t"),30)

    def print(self,text):
        print(getDateTimeString()+" "+ str(self.index)+"号玩家： "+text)


    def startJourney(self):
        self.goToHarbor()
        self.restock()
        self.depart()
        self.selectCity()
        self.waitForCity()
        time.sleep(20)
    def findPlayerCountByType(self,type):
        count = 0
        iconWitdhHeight = 11
        playerTypeMarkImagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\"+type+".bmp")
        
        try:
            findPlayerCountLk.acquire()
            x,y = self.simulatorInstance.window_capture(playerTypeMarkImagePath, A=[5,463,167,489])
            countOcrArea = [x+iconWitdhHeight+3, y, x+iconWitdhHeight+1+14+15, y+iconWitdhHeight+5]
            countImageBlob = self.simulatorInstance.output_window_screenshot(A=countOcrArea)
            ocrCount = getOCRfromImageBlob(countImageBlob)
            findPlayerCountLk.release()
        except Exception as e:
            findPlayerCountLk.release()
            raise e  

        if(x == 0 and y == 0):
            self.print("没打开人物列表？")
            return 0

        try:
            if(len(ocrCount[0]) == 0):
                return 0
            count = int(ocrCount[0][0])
            return count
        except:
            return 1

    def isPlayerInSite(self):
        leaveSiteImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\cloneCenter.bmp")
        minerImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\miner.bmp")
        cloneCenterX,y = self.simulatorInstance.window_capture(leaveSiteImgPath, A=[910,385,988,477])
        minerX,y = self.simulatorInstance.window_capture(minerImgPath, A=[927,525,996,593])

        if (cloneCenterX and not(minerX)):
            return "in"
        elif (minerX and not(cloneCenterX)):
            return "out"
        else:
            return "middle"
        

    def startMiningTask(self):
        if (self.syncBetweenUsers):
            self.print("账号差异化，等待x*60s")
            time.sleep(60*self.index)
            self.syncBetweenUsers = not(self.syncBetweenUsers)
        self.print("新一轮开始了")
        if(not(self.isSafe())):
            self.print("有海盗，蹲站")
            time.sleep(60+random.randint(0,5))
            return
        self.print("开始存货")
        self.stockOre()
        self.print("存货完毕")
        time.sleep(10)
        if(self.isSafe()):
            self.print("安全，出发")
            self.goOut()
            self.print("到达，开采")
        else:
            self.print("有海盗，蹲站")
            return
        self.print("采矿等待中")
        self.checkSafeForMinutes(13.2+random.randint(0,10)/10)
        self.print("回家")
        self.goHome()
        self.print("到家")
        time.sleep(30+random.randint(0,25))



    def stockOre(self):
        wait(lambda: self.simulatorInstance.click_keyboard("B"), 15)
        wait(lambda: self.simulatorInstance.click_point(86,430,True), 10)
        wait(lambda: self.simulatorInstance.click_keyboard("E"), 5)
        wait(lambda: self.simulatorInstance.click_point(98,129,True), 9)
        wait(lambda: self.simulatorInstance.click_point(380,136,True), 7)
        wait(lambda: self.simulatorInstance.click_point(961,31), 2)
        wait(lambda: self.simulatorInstance.click_point(961,31), 2)

    def isSafe(self):
        return self.findPlayerCountByType(self.exclamationRedPlayerType) < 1 and self.findPlayerCountByType(self.minusRedPlayerType) < 1 and self.findPlayerCountByType(self.whitePlayerType) < 1
    
    def checkSafeForMinutes(self, mins):
        frequency = 10
        totalSeconds = mins*60
        # count=0
        while(self.isSafe() and totalSeconds > 0):
            time.sleep(frequency)
            totalSeconds -= frequency
            #self.print("count:"+str(count))
            #count+=1
        if(self.isSafe()==False):
            self.syncBetweenUsers = True




        







        


    def saveImageToFile(self,imageBlob):
        screenshotImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\screenshots\\"+str(self.index)+"\\players.bmp")

        cv2.imwrite(screenshotImgPath, imageBlob)  

    def clickOnTestPic(self):
        targetImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\greenStars.bmp")

        #x,y = self.simulatorInstance.window_capture(targetImgPath, A=[0,325,194,598])
    
