import sys 
import win32gui
import win32con

def get_all_windows():
    hWnd_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    return hWnd_list

def getAllWindowsWithTitle():
    hwndList = get_all_windows()
    hwndWithTitle = [];
    for hwnd in hwndList:
        text = win32gui.GetWindowText(hwnd);
        className = win32gui.GetClassName(hwnd);
        if(text == '星战前夜：无烬星河 - MuMu模拟器'):
            hwndWithTitle.append({"hwnd": hwnd, "title": text, "className": className})
    return hwndWithTitle

def getWindowHwndObjectById(id):
    hwnds = getAllWindowsWithTitle()
    for hwnd in hwnds:
        if (hwnd["hwnd"] == id):
            return hwnd
    return None

def randomMethod():
    print(win32gui.GetWindowText(136319154))
    text = win32gui.GetWindowText(136319154)
    allHwnds = get_all_windows()
    for hwnd in allHwnds:
        if (win32gui.GetWindowText(hwnd) == text):
            print({"hwnd": hwnd, "text": text})

randomMethod()




