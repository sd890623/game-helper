from guiUtils import win
from datetime import datetime
from utils import wait,doMoreTimesWithWait,continueWithUntilBy,doAndWaitUntilBy,continueWithUntilByWithBackup,getTimeDiffInSeconds,getHour
from images import getNumberFromString
import time
from UWTask import UWTask

# todo list
# checkStats
class Battle:
    randomPoint=1029,698
    lastCallTime=0
    haveSentBattleFinNotification=False
    battleEnd={
        "okBtn":[695,857,745,875],
        "closeBtn":[695,857,745,875]
    }
    opentimeout=0

    def __init__(self, instance:win, uwtask:UWTask) -> None:
        self.instance=instance
        self.uwtask=uwtask
        self.lastCallTime=datetime(2021, 1, 1, 1, 1, 1)

    def suppressBattle(self):
        #runAway
        # wait(lambda: self.instance.clickPointV2(800,560),10)
        if(self.uwtask.inWater()):
            self.uwtask.print("retreated from battle")
            return

        print("in battle")
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,1)
        #use fast
        if(self.uwtask.hasSingleLineWordsInArea("fre",A=[77,110,106,125])):
            self.instance.clickPointV2(101,98)
        continueWithUntilBy(lambda: self.instance.rightClickPointV2(*self.randomPoint),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=self.battleEnd["okBtn"]) or self.uwtask.hasSingleLineWordsInArea("close", A=self.battleEnd["okBtn"]) or self.uwtask.inCityList(self.uwtask.allCityList),10,timeout=240)
        def exitBattle():
            wait(lambda: self.instance.clickPointV2(727,866),2)
            if(self.uwtask.hasSingleLineWordsInArea("yes",A=[1041,779,1118,811])):
                wait(lambda: self.instance.clickPointV2(1072,789),2)
        doAndWaitUntilBy(lambda: exitBattle(),lambda: self.uwtask.inWater(),5,2)


    def doBattle(self):
        x=0
        continueWithUntilBy(lambda: self.instance.clickPointV2(56,152), lambda: not self.uwtask.isPositionColorSimilarTo(56,152,(255,255,255)),1,10)
        while(x<5):
            wait(lambda: self.instance.clickPointV2(1074,797),0.6)
            wait(lambda: self.instance.clickPointV2(654,588),0.6)
            x+=1
        
        def backup():
            if(self.uwtask.hasSingleLineWordsInArea("notice",A=[684,314,754,337])):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(782,571),5,10)
                if(self.haveSentBattleFinNotification==False):
                    self.uwtask.sendNotification(f"Battle finished")
                    self.haveSentBattleFinNotification=True

        doAndWaitUntilBy(lambda: False, lambda: self.uwtask.hasSingleLineWordsInArea("auto",A=[139,84,192,101]),1,1,timeout=15,backupFunc=backup)

        if(self.uwtask.inWater()):
            return
        print("in battle")
        #use fast
        if(self.uwtask.hasSingleLineWordsInArea("fre",A=[77,110,106,125])):
            self.instance.clickPointV2(101,98)

        centralPos=718,452
        openSkillPos=1379,378
        waitPos=1382,529
        def getSkillPosByIndex(index):
            xDiff=76.3
            yDiff=75
            return (1161+int(index%4*xDiff),369+int(index/4)*yDiff)

        for x in range(5): 
            isFoeTurn=self.uwtask.isPositionColorSimilarTo(221,16,(165, 32, 28))
            if(isFoeTurn):
                time.sleep(4)
            number=self.uwtask.getNumberFromSingleLineInArea(A=[219,6,233,20])
            match number:
                case 1:
                    #No 1 Pao Buff
                    wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    # Alan: 6, Otto:6 , Ernst: 6
                    wait(lambda: self.instance.clickPointV2(*getSkillPosByIndex(6)),0.5)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    time.sleep(5)
                case 2:
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)
                    #No 2 eva Buff
                    # wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    # wait(lambda: self.instance.clickPointV2(getSkillPosByIndex(7)),0.5)
                    # wait(lambda: self.instance.longerClickPointV2(*centralPos),3)
                case 3:
                    #open skill #No3 ram buff
                    wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    wait(lambda: self.instance.clickPointV2(*getSkillPosByIndex(6)),0.5)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    time.sleep(4)
                case 4:
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)
                case 5:
                    #5  atk Buff
                    wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    wait(lambda: self.instance.clickPointV2(*getSkillPosByIndex(8)),0.5)
                    wait(lambda: self.instance.longerClickPointV2(*centralPos),3)
                case 6:
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)
                case 7:
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)
                case _:
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)
        
        continueWithUntilBy(lambda: self.instance.longerClickPointV2(170,87), lambda: self.uwtask.isPositionColorSimilarTo(170,87,(255, 255, 255)),1,20)
        time.sleep(15)
        if(self.uwtask.hasSingleLineWordsInArea("skill",A=[1363,381,1407,402])):
            wait(lambda: self.instance.clickPointV2(170,87),0.5)
            #Click on "no" for duel

        continueWithUntilBy(lambda: self.instance.rightClickPointV2(*self.randomPoint),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=self.battleEnd["okBtn"]) or self.uwtask.hasSingleLineWordsInArea("close", A=self.battleEnd["okBtn"]) or self.uwtask.inCityList(self.uwtask.allCityList),5,timeout=360)
        def backupFunc():
            exitBattle()
            self.uwtask.checkForDailyPopup()
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),5,3)

        def exitBattle():
            wait(lambda: self.instance.clickPointV2(727,866),2)
            if(self.uwtask.hasSingleLineWordsInArea("yes",A=[1041,779,1118,811])):
                wait(lambda: self.instance.clickPointV2(1072,789),2)
        doAndWaitUntilBy(lambda: exitBattle(),lambda: self.uwtask.inWater(),5,2,backupFunc=backupFunc)
        time.sleep(1)
        self.uwtask.checkForDailyPopup(4)
        if(not self.uwtask.inWater()):
            doAndWaitUntilBy(lambda: self.instance.rightClickPointV2(*self.randomPoint),lambda: self.uwtask.inWater(),1,1)

    def checkStats(self,town):
        time.sleep(2)
        # 0 crew not fixed
        if(self.uwtask.isPositionColorSimilarTo(140,63,(218,165,30)) or self.uwtask.isPositionColorSimilarTo(140,64,(232,202,44))):
            self.goBackPort(town)
            return False
        return True

    def checkInPort(self,town):
        now=datetime.now()
        if(getTimeDiffInSeconds(self.lastCallTime,now)>1800):
            if(now.minute>=30):
                self.uwtask.healInjury(town)
            if(self.uwtask.tradeRouteBuyFin==False):
               self.uwtask.buyInCity([town], products=["agarwood","ylang-ylang","mace","chinesetea","gardenia","begonia","sweetolive","azalea","ginseng","pinkdiamond"],marketMode=1)
            self.lastCallTime=now

    def selectOpponentInList(self,opponentsInList):
        firstPosi=(1227,257)
        area=[1210,248,1347,270]
        index=0
        while(index<16):
            yDiff=int(index%10*56.5)
            index+=1
            hasName=self.uwtask.hasArrayStringEqualSingleLineWords(opponentsInList,A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff])
            if(hasName):
                wait(lambda: self.instance.fastClickPointV2(firstPosi[0],firstPosi[1]+yDiff),0.5,disableWait=True)
                if(self.uwtask.hasSingleLineWordsInArea("pirate", A=[667,831,787,855])):
                    wait(lambda: self.instance.clickPointV2(39,695))
                    continue
                else:
                    time.sleep(1)
                    if(self.uwtask.hasSingleLineWordsInArea("pirate", A=[1187,129,1396,159])):
                        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inWater(), 1,30)
                        continue
                    else:
                        return True
        return False

    def quickWaitForCity(self,cityList=None,targetCity=None):
        self.uwtask.print("航行中")
        def inJourneyTask():
            self.uwtask.clickEnterCityButton()

        def backupFunc():
            self.uwtask.checkForDailyPopup(5)
            if(self.uwtask.hasSingleLineWordsInArea("huamei", A=[62,132,165,158])):
                continueWithUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inWater(), 1,30)
            self.uwtask.checkForBasicStuck()
            if(self.uwtask.hasSingleLineWordsInArea("auto",A=[138,80,186,98]) or self.uwtask.hasSingleLineWordsInArea("ok", A=self.battleEnd["okBtn"]) or self.uwtask.hasSingleLineWordsInArea("close", A=self.battleEnd["okBtn"])):
                self.suppressBattle()
            time.sleep(10)
            wait(lambda: self.uwtask.findCityAndClick(targetCity),40)
            doMoreTimesWithWait(lambda: self.instance.rightClickPointV2(*self.randomPoint),4,10)
        
        continueWithUntilByWithBackup(lambda: inJourneyTask(), lambda: self.uwtask.inCityList(cityList), 1, timeout=40,notifyFunc=lambda: self.uwtask.print("not found, wait for 4s"),backupFunc=backupFunc)
        self.uwtask.print("click twice")
        self.uwtask.clickEnterCityButton()

    def depart(self):
        firstLineArrowBtn=1401,540
        okBtn=778,568
        departBtn=1287,655
        def clickAndStock():
            wait(lambda: self.instance.clickPointV2(*self.uwtask.randomPoint),0.2)
            self.uwtask.restock()

        def clickAndStockBackup():
            self.uwtask.checkForDailyPopup()
            wait(lambda: self.instance.clickPointV2(*self.uwtask.randomPoint),0.2)
            if(self.uwtask.hasSingleLineWordsInArea("harbor", A=self.uwtask.titleArea)):
                self.uwtask.restock()
                self.instance.clickPointV2(*departBtn)
        clickAndStock()
        if(self.uwtask.hasSingleLineWordsInArea("crewsize",A=[1203,529,1274,550])):
            crewWords=self.uwtask.getSingleLineWordsInArea(A=[1274,529,1364,548],ocrType=2)

            actualCrew=getNumberFromString(crewWords.split("/")[0])
            maxCrew=getNumberFromString(crewWords.split("/")[1])
            if(actualCrew/maxCrew<0.97):
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(*firstLineArrowBtn),lambda: self.uwtask.hasSingleLineWordsInArea("recruit", A=self.uwtask.titleArea), 1,2)
                wait(lambda: self.instance.clickPointV2(1333,410),0)                
                wait(lambda: self.instance.longerClickPointV2(1350,526),2)
                wait(lambda: self.instance.clickPointV2(*okBtn),1)
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(*okBtn),lambda: self.uwtask.hasSingleLineWordsInArea("harbor", A=self.uwtask.titleArea), 1,2,backupFunc=lambda: self.instance.clickPointV2(*self.uwtask.leftTopBackBtn),timeout=10)

        self.uwtask.print("出海")
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*departBtn), lambda: self.uwtask.inWater(), 4,2, backupFunc=clickAndStockBackup)
        time.sleep(2)
        self.uwtask.checkForDailyPopup(3)

    def backupFromDashboardToSea(self):
        wait(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon),1)

    def goBackPort(self, town):
        wait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),0)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),lambda: self.uwtask.inWater(),1,1,backupFunc=self.backupFromDashboardToSea,timeout=10)
        wait(lambda: self.uwtask.findCityAndClick(town),0)
        self.quickWaitForCity([town],targetCity=town)
        self.opentimeout=0

    def leavePort(self):
        doMoreTimesWithWait(lambda: self.instance.rightClickPointV2(*self.randomPoint),2,1)
        self.uwtask.goToHarbor()
        self.depart()
        if(getHour() in [21,22,23,24,0,1,2]):
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(39,695),2,4)

    def checkStopped(self):
        return self.uwtask.getNumberFromSingleLineInArea(A=[1174,133,1197,150])==0
    
    def findOpponentOrReturn(self,opponentsInList,opponents,town):
        nameBoardInPrePanel=[62,132,165,158]
        wait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint3),0)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint3),lambda: self.uwtask.inWater(),1,1,backupFunc=self.backupFromDashboardToSea,timeout=10)
        clickedOpponentInList=self.selectOpponentInList(opponentsInList)
        if(not clickedOpponentInList):
            self.goBackPort(town)
            return False
        timeout=20
        combatScreenOpened=self.uwtask.hasSingleLineWordsInArea("huamei", A=nameBoardInPrePanel)
        if(not combatScreenOpened):
            wait(lambda: False,1)
        while(timeout>0 and not combatScreenOpened):
            if(self.uwtask.hasSingleLineWordsInArea("huamei", A=nameBoardInPrePanel)):
                break
            if(self.checkStopped()):
                return self.findOpponentOrReturn(opponentsInList,opponents,town)
            timeout-=1
            wait(lambda: False,1)
        if(timeout==0):
            wait(lambda: self.instance.clickPointV2(720,862),2)
            if(self.uwtask.hasSingleLineWordsInArea("huamei", A=nameBoardInPrePanel)):
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inWater(),1,1)
            return self.findOpponentOrReturn(opponentsInList,opponents,town)

        if(self.uwtask.hasArrayStringInSingleLineWords(opponents, A=[1187,129,1396,159]) and not self.uwtask.hasSingleLineWordsInArea("pirate",A=[1187,129,1396,159])):
            self.uwtask.print("opened")
            return doAndWaitUntilBy(lambda: self.instance.clickPointV2(720,825),lambda: self.uwtask.hasSingleLineWordsInArea("combat", A=[684,15,746,32]),1,1,timeout=10)
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inWater(), 1,30)
        self.opentimeout+=1
        if(self.opentimeout>2):
            self.goBackPort(town)
            return False
        return self.findOpponentOrReturn(opponentsInList,opponents,town)
        