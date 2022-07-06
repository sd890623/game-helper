from windows import *
from utils import wait
import guiUtils
import time

class Task:
    hwnd = None
    simulatorInstance = None
    def __init__(self, hwnd):
        self.hwnd = hwnd
        hwndObject = getWindowHwndObjectById(hwnd)
        self.simulatorInstance = guiUtils.win(hwndObject["hwnd"])

    def runTask(self):
        wait(lambda: self.simulatorInstance.click_keyboard("B"), 12)
        wait(lambda: self.simulatorInstance.click_point(43,84), 6)
        wait(lambda: self.simulatorInstance.click_point(101,150), 6)
        wait(lambda: self.simulatorInstance.click_point(636,30), 6)
        wait(lambda: self.simulatorInstance.send_str("b"), 6)
        wait(lambda: self.simulatorInstance.send_enter(), 12)
