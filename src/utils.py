import time
import random
from datetime import datetime
import datetime as dt
import threading

def wait(func, seconds = 3,disableWait=False):
    func()
    if(not(disableWait)):
        time.sleep(seconds+random.uniform(0,1))
    else:
        time.sleep(seconds)

def doMoreTimesWithWait(func, times=1, seconds=random.uniform(2,4)):
    while(times>0):
        wait(func, seconds)
        times-=1

def doAndWaitUntilBy(func, untilFunc, seconds = 2, frequency = 4, backupFunc=None):
    wait(func, seconds)
    timeout = 30
    while(not(untilFunc()) and timeout >0):
        time.sleep(frequency)
        timeout-=frequency
    if(timeout<=0):
        print("timed out, do backup function")
        for x in [0,1,2]:
            if(backupFunc):
                wait(backupFunc, seconds)
                wait(func,seconds)
            else:
                wait(func, seconds)
            if(untilFunc()):
                return
    time.sleep(random.randint(0,1))

def continueWithUntilBy(func, untilFunc, frequency = 5):
    wait(func, 0)
    while(not(untilFunc())):
        func()
        time.sleep(frequency)
    time.sleep(random.randint(0,1))

def continueWithUntilByWithBackup(func, untilFunc, frequency = 5, timeout=6000, backupFunc=lambda: False):
    wait(func, 0)
    while(not(untilFunc()) and timeout>0):
        func()
        print("not found, wait for 8s")
        time.sleep(frequency)
        timeout-=frequency
    if(timeout<=0):
        print("timed out, backup")
        wait(backupFunc,10)
        if(untilFunc()):
            return
        wait(backupFunc,10)
        if(untilFunc()):
            return
    time.sleep(random.randint(0,1))

def getDateTimeString():
    now = datetime.now()
    dt_string = now.strftime("%d %H:%M:%S")
    return("Time: "+dt_string)

#specia treatment by 
def hasOneArrayStringInStringAndNotVeryDifferent(string, array):
    found=False
    for stringInArray in array:
        if(stringInArray in string and (len(string)-len(stringInArray))<3):
            found=True
    return found

def isWorkHour():
    hour=dt.datetime.now().hour
    if(hour>=5 and hour<7):
        return False
    return True

findPlayerCountLk=threading.Lock()
