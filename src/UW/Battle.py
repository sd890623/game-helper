from guiUtils import win
from utils import *
# from UWTask import UWTask

class Battle:
    randomPoint=874,666

    def __init__(self, instance: win, uwtask) -> None:
        self.instance=instance
        self.uwtask=uwtask

    def suppressBattle(self):
        #runAway
        wait(lambda: self.instance.clickPointV2(800,560),10)
        if(self.uwtask.inWater()):
            self.uwtask.print("retreated from battle")
            return

        print("in battle")
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,1)
        #use fast
        if(self.uwtask.hasSingleLineWordsInArea("free",A=[74,226,112,242])):
            self.instance.clickPointV2(95,217)
        continueWithUntilBy(lambda: self.instance.rightClickPointV2(655,330),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.uwtask.hasSingleLineWordsInArea("close", A=[632,691,680,714]) or self.uwtask.inCityList(self.uwtask.allCityList),10,timeout=240)
        def exitBattle():
            wait(lambda: self.instance.clickPointV2(673,707),2)
            if(self.uwtask.hasSingleLineWordsInArea("yes",A=[946,617,1028,656])):
                wait(lambda: self.instance.clickPointV2(976,636),2)
        doAndWaitUntilBy(lambda: exitBattle(),lambda: self.uwtask.inWater(),5,2)


    def doBattle(self):
        #GoBattle #combat area [749,427,858,459]
        wait(lambda: self.instance.clickPointV2(839,437),10)     
        wait(lambda: self.instance.clickPointV2(724,357),3)     

        # if(self.uwtask.inWater()):
        #     self.uwtask.print("retreated from battle")
        #     return

        print("in battle")
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,1)
        #use fast
        if(self.uwtask.hasSingleLineWordsInArea("free",A=[74,226,112,242])):
            self.instance.clickPointV2(95,217)
        continueWithUntilBy(lambda: self.instance.rightClickPointV2(655,330),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.uwtask.hasSingleLineWordsInArea("close", A=[632,691,680,714]) or self.uwtask.inCityList(self.uwtask.allCityList),10,timeout=240)
        def exitBattle():
            wait(lambda: self.instance.clickPointV2(673,707),2)
            if(self.uwtask.hasSingleLineWordsInArea("yes",A=[946,617,1028,656])):
                wait(lambda: self.instance.clickPointV2(976,636),2)
        doAndWaitUntilBy(lambda: exitBattle(),lambda: self.uwtask.inWater(),5,2)
