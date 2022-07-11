import sys 
import win32gui
import win32con
import cv2
import os 


def get_all_windows():
    hWnd_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    return hWnd_list

def getAllWindowsWithTitle(title):
    hwndList = get_all_windows()
    hwndWithTitle = []
    for hwnd in hwndList:
        text = win32gui.GetWindowText(hwnd)
        className = win32gui.GetClassName(hwnd)
        if(text == title):
            hwndWithTitle.append({"hwnd": hwnd, "title": text, "className": className})
    return hwndWithTitle

def getWindowHwndObjectById(id):
    hwnds = get_all_windows()
    for hwnd in hwnds:
        if (hwnd == id):
            text = win32gui.GetWindowText(hwnd)
            className = win32gui.GetClassName(hwnd)
            return {"hwnd": hwnd, "title": text, "className": className}
    return None

def randomMethod():
    print(win32gui.GetWindowText(136319154))
    text = win32gui.GetWindowText(136319154)
    allHwnds = get_all_windows()
    for hwnd in allHwnds:
        if (win32gui.GetWindowText(hwnd) == text):
            print({"hwnd": hwnd, "text": text})

def getImages():
    print("Path at terminal when executing this file")
    print(os.getcwd() + "\n")

    print("This file path, relative to os.getcwd()")
    print(__file__ + "\n")

    print("This file full path (following symlinks)")
    full_path = os.path.realpath(__file__)
    print(full_path + "\n")

    print("This file directory and name")
    path, filename = os.path.split(full_path)
    print(path + ' --> ' + filename + "\n")

    print("This file directory only")
    print(os.path.dirname(full_path))


    path = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\greenStars.bmp")
    print(path)
    image =cv2.imread(path)
    print(image.shape)







