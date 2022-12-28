import sys
sys.path.append("src")
from windows import *
from UWTask import UWTask
from utils import isWorkHour

allWindowsWithTitle = getAllWindowsWithTitle("MEDIA-PC - Google Chrome")
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
# task.battleRoute()

#Init option
#Route choice: Must-set 0: kokola<->athens perfume route, 1: saint<->east africa nb route, 2: saint<->carribean
#4 saint<->hindu  #5 saint<->hindu double  #6 everyday BM(india) #7 SEA-carrebean #8Carrebean-NU-SEA triangle
task.setRouteOption(8)
#task.enableSB("ceuta",options=[10,11])
# task.enableSB("diu",options=[4,4,4])

# each time 6s(not counted)+8s(counted) 8d=11min, limit 10d=14min, 14*(8/14)=8min=480ss
# kochi: 12d=18min, 18*8/14=10min=600
task.waitForCityTimeOut=700
task.battleMode="run"
task.playNotification()
task.setCurrentCityFromScreen()
task.print("提示：长距旅行开启蓝旗;检查防灾物品；检查船耐久；设置免税港;设置水手最少数;檢查港口語言;检查市场购买勾;抗浪;删除到达城市;调最大仓")

while(True):
    if(not(isWorkHour())):
        task.print("not working hour,sleep for 30mins")
        time.sleep(1800)
        continue
    task.startTradeRoute()
    




