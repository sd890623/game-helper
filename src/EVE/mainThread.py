from threading import Thread
import sys
import os

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))
from windows import *
from MiningTask import MiningTask
import datetime as dt

# todo
# restart app when crash?
# ocr key words to replace image match
# Keep time difference by 60s all the time. Done partial
# 1280x720

def isWorkHour():
    hour = dt.datetime.now().hour
    if hour >= 5 and hour <= 9:
        return False
    return True

def runTask(hwnd, index,mode=0):
    #mode 0 standard, mode 1 for weekly high safety mining, mode 2 for gulan target mining
    task = MiningTask(hwnd, index,mode)
    while True:
        try:
            if not (isWorkHour()):
                print("not working hour,sleep for 30mins")
                time.sleep(1800)
                continue
            # task.testTask()
            task.startMiningTask()
        except Exception as e:
            task.closeWindow()
            print("thread failed, stop")
            raise (e)

def getModeFromIndex(name):
    parts = name.split('-')
    winIndex = parts[-1]
    if(winIndex=="1"):
        return -1
    elif(winIndex=="2"):
        return 2
def main():
    print("开工前todo list: 打开本地列表,v船到广角,驻地最后一个,改变战斗列表为名称排序")
    # ,
    allWindowsWithTitle = getAllWindowsWithTitles(["MuMu模拟器-1","MuMu模拟器-2"],1254, 741)
    threads = []
    for index, window in enumerate(allWindowsWithTitle):
        if(getModeFromIndex(window["title"])==-1):
            continue
        threads.append(
            Thread(
                target=runTask,
                name=str(window["hwnd"]),
                args=(
                    window["hwnd"],
                    index,
                    getModeFromIndex(window["title"])
                ),
            )
        )
    for thread in threads:
        thread.start()

if __name__ == "__main__":
    main()
