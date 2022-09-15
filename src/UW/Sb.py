from guiUtils import win
from utils import *
# from UWTask import UWTask

class Sb:
    okButton=653,483
    dismantleButton=59,333
    # def __init__(self, instance: win, uwtask:UWTask) -> None:
    def __init__(self, instance: win, uwtask) -> None:
        self.instance=instance
        self.uwtask=uwtask

    def gotoShipyard(self):
        self.uwtask.print("去船chang")
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),1)
        #click shipyard
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1129,330), lambda: self.uwtask.hasSingleLineWordsInArea("shipyard", A=self.uwtask.titleArea))
    
    def pickup(self):
        self.uwtask.print("去取船")
        # receive#1 ship area 234,321,329,342
        # receive #2 ship area 409,319,527,344
        if(self.uwtask.hasSingleLineWordsInArea(("quickbuild"), A=[1118,294,1231,319])):
            self.uwtask.print("being built, jump over")
            self.uwtask.shipBeingBuilt=True
            return
        #click receive#1 ship
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(1167,307), 2, 2) 
        #Enter random strings
        wait(lambda: self.instance.clickPointV2(715,366),2)
        self.instance.typewrite(str(random.randint(1,99)))
        self.instance.send_enter()
        #click ok
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.okButton), 2,5)
        #click a few times to out
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.okButton), 2, 2)

    def dismantle(self,index):
        if(self.uwtask.shipBeingBuilt):
            return
        self.uwtask.print("dismantle船")
        #click dismantle
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.dismantleButton), lambda: self.uwtask.hasSingleLineWordsInArea("dismantle", A=self.uwtask.titleArea),1)
        # #click 6th ship
        wait(lambda: self.instance.clickPointV2(591,137),2)
        #click dismantle
        wait(lambda: self.instance.clickPointV2(665,591),7)
        #click yes
        wait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),7)
        #click a few times to out
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.okButton), 2, 1)
        

    def build(self, option):
        if(self.uwtask.shipBeingBuilt):
            return 
        self.uwtask.print("造船")
        #click build
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(51,89), lambda: self.uwtask.hasSingleLineWordsInArea("build", A=self.uwtask.titleArea))    
        #click 1st ship 286,179
        #2nd row last col ship 1199,523
        #xDiff 183
        #yDiff 226
        buildX=int(287+183.6*(option%6))
        buildY=int(179+226*int(option/6))
        # print(buildX,buildY)
        wait(lambda: self.instance.clickPointV2(buildX,buildY),4)
        #click build
        wait(lambda: self.instance.clickPointV2(747,604),4)
        if(self.uwtask.hasSingleLineWordsInArea("notice", A=self.uwtask.noticeTitleArea)):
            wait(lambda: self.instance.clickPointV2(*self.uwtask.noticeOK),2)

        #click yes
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),2, 4)

        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.dismantleButton), lambda: self.uwtask.hasSingleLineWordsInArea("dismantle", A=self.uwtask.titleArea))
        
    def goBackTown(self,city):
        #go town
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.hasSingleLineWordsInArea(city, A=self.uwtask.inTownCityNameArea))