from windows import *
from Task import Task

yBuffer = 36

hwndObject = None;
id = 0
if (len(getAllWindowsWithTitle()) > id):
    hwndObject = getAllWindowsWithTitle()[id]
    

task = Task(136319154)
task.runTask()



