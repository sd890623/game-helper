import time
import random
from datetime import datetime
import threading

def wait(func, seconds = 3):
    func()
    time.sleep(seconds+random.uniform(0,1))

def doMoreTimesWithWait(func, times=1, seconds=random.uniform(2,4)):
    while(times>0):
        func()
        time.sleep(seconds+random.uniform(0,1))
        times-=1

def doAndWaitUntilBy(func, untilFunc, seconds = 2, frequency = 4):
    wait(func, seconds)
    timeout = 60
    while(not(untilFunc()) and timeout >0):
        time.sleep(frequency)
        timeout-=frequency
    if(timeout<=0):
        wait(lambda: func())
        if(untilFunc()):
            return
        wait(lambda: func())
        if(untilFunc()):
            return
        
def continueWithUntilBy(func, untilFunc, frequency = 5):
    while(not(untilFunc())):
        func()
        time.sleep(frequency)
    time.sleep(frequency)

def continueWithUntilByWithBackup(func, untilFunc, frequency = 5, timeout=6000, backupFunc=lambda: False):
    while(not(untilFunc()) and timeout>0):
        print("not found title")
        print("before in journey click")
        func()
        print("after in journey click")
        print("wait 6s")
        time.sleep(frequency)
        print("waited for 6s")
        timeout-=frequency
    if(timeout<=0):
        print("timed out, backup")
        wait(backupFunc,10)
        if(untilFunc()):
            return
        wait(backupFunc,10)
        if(untilFunc()):
            return
    time.sleep(2+random.uniform(0,1))

def getDateTimeString():
    now = datetime.now()
    dt_string = now.strftime("%d %H:%M:%S")
    return("Time: "+dt_string)

findPlayerCountLk=threading.Lock()
