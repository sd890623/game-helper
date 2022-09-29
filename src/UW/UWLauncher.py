import sys
sys.path.append("src")
from windows import *
from UWTask import UWTask
from utils import isWorkHour

allWindowsWithTitle = getAllWindowsWithTitle("Chrome Remote Desktop - MEDIA-PC")
if (len(allWindowsWithTitle) > 0):
    hwndObject = allWindowsWithTitle[0]

task = UWTask(hwndObject["hwnd"], "uw")
time.sleep(3)

#test
#task.testTask()

#todo


#Optional
# task.shipBuilding(options=[12,12],city="ceuta", times=1)
# task.targetCity="ceuta"

#Init option
#Route choice: Must-set 0: kokola<->athens perfume route, 1: saint<->east africa nb route, 2: saint<->carribean
#4 saint<->hindu
task.setRouteOption(2)
task.enableSB("ceuta",options=[12,12])
# task.enableSB("diu",options=[12,12])

# each time 6s(not counted)+8s(counted) 8d=11min, limit 10d=14min, 14*(8/14)=8min=480ss
# kochi: 12d=16min, 16*8/14=9min=540
task.waitForCityTimeOut=540
task.battleMode="run"
task.playNotification()
task.setCurrentCityFromScreen()
task.print("提示：长距旅行开启蓝旗;检查防灾物品；设置免税港;设置水手最少数;檢查港口語言;打开auto战斗")

while(True):
    if(not(isWorkHour())):
        task.print("not working hour,sleep for 30mins")
        time.sleep(1800)
        continue
    task.startTradeRoute()
    




