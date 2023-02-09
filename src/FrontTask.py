from windows import getChildHwndByTitleAndParentHwnd
from images import getOCRfromImageBlob, getCoordinateByScreenshotTarget, getOCRfromImageBlobMultiLine, getNumberfromImageBlob
from utils import wait, getDateTimeString, random, hasOneArrayStringInString, isStringSameOrSimilar, hasOneArrayStringSimilarToString
import guiUtils
from Messager import Messager
import math
import os
import cv2


class FrontTask(object):
    simulatorInstance = None
    index = None
    syncBetweenUsers = True

    def __init__(self, hwnd, index):
        childHwndObject = getChildHwndByTitleAndParentHwnd("MKSWindow#0", hwnd)
        parentWindow = guiUtils.win(hwnd, bor=True)
        parentWindow.moveWindow(10, 10)
        self.simulatorInstance = guiUtils.win(
            childHwndObject["hwnd"], parentHwnd=hwnd, bor=True)
        self.index = index
        self.messager = Messager()

    def print(self, text):
        print(getDateTimeString()+": "+text)

    def sendMessage(self, url, text):
        self.messager.sendMessage(url, getDateTimeString()+": "+text)

    def sendNotification(self, text):
        self.messager.sendNotification(getDateTimeString()+": "+text)

    def hasImageInScreen(self, imageName, A=[0, 0, 0, 0], greyMode=False, debug=False):
        imagePath = os.path.abspath(
            __file__ + "\\..\\..\\assets\\UWClickons\\"+imageName+".bmp")
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            if (debug):
                self.saveImageToFile(screenshotBlob)
            x, y = getCoordinateByScreenshotTarget(
                screenshotBlob, imagePath, greyMode)

            if (x and y):
                # print(x+A[0],y+A[1])
                return (x+A[0], y+A[1])
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def clickWithImage(self, imageName, A=[0, 0, 0, 0], imagePrefix=""):
        imagePrefix = (imagePrefix+"\\") if imagePrefix != "" else ""
        imagePath = os.path.abspath(
            __file__ + "\\..\\..\\assets\\UWClickons\\"+imagePrefix+imageName+".bmp")
        targetImage = cv2.imread(imagePath)
        targetHeigh, targetWidth, channel = targetImage.shape
        position = self.simulatorInstance.window_capture_v2(imagePath, A)
        if (position and position[0] and position[1]):
            # self.print(position[0]+int(targetWidth/2), position[1]+int(targetHeigh/2))
            wait(lambda: self.simulatorInstance.clickPointV2(
                position[0]+int(targetWidth/2), position[1]+int(targetHeigh/2)), 2)

    def getSingleLineWordsInArea(self, A=[0, 0, 0, 0], ocrType=1, debug=False):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            if (debug == True):
                self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if (len(ocrObj) == 0 or len(ocrObj[0]) == 0):
                return ""
            str = "".join(ocrObj[0])
            self.print("ocr " + str.lower())
            return str.lower()
        except Exception as e:
            print(e)
            return ""

    def getMultiLineWordsInArea(self, A=[0, 0, 0, 0], ocrType=1, debug=False):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            if (debug == True):
                self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlobMultiLine(screenshotBlob, ocrType)
            if (len(ocrObj) == 0 or len(ocrObj) == 0 or len(ocrObj[0]) == 0):
                return ""
            str = "".join(map(lambda lineObj: "".join(lineObj[0]), ocrObj))
            self.print("ocr " + str.lower())
            return str.lower()
        except Exception as e:
            print(e)
            return ""

    def hasSingleLineWordsInArea(self, words, A=[0, 0, 0, 0], ocrType=1, debug=False):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            if (debug == True):
                self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if (len(ocrObj) == 0 or len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])

            self.print(words + "==" + str)
            return isStringSameOrSimilar(words, str.lower())
        except Exception as e:
            print(e)
            return False

    def hasArrayStringEqualSingleLineWords(self, wordsArr, A=[0, 0, 0, 0], ocrType=1, debug=False):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            if (debug == True):
                self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if (len(ocrObj) == 0 or len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])

            self.print("one of "+",".join(wordsArr) + " in " + str)
            return hasOneArrayStringSimilarToString(str.lower(), wordsArr)
        except Exception as e:
            print(e)
            return False

    def hasArrayStringInSingleLineWords(self, wordsArr, A=[0, 0, 0, 0], ocrType=1, debug=False):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            if (debug == True):
                self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlob(screenshotBlob, ocrType)
            if (len(ocrObj) == 0 or len(ocrObj[0]) == 0):
                return False
            str = "".join(ocrObj[0])

            self.print("one of "+",".join(wordsArr) + " in " + str)
            return hasOneArrayStringInString(str.lower(), wordsArr)
        except Exception as e:
            print(e)
            return False

    def getNumberFromSingleLineInArea(self, A=[0, 0, 0, 0], debug=False):
        screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
        if (debug == True):
            self.saveImageToFile(screenshotBlob)
        return getNumberfromImageBlob(screenshotBlob)

    def hasArrayStringEqualMultiLineWords(self, wordsArr, A=[0, 0, 0, 0], ocrType=1, debug=False):
        try:
            screenshotBlob = self.simulatorInstance.outputWindowScreenshotV2(A)
            if (debug == True):
                self.saveImageToFile(screenshotBlob)
            ocrObj = getOCRfromImageBlobMultiLine(screenshotBlob, ocrType)
            if (len(ocrObj) == 0 or len(ocrObj[0]) == 0):
                return False
            str = "".join(map(lambda lineObj: "".join(lineObj[0]), ocrObj))
            self.print("one of "+",".join(wordsArr) + " in " + str)
            return hasOneArrayStringSimilarToString(str.lower(), wordsArr)
        except Exception as e:
            print(e)
            return False

    def bringWindowToFront(self):
        self.simulatorInstance.bringWindowToFront()

    def saveImageToFile(self, imageBlob, relaPath=False, filename=False):
        try:
            if (relaPath and filename):
                absPath = os.path.abspath(__file__ + relaPath)
                if not os.path.exists(absPath):
                    os.mkdir(absPath)
                    self.print("Directory " + absPath + " Created ")
                screenshotImgPath = absPath+"\\"+filename
            else:
                screenshotImgPath = os.path.abspath(__file__ + "\\..\\..\\assets\\screenshots\\"+str(
                    self.index)+"\\ocr-"+str(random.randint(0, 10000))+".bmp")
            cv2.imwrite(screenshotImgPath, imageBlob)
        except Exception as e:
            print(e)
            return False

    def isPositionColorSimilarTo(self, x, y, rgb):
        positionRGB = self.simulatorInstance.getColorRGBByPosition(x, y)
        if (not (positionRGB)):
            return False
        d = math.sqrt((positionRGB[0] - rgb[0]) ** 2 +
                      (positionRGB[1] - rgb[1]) ** 2 + (positionRGB[2] - rgb[2]) ** 2)
        if (d < 13):
            return True
        else:
            return False
