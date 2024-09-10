import time
import random
from datetime import datetime
import datetime as dt
import threading
import collections.abc
# from UWTask import UWTask
# from Battle import Battle
from datetime import datetime, timedelta
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

class Utils:
    # def __init__(self, uwtask: UWTask, battle: Battle) -> None:
    def __init__(self, uwtask, battle) -> None:
        self.uwtask=uwtask
        self.battle=battle
    def useSpecial(self, specialMode):
        if(specialMode=="battle"):
            self.uwtask.print("special check from being assult")
            if(self.uwtask.hasSingleLineWordsInArea("retreat",A=[1053,771,1120,792])):
                doMoreTimesWithWait(lambda: self.uwtask.simulatorInstance.clickPointV2(1101,696),2,3)
                time.sleep(30)
            # if(self.uwtask.hasSingleLineWordsInArea("retreat",A=[1053,771,1120,792])):
            #     time.sleep(30)
            if(self.uwtask.hasSingleLineWordsInArea("auto",A=[789,856,844,877])):
                self.battle.useFast()
                self.battle.clickAuto()
                time.sleep(250)
                doAndWaitUntilBy(lambda: self.battle.exitBattle(),lambda: self.uwtask.inWater(),timeout=30)
                return True
            if(self.battle.hasResultsBtn()):
                doAndWaitUntilBy(lambda: self.battle.exitBattle(),lambda: self.uwtask.inWater(),timeout=30)
                return True
        return False
    def doAndWaitUntilBy(self,func, untilFunc, seconds = 1, frequency = 4, backupFunc=None,timeout=10,specialMode=None):
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
                if(specialMode):
                    self.useSpecial(specialMode)
            return False
        time.sleep(seconds+ random.randint(0,1))
        return True
    
def doAndWaitUntilBy(func, untilFunc, seconds = 2, frequency = 4, backupFunc=None,timeout=10):
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
    time.sleep(random.randint(1,2))
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
                return True
        return False
    time.sleep(random.randint(0,1))
    return True

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
    if(hour==5):
        return False
    return True

def getHour():
    return dt.datetime.now().hour

def isArray(items):
    if(items is None):
        return False
    return isinstance(items, collections.abc.Sequence)

# stringA in StringB
def isStringSameOrSimilar(stringA, stringB):        
    """
    参数:
    stringA (int): 第一个参数的描述。
    stringB (str): 第二个参数的描述。
    
    StringA in StringB

    返回:
    bool: 
    """
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

def addNonExistElementToArray(array,element):
    name=None
    # check if element is an object
    if(isinstance(element, collections.abc.Mapping)):
        name=element.get("target")
    else:
        name=element
    if(name not in array):
        array.append(name)
        return array
    return False

def addNonExistArrayToArray(array,arrayToAdd):
    for element in arrayToAdd:
        name=None
        # check if element is an object
        if(isinstance(element, collections.abc.Mapping)):
            name=element.get("target")
        else:
            name=element
        if(name not in array):
            array.append(name)
    return array

def removeArrayElementFromArray(array,arrayToRemove):
    arrayCopy=list(array)
    for element in arrayToRemove:
        if(element in array):
            arrayCopy.remove(element)
    return arrayCopy

def waitUntilClockByHour(hour,extraMinute=0):
    print(f"wait until next {hour} hour sharp")
    now = datetime.now()
    next_hour = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=hour)
    # 计算等待时间（秒）
    wait_time = (next_hour - now).total_seconds()
    # 等待
    time.sleep(wait_time+60*extraMinute+5)

def isArrayAnyInArray(array,arrayToCheck):
    for element in arrayToCheck:
        if(element in array):
            return True
    return False

def isDst():
        return bool(time.localtime().tm_isdst)
    
def getCentralTime():
    return datetime.now()-timedelta(hours=1)-(timedelta(hours=1) if isDst() else timedelta(hours=0))

stockPairs=[(0,"depleted"),(1,"insufficient"),(2,"recommended"),(3,"abundant"),(4,"excessive")]
# return 0, depleted when string not found
def getStockIdFromString(string):
    if(not string):
        return 0
    for id, value in stockPairs:
        if isStringSameOrSimilar(value, string):
            return id
    return 0