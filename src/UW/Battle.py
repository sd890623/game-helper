from guiUtils import win
from utils import *
# from UWTask import UWTask

class Battle:
    randomPoint=874,666

    def __init__(self, instance: win, uwtask) -> None:
        self.instance=instance
        self.uwtask=uwtask

    def suppressBattle(self):
        wait(lambda: self.instance.clickPointV2(800,560),10)
        if(self.uwtask.inWater()):
            self.uwtask.print("retreated from battle")
            return

        print("in battle")
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,1)
        #use fast
        self.instance.clickPointV2(95,217)
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.randomPoint),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.uwtask.hasSingleLineWordsInArea("close", A=[632,691,680,714]),10)
        def exitBattle():
            wait(lambda: self.instance.clickPointV2(673,707),2)
            if(self.uwtask.hasSingleLineWordsInArea("yes",A=[946,617,1028,656],debug=True)):
                wait(lambda: self.instance.clickPointV2(976,636),2)
        doAndWaitUntilBy(lambda: exitBattle(),lambda: self.uwtask.inWater(),5,2)



