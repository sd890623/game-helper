import sys
sys.path.append("src")
from windows import getAllWindowsWithTitle
from UWTask import UWTask
from utils import isWorkHour
import time

allWindowsWithTitle = getAllWindowsWithTitle("神盾虚拟机 NP版 - VMware Workstation")
if (len(allWindowsWithTitle) > 0):
    hwndObject = allWindowsWithTitle[0]

task = UWTask(hwndObject["hwnd"], "uw")
time.sleep(3)

#test
# task.testTask()

#todo

#Optional
# task.shipBuilding(options=[12,12],city="ceuta", times=1)
# task.targetCity="naples"
task.setRouteOption(6)

task.tradeRouteBuyFin=True
# task.battleRoute()

#Init option
#Route choice: Must-set 0: mar-May-spring(SEA-Carrebean),1: Jun-Aug-Summer(Carrebean-EA),2: Sep-Oct Aut, Carrebean-EA,3: Winter Nov-Feb, Carrebean-EA
#4 summer, 5autumn, 6winter 7 spring
# task.enableSB("malacca",options=[5])

# each time 6s(not counted)+8s(counted) 8d=11min, limit 10d=14min, 14*(8/14)=8min=480ss
# kochi: 12d=18min, 18*8/14=10min=600
task.waitForCityTimeOut=650
task.battleMode="run"
task.playNotification()
task.setCurrentCityFromScreen()
task.print("提示：长距旅行开启蓝旗;检查防灾物品；检查船耐久；设置免税港;设置水手最少数;檢查港口語言;检查市场购买勾")
task.print("抗浪;删除到达城市;调最大仓;检查道具少,检查黑市可买")
while(True):
    if(not(isWorkHour())):
        task.print("not working hour,sleep for 30mins")
        time.sleep(1800)
        continue
    task.startTradeRoute()
    




