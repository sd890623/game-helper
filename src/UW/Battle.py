import sys
import os
sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

from guiUtils import win
from datetime import datetime
from utils import randomInt,wait,doMoreTimesWithWait,continueWithUntilBy,doAndWaitUntilBy,continueWithUntilByWithBackup,getTimeDiffInSeconds,getHour,hasOneArrayStringSimilarToString
from images import getNumberFromString
import time
from UWTask import UWTask
from constants import blackListForBattle

# todo list
# checkStats
class Battle:
    randomPoint=507,783
    lastCallTime=0
    haveSentBattleFinNotification=False
    battleEnd={
        "okBtn":[650,669,800,694],
        "closeBtn":[650,669,800,694]
    }
    opentimeout=0
    nameBoardInPrePanel=[61,163,157,190]

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
        if(self.uwtask.hasSingleLineWordsInArea("free",A=[77,110,106,125])):
            self.instance.clickPointV2(101,98)
        continueWithUntilBy(lambda: self.instance.rightClickPointV2(*self.randomPoint),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=self.battleEnd["okBtn"]) or self.uwtask.hasSingleLineWordsInArea("close", A=self.battleEnd["okBtn"]) or self.uwtask.inCityList(self.uwtask.allCityList),10,timeout=240)
        time.sleep(3)
        def exitBattle():
            wait(lambda: self.instance.clickPointV2(725,681),2)
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
            if(self.uwtask.hasSingleLineWordsInArea("notice",A=[682,268,755,294])):
                wait(lambda: self.instance.clickPointV2(571,568))
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(780,600),4,5)
                if(self.haveSentBattleFinNotification==False):
                    self.uwtask.sendNotification(f"Battle finished")
                    self.haveSentBattleFinNotification=True

        doAndWaitUntilBy(lambda: False, lambda: self.uwtask.hasSingleLineWordsInArea("auto",A=[789,856,844,877]),1,1,timeout=15,backupFunc=backup)

        if(self.uwtask.inWater()):
            return
        print("in battle")
        
        #use fast

        if(self.uwtask.hasSingleLineWordsInArea("fre",A=[694,866,725,881])):
            wait(lambda: self.instance.clickPointV2(718,867))
        if(not self.uwtask.hasSingleLineWordsInArea("using",A=[699,867,738,881]) and self.uwtask.hasSingleLineWordsInArea("fast",A=[699,848,739,866])):
            continueWithUntilBy(lambda: self.instance.clickPointV2(718,867), lambda: not self.uwtask.hasSingleLineWordsInArea("fast",A=[699,848,739,866]) or self.uwtask.isPositionColorSimilarTo(675,856,(255,255,85)))
            if(self.uwtask.hasSingleLineWordsInArea("purchase",A=[660,279,781,308])):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(786,591),2,2)
                if(self.haveSentBattleFinNotification==False):
                    self.uwtask.sendNotification(f"Battle finished")
                    self.haveSentBattleFinNotification=True

        centralPos=716,454
        openSkillPos=1270,786
        openSkilltab=1387,656
        expressskill=1224,853
        waitPos=1392,788
        def getSkillPosByIndex(index):
            xDiff=76.3
            yDiff=75
            return (1161+int(index%4*xDiff),369+int(index/4)*yDiff)

        for x in range(6): 
            while(self.uwtask.isPositionColorSimilarTo(39,135,(184, 0, 0)) or self.uwtask.isPositionColorSimilarTo(112,127,(219,29,36))):
                print("foe's turn, wait for 5s")
                time.sleep(5)
            if(self.uwtask.isPositionColorSimilarTo(1182,830,(59,59,59))):
                wait(lambda: self.instance.clickPointV2(*waitPos),3)
                continue
            number=self.uwtask.getNumberFromSingleLineInArea(A=[33,118,48,136])
            match number:
                case 1:
                    #No 1 Pao Buff
                    wait(lambda: self.instance.longerClickPointV2(*expressskill),0.5)    

                    #wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    #wait(lambda: self.instance.clickPointV2(1260,332),0.5)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),3,0.5)
                    time.sleep(5)
                case 2:
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)
                    #No 2 

                    # wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    # wait(lambda: self.instance.clickPointV2(*getSkillPosByIndex(8)),0.5)
                    # doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    # time.sleep(5)
                case 3:
                    #open skill #No3 ram buff
                    # wait(lambda: self.instance.clickPointV2(*waitPos),3)
                    wait(lambda: self.instance.clickPointV2(*expressskill),0.5)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),3,0.5)
                    time.sleep(2)
                    # wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    # wait(lambda: self.instance.clickPointV2(*getSkillPosByIndex(6)),0.5)
                    # doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    # time.sleep(3)

                case 4:
                    #5  melee Buff
                    # wait(lambda: self.instance.clickPointV2(*waitPos),3)

                    # wait(lambda: self.instance.clickPointV2(*openSkillPos),0.5)
                    # wait(lambda: self.instance.clickPointV2(*openSkilltab),0.5)
                    # wait(lambda: self.instance.clickPointV2(1272,408),0.5)
                    wait(lambda: self.instance.clickPointV2(*expressskill),0.5)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),3,0.5)
                    time.sleep(4)
                case 5:
                    #5  #ATK 
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)
                    # wait(lambda: self.instance.clickPointV2(*expressskill),0.5)
                    # doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    # time.sleep(2)

                case 6:
                    #open skill 
                    # wait(lambda: self.instance.clickPointV2(*waitPos),3)
                    wait(lambda: self.instance.clickPointV2(*expressskill),0.5)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    time.sleep(2)

                case 7:
                    # DEF
                    wait(lambda: self.instance.clickPointV2(*expressskill),0.5)
                    doMoreTimesWithWait(lambda: self.instance.longerClickPointV2(*centralPos),2,0.5)
                    time.sleep(2)
                case _:
                    wait(lambda: self.instance.clickPointV2(*waitPos),3)
        
        continueWithUntilBy(lambda: self.instance.clickPointV2(825+randomInt(),863+randomInt()), lambda: not self.uwtask.isPositionColorSimilarTo(1374,106,(235, 235, 235)),2)
        time.sleep(15)
        number=self.uwtask.getNumberFromSingleLineInArea(A=[1209,96,1237,112])
        if(type(number) == int and number>30):
            wait(lambda: self.instance.clickPointV2(825+randomInt(),863+randomInt()),0.5)

        continueWithUntilBy(lambda: self.instance.rightClickPointV2(*self.randomPoint),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=self.battleEnd["okBtn"]) or self.uwtask.hasSingleLineWordsInArea("close", A=self.battleEnd["okBtn"]) or self.uwtask.hasSingleLineWordsInArea("discard", A=[679,667,757,682]) or self.uwtask.inCityList(self.uwtask.allCityList),5,timeout=480)
        def backupFunc():
            exitBattle()
            if(self.uwtask.hasSingleLineWordsInArea("defeat",A=[1078,781,1162,807])):
                wait(lambda: self.instance.clickPointV2(1097,798),10)
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(859,497),2,3)
                wait(lambda: self.instance.clickPointV2(781,663),60)
            self.uwtask.checkForDailyPopup()
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),5,3)

        def exitBattle():
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(723,673),3,2)
            if(self.uwtask.hasSingleLineWordsInArea("ok",A=[756,597,804,620])):
                wait(lambda: self.instance.clickPointV2(632,566),2)
                wait(lambda: self.instance.clickPointV2(777,607),2)
        doAndWaitUntilBy(lambda: exitBattle(),lambda: self.uwtask.inWater(),5,2,backupFunc=backupFunc)
        time.sleep(1)
        self.uwtask.checkForDailyPopup(4)
        if(not self.uwtask.inWater()):
            doAndWaitUntilBy(lambda: self.instance.rightClickPointV2(*self.randomPoint),lambda: self.uwtask.inWater(),1,1)

    def test(self):
        continueWithUntilBy(lambda: self.instance.clickPointV2(825+randomInt(),863+randomInt()), lambda: not self.uwtask.isPositionColorSimilarTo(1374,106,(235, 235, 235)),2)

    def checkStats(self,town):
        time.sleep(1)
        # 0 SHIP DOWN OR 0 SAILORS
        if(self.uwtask.isPositionColorSimilarTo(241,69,(246,219,37)) or self.uwtask.isPositionColorSimilarTo(234,69,(250,234,94))):
            self.goBackPort(town)
            return False
        return True

    def checkInPort(self,town):
        now=datetime.now()
        if(getTimeDiffInSeconds(self.lastCallTime,now)>1800):
            if(now.minute>=30):
                self.uwtask.healInjury(town)
            # if(self.uwtask.tradeRouteBuyFin==False):
            #    self.uwtask.buyInCity([town], products=["agarwood","ylang-ylang","mace","chinesetea","gardenia","begonia","sweetolive","azalea","ginseng","doenjang","lris"],marketMode=1)
            self.lastCallTime=now

    def selectOpponentInList(self,opponentsInList):
        firstPosi=(1286,344)
        area=[1236,326,1362,345]
        #5TH AREA
        # 1232,601,1399,629
        index=0
        while(index<15):
            yDiff=int(index%11*56.2)
            index+=1
            ocrName=self.uwtask.getSingleLineWordsInArea(A=[area[0], area[1]+yDiff, area[2], area[3]+yDiff],debug=False)
            hasName=hasOneArrayStringSimilarToString(ocrName,opponentsInList) and not hasOneArrayStringSimilarToString(ocrName,blackListForBattle)

            if(hasName):
                wait(lambda: self.instance.fastClickPointV2(firstPosi[0],firstPosi[1]+yDiff),0.5,disableWait=True)
                if(self.uwtask.hasSingleLineWordsInArea("pirate", A=[667,831,787,855])):
                    wait(lambda: self.instance.clickPointV2(39,695),0)
                    continue
                else:
                    time.sleep(1)
                    if(self.uwtask.hasSingleLineWordsInArea("pirate", A=[1187,129,1396,159]) and not self.uwtask.hasSingleLineWordsInArea("ruthless", A=[1187,129,1396,159])):
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
            time.sleep(10)
            wait(lambda: self.uwtask.findCityAndClick(targetCity),40)
            doMoreTimesWithWait(lambda: self.instance.rightClickPointV2(*self.randomPoint),4,10)
        
        continueWithUntilByWithBackup(lambda: inJourneyTask(), lambda: self.uwtask.inCityList(cityList), 1, timeout=80,notifyFunc=lambda: self.uwtask.print("not found, wait for 4s"),backupFunc=backupFunc)
        self.uwtask.print("click twice")
        self.uwtask.clickEnterCityButton()

    def depart(self):
        firstLineArrowBtn=1401,500
        okBtn=752,607
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
        if(self.uwtask.hasSingleLineWordsInArea("crewsize",A=[1200,490,1276,514])):
            crewWords=self.uwtask.getSingleLineWordsInArea(A=[1273,492,1374,513],ocrType=2)

            actualCrew=getNumberFromString(crewWords.split("/")[0])
            maxCrew=getNumberFromString(crewWords.split("/")[1])
            if(actualCrew/maxCrew<0.97):
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(*firstLineArrowBtn),lambda: self.uwtask.hasSingleLineWordsInArea("recruit", A=self.uwtask.titleArea), 1,2)
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(1333,410),2,0)                
                wait(lambda: self.instance.longerClickPointV2(1350,526),2)
                wait(lambda: self.instance.clickPointV2(*okBtn),1)
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(*okBtn),lambda: self.uwtask.hasSingleLineWordsInArea("harbor", A=self.uwtask.titleArea), 1,2,backupFunc=lambda: self.instance.clickPointV2(*self.uwtask.leftTopBackBtn),timeout=10)

        self.uwtask.print("出海")
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*departBtn), lambda: self.uwtask.inWater(), 4,2, backupFunc=clickAndStockBackup,timeout=30)
        time.sleep(2)
        self.uwtask.checkForDailyPopup(3)

    def backupFromDashboardToSea(self):
        wait(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon),1)
        self.uwtask.checkForBasicStuck()

    def goBackPort(self, town):
        def backup():
            if(self.uwtask.hasSingleLineWordsInArea("result",A=[726,230,823,262])):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(723,673),3,2)
                if(self.uwtask.hasSingleLineWordsInArea("ok",A=[756,597,804,620])):
                    wait(lambda: self.instance.clickPointV2(632,566),2)
                    wait(lambda: self.instance.clickPointV2(777,607),2)
        if(self.uwtask.hasSingleLineWordsInArea("huamei", A=self.nameBoardInPrePanel)):
            doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inWater(),1,1)
        wait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),0)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint2),lambda: self.uwtask.inWater(),1,1,backupFunc=self.backupFromDashboardToSea,timeout=10)
        wait(lambda: self.uwtask.findCityAndClick(town,noExpect=True,backup=backup),0)
        self.quickWaitForCity([town],targetCity=town)
        self.opentimeout=0

    def leavePort(self):
        doMoreTimesWithWait(lambda: self.instance.rightClickPointV2(*self.randomPoint),2,1)
        self.uwtask.goToHarbor()
        self.depart()
        if(getHour() in [21,22,23,24,0,1,2]):
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(39,695),2,4)

    def findOpponentOrReturn(self,opponentsInList,opponents,town):
        wait(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint3),0)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightCatePoint3),lambda: self.uwtask.inWater(),1,1,backupFunc=self.backupFromDashboardToSea,timeout=10)
        clickedOpponentInList=self.selectOpponentInList(opponentsInList)
        if(not clickedOpponentInList):
            self.uwtask.print("no foe,return port")
            self.goBackPort(town)
            return False
        timeout=20
        combatScreenOpened=self.uwtask.hasSingleLineWordsInArea("huamei", A=self.nameBoardInPrePanel)
        if(not combatScreenOpened):
            wait(lambda: False,1)
        while(timeout>0 and not combatScreenOpened):
            if(self.uwtask.hasSingleLineWordsInArea("huamei", A=self.nameBoardInPrePanel)):
                break
            if(self.uwtask.checkStopped()):
                return self.findOpponentOrReturn(opponentsInList,opponents,town)
            timeout-=1
            wait(lambda: False,1)
        if(timeout==0):
            wait(lambda: self.instance.clickPointV2(720,862),2)
            if(self.uwtask.hasSingleLineWordsInArea("huamei", A=self.nameBoardInPrePanel)):
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inWater(),1,1)
            return self.findOpponentOrReturn(opponentsInList,opponents,town)

        def clickIntoBattle():
            self.instance.clickPointV2(683,829)
            # for small boss, enable only when required. Might cause stop of ship as 2nd click clicks after screen goes to sea.
            # self.instance.clickPointV2(726,820)

        if(self.uwtask.hasArrayStringInSingleLineWords(opponents, A=[1187,129,1396,159])): #and not self.uwtask.hasSingleLineWordsInArea("pirate",A=[1187,129,1396,159])):
            self.uwtask.print("opened")
            return continueWithUntilBy(lambda: clickIntoBattle(),lambda: self.uwtask.hasSingleLineWordsInArea("combat", A=[684,15,746,32]),3,timeout=10)
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inWater(), 1,30)
        self.opentimeout+=1
        if(self.opentimeout>2):
            self.goBackPort(town)
            return False
        return self.findOpponentOrReturn(opponentsInList,opponents,town)
        