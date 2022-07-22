import time
import random
from datetime import datetime
import threading

def wait(func, seconds = 2):
    func()
    time.sleep(seconds+random.randint(0,6))

def getDateTimeString():
    now = datetime.now()
    dt_string = now.strftime("%d %H:%M:%S")
    return("Time: "+dt_string)

findPlayerCountLk=threading.Lock()
