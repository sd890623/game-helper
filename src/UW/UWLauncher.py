import sys
sys.path.append("src")
from windows import *
from UWTask import UWTask
from UWTask import routeList
from utils import isWorkHour

allWindowsWithTitle = getAllWindowsWithTitle("Chrome Remote Desktop - MEDIA-PC")
if (len(allWindowsWithTitle) > 0):
    hwndObject = allWindowsWithTitle[0]

task = UWTask(hwndObject["hwnd"], "uw")
time.sleep(3)
# 11, +16
#test
# task.basicMarket()

# task.selectCityFromMapAndMove("groningen")
# task.testTask()

#todo


#Optional
# task.shipBuilding(options=[7,8],city="ceuta", times=1)
# task.targetCity="ceuta"
# task.fastStock=True disable

#Init option
# task.enableSB("ceuta",options=[7,8])
task.fastStock=False
task.playNotification()
task.setCurrentCityFromScreen()
task.print("提示：长距旅行开启蓝旗;检查防灾物品；设置免税港;设置水手最少数;檢查港口語言;打开auto战斗")

while(True):
    if(not(isWorkHour())):
        task.print("not working hour,sleep for 30mins")
        time.sleep(1800)
        continue
    task.startTradeRoute()
    




