from guiUtils import win
from utils import *
import os
# from UWTask import UWTask

marketBuyData={
    "kokkola":["amber"],
    "saint":["chrysoberyl","tourmaline"],
    "gdansk":["tourmaline","amber"],
    "copenhagen":["amber","chrysoberyl"],
    "oslo":["flax","feather"],
    # "kokkola":[""],
    "montpel":["garnet"],
    "marseille":["garnet","etchings","cannon","bronzeStatue","perfume"],
    "genoa":["glasswork","oilPainting","etchings","cannon"],
    "pisa":["marbleStatue","cannon"],
    "sasari":["garnet"],
}
coinPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"coinInBuy"+".bmp")

class Market:
    randomPoint=851,618
    buySellWholeArea=[187,99,949,395]
    maxArea=[1073,126,1137,145]
    # def __init__(self, instance: win, uwtask:UWTask) -> None:
    def __init__(self, instance: win, uwtask) -> None:
        self.instance=instance
        self.uwtask=uwtask

    #             x   y    x   y
    #priceAreaSlot1: [337,203,388,221]
    #priceAreaSlot6: [860,334,905,352]
    #xDiff 437.5
    #yDiff 472
    #move by slot and choose wisely to buy
    def buyExpensive(self):
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
            # print([338+xDiff,203+yDiff,389+xDiff,221+yDiff])
            price = self.uwtask.getNumberFromSingleLineInArea(A=[338+xDiff,203+yDiff,389+xDiff,221+yDiff])
            #269,137,326,155
            #logic re food type
            if(not(price)):
                continue
            if(price>300 and self.uwtask.hasSingleLineWordsInArea("food", A=[269+xDiff,137+yDiff,326+xDiff,155+yDiff])):
                continue

            buyList.append((index-1, price))

        #sort by price high to low
        buyList=sorted(buyList, key=lambda student: student[1], reverse=True)
        print(buyList)

        #Click from list and buy
        for buyObj in buyList:
            if(self.uwtask.hasSingleLineWordsInArea("max", A=self.maxArea)):
                break
            index=buyObj[0]
            xDiff=int(index%3*261.5)
            yDiff=int(index/3)*131
            self.uwtask.print("buy item "+str(index))
            wait(lambda: self.instance.clickPointV2(337+xDiff,206+yDiff),0.2,disableWait=True)
        
        wait(lambda: self.instance.clickPointV2(1212,693),1)
        wait(lambda: self.instance.clickPointV2(725,617),5)
        self.bargin()
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,0)
        self.uwtask.print("buy fin")

    def sellGoodsWithMargin(self):
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(47,149), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=self.uwtask.titleArea),2,2)
        #xDiff 261
        #yDiff 131
        index=0
        #Loop through and find what can be bought
        self.uwtask.print("sell items")
        while (index<13):
            xDiff=int(index%3*261)
            yDiff=int(index/3)*130
            index+=1
            # print([318+xDiff,206+yDiff,398+xDiff,226+yDiff]])
            if(self.uwtask.hasSingleLineWordsInArea("-", A=[318+xDiff,206+yDiff,398+xDiff,226+yDiff], ocrType=2)):
                continue
            wait(lambda: self.instance.clickPointV2(330+xDiff,210+yDiff),0.2,disableWait=True)
        wait(lambda: self.instance.clickPointV2(1212,693),1)
        wait(lambda: self.instance.clickPointV2(725,617),5)
        self.bargin()
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,0)
        gemLocation= self.uwtask.hasImageInScreen("gemBeforeMoney", A=[941,7,1095,41])
        moneyScanArea=[gemLocation[0]-159,gemLocation[1],gemLocation[0]-5,gemLocation[1]+30] if gemLocation else [833,8,1000,41]
        savingOcr=self.uwtask.getSingleLineWordsInArea(A=moneyScanArea,ocrType=2)
        self.uwtask.sendMessage("UW","current saving is: "+(savingOcr if savingOcr else "undefined"))
        self.uwtask.print("sell fin")

    def buyProductsInMarket(self,products):
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(62,89), lambda: self.uwtask.hasSingleLineWordsInArea("purch", A=self.uwtask.titleArea), 2,2)
        print(products)
        boughtTick=0

        #xDiff 261
        #yDiff 131
        index=0
        #Loop through and find what can be bought
        self.uwtask.print("buy items")
        while (index<9):
            xDiff=int(index%3*261)
            yDiff=int(index/3)*130
            index+=1
            #print([176+xDiff,200+yDiff,286+xDiff,235+yDiff])
            #red check area 260,203,346,221
            if(self.uwtask.hasSingleLineWordsInArea("unlock", A=[260+xDiff,203+yDiff,346+xDiff,221+yDiff])):
                continue   
            productName=self.uwtask.getSingleLineWordsInArea(A=[267+xDiff,114+yDiff,381+xDiff,137+yDiff])
            if(not(productName)):
                continue
            if(hasOneArrayStringInStringAndNotVeryDifferent(productName, products)):
                wait(lambda: self.instance.clickPointV2(330+xDiff,210+yDiff),0.2,disableWait=True)
                boughtTick+=1   
            #check if max, notify buyFin for master class   
            if(self.uwtask.hasSingleLineWordsInArea("max", A=self.maxArea)):
                self.uwtask.tradeRouteBuyFin=True
                break

        wait(lambda: self.instance.clickPointV2(1212,693),1)
        wait(lambda: self.instance.clickPointV2(725,617),5)
        self.bargin()
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,0)
        self.uwtask.print("buy fin")
        return boughtTick

    def buyProductsInCityTwice(self,products):
        boughtTick=self.buyProductsInMarket(products)
        if(self.uwtask.tradeRouteBuyFin):
            return
        if(boughtTick==0):
            return

        while(True):
            if(int(self.uwtask.getNumberFromSingleLineInArea(A=[818,76,836,95]))>27):
                break
            else:
                time.sleep(60)
                wait(lambda: self.instance.clickPointV2(*self.randomPoint),3)


        self.buyProductsInMarket(products)



    def bargin(self):
            #sell area
            #846,648,1095,690
            #buy area
            #825,647,1095,690
            #try wider 
        if(self.uwtask.hasSingleLineWordsInArea("es", A=[902,615,1100,658])):
            time.sleep(1)
            #click yes
            wait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),2)
            #wait for dialog, click no regardless of successful.
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(895,570),3, 0.5)
