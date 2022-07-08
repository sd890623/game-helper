from windows import *
from Task import Task

yBuffer = 36

hwndObject = None;
id = 0
allWindowsWithTitle = getAllWindowsWithTitle("星战前夜：无烬星河 - MuMu模拟器")
if (len(allWindowsWithTitle) > id):
    hwndObject = allWindowsWithTitle[id]

print(allWindowsWithTitle)    



task = Task(526402, 2)
#print(task.clickOnTestPic())
#print(task.findPlayerCountByType(Task.whitePlayerType))
#task.runTask()
while(True):
    task.startMiningTask()



