from windows import *
from UWTask import UWTask
from datetime import datetime


yBuffer = 36

hwndObject = None
id = 0
allWindowsWithTitle = getAllWindowsWithTitle("Chrome Remote Desktop - Media-PC")
if (len(allWindowsWithTitle) > id):
    hwndObject = allWindowsWithTitle[id]

print(allWindowsWithTitle) 




task = UWTask(722778, 0)
# task.market()

try:
    while(True):
        task.startJourney()
except Exception as e:
    print(e)
    




