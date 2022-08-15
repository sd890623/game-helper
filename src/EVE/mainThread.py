from threading import Thread
import sys
sys.path.append("src")
from windows import *
from EVETask import EVETask
import datetime as dt

# todo 
# restart app when crash?
# ocr key words to replace image match
# Keep time difference by 60s all the time. Done partial

def isWorkHour():
    hour=dt.datetime.now().hour
    if(hour>=5 and hour<=8):
        return False
    return True

def runTask(hwnd, index):
    task = EVETask(hwnd, index)
    while(True):
        try:
            if(not(isWorkHour())):
                print("not working hour,sleep for 30mins")
                time.sleep(1800)
                continue
            task.startMiningTask()
        except Exception as e:
            task.closeWindow()
            print("thread failed, stop")
            raise(e)

def main():
    print("开工前todo list: 打开本地列表,v船到广角,检查快捷列表有无长字符,改变战斗列表为名称排序")
    allWindowsWithTitle = getAllWindowsWithTitle("星战前夜：无烬星河 - MuMu模拟器")
    threads = []
    for index,window in enumerate(allWindowsWithTitle):
        threads.append(Thread(target=runTask, name=str(window["hwnd"]), args=(window["hwnd"],index,)))
    for thread in threads:
        thread.start()


if __name__ == '__main__':
    main()