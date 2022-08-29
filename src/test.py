from windows import *
from EVE.EVETask import EVETask

id = 0
allWindowsWithTitle = getAllWindowsWithTitle("星战前夜：无烬星河 - MuMu模拟器")
if (len(allWindowsWithTitle) > id):
    hwndObject = allWindowsWithTitle[id]

print(allWindowsWithTitle)    

task = EVETask(hwndObject["hwnd"], 0)
#print(task.clickOnTestPic())
#print(task.findPlayerCountByType(Task.whitePlayerType))
task.closeWindow()
task.startMiningTask()