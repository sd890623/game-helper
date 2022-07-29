from guiUtils import win
from utils import *
import os
# from UWTask import UWTask

class Sb:
    # def __init__(self, instance: win, uwtask:UWTask) -> None:
    def __init__(self, instance: win, uwtask) -> None:
        self.instance=instance
        self.uwtask=uwtask   

    def gotoShipyard(self):
        self.uwtask.print("去船chang")
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),2)
        #click shipyard
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1079,306), lambda: self.uwtask.hasSingleLineWordsInArea("shipyard", A=self.uwtask.titleArea))
    
    def pickup(self):
        self.uwtask.print("去取船")
        #click build
        continueWithUntilBy(lambda: self.instance.clickPointV2(48,88), lambda: self.uwtask.hasSingleLineWordsInArea("build", A=self.uwtask.titleArea))
        #click build in tab
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(355,80), 2, 4)
        # receive#1 ship area 212,312,349,338
        # receive #2 ship area 391,311,528,339
        if(self.uwtask.hasSingleLineWordsInArea(("quickbuild"), A=[212,312,349,338])):
            self.uwtask.print("being built, jump over")
            self.uwtask.shipBeingBuilt=True
            return
        #click receive#1 ship
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(267,322), 2, 4)        
        #click receive#2 ship
        # doMoreTimesWithWait(lambda: self.instance.clickPointV2(465,327), 2, 4)
        #click ok
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(637,494), 2,7)
        #click a few times to out
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(639,550), 2, 2)
        continueWithUntilBy(lambda: self.instance.clickPointV2(72,335), lambda: self.uwtask.hasSingleLineWordsInArea("dismantle", A=self.uwtask.titleArea))


    def dismantle(self,index):
        if(self.uwtask.shipBeingBuilt):
            return
        self.uwtask.print("dismantle船")
        #click dismantle
        continueWithUntilBy(lambda: self.instance.clickPointV2(72,335), lambda: self.uwtask.hasSingleLineWordsInArea("dismantle", A=self.uwtask.titleArea))
        # #click 1st ship
        # wait(lambda: self.instance.clickPointV2(218,137),4)
        # #click 5th ship+index xdiff, no need
        wait(lambda: self.instance.clickPointV2(502,140),4)
        #click dismantle
        wait(lambda: self.instance.clickPointV2(554,602),7)
        #click yes
        wait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),7)
        #click a few times to out
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(541,598), 2, 1)
        

    def build(self, option):
        if(self.uwtask.shipBeingBuilt):
            return 
        self.uwtask.print("造船")
        #click build
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(48,88), lambda: self.uwtask.hasSingleLineWordsInArea("build", A=self.uwtask.titleArea))    
        #click 1st ship 279,213
        #2nd row last col ship 1172,427
        #xDiff 178.6
        #yDiff 214
        buildX=int(279+178.6*(option%6))
        buildY=int(213+214*int(option/6))
        # print(buildX,buildY)
        wait(lambda: self.instance.clickPointV2(buildX,buildY),4)
        #click build
        wait(lambda: self.instance.clickPointV2(707,609),4)
        #click yes
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),2, 4)
        continueWithUntilBy(lambda: self.instance.clickPointV2(72,335), lambda: self.uwtask.hasSingleLineWordsInArea("dismantle", A=self.uwtask.titleArea))
        
    def goBackTown(self,city):
        #go town
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.hasSingleLineWordsInArea(city, A=self.uwtask.inTownCityNameArea))