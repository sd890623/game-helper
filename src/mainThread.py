from threading import Thread
from windows import *
from Task import Task

def runTask(hwnd, index):
    task = Task(hwnd, index)
    while(True):
        task.startMiningTask()
def main():
    allWindowsWithTitle = getAllWindowsWithTitle("星战前夜：无烬星河 - MuMu模拟器")
    threads = []
    for index,window in enumerate(allWindowsWithTitle):
        threads.append(Thread(target=runTask, name=str(window["hwnd"]), args=(window["hwnd"],index,)))
    for thread in threads:
        thread.start()



if __name__ == '__main__':
    main()