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
        wait(lambda: self.instance.click_point(54,88),1)
        doAndWaitUntilBy(lambda: self.instance.click_point(54,88), lambda: self.uwtask.hasSingleLineWordsInArea("purch", A=[54,17,142,55]), 1)        
        while(count>0):
            if(self.uwtask.hasSingleLineWordsInArea("max", A=[1212,126,1265,139])):
                break
            position=self.instance.window_capture_v2(coinPath, A=[172,99,1192,370])
            count-=1
            if(position):
                self.uwtask.print("buy item x")
                wait(lambda: self.instance.click_point(position[0], position[1]),0.2)  
                wait(lambda: self.instance.click_point(1398,808),1)
                wait(lambda: self.instance.click_point(809,658))
                self.uwtask.bargin()
                doMoreTimesWithWait(lambda: self.instance.click_point(809,658),3,1) 

    def sellV1(self):
        count=11
        wait(lambda: self.instance.click_point(40,146),1)
        doAndWaitUntilBy(lambda: self.instance.click_point(40,146), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=[54,17,142,55]), 1)
        while(count>0):
            position=self.instance.window_capture_v2(coinPath, A=[172,99,1192,370])
            if(self.uwtask.hasSingleLineWordsInArea("noitemtosell", A=[623,444,737,469])):
                break
            else:
                self.uwtask.print("sell item x")
                count-=1
                wait(lambda: self.instance.click_point(position[0], position[1]),0.2)
                if(self.uwtask.hasSingleLineWordsInArea("-", A=[1401,761,1469,782], ocrType=2)):
                    self.uwtask.clickWithImage("crossInSell", A=[1203,94,1274,131])
                    continue  
                wait(lambda: self.instance.click_point(1398,808),1)
                wait(lambda: self.instance.click_point(809,658))
                self.uwtask.bargin()
                doMoreTimesWithWait(lambda: self.instance.click_point(809,658),3,1)     


    #             x   y    x   y
    #slot1Area: [176,200,286,235]
    #slot9Area: [1075,205,1188,232]
    #slot18Area: [1075,336,1188,363]
    #priceOnlySlot#1: [223,210,252,223]
    #move by slot and choose wisely to buy
    def buyV2(self):
        index=0
        end=False
        buyList=[]

        wait(lambda: self.instance.click_point(54,88),1)
        doAndWaitUntilBy(lambda: self.instance.click_point(54,88), lambda: self.uwtask.hasSingleLineWordsInArea("purch", A=[54,17,142,55]), 1)        

        #Loop through and find what can be bought
        while (index<15 and end==False):
            xDiff=int(index%9*112.3)
            yDiff=(0 if (index<9) else 1)*131
            index+=1
            #print([176+xDiff,200+yDiff,286+xDiff,235+yDiff])
            if(self.uwtask.hasImageInScreen("redLock", A=[176+xDiff,200+yDiff,286+xDiff,235+yDiff])):
                continue
            price = self.uwtask.getNumberFromSingleLineInArea(A=[233+xDiff,212+yDiff,262+xDiff,225+yDiff])
            if(not(price)):
                continue
            buyList.append((index-1, price))

        #sort by price high to low
        buyList=sorted(buyList, key=lambda student: student[1], reverse=True)
        print(buyList)

        #Click from list and buy
        for buyObj in buyList:
            if(self.uwtask.hasSingleLineWordsInArea("max", A=[1212,126,1265,139])):
                break
            index=buyObj[0]
            xDiff=int(index%9*112.3)
            yDiff=(0 if (index<9) else 1)*131
            self.uwtask.print("buy item "+str(index))
            wait(lambda: self.instance.click_point(228+xDiff,218+yDiff),0.2)
        
        wait(lambda: self.instance.click_point(1398,808),1)
        wait(lambda: self.instance.click_point(809,658))
        self.uwtask.bargin()
        doMoreTimesWithWait(lambda: self.instance.click_point(809,658),3,1)  
        self.uwtask.print("buy fin")
           
    def sellV2(self):
        wait(lambda: self.instance.click_point(40,146),1)
        doAndWaitUntilBy(lambda: self.instance.click_point(40,146), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=[54,17,142,55]), 1)

        moveIndex=0
        moveEnd=False
        #Move ocr slot from 0 to 5 if cant sell in slot 0
        while(moveIndex<6 and moveEnd==False):
            xDiff=int(moveIndex%9*112.3)
            moveIndex+=1
            #in slot index, sell continuesly until all sold/red price
            while(True):
                if(self.uwtask.hasSingleLineWordsInArea("noitemtosell", A=[623,444,737,469])):
                    moveEnd=True
                    break
                self.uwtask.print("sell item x")
                wait(lambda: self.instance.click_point(228+xDiff,218),0.2)
                if(self.uwtask.hasSingleLineWordsInArea("-", A=[1401,761,1469,782], ocrType=2)):
                    self.uwtask.clickWithImage("crossInSell", A=[1203,94,1274,131])
                    break
                wait(lambda: self.instance.click_point(1398,808),1)
                wait(lambda: self.instance.click_point(809,658))
                self.uwtask.bargin()
                doMoreTimesWithWait(lambda: self.instance.click_point(809,658),3,1)    
        self.uwtask.print("sell fin")

    def sellV3(self):
        wait(lambda: self.instance.click_point(40,146),1)
        doAndWaitUntilBy(lambda: self.instance.click_point(40,146), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=[54,17,142,55]), 1)
        
        index=0
        #Loop through and find what can be bought
        self.uwtask.print("sell items")
        while (index<9):
            xDiff=int(index%9*112.3)
            index+=1
            if(self.uwtask.hasSingleLineWordsInArea("-", A=[217+xDiff,210,275+xDiff,224], ocrType=2)):
                continue
            wait(lambda: self.instance.click_point(228+xDiff,218),0.2)
        wait(lambda: self.instance.click_point(1398,808),1)
        wait(lambda: self.instance.click_point(809,658))
        self.uwtask.bargin()
        doMoreTimesWithWait(lambda: self.instance.click_point(809,658),3,1) 
        self.uwtask.print("sell fin")