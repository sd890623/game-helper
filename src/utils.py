import time
import random

def wait(func, seconds = 2):
    func()
    time.sleep(seconds+random.randint(0,3))
