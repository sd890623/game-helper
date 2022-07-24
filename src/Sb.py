from guiUtils import win
from utils import *
import os
# from UWTask import UWTask

class Sb:
    # def __init__(self, instance: win, uwtask:UWTask) -> None:
    def __init__(self, instance: win, uwtask) -> None:
        self.instance=instance
        self.uwtask=uwtask    

    def pickup(self):
        self.uwtask.print("去取船")
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),2)
        #click shipyard
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1079,306), lambda: self.uwtask.hasSingleLineWordsInArea("shipyard", A=self.uwtask.titleArea))
        #click build
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(48,88), lambda: self.uwtask.hasSingleLineWordsInArea("build", A=self.uwtask.titleArea))
        #click build in tab
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(355,80), 2, 2)
        #click receive
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(264,322), 2, 2)
        #click ok
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(637,494), 2,6)
        #click a few times to out
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(639,550), 3, 2)

    def dismantle(self):
        self.uwtask.print("dismantle船")
        #click dismantle
        continueWithUntilBy(lambda: self.instance.clickPointV2(72,335), lambda: self.uwtask.hasSingleLineWordsInArea("dismantle", A=self.uwtask.titleArea))
        #click 1st ship
        wait(lambda: self.instance.clickPointV2(218,137))
        #click dismantle
        wait(lambda: self.instance.clickPointV2(554,602),7)
        #click yes
        wait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),7)
        #click a few times to out
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(541,598), 3, 2)
        

    def build(self):
        self.uwtask.print("造船")
        #click build
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(48,88), lambda: self.uwtask.hasSingleLineWordsInArea("build", A=self.uwtask.titleArea))    
        #click 1st ship
        wait(lambda: self.instance.clickPointV2(306,206))
        #click build
        wait(lambda: self.instance.clickPointV2(707,609))
        #click yes
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),2, 7)
        #go town
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.hasSingleLineWordsInArea("seville", A=self.uwtask.inTownCityNameArea))