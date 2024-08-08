import cv2
from cnocr import CnOcr
import numpy as np

ocr = CnOcr(cand_alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-'",det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
numberOcr=CnOcr(cand_alphabet="1234567890()-/,",det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
mixedOcr = CnOcr(cand_alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-1234567890'",det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
chineseOcr=CnOcr(det_model_name='naive_det')

def getCoordinateByScreenshotTarget(screenshotBlob, imagePath, greyMode=False):
    targetImage = cv2.imread(imagePath)
    targetHeigh, targetWidth, channel = targetImage.shape
    if(greyMode):
        targetImage=get_grayscale(targetImage)
        screenshotBlob=get_grayscale(screenshotBlob)
    result = cv2.matchTemplate(screenshotBlob, targetImage, cv2.TM_SQDIFF_NORMED)
    cv2 .normalize (result ,result ,0 ,1 ,cv2 .NORM_MINMAX ,-1 )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = min_loc

    if(min_val<0):
        min_val=-min_val
    if min_val<=(1e-8) and min_loc[0 ]!=0 and min_loc[1 ]!=0:
        return (min_loc[0 ],min_loc[1 ])
    else :
        return 0 ,0

def findImageFromSearchImage(screenshotBlob, template_image_path, threshold=0.9):
    # 读取目标图像和搜索图像
    template_image = cv2.imread(template_image_path)

    # 转换为浮点型图像
    search_float = np.float32(screenshotBlob)
    template_float = np.float32(template_image)

    # 执行模板匹配
    result = cv2.matchTemplate(search_float, template_float, cv2.TM_CCOEFF_NORMED)

    # 获取模板图像的尺寸
    template_height, template_width = template_image.shape[:2]

    # 找到匹配的最大值及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 判断是否找到匹配
    if max_val >= threshold:
        # 匹配成功
        top_left = max_loc
        bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

        # 计算相对位移（相对于搜索图像的左上角）
        relative_x = top_left[0]
        relative_y = top_left[1]

        return (relative_x, relative_y)
    else:
        # 匹配失败
        return 0,0

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
    elif(ocrType==3):
        ocrInstance=mixedOcr
    elif(ocrType==4):
        ocrInstance=chineseOcr
    res = ocrInstance.ocr_for_single_line(imageBlob)
    return res

def getOCRfromImageBlobMultiLine(imageBlob, ocrType=1):
    #gray = get_grayscale(imageBlob)
    ocrInstance=None
    if(ocrType==1):
        ocrInstance=ocr
    elif(ocrType==2):
        ocrInstance=numberOcr
    res = ocrInstance.ocr(imageBlob)
    return res

def getNumberFromString(str):
    if("," in str):
        return int(str.replace(",",""))
    else:
        return int(str)
    
def getNumberfromImageBlob(imageBlob):
    #gray = get_grayscale(imageBlob)
    try:
        res = numberOcr.ocr_for_single_line(imageBlob)
        if(len(res[0]) == 0):
            return None
        str = "".join(res[0])
        print("ocred number: "+ str)
        return getNumberFromString(str)
    except Exception as e:
        print(e)    
        return None       
    