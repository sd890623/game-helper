import time
import win32gui
import win32con
import cv2
import os
import win32api


def get_all_windows():
    hWnd_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    return hWnd_list


def getAllWindowsWithTitles(titles, x=1280, y=735):
    hwndList = get_all_windows()
    hwndWithTitle = []
    for index, title in enumerate(titles):
        for hwnd in hwndList:
            text = win32gui.GetWindowText(hwnd)
            className = win32gui.GetClassName(hwnd)
            if text == title:
                win32gui.MoveWindow(hwnd, 50 + index * 300, 50, x, y, True)
                hwndWithTitle.append({"hwnd": hwnd, "title": text, "className": className})
    return hwndWithTitle

def getAllWindowsStartingWithTitles(titles, x=1280, y=735):
    hwndList = get_all_windows()
    hwndWithTitle = []
    index=0
    for title in titles:
        for hwnd in hwndList:
            text = win32gui.GetWindowText(hwnd)
            className = win32gui.GetClassName(hwnd)
            if text.startswith(title):
                win32gui.MoveWindow(hwnd, 50 + index * 400, 50, x, y, True)
                index+=1
                hwndWithTitle.append({"hwnd": hwnd, "title": text, "className": className})
    return hwndWithTitle


def getAllWindowsWithTitle(title):
    hwndList = get_all_windows()
    hwndWithTitle = []
    for hwnd in hwndList:
        text = win32gui.GetWindowText(hwnd)
        className = win32gui.GetClassName(hwnd)
        if text == title:
            hwndWithTitle.append({"hwnd": hwnd, "title": text, "className": className})
    return hwndWithTitle


def getWindowHwndObjectById(id):
    hwnds = get_all_windows()
    for hwnd in hwnds:
        if hwnd == id:
            text = win32gui.GetWindowText(hwnd)
            className = win32gui.GetClassName(hwnd)
            return {"hwnd": hwnd, "title": text, "className": className}
    return None


def getChildHwndByIdAndParentHwnd(childId, parentHwnd):
    hWnd_child_list = []
    win32gui.EnumChildWindows(
        parentHwnd, lambda hWnd, param: param.append(hWnd), hWnd_child_list
    )
    for hwnd in hWnd_child_list:
        if childId == hwnd:
            className = win32gui.GetClassName(hwnd)
            text = win32gui.GetWindowText(hwnd)
            dimen = win32gui
            return {"hwnd": hwnd, "title": text, "className": className}
    return None


def getChildHwndByTitleAndParentHwnd(childTitle, parentHwnd):
    hWnd_child_list = []
    win32gui.EnumChildWindows(
        parentHwnd, lambda hWnd, param: param.append(hWnd), hWnd_child_list
    )
    for hwnd in hWnd_child_list:
        text = win32gui.GetWindowText(hwnd)
        if text == childTitle:
            className = win32gui.GetClassName(hwnd)
            return {"hwnd": hwnd, "title": text, "className": className}
    return None


def getChildHwndByClassAndParentHwnd(childClass, parentHwnd):
    hWnd_child_list = []
    win32gui.EnumChildWindows(
        parentHwnd, lambda hWnd, param: param.append(hWnd), hWnd_child_list
    )
    for hwnd in hWnd_child_list:
        text = win32gui.GetClassName(hwnd)
        if text == childClass:
            className = win32gui.GetClassName(hwnd)
            return {"hwnd": hwnd, "title": text, "className": className}
    return None


def getFakeHwndObjectById(id):
    return {"hwnd": id, "title": "text", "className": "className"}


def randomMethod():
    print(win32gui.GetWindowText(136319154))
    text = win32gui.GetWindowText(136319154)
    allHwnds = get_all_windows()
    for hwnd in allHwnds:
        if win32gui.GetWindowText(hwnd) == text:
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
    print(path + " --> " + filename + "\n")

    print("This file directory only")
    print(os.path.dirname(full_path))

    path = os.path.abspath(__file__ + "\\..\\..\\assets\\clickOns\\greenStars.bmp")
    print(path)
    image = cv2.imread(path)
    print(image.shape)


# def getWholeScreenshot():
#     hdesktop = win32gui.GetDesktopWindow()
#     hwndDC = win32gui.GetWindowDC(hdesktop)
#     mfcDC  = win32gui.CreateDCFromHandle(hwndDC)
#     saveDC = mfcDC.CreateCompatibleDC()

#     saveBitMap = win32gui.CreateBitmap()
#     saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

#     saveDC.SelectObject(saveBitMap)

#     result = saveDC.BitBlt((0, 0), (w, h), mfcDC, (left, top), win32con.SRCCOPY)

#     bmpinfo = saveBitMap.GetInfo()
#     bmpstr = saveBitMap.GetBitmapBits(True)

#     im = Image.frombuffer(
#         'RGB',
#         (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
#         bmpstr, 'raw', 'BGRX', 0, 1)

#     win32gui.DeleteObject(saveBitMap.GetHandle())
#     saveDC.DeleteDC()
#     mfcDC.DeleteDC()
#     win32gui.ReleaseDC(hdesktop, hwndDC)

#     if result == None:
#         #PrintWindow Succeeded
#         im.save("test.png")


class FrontWindow:
    # def __init__(self):

    def mouseMove(self, x, y):
        win32api.SetCursorPos((x, y))

    def mouseClick(self, x, y):
        self.mouseMove(x, y)
        time.sleep(0.03)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.03)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
