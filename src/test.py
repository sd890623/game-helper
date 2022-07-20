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

now = datetime.now()
dt_string = now.strftime("%d %H:%M:%S")
print("Time: ", dt_string)





task = UWTask(198518, 0)
# task.startJourney()

while(True):
    task.startJourney()




