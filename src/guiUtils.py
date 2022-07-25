import random #line:1
from ctypes import windll ,byref #line:2
from ctypes .wintypes import HWND ,POINT #line:3
import string #line:4
import time #line:5
import win32api #line:6
import win32con ,win32gui ,win32ui #line:7
import cv2 #line:8
import numpy as np #line:9
import base64 #line:10
import operator #line:11
import requests #line:12
import easyocr #line:13
import pydirectinput
from PIL import Image #line:23

def base642Str (OOO0OOOOOOOO0000O ):#line:16
    OO0O00O0O0OO00O00 =base64 .b64encode (OOO0OOOOOOOO0000O )#line:17
    return OO0O00O0O0OO00O00 .decode ('utf-8')#line:18
scale =1 #line:21

def getDecimalValueFromKeyStroke (keyStroke):
    mapping = [{"key": "b", "value": 66}, {"key": "q", "value": 81}, {"key": "w", "value": 87}, {"key": "e", "value": 69}, {"key": "r", "value": 82}, {"key": "t", "value": 84}, {"key": "y", "value": 89}, {"key": "1", "value": 49}, {"key": "2", "value": 50}, {"key": "3", "value": 51}, {"key": "4", "value": 52}, {"key": "5", "value": 53}, {"key": "6", "value": 54}, {"key": "`", "value": 192} ]
    for object in mapping:
        if (object["key"] == keyStroke.lower()):
            return object["value"]
    return None

def getPointOnLine (O0O000000000OO000 ,OOOOOOOO0O0O00O0O ,O0O0OOOOOO000O000 ,O00000O000O00000O ,O0OO0000OOO000OOO ):#line:26
    ""#line:29
    OOO0OO0000000OOO0 =((O0O0OOOOOO000O000 -O0O000000000OO000 )*O0OO0000OOO000OOO )+O0O000000000OO000 #line:30
    O0OOOO00OOO0OOOOO =((O00000O000O00000O -OOOOOOOO0O0O00O0O )*O0OO0000OOO000OOO )+OOOOOOOO0O0O00O0O #line:31
    return int (round (OOO0OO0000000OOO0 )),int (round (O0OOOO00OOO0OOOOO ))#line:32
class win ():#line:35
    def __init__ (OO00OO0O00O0OOO0O ,OO0OOO0O0OOOO0O0O ,bor =False ):#line:37
        OO00OO0O00O0OOO0O .reader =easyocr .Reader (['ch_sim','en'])#line:38
        if not bor :#line:39
            O00OO00OOO0O00OOO =[]#line:40
            def O0O00OO00OOOO0OO0 (OOO000OOO0OO00O00 ,O0OOOO00000O0O0O0 ):#line:42
                O00OO00OOO0O00OOO .append (OOO000OOO0OO00O00 )#line:43
                return True #line:44
            win32gui .EnumChildWindows (OO0OOO0O0OOOO0O0O ,O0O00OO00OOOO0OO0 ,'')#line:46
            global hwn #line:47
            hwn =O00OO00OOO0O00OOO [0 ]#line:48
            OO00OO0O00O0OOO0O .hwnd =hwn #line:49
        else :#line:50
            OO00OO0O00O0OOO0O .hwnd =OO0OOO0O0OOOO0O0O #line:51


    def outputWindowScreenshotV2(self ,A =[0 ,0 ,0 ,0 ],value =0.95 ):
        left, top, right, bot = win32gui.GetWindowRect(self .hwnd )#line:58
        w = right - left
        h = bot - top
        targetWidth =A [2 ]-A [0 ]#line:72
        targetHeight =A [3 ]-A [1 ]#line:73
        if(targetHeight == 0 and targetWidth == 0):
            targetWidth=w
            targetHeight=h
        win32gui.SetForegroundWindow(self .hwnd)
        time.sleep(0.5)

        hdesktop = win32gui.GetDesktopWindow()
        winDc =win32gui .GetWindowDC (hdesktop)#line:66
        mfcDc =win32ui .CreateDCFromHandle (winDc )#line:67
        saveDc =mfcDc .CreateCompatibleDC ()#line:68
        saveBitMap =win32ui .CreateBitmap ()#line:69
        saveBitMap.CreateCompatibleBitmap (mfcDc ,targetWidth ,targetHeight )#line:70
        saveDc .SelectObject (saveBitMap )#line:71

        saveDc .BitBlt ((0 ,0 ),(targetWidth ,targetHeight ),mfcDc ,(left+A[0], top+A[1]),win32con .SRCCOPY )#line:74
        OOOOO0OOO00OOOOO0 =saveBitMap .GetInfo ()#line:77
        O0O00OOOOO0OOO00O =saveBitMap .GetBitmapBits (True )#line:78
        OOOO00O0O0OO00000 =Image .frombuffer ('RGB',(OOOOO0OOO00OOOOO0 ['bmWidth'],OOOOO0OOO00OOOOO0 ['bmHeight']),O0O00OOOOO0OOO00O ,'raw','BGRX',0 ,1 )#line:81
        OOO00OOOOO0OO0O00 =cv2 .cvtColor (np .asarray (OOOO00O0O0OO00000 ),cv2 .COLOR_RGB2BGR )#line:82

        mfcDc.DeleteDC()
        saveDc.DeleteDC()
        win32gui.DeleteObject (saveBitMap.GetHandle())#line:111
        win32gui.ReleaseDC (self.hwnd ,winDc)#line:114

        return OOO00OOOOO0OO0O00


    def output_window_screenshot(self ,A =[0 ,0 ,0 ,0 ],value =0.95 ):
        OO00O0OO0O0OOO000 =win32gui .GetWindowRect (self .hwnd )#line:58
        OO00O0OO0O0OOO000 =list (OO00O0OO0O0OOO000 )#line:59
        width =OO00O0OO0O0OOO000 [2 ]-OO00O0OO0O0OOO000 [0 ]#line:61
        height =OO00O0OO0O0OOO000 [3 ]-OO00O0OO0O0OOO000 [1 ]#line:62
        targetWidth =A [2 ]-A [0 ]#line:72
        targetHeight =A [3 ]-A [1 ]#line:73
        if(targetHeight == 0 and targetWidth == 0):
            targetWidth=width
            targetHeight=height
        winDc =win32gui .GetWindowDC (self .hwnd )#line:66
        mfcDc =win32ui .CreateDCFromHandle (winDc )#line:67
        saveDc =mfcDc .CreateCompatibleDC ()#line:68
        saveBitMap =win32ui .CreateBitmap ()#line:69
        saveBitMap.CreateCompatibleBitmap (mfcDc ,targetWidth ,targetHeight )#line:70
        saveDc .SelectObject (saveBitMap )#line:71

        saveDc .BitBlt ((0 ,0 ),(targetWidth ,targetHeight ),mfcDc ,(A [0 ],A [1 ]),win32con .SRCCOPY )#line:74
        OOOOO0OOO00OOOOO0 =saveBitMap .GetInfo ()#line:77
        O0O00OOOOO0OOO00O =saveBitMap .GetBitmapBits (True )#line:78
        OOOO00O0O0OO00000 =Image .frombuffer ('RGB',(OOOOO0OOO00OOOOO0 ['bmWidth'],OOOOO0OOO00OOOOO0 ['bmHeight']),O0O00OOOOO0OOO00O ,'raw','BGRX',0 ,1 )#line:81
        OOO00OOOOO0OO0O00 =cv2 .cvtColor (np .asarray (OOOO00O0O0OO00000 ),cv2 .COLOR_RGB2BGR )#line:82

        mfcDc.DeleteDC()
        saveDc.DeleteDC()
        win32gui.DeleteObject (saveBitMap.GetHandle())#line:111
        win32gui.ReleaseDC (self.hwnd ,winDc)#line:114

        return OOO00OOOOO0OO0O00

        
    def window_capture (self ,O000OO00O0OO0O00O ,A =[0 ,0 ,0 ,0 ],value =0.95 ):#line:54
        try:
            OO00O0OO0O0OOO000 =win32gui .GetWindowRect (self .hwnd )#line:58
            OO00O0OO0O0OOO000 =list (OO00O0OO0O0OOO000 )#line:59
            width =OO00O0OO0O0OOO000 [2 ]-OO00O0OO0O0OOO000 [0 ]#line:61
            height =OO00O0OO0O0OOO000 [3 ]-OO00O0OO0O0OOO000 [1 ]#line:62
            targetWidth =A [2 ]-A [0 ]#line:72
            targetHeight =A [3 ]-A [1 ]#line:73
            if(targetHeight == 0 and targetWidth == 0):
                targetWidth=width
                targetHeight=height
            winDc =win32gui .GetWindowDC (self .hwnd )#line:66
            mfcDc =win32ui .CreateDCFromHandle (winDc )#line:67
            saveDc =mfcDc .CreateCompatibleDC ()#line:68
            saveBitMap =win32ui .CreateBitmap ()#line:69
            saveBitMap.CreateCompatibleBitmap (mfcDc ,targetWidth ,targetHeight )#line:70
            saveDc .SelectObject (saveBitMap )#line:71

            saveDc .BitBlt ((0 ,0 ),(targetWidth ,targetHeight ),mfcDc ,(A [0 ],A [1 ]),win32con .SRCCOPY )#line:74
            OOOOO0OOO00OOOOO0 =saveBitMap .GetInfo ()#line:77
            O0O00OOOOO0OOO00O =saveBitMap .GetBitmapBits (True )#line:78
            OOOO00O0O0OO00000 =Image .frombuffer ('RGB',(OOOOO0OOO00OOOOO0 ['bmWidth'],OOOOO0OOO00OOOOO0 ['bmHeight']),O0O00OOOOO0OOO00O ,'raw','BGRX',0 ,1 )#line:81
            OOO00OOOOO0OO0O00 =cv2 .cvtColor (np .asarray (OOOO00O0O0OO00000 ),cv2 .COLOR_RGB2BGR )#line:82
            OOO0O00OO0O00OOOO =OOO00OOOOO0OO0O00 #line:83
            O00OOO0O000000000 =cv2 .imread (O000OO00O0OO0O00O )#line:87
            O00O0OOO000O0OOO0 ,O0O0OO000O00O000O =O00OOO0O000000000 .shape [:2 ]#line:89
            O0000OO00O00OOOOO =cv2 .matchTemplate (OOO0O00OO0O00OOOO ,O00OOO0O000000000 ,cv2 .TM_SQDIFF_NORMED )#line:91
            cv2 .normalize (O0000OO00O00OOOOO ,O0000OO00O00OOOOO ,0 ,1 ,cv2 .NORM_MINMAX ,-1 )#line:93
            O0000O00O00O0OO0O ,OOO000OO0OOOO0000 ,O00O00O0OO0OOOOOO ,O0OOOO00000OOOO00 =cv2 .minMaxLoc (O0000OO00O00OOOOO )#line:95
            OOOOO0OOOOOO0OOO0 =str (O0000O00O00O0OO0O )#line:99

            mfcDc.DeleteDC()
            saveDc.DeleteDC()
            win32gui.DeleteObject (saveBitMap.GetHandle())#line:111
            win32gui.ReleaseDC (self.hwnd ,winDc)#line:114

            if abs (float (OOOOO0OOOOOO0OOO0 ))<=0.05 and O00O00O0OO0OOOOOO [0 ]!=0 and O00O00O0OO0OOOOOO [1 ]!=0 :#line:115
                return O00O00O0OO0OOOOOO [0 ]+A [0 ],O00O00O0OO0OOOOOO [1 ]+A [1 ]#line:117
            else :#line:118
                return 0 ,0 #line:120
        except Exception as e:
            print("window_capture error")
            raise e

    def window_capture_v2 (self ,O000OO00O0OO0O00O ,A =[0 ,0 ,0 ,0 ],value =0.95 ):#line:54
        try:
            left, top, right, bot = win32gui.GetWindowRect(self .hwnd )#line:58
            w = right - left
            h = bot - top

            targetWidth =A [2 ]-A [0 ]#line:72
            targetHeight =A [3 ]-A [1 ]#line:73
            if(targetHeight == 0 and targetWidth == 0):
                targetWidth=w
                targetHeight=h

            win32gui.SetForegroundWindow(self .hwnd)
            time.sleep(0.5)

            hdesktop = win32gui.GetDesktopWindow()
            winDc =win32gui .GetWindowDC (hdesktop)#line:66
            mfcDc =win32ui .CreateDCFromHandle (winDc )#line:67
            saveDc =mfcDc .CreateCompatibleDC ()#line:68
            saveBitMap =win32ui .CreateBitmap ()#line:69
            saveBitMap.CreateCompatibleBitmap (mfcDc ,targetWidth ,targetHeight )#line:70
            saveDc .SelectObject (saveBitMap )#line:71

            saveDc .BitBlt ((0 ,0 ),(targetWidth ,targetHeight ),mfcDc ,(left+A[0], top+A[1]),win32con .SRCCOPY )#line:74
            OOOOO0OOO00OOOOO0 =saveBitMap .GetInfo ()#line:77
            O0O00OOOOO0OOO00O =saveBitMap .GetBitmapBits (True )#line:78
            OOOO00O0O0OO00000 =Image .frombuffer ('RGB',(OOOOO0OOO00OOOOO0 ['bmWidth'],OOOOO0OOO00OOOOO0 ['bmHeight']),O0O00OOOOO0OOO00O ,'raw','BGRX',0 ,1 )#line:81
            OOO00OOOOO0OO0O00 =cv2 .cvtColor (np .asarray (OOOO00O0O0OO00000 ),cv2 .COLOR_RGB2BGR )#line:82
            OOO0O00OO0O00OOOO =OOO00OOOOO0OO0O00 #line:83
            O00OOO0O000000000 =cv2 .imread (O000OO00O0OO0O00O )#line:87
            O00O0OOO000O0OOO0 ,O0O0OO000O00O000O =O00OOO0O000000000 .shape [:2 ]#line:89
            O0000OO00O00OOOOO =cv2 .matchTemplate (OOO0O00OO0O00OOOO ,O00OOO0O000000000 ,cv2 .TM_SQDIFF_NORMED )#line:91
            cv2 .normalize (O0000OO00O00OOOOO ,O0000OO00O00OOOOO ,0 ,1 ,cv2 .NORM_MINMAX ,-1 )#line:93
            O0000O00O00O0OO0O ,OOO000OO0OOOO0000 ,O00O00O0OO0OOOOOO ,O0OOOO00000OOOO00 =cv2 .minMaxLoc (O0000OO00O00OOOOO )#line:95
            OOOOO0OOOOOO0OOO0 =str (O0000O00O00O0OO0O )#line:99

            mfcDc.DeleteDC()
            saveDc.DeleteDC()
            win32gui.DeleteObject (saveBitMap.GetHandle())#line:111
            win32gui.ReleaseDC (self.hwnd ,winDc)#line:114

            if abs (float (OOOOO0OOOOOO0OOO0 ))<=0.05 and O00O00O0OO0OOOOOO [0 ]!=0 and O00O00O0OO0OOOOOO [1 ]!=0 :#line:115
                return O00O00O0OO0OOOOOO [0 ]+A [0 ],O00O00O0OO0OOOOOO [1 ]+A [1 ]#line:117
            else :#line:118
                return 0 ,0 #line:120
        except Exception as e:
            print("window_capture error")
            raise e

    def window_str (OOO0OOOOOOOOOO0O0 ,A =[0 ,0 ,0 ,0 ],bor =True ):#line:122
        O0O0O0OO000O000OO =win32gui .GetWindowRect (OOO0OOOOOOOOOO0O0 .hwnd )#line:128
        O0O0O0OO000O000OO =list (O0O0O0OO000O000OO )#line:129
        OO00000O00OO0O0O0 =O0O0O0OO000O000OO [2 ]-O0O0O0OO000O000OO [0 ]#line:131
        OO0O00O00OOOO0000 =O0O0O0OO000O000OO [3 ]-O0O0O0OO000O000OO [1 ]#line:132
        O0000O0O0O0O0OO0O =A [2 ]-A [0 ]#line:133
        O0OOOOO000O000000 =A [3 ]-A [1 ]#line:134
        OO0OOO0O0O0O0O0O0 =win32gui .GetWindowDC (OOO0OOOOOOOOOO0O0 .hwnd )#line:136
        O00O0O0O0OOOOO0O0 =win32ui .CreateDCFromHandle (OO0OOO0O0O0O0O0O0 )#line:137
        O0O0OO00OOO0O0O00 =O00O0O0O0OOOOO0O0 .CreateCompatibleDC ()#line:138
        O0O0OOO00OOOOOOO0 =win32ui .CreateBitmap ()#line:139
        O0O0OOO00OOOOOOO0 .CreateCompatibleBitmap (O00O0O0O0OOOOO0O0 ,O0000O0O0O0O0OO0O ,O0OOOOO000O000000 )#line:140
        O0O0OO00OOO0O0O00 .SelectObject (O0O0OOO00OOOOOOO0 )#line:141
        O0000O0O0O0O0OO0O =A [2 ]-A [0 ]#line:142
        O0OOOOO000O000000 =A [3 ]-A [1 ]#line:143
        O0O0OO00OOO0O0O00 .BitBlt ((0 ,0 ),(O0000O0O0O0O0OO0O ,O0OOOOO000O000000 ),O00O0O0O0OOOOO0O0 ,(A [0 ],A [1 ]),win32con .SRCCOPY )#line:144
        OOO000O00O0000O00 =O0O0OOO00OOOOOOO0 .GetInfo ()#line:147
        O0O0OO0OO0O0OOOO0 =O0O0OOO00OOOOOOO0 .GetBitmapBits (True )#line:148
        OO00O0000OOO0O0OO =Image .frombuffer ('RGB',(OOO000O00O0000O00 ['bmWidth'],OOO000O00O0000O00 ['bmHeight']),O0O0OO0OO0O0OOOO0 ,'raw','BGRX',0 ,1 )#line:151
        OO000O0000OO00000 =cv2 .cvtColor (np .asarray (OO00O0000OOO0O0OO ),cv2 .COLOR_RGB2BGR )#line:153
        O0OO0OO000OO0O00O =OOO0OOOOOOOOOO0O0 .reader .readtext (OO000O0000OO00000 )#line:166
        if O0OO0OO000OO0O00O !=[]:#line:167
            if bor :#line:168
                OO0OOOO0O0O0O0000 ,OO00O0000O0O000OO =int ((O0OO0OO000OO0O00O [0 ][0 ][1 ][0 ]+O0OO0OO000OO0O00O [0 ][0 ][0 ][0 ])/2 +A [0 ]),int ((O0OO0OO000OO0O00O [0 ][0 ][1 ][1 ]+O0OO0OO000OO0O00O [0 ][0 ][0 ][1 ])/2 +A [1 ])#line:170
                return OO0OOOO0O0O0O0000 ,OO00O0000O0O000OO ,O0OO0OO000OO0O00O [0 ][2 ]#line:171
            else :#line:172
                return O0OO0OO000OO0O00O [0 ][2 ]#line:173
        else :#line:174
            return ''#line:175
    def window_color (O000000O0O00OOO0O ,O00OO0O0O0O0OOOO0 ,A =[0 ,0 ,0 ,0 ]):#line:176
        O0O00O0OOO00O0O00 =win32gui .GetWindowRect (O000000O0O00OOO0O .hwnd )#line:178
        O0O00O0OOO00O0O00 =list (O0O00O0OOO00O0O00 )#line:179
        OOO000O00OO0OOO0O =O0O00O0OOO00O0O00 [2 ]-O0O00O0OOO00O0O00 [0 ]#line:181
        OOOO0OOOOOOOOO0OO =O0O00O0OOO00O0O00 [3 ]-O0O00O0OOO00O0O00 [1 ]#line:182
        OOOO00OOOOO0OOO0O =A [2 ]-A [0 ]#line:183
        OOOO0OOOO000O0O0O =A [3 ]-A [1 ]#line:184
        O00OO0O0O00OO0OO0 =win32gui .GetWindowDC (O000000O0O00OOO0O .hwnd )#line:186
        O0O0OO000OO00O0OO =win32ui .CreateDCFromHandle (O00OO0O0O00OO0OO0 )#line:187
        OO0O0O0O00O0000O0 =O0O0OO000OO00O0OO .CreateCompatibleDC ()#line:188
        OO0OOO00OOO0O0OOO =win32ui .CreateBitmap ()#line:189
        OO0OOO00OOO0O0OOO .CreateCompatibleBitmap (O0O0OO000OO00O0OO ,OOOO00OOOOO0OOO0O ,OOOO0OOOO000O0O0O )#line:190
        OO0O0O0O00O0000O0 .SelectObject (OO0OOO00OOO0O0OOO )#line:191
        OOOO00OOOOO0OOO0O =A [2 ]-A [0 ]#line:192
        OOOO0OOOO000O0O0O =A [3 ]-A [1 ]#line:193
        OO0O0O0O00O0000O0 .BitBlt ((0 ,0 ),(OOOO00OOOOO0OOO0O ,OOOO0OOOO000O0O0O ),O0O0OO000OO00O0OO ,(A [0 ],A [1 ]),win32con .SRCCOPY )#line:194
        O00OO00O0O0OOOOOO =OO0OOO00OOO0O0OOO .GetInfo ()#line:197
        OOOO0OO0O0O0OOO00 =OO0OOO00OOO0O0OOO .GetBitmapBits (True )#line:198
        O0O00OO00O000OOOO =Image .frombuffer ('RGB',(O00OO00O0O0OOOOOO ['bmWidth'],O00OO00O0O0OOOOOO ['bmHeight']),OOOO0OO0O0O0OOO00 ,'raw','BGRX',0 ,1 )#line:201
        O00000OO0O0OOOOO0 =cv2 .cvtColor (np .asarray (O0O00OO00O000OOOO ),cv2 .COLOR_RGB2BGR )#line:202
        O0OOOOOO0O00OOO0O ='D:\img\imgs'+'.jpg'#line:203
        cv2 .imwrite (O0OOOOOO0O00OOO0O ,O00000OO0O0OOOOO0 )#line:205
        for OOO0O0O0000O0O0O0 in range (len (O00000OO0O0OOOOO0 )):#line:206
            for OO0OO00O0000OO0O0 in range (len (O00000OO0O0OOOOO0 [0 ])):#line:207
                if all (operator .eq (O00000OO0O0OOOOO0 [OOO0O0O0000O0O0O0 ,OO0OO00O0000OO0O0 ],O00OO0O0O0O0OOOO0 )):#line:208
                    return True #line:210
        return False #line:212
    def mouse_move (OO00OO0OO00000OOO ,OO0OOO00OO0OOOO0O ,O0OO00O0O00O0OO0O ):#line:216
        if O0OO00O0O00O0OO0O is not None and OO0OOO00OO0OOOO0O is not None :#line:217
            O0O0000OOOO00OO00 =(OO0OOO00OO0OOOO0O ,O0OO00O0O00O0OO0O )#line:218
            win32api .SetCursorPos (O0O0000OOOO00OO00 )#line:219
            OO00OO0OO00000OOO .x =OO0OOO00OO0OOOO0O #line:220
            OO00OO0OO00000OOO .y =O0OO00O0O00O0OO0O #line:221
    def new_mousemove(self, x, y):
        tmp = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, tmp)
    def moveClickAndDrag(self, position, direction):
        x =position[0] +random .randint (10 ,10 )
        y =position[1] +random .randint (10 ,10 )
        win32api .SendMessage (self .hwnd ,win32con .WM_LBUTTONDOWN ,0 ,((y )<<16 |(x )));
        time.sleep(1)
        if (direction == "up"):
            self.mouse_move(x, y-80)
            time.sleep(1)
            win32api .SendMessage (self .hwnd ,win32con .WM_LBUTTONUP ,0 ,((y-80 )<<16 |(x )));
        elif (direction == "down"):
            self.mouse_move(x, y+80)
            time.sleep(1)
            win32api .SendMessage (self .hwnd ,win32con .WM_LBUTTONUP ,0 ,((y+80 )<<16 |(x )));
    def newClickAndDrag(self, position, direction):
        x =position[0] +random .randint (10 ,10 )
        y =position[1] +random .randint (10 ,10 )
        if (direction == "up"):
            self.move(x,y,x,y+80)
        elif (direction == "down"):
            self.move(x,y,x,y-80)

    def mouseWheel(self, position, direction):
        win32gui.SetForegroundWindow(self.hwnd)
        x =position[0] +random .randint (10 ,10 )
        y =position[1] +random .randint (10 ,10 )
        self.new_mousemove(x, y)

        if (direction == "up"):
            win32api.PostMessage(self.hwnd, win32con.WM_MOUSEWHEEL, win32api.MAKELONG(0, 120), win32api.MAKELONG(x,y))
            win32api.SendMessage(self.hwnd, win32con.WM_NCHITTEST, 0, win32api.MAKELONG(x,y))

        elif (direction == "down"):
            win32api.PostMessage(self.hwnd, win32con.WM_MOUSEWHEEL, win32api.MAKELONG(0, -120), win32api.MAKELONG(x,y))
            win32api.SendMessage(self.hwnd, win32con.WM_NCHITTEST, 0, win32api.MAKELONG(x,y))

    def click_point (O0000000OOO00000O ,x ,y ,bor =True ):#line:223
        if bor :#line:224
            xRandom =x +random .randint (-5 ,5 )#line:225
            yRandom =y +random .randint (-5 ,5 )#line:226
        long_position = win32api.MAKELONG(xRandom, yRandom)
        win32api .SendMessage (O0000000OOO00000O .hwnd ,win32con .WM_LBUTTONDOWN ,win32con.MK_LBUTTON ,long_position);#line:228
        win32api .SendMessage (O0000000OOO00000O .hwnd ,win32con .WM_LBUTTONUP ,win32con.MK_LBUTTON , long_position);#line:229
    def clickPointV2(self,x,y,random=False):
        if(random):
            xRandom =x +random .randint (-5 ,5 )
            yRandom =y +random .randint (-5 ,5 )
        else:
            xRandom=x
            yRandom=y
        left, top, right, bot = win32gui.GetWindowRect(self.hwnd)
        pydirectinput.moveTo(xRandom+left, yRandom+top)
        time.sleep(0.5)
        pydirectinput.leftClick(xRandom+left, yRandom+top)

    def doubleClickPointV2(self,x,y,random=False):
        if(random):
            xRandom =x +random .randint (-5 ,5 )
            yRandom =y +random .randint (-5 ,5 )
        else:
            xRandom=x
            yRandom=y
        left, top, right, bot = win32gui.GetWindowRect(self.hwnd)
        pydirectinput.moveTo(xRandom+left, yRandom+top)
        time.sleep(0.5)
        pydirectinput.doubleClick(xRandom+left, yRandom+top)

    def rightClickPointV2(self,x,y,random=False):
        if(random):
            xRandom =x +random .randint (-5 ,5 )
            yRandom =y +random .randint (-5 ,5 )
        else:
            xRandom=x
            yRandom=y
        left, top, right, bot = win32gui.GetWindowRect(self.hwnd)
        pydirectinput.rightClick(xRandom+left, yRandom+top)

    def send_enter (O00000OOOOOOOOOO0 ):#line:231
        win32api .SendMessage (O00000OOOOOOOOOO0 .hwnd ,win32con .WM_KEYDOWN ,13 ,0 )#line:232
        win32api .SendMessage (O00000OOOOOOOOOO0 .hwnd ,win32con .WM_KEYUP ,13 ,0 )#line:233
    def click_keyboard (O00000OOOOOOOOOO0, keyStroke ):#line:231
        if (getDecimalValueFromKeyStroke(keyStroke)):
            win32api .SendMessage (O00000OOOOOOOOOO0 .hwnd ,win32con .WM_KEYDOWN ,getDecimalValueFromKeyStroke(keyStroke) ,0 )#line:232
            win32api .SendMessage (O00000OOOOOOOOOO0 .hwnd ,win32con .WM_KEYUP ,getDecimalValueFromKeyStroke(keyStroke) ,0 )#line:233
    def send_str (OO0O00000O0O0O0O0 ,OO00000OOOOOOOOO0 ):#line:235
        O0O0OOO0OOOOO0O00 =[ord (OOOOO0O0OO0OO00O0 )for OOOOO0O0OO0OO00O0 in OO00000OOOOOOOOO0 ]#line:236
        for OOO0000OOOOO0OO0O in O0O0OOO0OOOOO0O00 :#line:237
            win32api .PostMessage (OO0O00000O0O0O0O0 .hwnd ,win32con .WM_CHAR ,OOO0000OOOOO0OO0O ,0 )#line:238
    def move (OOOO0O000O00000OO ,OOOO00000O0O00OOO ,OO0000OOO00000000 ,OO00OO0OOOO0O00OO ,O0OO0O0OOO0OO00O0 ):#line:240
        O00OO0O000OOO0O0O =win32api .MAKELONG (OOOO00000O0O00OOO ,OO0000OOO00000000 )#line:241
        O0OO000O000OOO0OO =win32api .MAKELONG (OO00OO0OOOO0O00OO ,O0OO0O0OOO0OO00O0 )#line:243
        print ('开始点击')#line:244
        win32api .SendMessage (OOOO0O000O00000OO .hwnd ,win32con .WM_LBUTTONDOWN ,0 ,((OO0000OOO00000000 )<<16 |(OOOO00000O0O00OOO )))#line:245
        print ('开始移动')#line:246
        time .sleep (1 )#line:247
        win32gui .SendMessage (OOOO0O000O00000OO .hwnd ,win32con .WM_MOUSEMOVE ,win32con .MK_LBUTTON ,O0OO000O000OOO0OO )#line:248
        time .sleep (1 )#line:249
        win32gui .SendMessage (OOOO0O000O00000OO .hwnd ,win32con .WM_LBUTTONUP ,0 ,0 )#line:250
        time .sleep (1 )#line:251

    def close_window(self):
        win32gui.PostMessage(self.hwnd,win32con.WM_CLOSE,0,0)

def image_binarization (O00OO000O0000OO00 ):#line:254
    O00OOOO000O000O00 =cv2 .cvtColor (O00OO000O0000OO00 ,cv2 .COLOR_BGR2GRAY )#line:257
    O0OO000O0O00OO0O0 ,OO0O00OOOO0O00OO0 =cv2 .threshold (O00OOOO000O000O00 ,127 ,255 ,cv2 .THRESH_BINARY )#line:261
    return OO0O00OOOO0O00OO0 #line:263
def Ocr (OO000O0O00O00OOO0 ,O00000000OO000O0O ,value =None ):#line:266
    O00OOO00000OOO0O0 =[]#line:267
    OO00OO00OO0OOOO0O =OO000O0O00O00OOO0 .ocr .ocr (O00000000OO000O0O ,cls =True )#line:268
    if OO00OO00OO0OOOO0O :#line:269
        for OOOOOOO0OOO0OO00O in OO00OO00OO0OOOO0O :#line:270
            if value ==OOOOOOO0OOO0OO00O [1 ][0 ]:#line:271
                O00OOO00000OOO0O0 .append ([OOOOOOO0OOO0OO00O [0 ],OOOOOOO0OOO0OO00O [1 ][0 ]])#line:272
            elif not value :#line:273
                O00OOO00000OOO0O0 .append ([OOOOOOO0OOO0OO00O [0 ],OOOOOOO0OOO0OO00O [1 ][0 ]])#line:274
    return O00OOO00000OOO0O0 #line:275
def findhwnd (les ='LDPlayerMainFrame'):#line:278
    OO0OOO00000O0OO00 =[]#line:279
    OO0OOO00000O0OO00 =get_all_windows ()#line:280
    O0O0O0O0OOO000OOO =[]#line:281
    for OOO00O0O0O0000000 in OO0OOO00000O0OO00 :#line:283
        OO0OOO00O0OO0OOO0 =get_title (OOO00O0O0O0000000 ,les )#line:284
        if OO0OOO00O0OO0OOO0 !=None :#line:285
            O0O0O0O0OOO000OOO .append (OO0OOO00O0OO0OOO0 )#line:286
    return O0O0O0O0OOO000OOO #line:288
def get_all_windows ():#line:291
    O00O0OO0O0OO0O00O =[]#line:292
    win32gui .EnumWindows (lambda O00O00O000O000OOO ,O0OOOO00OO0OO00O0 :O0OOOO00OO0OO00O0 .append (O00O00O000O000OOO ),O00O0OO0O0OO0O00O )#line:293
    return O00O0OO0O0OO0O00O #line:295

def get_title (OOO000000OOOOO0OO ,OOO0OO0OOOOO00000 ):#line:298
    OO0O0OO00OOO0O0OO =win32gui .GetClassName (OOO000000OOOOO0OO )#line:299
    if OO0O0OO00OOO0O0OO ==OOO0OO0OOOOO00000 :#line:300
        return OOO000000OOOOO0OO #line:301
class c_keybord (object ):#line:304
    def __init__ (O00O0OOO0OO0O0OOO ,O0OOOO0O0OO0OOO0O :HWND ):#line:305
        ""#line:310
        O00O0OOO0OO0O0OOO .handle =O0OOOO0O0OO0OOO0O #line:311
        O00O0OOO0OO0O0OOO .PostMessageW =windll .user32 .PostMessageW #line:312
        O00O0OOO0OO0O0OOO .MapVirtualKeyW =windll .user32 .MapVirtualKeyW #line:313
        O00O0OOO0OO0O0OOO .VkKeyScanA =windll .user32 .VkKeyScanA #line:314
        O00O0OOO0OO0O0OOO .WM_KEYDOWN =0x100 #line:315
        O00O0OOO0OO0O0OOO .WM_KEYUP =0x101 #line:316
        O00O0OOO0OO0O0OOO .VkCode ={"back":0x08 ,"tab":0x09 ,"return":0x0D ,"shift":0x10 ,"control":0x11 ,"menu":0x12 ,"pause":0x13 ,"capital":0x14 ,"escape":0x1B ,"space":0x20 ,"end":0x23 ,"home":0x24 ,"left":0x25 ,"up":0x26 ,"right":0x27 ,"down":0x28 ,"print":0x2A ,"snapshot":0x2C ,"insert":0x2D ,"delete":0x2E ,"lwin":0x5B ,"rwin":0x5C ,"numpad0":0x60 ,"numpad1":0x61 ,"numpad2":0x62 ,"numpad3":0x63 ,"numpad4":0x64 ,"numpad5":0x65 ,"numpad6":0x66 ,"numpad7":0x67 ,"numpad8":0x68 ,"numpad9":0x69 ,"multiply":0x6A ,"add":0x6B ,"separator":0x6C ,"subtract":0x6D ,"decimal":0x6E ,"divide":0x6F ,"f1":0x70 ,"f2":0x71 ,"f3":0x72 ,"f4":0x73 ,"f5":0x74 ,"f6":0x75 ,"f7":0x76 ,"f8":0x77 ,"f9":0x78 ,"f10":0x79 ,"f11":0x7A ,"f12":0x7B ,"numlock":0x90 ,"scroll":0x91 ,"lshift":0xA0 ,"rshift":0xA1 ,"lcontrol":0xA2 ,"rcontrol":0xA3 ,"lmenu":0xA4 ,"rmenu":0XA5 }#line:377
    def get_virtual_keycode (OO00OO0OOOO00O0OO ,O0000OO00OO00OOOO :str ):#line:379
        ""#line:386
        if len (O0000OO00OO00OOOO )==1 and O0000OO00OO00OOOO in string .printable :#line:387
            return OO00OO0OOOO00O0OO .VkKeyScanA (ord (O0000OO00OO00OOOO ))&0xff #line:388
        else :#line:389
            return OO00OO0OOOO00O0OO .VkCode [O0000OO00OO00OOOO ]#line:390
    def key_down (OO0O0O0OO0OOO000O ,OO0OOO0O000000O0O ,O0OOOOO0000OOOO00 ):#line:392
        ""#line:398
        O0O0OO0OOOOOOO0O0 =OO0OOO0O000000O0O #line:400
        O000OO00O00O00OOO =(O0OOOOO0000OOOO00 <<16 )|1 #line:401
        OO0O0O0OO0OOO000O .PostMessageW (OO0O0O0OO0OOO000O .handle ,OO0O0O0OO0OOO000O .WM_KEYDOWN ,O0O0OO0OOOOOOO0O0 ,O000OO00O00O00OOO )#line:402
    def key_up (OOOOOOOOO0000O000 ,O00O0OO0O00000000 ,O0O00OO0OOO0000OO ):#line:404
        ""#line:410
        OOO0000O0O0OO00OO =O00O0OO0O00000000 #line:411
        O0OO00000O00OOO00 =(O0O00OO0OOO0000OO <<16 )|0XC0000001 #line:412
        OOOOOOOOO0000O000 .PostMessageW (OOOOOOOOO0000O000 .handle ,OOOOOOOOO0000O000 .WM_KEYUP ,OOO0000O0O0OO00OO ,O0OO00000O00OOO00 )#line:413
    def key_click (O00O0OOO00OOO000O ,O0OOO0OO000OOOOO0 :str ,wait =0.2 ):#line:415
        O0OO0O0OO0O0O0000 =O00O0OOO00OOO000O .get_virtual_keycode (O0OOO0OO000OOOOO0 )#line:417
        OO00OOOOO0O00OOO0 =O00O0OOO00OOO000O .MapVirtualKeyW (O0OO0O0OO0O0O0000 ,0 )#line:418
        O00O0OOO00OOO000O .key_down (O0OO0O0OO0O0O0000 ,OO00OOOOO0O00OOO0 )#line:419
        time .sleep (wait )#line:420
        O00O0OOO00OOO000O .key_up (O0OO0O0OO0O0O0000 ,OO00OOOOO0O00OOO0 )#line:421
def getPointOnLine (O0OOO0OO0OOOO0000 ,O00OOOO0OO00OO0O0 ,O0O0O0O0000O0OOO0 ,OO0O00O00000OO000 ,O000OOOOO0O0O000O ):#line:424
    ""#line:427
    OOO0OOOO0O000000O =((O0O0O0O0000O0OOO0 -O0OOO0OO0OOOO0000 )*O000OOOOO0O0O000O )+O0OOO0OO0OOOO0000 #line:428
    OOO0O000OO0O0O0O0 =((OO0O00O00000OO000 -O00OOOO0OO00OO0O0 )*O000OOOOO0O0O000O )+O00OOOO0OO00OO0O0 #line:429
    return int (round (OOO0OOOO0O000000O )),int (round (OOO0O000OO0O0O0O0 ))#line:430
class WinMouse (object ):#line:433
    def __init__ (OOO000O00O0O0OOOO ,OO00OO00O0OO00O00 :int ,num_steps =80 ):#line:434
        OOO000O00O0O0OOOO .handle =OO00OO00O0OO00O00 #line:435
        OOO000O00O0O0OOOO .__OOO000O000000OOOO =win32api #line:436
        OOO000O00O0O0OOOO .__O0O0OO000O0OOO0O0 =win32con #line:437
        OOO000O00O0O0OOOO .num_steps =num_steps #line:438
        OOO000O00O0O0OOOO .__O0OOOO0O00OO000O0 =win32api .GetSystemMetrics (win32con .SM_CXSCREEN )#line:439
        OOO000O00O0O0OOOO .__O0O00O0OO0O0OOOO0 =win32api .GetSystemMetrics (win32con .SM_CYSCREEN )#line:440
    def __OO0OO0OOO00OOO0O0 (O0O00000OO0O0OOO0 ,O000O0O0OO00O0OOO ):#line:442
        O0O00000OO0O0OOO0 .__OOO000O000000OOOO .PostMessage (O0O00000OO0O0OOO0 .handle ,O0O00000OO0O0OOO0 .__O0O0OO000O0OOO0O0 .WM_LBUTTONDOWN ,O0O00000OO0O0OOO0 .__O0O0OO000O0OOO0O0 .MK_LBUTTON ,O000O0O0OO00O0OOO )#line:443
    def __OO000OOOOOO0O00OO (O00000OOO00OO0000 ,O000O00OOO000OO00 ):#line:445
        O00000OOO00OO0000 .__OOO000O000000OOOO .PostMessage (O00000OOO00OO0000 .handle ,O00000OOO00OO0000 .__O0O0OO000O0OOO0O0 .WM_LBUTTONUP ,None ,O000O00OOO000OO00 )#line:446
    def __OO0O0O000O00OO00O (O000O000O0O0OOOO0 ,OO0O00O0OO00000O0 ):#line:448
        O000O000O0O0OOOO0 .__OOO000O000000OOOO .PostMessage (O000O000O0O0OOOO0 .handle ,O000O000O0O0OOOO0 .__O0O0OO000O0OOO0O0 .WM_MOUSEMOVE ,O000O000O0O0OOOO0 .__O0O0OO000O0OOO0O0 .MK_LBUTTON ,OO0O00O0OO00000O0 )#line:449
    def __O000O00OO00O0O000 (O0OO00000O0OO00OO ,OOOO0O0OO0OO0O00O ):#line:451
        O0OO00000O0OO00OO .__OOO000O000000OOOO .PostMessage (O0OO00000O0OO00OO .handle ,O0OO00000O0OO00OO .__O0O0OO000O0OOO0O0 .WM_RBUTTONDOWN ,O0OO00000O0OO00OO .__O0O0OO000O0OOO0O0 .MK_RBUTTON ,OOOO0O0OO0OO0O00O )#line:452
    def __OO000O0O0O0OO0000 (OOOO0OOOO0000O000 ,O000O0O00O00OOO0O ):#line:454
        OOOO0OOOO0000O000 .__OOO000O000000OOOO .PostMessage (OOOO0OOOO0000O000 .handle ,OOOO0OOOO0000O000 .__O0O0OO000O0OOO0O0 .WM_RBUTTONUP ,None ,O000O0O00O00OOO0O )#line:455
    def __OO00O0O0O000O0000 (OO000O0OOOOO0OO00 ,OO0O00O0000000OOO ):#line:457
        OO000O0OOOOO0OO00 .__OOO000O000000OOOO .PostMessage (OO000O0OOOOO0OO00 .handle ,OO000O0OOOOO0OO00 .__O0O0OO000O0OOO0O0 .WM_MOUSEMOVE ,OO000O0OOOOO0OO00 .__O0O0OO000O0OOO0O0 .MK_RBUTTON ,OO0O00O0000000OOO )#line:458
    def left_click (OOOOOOO000O0000OO ,O0OO00OO00000OOOO :int ,O0OOO0O0OO0OOOOO0 :int ,wait =0.2 ):#line:460
        OO00O0OOOO000OO00 =OOOOOOO000O0000OO .__OOO000O000000OOOO .MAKELONG (O0OO00OO00000OOOO ,O0OOO0O0OO0OOOOO0 )#line:461
        OOOOOOO000O0000OO .__OO0OO0OOO00OOO0O0 (param =OO00O0OOOO000OO00 )#line:462
        time .sleep (wait )#line:463
        OOOOOOO000O0000OO .__OO000OOOOOO0O00OO (param =OO00O0OOOO000OO00 )#line:464
    def left_doubleClick (OO000O0OOOOOO0000 ,OOOOOO000OO000O00 :int ,OO00O00OOOO0OOO0O :int ,click =2 ,wait =0.4 ):#line:466
        wait =wait /click #line:467
        OO0OO0OOO000OO00O =OO000O0OOOOOO0000 .__OOO000O000000OOOO .MAKELONG (OOOOOO000OO000O00 ,OO00O00OOOO0OOO0O )#line:468
        for O000OOOOOOO0000OO in range (click ):#line:469
            OO000O0OOOOOO0000 .__OO0OO0OOO00OOO0O0 (param =OO0OO0OOO000OO00O )#line:470
            time .sleep (wait )#line:471
            OO000O0OOOOOO0000 .__OO000OOOOOO0O00OO (param =OO0OO0OOO000OO00O )#line:472
    def left_click_move (OOOOO00O000O000OO ,OOOOO00O0OO00OO0O :int ,OO00O0000OO00000O :int ,OOOO00OO0O0O0OOO0 :int ,O0OOOO000OOO0OOOO :int ,wait =2 ):#line:474
        O0O000OOO0000O000 =OOOOO00O000O000OO .__OOO000O000000OOOO .MAKELONG (OOOOO00O0OO00OO0O ,OO00O0000OO00000O )#line:475
        OOOOO00O000O000OO .__OO0OO0OOO00OOO0O0 (O0O000OOO0000O000 )#line:476
        O0OOOO00OO000O0OO =[getPointOnLine (OOOOO00O0OO00OO0O ,OO00O0000OO00000O ,OOOO00OO0O0O0OOO0 ,O0OOOO000OOO0OOOO ,OO00OO0O0OO000O00 /OOOOO00O000O000OO .num_steps )for OO00OO0O0OO000O00 in range (OOOOO00O000O000OO .num_steps )]#line:477
        O0OOOO00OO000O0OO .append ((OOOO00OO0O0O0OOO0 ,O0OOOO000OOO0OOOO ))#line:478
        O000O00OO0O0OO0OO =wait /OOOOO00O000O000OO .num_steps #line:479
        O00OOO00O00OOOOOO =list (set (O0OOOO00OO000O0OO ))#line:480
        O00OOO00O00OOOOOO .sort (key =O0OOOO00OO000O0OO .index )#line:481
        for O0000O0000O00O0O0 in O00OOO00O00OOOOOO :#line:482
            O0O00O00O0OO000O0 ,O0O000O00OO0000OO =O0000O0000O00O0O0 #line:483
            O0O000OOO0000O000 =OOOOO00O000O000OO .__OOO000O000000OOOO .MAKELONG (O0O00O00O0OO000O0 ,O0O000O00OO0000OO )#line:484
            OOOOO00O000O000OO .__OO0O0O000O00OO00O (O0O000OOO0000O000 )#line:485
            time .sleep (O000O00OO0O0OO0OO )#line:486
        OOOOO00O000O000OO .__OO000OOOOOO0O00OO (O0O000OOO0000O000 )#line:491
    def right_click (OO00O000OO0000O0O ,O0OO00O0O0OO00O0O :int ,OOO0000OOO0OOOO00 :int ,wait =0.2 ):#line:493
        OO0OO0000O00000O0 =OO00O000OO0000O0O .__OOO000O000000OOOO .MAKELONG (O0OO00O0O0OO00O0O ,OOO0000OOO0OOOO00 )#line:494
        OO00O000OO0000O0O .__O000O00OO00O0O000 (param =OO0OO0000O00000O0 )#line:495
        time .sleep (wait )#line:496
        OO00O000OO0000O0O .__OO000O0O0O0OO0000 (param =OO0OO0000O00000O0 )#line:497
    def right_doubleClick (O00OOO0OO0O0O00OO ,O0OO0OO0O000O0000 :int ,O000000OO0OOO000O :int ,click =2 ,wait =0.4 ):#line:499
        wait =wait /click #line:500
        O00000O000000000O =O00OOO0OO0O0O00OO .__OOO000O000000OOOO .MAKELONG (O0OO0OO0O000O0000 ,O000000OO0OOO000O )#line:501
        for OO0O0000OO0O0O0OO in range (click ):#line:502
            O00OOO0OO0O0O00OO .__O000O00OO00O0O000 (param =O00000O000000000O )#line:503
            time .sleep (wait )#line:504
            O00OOO0OO0O0O00OO .__OO000O0O0O0OO0000 (param =O00000O000000000O )#line:505
    def right_click_move (O00000O00O000O000 ,OOO00OO00O0000000 :int ,OOOOOOOO0OO0OO00O :int ,OOOO0000OO00O00O0 :int ,O00O0OO00OOO0O000 :int ,wait =2 ):#line:507
        OOO00OOO0OO0O0000 =O00000O00O000O000 .__OOO000O000000OOOO .MAKELONG (OOO00OO00O0000000 ,OOOOOOOO0OO0OO00O )#line:508
        O00000O00O000O000 .__O000O00OO00O0O000 (OOO00OOO0OO0O0000 )#line:509
        OOOOOOOOOO000O0OO =[getPointOnLine (OOO00OO00O0000000 ,OOOOOOOO0OO0OO00O ,OOOO0000OO00O00O0 ,O00O0OO00OOO0O000 ,OOO00O0OOO00OOOOO /O00000O00O000O000 .num_steps )for OOO00O0OOO00OOOOO in range (O00000O00O000O000 .num_steps )]#line:510
        OOOOOOOOOO000O0OO .append ((OOOO0000OO00O00O0 ,O00O0OO00OOO0O000 ))#line:511
        O00OO000O00OO0000 =wait /O00000O00O000O000 .num_steps #line:512
        O0000OOOOO0OO0OOO =list (set (OOOOOOOOOO000O0OO ))#line:513
        O0000OOOOO0OO0OOO .sort (key =OOOOOOOOOO000O0OO .index )#line:514
        for OOO0OO00OOOOO0000 in O0000OOOOO0OO0OOO :#line:515
            OOO0OOO0OOO0OOO0O ,O000O0000O00O0000 =OOO0OO00OOOOO0000 #line:516
            OOO00OOO0OO0O0000 =O00000O00O000O000 .__OOO000O000000OOOO .MAKELONG (OOO0OOO0OOO0OOO0O ,O000O0000O00O0000 )#line:517
            O00000O00O000O000 .__OO00O0O0O000O0000 (OOO00OOO0OO0O0000 )#line:518
            time .sleep (O00OO000O00OO0000 )#line:519
        O00000O00O000O000 .__OO000O0O0O0OO0000 (OOO00OOO0OO0O0000 )#line:520