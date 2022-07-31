from guiUtils import win
from utils import *
import os
# from UWTask import UWTask


coinPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"coinInBuy"+".bmp")

class Market:
    # def __init__(self, instance: win, uwtask:UWTask) -> None:
    def __init__(self, instance: win, uwtask) -> None:

        self.instance=instance
        self.uwtask=uwtask
    
    def buyV1(self):
        count=11
        wait(lambda: self.instance.clickPointV2(54,88),1)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(54,88), lambda: self.uwtask.hasSingleLineWordsInArea("purch", A=[54,17,142,55]), 1)        
        while(count>0):
            if(self.uwtask.hasSingleLineWordsInArea("max", A=[1212,126,1265,139])):
                break
            position=self.instance.window_capture_v2(coinPath, A=[172,99,1192,370])
            count-=1
            if(position):
                self.uwtask.print("buy item x")
                wait(lambda: self.instance.clickPointV2(position[0], position[1]),0.2)  
                wait(lambda: self.instance.clickPointV2(1398,808),1)
                wait(lambda: self.instance.clickPointV2(809,658))
                self.uwtask.bargin()
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(809,658),3,1) 

    def sellV1(self):
        count=11
        wait(lambda: self.instance.clickPointV2(44,144),1)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(44,144), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=[54,17,142,55]), 1)
        while(count>0):
            position=self.instance.window_capture_v2(coinPath, A=[172,99,1192,370])
            if(self.uwtask.hasSingleLineWordsInArea("noitemtosell", A=[623,444,737,469])):
                break
            else:
                self.uwtask.print("sell item x")
                count-=1
                wait(lambda: self.instance.clickPointV2(position[0], position[1]),0.2)
                if(self.uwtask.hasSingleLineWordsInArea("-", A=[1401,761,1469,782], ocrType=2)):
                    self.uwtask.clickWithImage("crossInSell", A=[1203,94,1274,131])
                    continue  
                wait(lambda: self.instance.clickPointV2(1398,808),1)
                wait(lambda: self.instance.clickPointV2(809,658))
                self.uwtask.bargin()
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(809,658),3,1)     


    #             x   y    x   y
    #priceAreaSlot1: [222,221,288,235]
    #priceAreaSlot12: [861,366,928,380]
    #xDiff 127.8
    #yDiff 145
    #move by slot and choose wisely to buy
    def buyV2(self):
        index=0
        end=False
        buyList=[]

        wait(lambda: self.instance.clickPointV2(54,88),1)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(54,88), lambda: self.uwtask.hasSingleLineWordsInArea("purch", A=self.uwtask.titleArea), 2,2)        

        #Loop through and find what can be bought
        while (index<12 and end==False):
            xDiff=int(index%6*127.8)
            yDiff=(0 if (index<6) else 1)*145
            index+=1
            #print([176+xDiff,200+yDiff,286+xDiff,235+yDiff])
            #red check area 200,219,222,238
            if(self.uwtask.hasImageInScreen("redLock", A=[200+xDiff,219+yDiff,222+xDiff,238+yDiff])):
                continue
            #244,219,280,237
            #special rule for coin xx 2 digit price
            price = self.uwtask.getNumberFromSingleLineInArea(A=[244+xDiff,220+yDiff,290+xDiff,238+yDiff])
            if(str(price)[0]=="9" and len(str(price))==3):
                continue
            if(not(price)):
                continue
            buyList.append((index-1, price))

        #sort by price high to low
        buyList=sorted(buyList, key=lambda student: student[1], reverse=True)
        print(buyList)

        #Click from list and buy
        for buyObj in buyList:
            if(self.uwtask.hasSingleLineWordsInArea("max", A=[975,125,1038,138])):
                break
            index=buyObj[0]
            xDiff=int(index%6*127.8)
            yDiff=(0 if (index<6) else 1)*145
            self.uwtask.print("buy item "+str(index))
            wait(lambda: self.instance.clickPointV2(247+xDiff,226+yDiff),0.2)
        
        wait(lambda: self.instance.clickPointV2(1168,724),1)
        wait(lambda: self.instance.clickPointV2(710,631),5)
        self.bargin()
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(645,626),3,1) 
        self.uwtask.print("buy fin")

    def sellV3(self):
        wait(lambda: self.instance.clickPointV2(44,144),1)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(44,144), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=self.uwtask.titleArea),2,2)
        #xDiff 127.8
        #yDiff 145        
        index=0
        #Loop through and find what can be bought
        self.uwtask.print("sell items")
        while (index<9):
            xDiff=int(index%6*127.8)
            yDiff=int(index/6)*145
            index+=1
            if(self.uwtask.hasSingleLineWordsInArea("-", A=[222+xDiff,221+yDiff,288+xDiff,235+yDiff], ocrType=2)):
                continue
            wait(lambda: self.instance.clickPointV2(222+xDiff,221+yDiff),0.2)
        wait(lambda: self.instance.clickPointV2(1168,724),1)
        wait(lambda: self.instance.clickPointV2(710,631),5)
        self.bargin()
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(645,626),3,1) 
        self.uwtask.print("sell fin")

    def bargin(self):
            #sell area
            #846,648,1095,690
            #buy area
            #825,647,1095,690
            #try wider
        if(self.uwtask.hasSingleLineWordsInArea("yes", A=[825,648,1095,690])):
            time.sleep(2)
            #click yes
            wait(lambda: self.instance.clickPointV2(962,667),15)
            #wait for dialog, click no regardless of successful.
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(956,603),3, 2)