import time

def wait(func, seconds = 2):
    func()
    time.sleep(seconds)
