import cv2
from cnocr import CnOcr

ocr = CnOcr(cand_alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-")
numberOcr=CnOcr(cand_alphabet="1234567890-(),")
def getCoordinateByScreenshotTarget(screenshotBlob, imagePath, greyMode=False):
    targetImage = cv2.imread(imagePath)
    targetHeigh, targetWidth, channel = targetImage.shape
    if(greyMode):
        targetImage=get_grayscale(targetImage)
        screenshotBlob=get_grayscale(screenshotBlob)
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

def getOCRfromImageBlob(imageBlob, ocrType=1):
    #gray = get_grayscale(imageBlob)
    ocrInstance=None
    if(ocrType==1):
        ocrInstance=ocr
    elif(ocrType==2):
        ocrInstance=numberOcr
    res = ocrInstance.ocr_for_single_line(imageBlob)
    return res

def getNumberfromImageBlob(imageBlob):
    #gray = get_grayscale(imageBlob)
    try:
        res = numberOcr.ocr_for_single_line(imageBlob)
        if(len(res[0]) == 0):
            return False
        str = "".join(res[0])
        print("ocred number: "+ str)
        if("," in str):
            return int(str.replace(",",""))+1000
        else:
            return int(str)
    except Exception as e:
        print(e)    
        return False       