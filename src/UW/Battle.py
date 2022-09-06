from guiUtils import win
from utils import *
# from UWTask import UWTask

class Battle:
    def __init__(self, instance: win, uwtask) -> None:
        self.instance=instance
        self.uwtask=uwtask

    def suppressBattle(self):
        end=False

