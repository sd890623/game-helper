import sys
import time
import os

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

from windows import getAllWindowsWithTitle
from UWTask import UWTask
from utils import isWorkHour,getCentralTime

def run(props):
    battleOn=props.get("battleOn")
    battleCity=props.get("battleCity")
    goBM=props.get("goBM")
    focusedBarterTrade=props.get("focusedBarterTrade")
    testMode=props.get("testMode")
    allWindowsWithTitle = getAllWindowsWithTitle("神盾虚拟机 NP版 - VMware Workstation")
    if (len(allWindowsWithTitle) > 0):
        hwndObject = allWindowsWithTitle[0]

    task = UWTask(hwndObject["hwnd"], "uw")
    task.initMarket()

    time.sleep(3)

    #todo

    #Optional
    # task.shipBuilding(options=[12,12],city="ceuta", times=1)
    # task.targetCity="naples"

    task.print("每日检查： 仓清空，市场购买勾，时间可用，检查道具多于3格")
    task.print("特别检查：检查航海道具；检查船耐久;检查忠诚；检查屏幕设置；检查探险工具超1000;钓鱼，探险工具使用中,adv/battle fast,set Sami village")
    task.battleCity=battleCity

    if(battleOn):
        task.setRouteOption()
        task.battleRoute(battleCity,battleOnMode=True)

    # task.enableSB("malacca",options=[5])

    # each time 6s(not counted)+8s(counted) 8d=11min, limit 10d=14min, 14*(8/14)=8min=480ss
    # kochi: 12d=18min, 18*8/14=10min=600
    task.waitForCityTimeOut=650
    task.battleMode="run"
    task.goBM=goBM
    task.focusedBarterTrade= focusedBarterTrade
    task.setRouteOption()
    # task.playNotification()

    #test
    if(testMode):
        task.testTask()

    initialRouteIndex=False
    while(initialRouteIndex is False):
        initialRouteIndex=task.getInitialRouteIndex()
    while(True):
        if(not(isWorkHour())):
            task.print("not working hour,sleep for 30mins")
            time.sleep(1800)
            continue
        if(focusedBarterTrade):
            while(task.lastExecuted is not None and (getCentralTime().day == task.lastExecuted.day)):
                time.sleep(60)
                task.print("sleep for 2nd day")
            task.specialConfUpdate()
            task.setRouteOption()
            initialRouteIndex=task.getInitialRouteIndex()
            task.startFocusedBartingTrade(initialRouteIndex if task.initialRun else 0)
            task.initialRun=False
        else:
            task.startTradeRoute(initialRouteIndex if task.initialRun else 0)
            task.initialRun=False
            task.startMerchantQuest()
            task.startDailyBattle(battleCity)
        # task.startJourney()
        




