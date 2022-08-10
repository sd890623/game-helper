from windows import *
from images import *
from utils import *
import guiUtils

class FrontTask(object):
    hwnd = None
    simulatorInstance = None
    index = None
    syncBetweenUsers = True
    def __init__(self, hwnd, index):
        self.hwnd = hwnd
        self.index = index
        hwndObject = getWindowHwndObjectById(hwnd)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"], bor= True)

    def print(self,text):
        print(getDateTimeString()+"： "+text)

    def hasImageInScreen(self, imageName, A=[0,0,0,0], greyMode=False):
            imagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+imageName+".bmp")
            try:
                screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
                # self.saveImageToFile(screenshotBlob)
                x,y = getCoordinateByScreenshotTarget(screenshotBlob, imagePath, greyMode)

                if(x and y):
                    print(x+A[0],y+A[1])
                    return (x+A[0],y+A[1])
                else:
                    return False
            except Exception as e:
                print(e)    
                return False  

    def clickWithImage(self, imageName, A=[0,0,0,0], imagePrefix=""):
        imagePrefix=(imagePrefix+"\\") if imagePrefix!="" else ""
        imagePath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+imagePrefix+imageName+".bmp")
        targetImage = cv2.imread(imagePath)
        targetHeigh, targetWidth, channel = targetImage.shape
        position=self.simulatorInstance.window_capture_v2(imagePath, A)
        if(position):
            #self.print(position[0]+int(targetWidth/2), position[1]+int(targetHeigh/2))
            wait(lambda: self.simulatorInstance.clickPointV2(position[0]+int(targetWidth/2), position[1]+int(targetHeigh/2)), 2)

    def getSingleLineWordsInArea(self, A=[0,0,0,0], ocrType=1):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            # self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if(len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])
            self.print("ocr "+ str.lower())
            return str.lower()
        except Exception as e:
            print(e)    
            return False    

    def hasSingleLineWordsInArea(self, words, A=[0,0,0,0], ocrType=1):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            # self.saveImageToFile(screenshotBlob)
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
        # self.saveImageToFile(screenshotBlob)
        return getNumberfromImageBlob(screenshotBlob)

    def bringWindowToFront(self):
        self.simulatorInstance.bringWindowToFront()

    def saveImageToFile(self,imageBlob):
        screenshotImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\screenshots\\"+str(self.index)+"\\players.bmp")
        cv2.imwrite(screenshotImgPath, imageBlob)  