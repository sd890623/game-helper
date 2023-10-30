import time
import random
from datetime import datetime
import datetime as dt
import threading
import collections.abc
from strsimpy.damerau import Damerau

stringDist = Damerau().distance

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

def doAndWaitUntilBy(func, untilFunc, seconds = 2, frequency = 4, backupFunc=None,timeout=30):
    wait(func, seconds)
    while(not(untilFunc()) and timeout >0):
        time.sleep(frequency)
        timeout-=frequency
    if(timeout<=0):
        print("timed out, do backup function")
        for x in [0,1,2,3]:
            if(backupFunc):
                wait(backupFunc, seconds)
            else:
                wait(func, seconds)
            if(untilFunc()):
                return True
        return False
    time.sleep(random.randint(0,1))
    return True

def continueWithUntilBy(func, untilFunc, frequency = 5,timeout=30,firstWait=0):
    wait(func, firstWait)
    while(not(untilFunc()) and timeout>0):
        func()
        time.sleep(frequency)
        timeout-=frequency
    if(timeout<=0):
        print("timed out, do backup function")
        for x in [0,1,2,3]:
            wait(func,frequency)
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

def getTimeDiffInSeconds(earlier,later):
    return (later-earlier).total_seconds()

#specia treatment by 
def hasOneArrayStringInStringAndNotVeryDifferent(string, array):
    if(not(string)):
        return False
    found=False
    for stringInArray in array:
        if(isStringSameOrSimilar(stringInArray,string)):
            found=True
    return found

def stringhasStartsWithOneArrayString(string, array):
    if(not(string)):
        return False
    found=False
    for stringInArray in array:
        if(string.startswith(stringInArray)):
            found=True
    return found

def hasOneArrayStringInString(string, array):
    if(not(string)):
        return False
    for stringInArray in array:
        if(stringInArray in string):
            return True
    return False

def hasOneArrayStringSimilarToString(string, array):
    if(not(string)):
        return False
    for stringInArray in array:
        if(isStringSameOrSimilar(stringInArray,string)):
            return True
    return False

def isWorkHour():
    hour=dt.datetime.now().hour
    if(hour>=5 and hour<7):
        return False
    return True

def getHour():
    return dt.datetime.now().hour

def isArray(items):
    if(items is None):
        return False
    return isinstance(items, collections.abc.Sequence)

def isStringSameOrSimilar(stringA, stringB):        
    if stringA==stringB:
        return True
    elif stringA in stringB: #len(stringA)<7 and 
        return True
    elif stringDist(stringA,stringB)/len(stringA)<0.2:
        return True
    else:
        return False

def randomInt(max_value=5):
    return random.randint(-max_value, max_value)
                          
findPlayerCountLk=threading.Lock()
