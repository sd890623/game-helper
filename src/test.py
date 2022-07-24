from windows import *
from UWTask import UWTask
from datetime import datetime


yBuffer = 36

hwndObject = None
id = 0
allWindowsWithTitle = getAllWindowsWithTitle("Chrome Legacy Window")
if (len(allWindowsWithTitle) > id):
    hwndObject = allWindowsWithTitle[id]

print(allWindowsWithTitle) 


# mouse=FrontWindow()
# mouse.mouseClick(1398,162)

task = UWTask(264478, 0)
# task.waitForCity()
# task.targetCity="ceuta"
task.playNotification()
task.setCurrentCityFromScreen()
try:
    while(True):
        task.startJourney()
except Exception as e:
    print(e)
    




