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
        wait(lambda: self.instance.clickPointV2(1161,558),2)
        for i in [0,1,2]:
            if(self.uwtask.hasSingleLineWordsInArea(("receive"), A=[273,276+i*119,391,299+i*119])):
                self.uwtask.pickedUpShip=True
                #click receive#1 ship
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(326,290+i*119), 2, 2) 
                #Enter random strings
                wait(lambda: self.instance.clickPointV2(715,366),2)
                self.instance.typewrite(str(random.randint(1,99)))
                self.instance.send_enter()
                #click ok
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.okButton), 2,5)
                #click a few times to out
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.okButton), 4, 2)
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(1062,642), 4, 1)


    def dismantle(self,index):
        if(not self.uwtask.pickedUpShip):
            return
        self.uwtask.print("dismantle船")
        #click dismantle
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.dismantleButton), lambda: self.uwtask.hasSingleLineWordsInArea("dismantle", A=self.uwtask.titleArea),1)
        # #click 8th ship
        wait(lambda: self.instance.clickPointV2(741,138),2)
        #click dismantle
        wait(lambda: self.instance.clickPointV2(665,591),7)
        #click yes
        wait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),7)
        #click a few times to out
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.okButton), 2, 1)
        

    def build(self, option):
        if(not self.uwtask.pickedUpShip):
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