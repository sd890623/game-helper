import sys
sys.path.append("src")
from windows import *
from UWTask import UWTask

allWindowsWithTitle = getAllWindowsWithTitle("Windows 10 x64 - VMware Workstation")
if (len(allWindowsWithTitle) > 0):
    hwndObject = allWindowsWithTitle[0]

task = UWTask(hwndObject["hwnd"], "eve")
task.print("提示： 切换中文输入法；虚拟机屏幕focus且鼠标在内；")
time.sleep(3)

#test
# task.market()

#Optional
# task.shipBuilding(options=[4,5],city="antwerp", times=1)
# task.targetCity="ceuta"

#Init option
task.enableSB("antwerp",options=[4,5])
task.playNotification()
task.setCurrentCityFromScreen()

try:
    while(True):
        task.startJourney()
except Exception as e:
    print(e)
    




