from guiUtils import win
from utils import *
import os
import json
from datetime import date

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

hasBMCities=["kokkola","saint","stockhol","visby","beck","copenhag","oslo","hamburg","bremen","amsterda","london","antwerp","calais","plymouth",
"bristol","dublin","nantes","bordeau","porto","lisboa","faro","seville","ceuta","laga","bathurst","elmina","luanda","cape","sofala","mozambiqu",
"zanzibar","manbasa","hadiboh","aden","jeddah","muscat","hormuz","basrah","baghdad","goa","kozhikod",
"algiers","valencia","barcelona","montpellie","marseille","geona","pisa","calvi","tunis","syracuse","ragusa",
"alexandria","cairo","candia","athens","thessaloni","constantino"]
capitals=["london","amsterda","lisboa","seville","constantino"]
coinPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"coinInBuy"+".bmp")

class Market:
    randomPoint=851,618
    buySellWholeArea=[187,99,949,395]
    maxArea=[1073,126,1137,145]
    today = date.today().strftime("%d-%m-%Y")

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

    def sellGoodsWithMargin(self,simple=False,types=None):
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(47,149), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=self.uwtask.titleArea),2,2)
        def sellItemsInScreen():
            #Loop through and find what can be bought
            #xDiff 261
            #yDiff 131
            index=0
            while (index<13):
                xDiff=int(index%3*261)
                yDiff=int(index/3)*130
                index+=1
                if(simple==False):
                    # print([318+xDiff,206+yDiff,398+xDiff,226+yDiff]])
                    if(self.uwtask.hasSingleLineWordsInArea("-", A=[318+xDiff,206+yDiff,398+xDiff,226+yDiff], ocrType=2)):
                        continue
                if(isArray(types)):
                    typeOcr=self.uwtask.getSingleLineWordsInArea(A=[271+xDiff,137+yDiff,333+xDiff,155+yDiff])
                    if(hasOneArrayStringInStringAndNotVeryDifferent(typeOcr,types)):
                        wait(lambda: self.instance.clickPointV2(330+xDiff,210+yDiff),0.2,disableWait=True)
                if(types == None):
                    wait(lambda: self.instance.clickPointV2(330+xDiff,210+yDiff),0.2,disableWait=True)
            wait(lambda: self.instance.clickPointV2(1212,693),1)
            wait(lambda: self.instance.clickPointV2(725,617),5)
            self.bargin()
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,0)

        self.uwtask.print("sell items")
        sellItemsInScreen()
        if(not(self.uwtask.hasSingleLineWordsInArea("noitemstosell", A=[491,387,688,415]))):
            sellItemsInScreen()

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
            productName=self.uwtask.getSingleLineWordsInArea(A=[267+xDiff,114+yDiff,419+xDiff,137+yDiff])
            if(not(productName)):
                continue
            if(hasOneArrayStringInStringAndNotVeryDifferent(productName, products)):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(330+xDiff,210+yDiff),2,0.2,disableWait=True)
                boughtTick+=1   
            #check if max, notify buyFin for master class   
            if(self.uwtask.hasSingleLineWordsInArea("max", A=self.maxArea)):
                self.uwtask.tradeRouteBuyFin=True
                break

        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1212,693),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[698,607,737,624]),1,1)
        wait(lambda: self.instance.clickPointV2(725,617),1)
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
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(895,570),6, 0.5)

    def shouldBuyBlackMarket(self,city):
        with open('src/UW/blackMarket.json', 'r') as f:
            boughtCities = json.load(f)
        if((city in hasBMCities) and (city not in boughtCities)):
            return True

    def buyInBlackMarket(self,city):
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(94,209), lambda: self.uwtask.hasSingleLineWordsInArea("blackmarket", A=self.uwtask.titleArea),2,1)

        #must rule  rosewood must,
        #ducat rule  value >400000 no, 
        #else gem
        def clickBuy(x,y):
            wait(lambda: self.instance.clickPointV2(x,y),0.2,disableWait=True)
            wait(lambda: self.uwtask.clickWithImage("calculator", A=[732,454,793,530]),0)
            wait(lambda: self.instance.clickPointV2(907,502),0.2,disableWait=True)
            wait(lambda: self.instance.clickPointV2(1006,470),0.2,disableWait=True)
            #quick purchase
            wait(lambda: self.instance.clickPointV2(737,599),1)
            if(self.uwtask.hasSingleLineWordsInArea("purchase", A=[613,236,699,258])):
                wait(lambda: self.instance.clickPointV2(719,482))
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(94,209),2,0.2,disableWait=True)

        index=0
        self.uwtask.print("buy BM items")
        while (index<12):
            xDiff=int(index%3*262)
            yDiff=int(int(index/3)*130.5)
            index+=1
            productName=self.uwtask.getSingleLineWordsInArea(A=[268+xDiff,113+yDiff,449+xDiff,136+yDiff])
            if(not(productName)):
                continue 
            if("rose" in productName):# or "intermediatetrade" in productName):
                clickBuy(319+xDiff,184+yDiff)
                continue
            gemAreaOCR=self.uwtask.getNumberFromSingleLineInArea(A=[302+xDiff,203+yDiff,327+xDiff,228+yDiff])
            if(self.uwtask.hasImageInScreen("gemInBM2",A=[302+xDiff,203+yDiff,327+xDiff,228+yDiff]) and
            (not gemAreaOCR or gemAreaOCR==0)):
                #Gem case
                if("enhancedmedium" in productName and "special" not in productName):
                    clickBuy(319+xDiff,184+yDiff)
                continue
            else:
                #Ducat case
                price=self.uwtask.getNumberFromSingleLineInArea(A=[275+xDiff,208+yDiff,384+xDiff,225+yDiff])
                if("keel" in productName or "superior" in productName):
                    continue
                if(price and price>31):
                    clickBuy(319+xDiff,184+yDiff)
        screenshotBlob = self.instance.outputWindowScreenshotV2()
        self.uwtask.saveImageToFile(screenshotBlob, relaPath="\\..\\..\\assets\\screenshots\\UW\\"+self.today,filename=city+".jpg")
    
    def buyBlackMarket(self,city):
        def getTime():
            try:
                timeOCR=self.uwtask.getSingleLineWordsInArea(A=[1255,213,1296,232], ocrType=2)
                return int(timeOCR[0:2])
            except Exception as e:
                print(e)    
                return 12

        def recursiveVisitBM():
                while(getTime()>5 and getTime()<20):
                    time.sleep(30)
                if(not self.uwtask.clickInMenu("temshop","temshop")):
                    return
                if(not self.uwtask.hasSingleLineWordsInArea("black", A=[23,193,141,225])):
                    doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.inCityList([city]), 3,2)
                    time.sleep(15)
                    recursiveVisitBM()

        if(city in capitals):
            self.uwtask.clickInMenu("temshop","temshop")
        else:
            recursiveVisitBM()
        if(self.uwtask.hasSingleLineWordsInArea("temshop", A=self.uwtask.titleArea)):
            self.buyInBlackMarket(city)
                
        with open('src/UW/blackMarket.json', 'r') as f:
            boughtCities = json.load(f)
        boughtCities.append(city)
        with open('src/UW/blackMarket.json', 'w') as json_file:
            json.dump(boughtCities, json_file)
        

            