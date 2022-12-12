from guiUtils import win
from datetime import datetime
from utils import *
# from UWTask import UWTask

class Battle:
    randomPoint=874,666
    lastCallTime=0

    def __init__(self, instance: win, uwtask) -> None:
        self.instance=instance
        self.uwtask=uwtask
        self.lastCallTime=datetime(2021, 1, 1, 1, 1, 1)

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
        x=0
        continueWithUntilBy(lambda: self.instance.clickPointV2(80,220), lambda: not self.uwtask.isPositionColorSimilarTo(80,220,(248, 255, 255)),1,10)
        while(x<5):
            wait(lambda: self.instance.clickPointV2(980,629),0.6)
            wait(lambda: self.instance.clickPointV2(560,511),0.6)
            x+=1

        doAndWaitUntilBy(lambda: False, lambda: self.uwtask.hasSingleLineWordsInArea("auto",A=[136,202,186,219]),1,1,timeout=20)

        if(self.uwtask.inWater()):
            return
        print("in battle")
        #use fast
        if(self.uwtask.hasSingleLineWordsInArea("free",A=[73,225,104,242])):
            self.instance.clickPointV2(95,217)

        centralPos=654,369
        openSkillPos=1259,294


        for x in range(8):
            number=self.uwtask.getNumberFromSingleLineInArea(A=[223,5,239,19])
            match number:
                #3 1184,368 # 6: 1113,425 #7 1185,434 #4 1249,370
                case 1:
                    #open skill #No 1 Pao Buff, #5
                    wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    wait(lambda: self.instance.clickPointV2(1044,430),1)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    time.sleep(5)
                case 2:
                    # wait(lambda: self.instance.clickPointV2(1257,443),3)
                    #open skill #No 6 eva Buff
                    wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    wait(lambda: self.instance.clickPointV2(1113,425),0.5)
                    wait(lambda: self.instance.longerClickPointV2(*centralPos),3)
                case 3:
                    # wait(lambda: self.instance.clickPointV2(1257,443),3)
                    #open skill 
                    wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    #No3 ram buff #7
                    wait(lambda: self.instance.clickPointV2(1184,432),0.5)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    time.sleep(4)
                case 4:
                    #open skill #No 6 atk Buff
                    wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    wait(lambda: self.instance.clickPointV2(1113,425),0.5)
                    wait(lambda: self.instance.longerClickPointV2(*centralPos),3)
                    # wait(lambda: self.instance.clickPointV2(1257,443),3)
                case 5:
                    wait(lambda: self.instance.clickPointV2(1257,443),3)
                    # #open skill #ram atk
                    # wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    # wait(lambda: self.instance.clickPointV2(1119,433),0.5)
                    # doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    # time.sleep(4)
                case 6:
                    wait(lambda: self.instance.clickPointV2(1257,443),3)
                    # #open skill 
                    # wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    # #No5 atk buff
                    # wait(lambda: self.instance.clickPointV2(1113,425),0.5)
                    # wait(lambda: self.instance.longerClickPointV2(*centralPos),3)
                case 7:
                    wait(lambda: self.instance.clickPointV2(1257,443),3)

                case _:
                    wait(lambda: self.instance.clickPointV2(1257,443),3)
        
        continueWithUntilBy(lambda: self.instance.longerClickPointV2(160,218), lambda: self.uwtask.isPositionColorSimilarTo(181,209,(248, 255, 255)),1,20)
        time.sleep(15)
        if(self.uwtask.hasSingleLineWordsInArea("skill",A=[1236,303,1279,322])):
            wait(lambda: self.instance.clickPointV2(160,218),0.5)
            #Click on "no" for duel

        continueWithUntilBy(lambda: self.instance.rightClickPointV2(655,330),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.uwtask.hasSingleLineWordsInArea("close", A=[632,691,680,714]) or self.uwtask.inCityList(self.uwtask.allCityList),5,timeout=360)
        def backupFunc():
            exitBattle()
            self.uwtask.checkForDailyPopup()
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(673,707),5,3)

        def exitBattle():
            wait(lambda: self.instance.clickPointV2(673,707),2)
            if(self.uwtask.hasSingleLineWordsInArea("yes",A=[946,617,1028,656])):
                wait(lambda: self.instance.clickPointV2(976,636),2)
        doAndWaitUntilBy(lambda: exitBattle(),lambda: self.uwtask.inWater(),5,2,backupFunc=backupFunc)
        time.sleep(3)
        self.uwtask.checkForDailyPopup(2)
        if(not self.uwtask.inWater()):
            doAndWaitUntilBy(lambda: self.instance.rightClickPointV2(*self.randomPoint),lambda: self.uwtask.inWater(),1,1)

    def checkStats(self,town):
        if(self.uwtask.isPositionColorSimilarTo(139,66,(255,240,58)) or self.uwtask.isPositionColorSimilarTo(140,64,(232,202,44))):
            self.goBackPort(town)
            return False
        return True

    def checkInPort(self,town):
        now=datetime.now()
        if(getTimeDiffInSeconds(self.lastCallTime,now)>1800):
            if(now.minute>=30):
                self.uwtask.healInjury(town)
            if(self.uwtask.tradeRouteBuyFin==False):
                self.uwtask.buyInCity(town, products=["agarwood","ylang-ylang"],marketMode=1)
            self.lastCallTime=now

    def selectOpponentInList(self,opponents):
        firstPosi = (1137,257)
        area=[1087,238,1264,264]
        index=0
        while(index<13):
            yDiff=int(index%8*57.25)
            ocrOpponentName=self.uwtask.hasArrayStringInAreaSingleLineWords(opponents,A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])
            if(ocrOpponentName):
                wait(lambda: self.instance.fastClickPointV2(firstPosi[0],firstPosi[1]+yDiff),0.5,disableWait=True)
                return True
            index+=1
        return False

    def quickWaitForCity(self,cityList=None,targetCity=None):
        self.uwtask.print("航行中")
        def inJourneyTask():
            self.uwtask.clickEnterCityButton()

        def backupFunc():
            self.uwtask.checkForDailyPopup(5)
            if(self.uwtask.hasSingleLineWordsInArea("lih", A=[63,125,102,151])):
                continueWithUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inWater(), 1,30)
            if(self.uwtask.hasSingleLineWordsInArea("notice",A=[452,292,546,316])):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(813,436),5,10)
            if(self.uwtask.hasSingleLineWordsInArea("notice",A=[482,299,557,325])):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(785,430),5,10)
            #More checks
            if(self.uwtask.hasSingleLineWordsInArea("info",A=[452,292,546,316])):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(813,436),5,10)
            if(self.uwtask.hasSingleLineWordsInArea("ok", A=[632,691,680,714]) or self.uwtask.hasSingleLineWordsInArea("close", A=[632,691,680,714])):
                battle=Battle(self.instance,self)
                battle.suppressBattle()
            time.sleep(10)
            wait(lambda: self.uwtask.findCityAndClick(targetCity),40)
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
                self.instance.clickPointV2(1183,568)
        clickAndStock()
        if(self.uwtask.hasSingleLineWordsInArea("crewsize",A=[1077,449,1154,473])):
            actualCrew=self.uwtask.getNumberFromSingleLineInArea(A=[1154,451,1181,471])
            maxCrew=self.uwtask.getNumberFromSingleLineInArea(A=[1187,451,1213,469])
            if(actualCrew/maxCrew<0.97):
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(1164,464),lambda: self.uwtask.hasSingleLineWordsInArea("recruit", A=self.uwtask.titleArea), 1,2)
                wait(lambda: self.instance.clickPointV2(1211,399),0)                
                wait(lambda: self.instance.longerClickPointV2(1240,509),2)
                wait(lambda: self.instance.clickPointV2(714,483),1)
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(714,483),lambda: self.uwtask.hasSingleLineWordsInArea("harbor", A=self.uwtask.titleArea), 1,2,backupFunc=lambda: self.instance.clickPointV2(*self.uwtask.leftTopBackBtn))

        self.uwtask.print("出海")
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1183,568), lambda: self.uwtask.inWater(), 4,2, backupFunc=clickAndStockBackup)
        time.sleep(2)
        self.uwtask.checkForDailyPopup(3)


    def goBackPort(self, town):
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),2,0)
        wait(lambda: self.uwtask.findCityAndClick(town),0)
        self.quickWaitForCity([town],targetCity=town)

    def leavePort(self):
        doMoreTimesWithWait(lambda: self.instance.rightClickPointV2(*self.randomPoint),2,1)
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
        combatScreenOpened=self.uwtask.hasSingleLineWordsInArea("lih", A=[63,125,102,151])
        if(not combatScreenOpened):
            wait(lambda: False,1)
        while(timeout>0 and not combatScreenOpened):
            if(self.uwtask.hasSingleLineWordsInArea("lih", A=[63,125,102,151])):
                break
            timeout-=1
            wait(lambda: False,1)
        if(timeout==0):
            wait(lambda: self.instance.clickPointV2(652,695),2)
            self.goBackPort(town)
            return False  

        if(self.uwtask.hasArrayStringInAreaSingleLineWords(opponents, A=[1085,129,1265,156])):
            self.uwtask.print("opened")
            def backup():
                self.findOpponentOrReturn(opponents,town)
            doAndWaitUntilBy(lambda: self.instance.clickPointV2(663,639),lambda: self.uwtask.hasSingleLineWordsInArea("combat", A=[600,12,699,49]),1,1,backupFunc=backup)
            return True
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inWater(), 1,30)
        return self.findOpponentOrReturn(opponents,town)
        