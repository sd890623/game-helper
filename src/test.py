from windows import *
from Task import Task
from datetime import datetime


yBuffer = 36

hwndObject = None;
id = 0
allWindowsWithTitle = getAllWindowsWithTitle("星战前夜：无烬星河 - MuMu模拟器")
if (len(allWindowsWithTitle) > id):
    hwndObject = allWindowsWithTitle[id]

print(allWindowsWithTitle)    

now = datetime.now()
dt_string = now.strftime("%d %H:%M:%S")
print("Time: ", dt_string)





task = Task(67360, 0)
#print(task.clickOnTestPic())
#print(task.findPlayerCountByType(Task.whitePlayerType))
task.runTask()




