import time
import random
from datetime import datetime

def wait(func, seconds = 2):
    func()
    time.sleep(seconds+random.randint(0,3))

def getDateTimeString():
    now = datetime.now()
    dt_string = now.strftime("%d %H:%M:%S")
    return("Time: "+dt_string)