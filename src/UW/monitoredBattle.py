import sys
import os
sys.path.append("src")
# sys.path.append(os.getcwd() + '/..')

# from src.windows import getAllWindowsWithTitle
from windows import getAllWindowsWithTitle
from UWTask import UWTask
import psutil
import multiprocessing

allWindowsWithTitle = getAllWindowsWithTitle("神盾虚拟机 NP版 - VMware Workstation")
if (len(allWindowsWithTitle) > 0):
    hwndObject = allWindowsWithTitle[0]

def runAmbushMonitor(monitorProcess: psutil.Process):
    task = UWTask(hwndObject["hwnd"], "uw", monitorProcess)

def runBattle():
    task = UWTask(hwndObject["hwnd"], "uw")
    task.battleRoute()

if __name__ == '__main__':
    battleProcess=multiprocessing.Process(target=runBattle)
    battleProcess.start()
    proc = psutil.Process(battleProcess.pid)
    
    # proc.wait()
    ambushMonitorProcess=multiprocessing.Process(target=runAmbushMonitor,args=(proc,))
    ambushMonitorProcess.start()
    ambushMonitorProcess.wait()

