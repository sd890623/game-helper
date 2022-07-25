from windows import *
from UWTask import UWTask
from datetime import datetime


yBuffer = 36

hwndObject = None
id = 0
allWindowsWithTitle = getAllWindowsWithTitle("Windows 10 x64 - VMware Workstation")
if (len(allWindowsWithTitle) > id):
    hwndObject = allWindowsWithTitle[id]

print(allWindowsWithTitle) 


# mouse=FrontWindow()
# mouse.mouseClick(1398,162)

task = UWTask(hwndObject["hwnd"], 0)
task.bringWindowToFront()
task.shipBuilding(options=[0])
# # task.targetCity="ceuta"
# task.playNotification()
# task.setCurrentCityFromScreen()
# try:
#     while(True):
#         task.startJourney()
# except Exception as e:
#     print(e)
    




