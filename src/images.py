import cv2
from cnocr import CnOcr

ocr = CnOcr(cand_alphabet="0123456789")
def getCoordinateByScreenshotTarget(screenshotBlob, imagePath):
    targetImage = cv2.imread(imagePath)
    targetHeigh, targetWidth = targetImage.shape
    
    result = cv2.matchTemplate(screenshotBlob, targetImage, cv2.TM_SQDIFF_NORMED)
    upperLeft = cv2.minMaxLoc(result)[2]
    lowerRight = (upperLeft[0] + targetWidth, upperLeft[1] + targetHeigh)
    middlePoint = (int((upperLeft[0]+lowerRight[0])/2), int((upperLeft[1]+lowerRight[1])/2))

    return middlePoint


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)

def getOCRfromImageBlob(imageBlob):
    #gray = get_grayscale(imageBlob)
    res = ocr.ocr_for_single_line(imageBlob)
    return res
