from guiUtils import win
from utils import *
from UWTask import UWTask

class Sb:
    okButton=716,564
    dismantleBtn=65,337
    buildBtn=52,82
    noticeTitleArea=[619,234,688,259]
    noticeOK=708,482
    # def __init__(self, instance: win, uwtask:UWTask) -> None:
    def __init__(self, instance: win, uwtask:UWTask) -> None:
        self.instance=instance
        self.uwtask=uwtask

    def gotoShipyard(self):
        self.uwtask.print("去船chang")
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),1)
        #click shipyard
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1259,333), lambda: self.uwtask.hasSingleLineWordsInArea("shipyard", A=self.uwtask.titleArea))
    
    def pickup(self):
        self.uwtask.print("去取船")
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.buildBtn), lambda: self.uwtask.hasSingleLineWordsInArea("build", A=self.uwtask.titleArea),1)
        wait(lambda: self.instance.clickPointV2(1369,854),2)
        for i in [0]:
            if(self.uwtask.hasSingleLineWordsInArea(("receive"), A=[335,353+i*119,441,378+i*119])):
                self.uwtask.pickedUpShip=True
                #click receive#1 ship
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(395,359+i*119), 2, 2) 
                #Enter random strings
                wait(lambda: self.instance.clickPointV2(778,446),2)
                self.instance.typewrite(str(random.randint(1,99)))
                self.instance.send_enter()
                #click ok
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.okButton), 2,5)
                #click a few times to out
                continueWithUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.randomPoint),lambda: self.uwtask.hasSingleLineWordsInArea(("notice"), A=[687,313,754,335]),2)
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(775,564), 3, 2)

    def dismantle(self,index):
        if(not self.uwtask.pickedUpShip):
            return
        self.uwtask.print("dismantle船")
        #click dismantle
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.dismantleBtn), lambda: self.uwtask.hasSingleLineWordsInArea("dismantle", A=self.uwtask.titleArea),1)
        # #click 6th ship
        wait(lambda: self.instance.clickPointV2(650,248),2)
        #click dismantle
        wait(lambda: self.instance.clickPointV2(725,678),7)
        #click yes
        wait(lambda: self.instance.clickPointV2(782,600),7)
        #click a few times to out
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.okButton), 2, 1)
        

    def build(self, option):
        if(not self.uwtask.pickedUpShip):
            return 
        self.uwtask.print("造船")
        #click build
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.buildBtn), lambda: self.uwtask.hasSingleLineWordsInArea("build", A=self.uwtask.titleArea))    
        #click 1st ship 304,232
        #2nd row last col ship 1313,479
        #xDiff 201.8
        #yDiff 247
        buildX=int(304+201.8*(option%6))
        buildY=int(232+247*int(option/6))
        # print(buildX,buildY)
        wait(lambda: self.instance.clickPointV2(buildX,buildY),4)
        #click build
        wait(lambda: self.instance.clickPointV2(797,663),4)
        if(self.uwtask.hasSingleLineWordsInArea("notice", A=self.noticeTitleArea)):
            wait(lambda: self.instance.clickPointV2(*self.noticeOK),2)

        #click yes
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),2, 4)

        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.dismantleBtn), lambda: self.uwtask.hasSingleLineWordsInArea("dismantle", A=self.uwtask.titleArea))
        
    def goBackTown(self,city):
        #go town
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.hasSingleLineWordsInArea(city, A=self.uwtask.inTownCityNameArea),3)