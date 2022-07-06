import cv2

def getCoordinateByScreenshotTarget(screenshotPath, imagePath):
    screenshot = cv2.imread(screenshotPath)
    targetImage = cv2.imread(imagePath)
    targetHeigh, targetWidth = targetImage.shape
    
    result = cv2.matchTemplate(screenshot, targetImage, cv2.TM_SQDIFF_NORMED)
    upperLeft = cv2.minMaxLoc(result)[2]
    lowerRight = (upperLeft[0] + targetWidth, upperLeft[1] + targetHeigh)
    middlePoint = (int((upperLeft[0]+lowerRight[0])/2), int((upperLeft[1]+lowerRight[1])/2))

    return middlePoint

