import time
import random
from datetime import datetime
import datetime as dt
import threading
import collections.abc


def wait(func, seconds = 3,disableWait=False):
    func()
    if(not(disableWait)):
        time.sleep(seconds+random.uniform(0,1))
    else:
        time.sleep(seconds)

def doMoreTimesWithWait(func, times=1, seconds=random.uniform(2,4),disableWait=False):
    while(times>0):
        wait(func, seconds, disableWait)
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

def continueWithUntilBy(func, untilFunc, frequency = 5,timeout=30):
    wait(func, 0)
    while(not(untilFunc()) and timeout>0):
        func()
        time.sleep(frequency)
        timeout-=frequency
    if(timeout<=0):
        print("timed out, do backup function")
        for x in [0,1,2]:
            wait(func)
            if(untilFunc()):
                return
    time.sleep(random.randint(0,1))

def continueWithUntilByWithBackup(func, untilFunc, frequency = 5, timeout=6000, notifyFunc=lambda: False, backupFunc=lambda: False):
    wait(func, 0)
    while(not(untilFunc()) and timeout>0):
        func()
        if(notifyFunc()):
            notifyFunc()
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
    if(not(string)):
        return False
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

def isArray(items):
    if(items==None):
        return False
    return isinstance(items, collections.abc.Sequence)

findPlayerCountLk=threading.Lock()
