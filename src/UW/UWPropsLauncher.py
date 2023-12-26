import sys
import time
import os

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

from windows import getAllWindowsWithTitle
from UWTask import UWTask
from utils import isWorkHour

def run(props):
    battleOn=props.get("battleOn")
    battleCity=props.get("battleCity")
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

    task.tradeRouteBuyFin=True
    task.print("抗浪;删除到达城市;调最大仓;检查道具少,检查黑市可买")
    task.print("提示：检查物品栏，长距旅行开启蓝旗;检查防灾物品；检查船耐久；设置免税港;设置水手最少数;檢查港口語言;检查市场购买勾")

    if(battleOn):
        task.battleRoute(battleCity)


    # task.enableSB("malacca",options=[5])

    # each time 6s(not counted)+8s(counted) 8d=11min, limit 10d=14min, 14*(8/14)=8min=480ss
    # kochi: 12d=18min, 18*8/14=10min=600
    task.waitForCityTimeOut=650
    task.battleMode="run"
    task.playNotification()
    initialRouteIndex=False
    while(initialRouteIndex is False):
        initialRouteIndex=task.getInitialRouteIndex()
    while(True):
        if(not(isWorkHour())):
            task.print("not working hour,sleep for 30mins")
            time.sleep(1800)
            continue
        task.startMerchantQuest()
        task.startDailyBattle()
        task.startTradeRoute(initialRouteIndex if task.initialRun else 0)
        task.initialRun=False
        # task.startJourney()
        




