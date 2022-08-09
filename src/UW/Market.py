from guiUtils import win
from utils import *
import os
# from UWTask import UWTask


coinPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"coinInBuy"+".bmp")

class Market:
    randonPoint=851,618
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
    #priceAreaSlot1: [337,203,388,221]
    #priceAreaSlot6: [860,334,905,352]
    #xDiff 437.5
    #yDiff 472
    #move by slot and choose wisely to buy
    def buyV2(self):
        index=0
        end=False
        buyList=[]

        doAndWaitUntilBy(lambda: self.instance.clickPointV2(62,89), lambda: self.uwtask.hasSingleLineWordsInArea("purch", A=self.uwtask.titleArea), 2,2)        

        #Loop through and find what can be bought
        while (index<12 and end==False):
            xDiff=int(index%3*261.5)
            yDiff=int(index/3)*131
            index+=1
            #print([176+xDiff,200+yDiff,286+xDiff,235+yDiff])
            #red check area 260,203,346,221
            if(self.uwtask.hasSingleLineWordsInArea("unlock", A=[260+xDiff,203+yDiff,346+xDiff,221+yDiff])):
                continue
            #244,219,280,237
            # print([340+xDiff,203+yDiff,391+xDiff,221+yDiff])
            price = self.uwtask.getNumberFromSingleLineInArea(A=[340+xDiff,203+yDiff,391+xDiff,221+yDiff])
            #269,137,326,155
            #logic re food type
            if(self.uwtask.hasSingleLineWordsInArea("food", A=[269+xDiff,137+yDiff,326+xDiff,155+yDiff]) and price>200):
                continue
            if(not(price)):
                continue
            buyList.append((index-1, price))

        #sort by price high to low
        buyList=sorted(buyList, key=lambda student: student[1], reverse=True)
        print(buyList)

        #Click from list and buy
        for buyObj in buyList:
            if(self.uwtask.hasSingleLineWordsInArea("max", A=[1073,126,1137,145])):
                break
            index=buyObj[0]
            xDiff=int(index%3*261.5)
            yDiff=int(index/3)*131
            self.uwtask.print("buy item "+str(index))
            wait(lambda: self.instance.clickPointV2(337+xDiff,206+yDiff),0.2)
        
        wait(lambda: self.instance.clickPointV2(1212,693),1)
        wait(lambda: self.instance.clickPointV2(725,617),5)
        self.bargin()
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randonPoint),3,1) 
        self.uwtask.print("buy fin")

    def sellV3(self):
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(47,149), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=self.uwtask.titleArea),2,2)
        #xDiff 261
        #yDiff 131      
        index=0
        #Loop through and find what can be bought
        self.uwtask.print("sell items")
        while (index<9):
            xDiff=int(index%3*261)
            yDiff=int(index/3)*130
            index+=1
            # print([322+xDiff,204+yDiff,382+xDiff,218+yDiff])
            if(self.uwtask.hasSingleLineWordsInArea("-", A=[322+xDiff,204+yDiff,382+xDiff,218+yDiff], ocrType=2)):
                continue
            wait(lambda: self.instance.clickPointV2(330+xDiff,210+yDiff),0.2)
        wait(lambda: self.instance.clickPointV2(1212,693),1)
        wait(lambda: self.instance.clickPointV2(725,617),5)
        self.bargin()
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randonPoint),3,1) 
        self.uwtask.print("sell fin")

    def bargin(self):
            #sell area
            #846,648,1095,690
            #buy area
            #825,647,1095,690
            #try wider
        if(self.uwtask.hasSingleLineWordsInArea("yes", A=[813,616,1149,662])):
            time.sleep(2)
            #click yes
            wait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),15)
            #wait for dialog, click no regardless of successful.
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(895,570),3, 2)