import time
import random
from datetime import datetime
import threading

def wait(func, seconds = 5):
    func()
    time.sleep(seconds+random.randint(0,3))

def doMoreTimesWithWait(func, times=1, seconds=3):
    while(times>0):
        func()
        time.sleep(seconds)
        times-=1
    time.sleep(random.randint(0,3))

def doAndWaitUntilBy(func, untilFunc, seconds = 2, frequency = 5):
    wait(func, seconds)
    timeout = 60
    while(not(untilFunc()) and timeout >0):
        time.sleep(frequency)
        timeout-=frequency
    if(timeout<=0):
        func()
    time.sleep(frequency)
        
def continueWithUntilBy(func, untilFunc, frequency = 5):
    while(not(untilFunc())):
        func()
        time.sleep(frequency)
    time.sleep(frequency)

def getDateTimeString():
    now = datetime.now()
    dt_string = now.strftime("%d %H:%M:%S")
    return("Time: "+dt_string)

findPlayerCountLk=threading.Lock()
