from threading import Thread
from windows import *
from Task import Task
import time

def runTask(hwnd, index):
    task = Task(hwnd, index)
    time.sleep(index*40)
    while(True):
        try:
            #task.runTask()
            task.startMiningTask()
        except:
            print("thread failed, wait 60s")
            time.sleep(60)
        


def main():
    print("开工前todo list: 打开本地列表，v船到广角，检查快捷列表有无长字符")
    allWindowsWithTitle = getAllWindowsWithTitle("星战前夜：无烬星河 - MuMu模拟器")
    threads = []
    for index,window in enumerate(allWindowsWithTitle):
        threads.append(Thread(target=runTask, name=str(window["hwnd"]), args=(window["hwnd"],index,)))
    for thread in threads:
        thread.start()



if __name__ == '__main__':
    main()