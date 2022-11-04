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
        if(self.uwtask.hasSingleLineWordsInArea("free",A=[73,225,104,242])):
            self.instance.clickPointV2(95,217)
        continueWithUntilBy(lambda: self.instance.rightClickPointV2(655,330),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.uwtask.hasSingleLineWordsInArea("close", A=[632,691,680,714]) or self.uwtask.inCityList(self.uwtask.allCityList),10,timeout=240)
        def exitBattle():
            wait(lambda: self.instance.clickPointV2(673,707),2)
            if(self.uwtask.hasSingleLineWordsInArea("yes",A=[946,617,1028,656])):
                wait(lambda: self.instance.clickPointV2(976,636),2)
        doAndWaitUntilBy(lambda: exitBattle(),lambda: self.uwtask.inWater(),5,2)


    def doBattle(self):
        #GoBattle #combat area [749,427,858,459]
        x=0
        while(x<5):
            wait(lambda: self.instance.clickPointV2(980,629),1)
            wait(lambda: self.instance.clickPointV2(714,511),1)
            x+=1


        wait(lambda: self.instance.clickPointV2(724,357),3)   
        timeout=50  
        while(timeout>0):
            foundAutoOcr=self.uwtask.hasSingleLineWordsInArea("auto",A=[133,198,190,220])
            if(foundAutoOcr):
                wait(lambda: self.instance.clickPointV2(160,218),1)
                break
            time.sleep(0.5)
            timeout-=1
            if(timeout==0):
                break

        print("in battle")
        # doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),5,1)
        if(self.uwtask.inWater()):
            return
        #use fast
        if(self.uwtask.hasSingleLineWordsInArea("free",A=[73,225,104,242])):
            self.instance.clickPointV2(95,217)
        # time.sleep(10)
        # if(self.uwtask.hasSingleLineWordsInArea("free",A=[73,225,104,242])):
        #     self.instance.clickPointV2(95,217)

        wait(lambda: self.instance.clickPointV2(160,218),1)
        wait(lambda: self.instance.clickPointV2(160,218),1)
        wait(lambda: self.instance.clickPointV2(160,218),1)
        wait(lambda: self.instance.clickPointV2(160,218),1)

        wait(lambda: self.instance.clickPointV2(160,218),1)


        continueWithUntilBy(lambda: self.instance.rightClickPointV2(655,330),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.uwtask.hasSingleLineWordsInArea("close", A=[632,691,680,714]) or self.uwtask.inCityList(self.uwtask.allCityList),5,timeout=360)
        def exitBattle():
            wait(lambda: self.instance.clickPointV2(673,707),2)
            if(self.uwtask.hasSingleLineWordsInArea("yes",A=[946,617,1028,656])):
                wait(lambda: self.instance.clickPointV2(976,636),2)
        doAndWaitUntilBy(lambda: exitBattle(),lambda: self.uwtask.inWater(),5,2)

    def selectOpponentInList(self,opponents):
        firstPosi = (1137,257)
        area=[1087,238,1264,264]
        index=0
        while(index<8):
            yDiff=int(index%7*57.25)
            ocrOpponentName=self.uwtask.hasArrayStringInAreaSingleLineWords(opponents,A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])
            if(ocrOpponentName):
                wait(lambda: self.instance.fastClickPointV2(firstPosi[0],firstPosi[1]+yDiff),0.5,disableWait=True)
                # if(self.uwtask.hasArrayStringInAreaSingleLineWords(shortOpponents, A=[596,665,735,699],debug=True) or self.uwtask.hasArrayStringInAreaSingleLineWords(shortOpponents, A=[1084,126,1241,155])):
                return True
                # return False
            index+=1
        return False

    def quickWaitForCity(self,cityList=None,targetCity=None):
        self.uwtask.print("航行中")
        def inJourneyTask():
            self.uwtask.clickEnterCityButton()

        def backupFunc():
            self.uwtask.checkForDailyPopup()
            if(self.uwtask.hasSingleLineWordsInArea("notice",A=[452,292,546,316])):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(813,436),5,10)
            if(self.uwtask.hasSingleLineWordsInArea("notice",A=[482,299,557,325])):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(785,430),5,10)
            #More checks
            if(self.uwtask.hasSingleLineWordsInArea("info",A=[452,292,546,316])):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(813,436),5,10)
            if(self.uwtask.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.uwtask.hasSingleLineWordsInArea("close", A=[632,691,680,714])):
                battle=Battle(self.simulatorInstance,self)
                battle.suppressBattle()
            time.sleep(10)
            wait(lambda: self.uwtask.findCityAndClick(targetCity),60)
            doMoreTimesWithWait(lambda: self.instance.rightClickPointV2(*self.randomPoint),4,10)
        
        continueWithUntilByWithBackup(lambda: inJourneyTask(), lambda: self.uwtask.inCityList(cityList), 1, timeout=90,notifyFunc=lambda: self.uwtask.print("not found, wait for 4s"),backupFunc=backupFunc)
        self.uwtask.print("click twice")
        self.uwtask.clickEnterCityButton()

    def depart(self):
        def clickAndStock():
            wait(lambda: self.instance.clickPointV2(979,538),0.2)
            self.uwtask.restock()

        def clickAndStockBackup():
            self.uwtask.checkForDailyPopup()
            wait(lambda: self.instance.clickPointV2(979,538),0.2)
            if(self.uwtask.hasSingleLineWordsInArea("harbor", A=self.uwtask.titleArea)):
                self.uwtask.restock()
        clickAndStock()
        if(self.uwtask.hasSingleLineWordsInArea("crewsize",A=[1077,449,1154,473])):
            actualCrew=self.uwtask.getNumberFromSingleLineInArea(A=[1154,451,1181,471])
            maxCrew=self.uwtask.getNumberFromSingleLineInArea(A=[1187,451,1213,469])
            if(actualCrew/maxCrew<0.95):
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(1164,464),lambda: self.uwtask.hasSingleLineWordsInArea("recruit", A=self.uwtask.titleArea), 1,2)
                wait(lambda: self.instance.clickPointV2(1211,399),0)                
                wait(lambda: self.instance.clickPointV2(1240,509),0)
                wait(lambda: self.instance.clickPointV2(714,483),1)
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(714,483),lambda: self.uwtask.hasSingleLineWordsInArea("harbor", A=self.uwtask.titleArea), 1,2)

        self.uwtask.print("出海")
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1183,568), lambda: self.uwtask.inWater(), 4,2, backupFunc=clickAndStockBackup)

    def goBackPort(self, town):
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),2,0)
        wait(lambda: self.uwtask.findCityAndClick(town),0)
        self.quickWaitForCity([town],targetCity=town)

    def leavePort(self):
        if(not self.uwtask.inWater()):
            self.uwtask.goToHarbor()
            self.depart()

    def findOpponentOrReturn(self,opponents,town):
        firstPosi = (1137,257)
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint3),2,0)
        clickedOpponentInList=self.selectOpponentInList(opponents)
        if(not clickedOpponentInList):
            self.goBackPort(town)
            return False
        timeout=12
        combatScreenOpened=self.uwtask.hasArrayStringInAreaSingleLineWords(["combat","com","bat"], A=[635,691,697,717])
        if(not combatScreenOpened):
            wait(lambda: False,1)
        while(timeout>0 and not combatScreenOpened):
            speed=self.uwtask.getNumberFromSingleLineInArea(A=[1049,132,1085,146])
            if(speed<60 and self.uwtask.hasArrayStringInAreaSingleLineWords(opponents, A=[1087,238,1264,264])):
                wait(lambda: self.instance.fastClickPointV2(firstPosi[0],firstPosi[1]),0.5,disableWait=True)
                if(self.uwtask.hasArrayStringInAreaSingleLineWords(["combat","com","bat"], A=[635,691,697,717])):
                    break
            timeout-=1
            wait(lambda: False,1)
        if(timeout==0):
            self.goBackPort(town)
            return False  

        if(self.uwtask.hasArrayStringInAreaSingleLineWords(opponents, A=[1085,129,1265,156])):
            self.uwtask.print("opened")
            return True
        self.goBackPort(town)
        return False  

        