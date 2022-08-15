import sys
sys.path.append("src")
from windows import *
from UWTask import UWTask
from UWTask import routeList

allWindowsWithTitle = getAllWindowsWithTitle("Chrome Remote Desktop - MEDIA-PC")
if (len(allWindowsWithTitle) > 0):
    hwndObject = allWindowsWithTitle[0]

task = UWTask(hwndObject["hwnd"], "uw")
time.sleep(3)
# 11, +16
#test
# task.testTask()

# task.buyInCity("copenhagen",routeList[0]["buyProducts"])

#Optional
# task.shipBuilding(options=[4,5],city="ceuta", times=1)
# task.targetCity="ceuta"
# task.fastStock=True disable

#Init option
# task.enableSB("faro",options=[10,10])
task.fastStock=False
task.playNotification()
task.setCurrentCityFromScreen()
task.print("提示：虚拟机屏幕focus且鼠标在内；长距旅行开启蓝旗;船拉平最远距离;设置免税港")

while(True):
    task.startTradeRoute()
    




