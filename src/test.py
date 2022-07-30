from windows import *
from UWTask import UWTask
from datetime import datetime


yBuffer = 36

hwndObject = None
id = 0
allWindowsWithTitle = getAllWindowsWithTitle("Windows 10 x64 - VMware Workstation")
if (len(allWindowsWithTitle) > id):
    hwndObject = allWindowsWithTitle[id]

print(allWindowsWithTitle) 


# mouse=FrontWindow()
# mouse.mouseClick(1398,162)

task = UWTask(hwndObject["hwnd"], 0)
task.print("提示： 切换中文输入法；虚拟机屏幕focus且鼠标在内；")
# task.selectCityFromMapAndMove("london")
# task.shipBuilding(options=[4,5],city="antwerp", times=1)
time.sleep(3)

#test
# task.market()

task.enableSB("antwerp",options=[4,5])
# task.targetCity="ceuta"
task.playNotification()
task.setCurrentCityFromScreen()

try:
    while(True):
        task.startJourney()
except Exception as e:
    print(e)
    




