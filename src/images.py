import cv2
from cnocr import CnOcr

ocr = CnOcr(cand_alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-")
def getCoordinateByScreenshotTarget(screenshotBlob, imagePath):
    targetImage = cv2.imread(imagePath)
    targetHeigh, targetWidth, channel = targetImage.shape
    
    result = cv2.matchTemplate(screenshotBlob, targetImage, cv2.TM_SQDIFF_NORMED)
    # return (cv2.minMaxLoc(result)[2])
    cv2 .normalize (result ,result ,0 ,1 ,cv2 .NORM_MINMAX ,-1 )#line:93
    a ,b ,c ,d =cv2 .minMaxLoc (result )#line:95
    OOOOO0OOOOOO0OOO0 =str (a )#line:99

    if abs (float (OOOOO0OOOOOO0OOO0 ))<=0.05 and c [0 ]!=0 and c [1 ]!=0 :#line:115
        return (c [0 ],c [1 ])
    else :#line:118
        return 0 ,0 #line:120

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
