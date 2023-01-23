from guiUtils import win
from utils import wait,doMoreTimesWithWait,doAndWaitUntilBy,hasOneArrayStringInStringAndNotVeryDifferent,isArray,stringhasStartsWithOneArrayString
import os
import json
import time
from datetime import date
from UWTask import UWTask

marketBuyData={
    "kokkola":["amber"],
    "saint":["chrysoberyl","tourmaline"],
    "gda":["tourmaline","amber"],
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
"bristol","dublin","edinburgh","nantes","bordeaux","porto","lisboa","faro","seville","ceuta","laga","bathurst","elmina","luanda","cape","sofala","mozambiqu",
"zanzibar","toamasina","manbasa","hadiboh","aden","jeddah","muscat","hormuz","basrah","baghdad","goa","kozhikod",
"algiers","valencia","barcelona","montpellie","marseille","geona","pisa","calvi","tunis","syracuse","ragusa",
"alexandria","cairo","candia","athens","thessaloni","constantino",
"royal","santiago","caracas","trujil","veracruz","rida","santo","portobelo",
"pasay","malacca","palembang","banjarmasin","surabaya","jayakarta",
"macau","quanzhou","hobe","hangzhou","peking","hanyang","jeju","changan'an"
]
capitals=["london","amsterda","lisboa","seville","constantino","hanyang","peking","edo"]
coinPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"coinInBuy"+".bmp")

class Market:
    randomPoint=851,678
    buySellWholeArea=[187,99,949,395]
    today=None
    transactClick=307,177
    transactOKBtn=781,700
    purchaseBtn=55,90
    @staticmethod
    def deductBuyBMFromRouteObj(routeObject):
        cities=routeObject["buyCities"]
        if(not routeObject.get("deductBuyBM")):
            return cities
        with open('src/UW/blackMarket.json', 'r') as f:
            boughtCities = json.load(f)
        def filterCallback(city):
            return (city not in boughtCities)
        return list(filter(filterCallback, cities))

    @staticmethod
    def deductSellBMFromCities(cities):
        with open('src/UW/blackMarket.json', 'r') as f:
            boughtCities = json.load(f)
        def filterCallback(city):
            if(city['types']=="BM" and city['name'] in boughtCities):
                return False
            return True
        return list(filter(filterCallback, cities))

    # def __init__(self, instance: win, uwtask:UWTask) -> None:
    def __init__(self, instance: win, uwtask:UWTask,marketMode=0) -> None:
        self.instance=instance
        self.uwtask=uwtask
        self.marketMode=marketMode
        self.today=date.today().strftime("%d-%m-%Y")

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

        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.purchaseBtn), lambda: self.uwtask.hasSingleLineWordsInArea("purchase", A=self.uwtask.titleArea), 2,2)

        #Loop through and find what can be bought
        while (index<12 and end is False):
            xDiff=int(index%4*225.5)
            yDiff=int(index/4)*134
            index+=1
            #print([176+xDiff,200+yDiff,286+xDiff,235+yDiff])
            #red check area 260,203,346,221
            # if(self.uwtask.hasSingleLineWordsInArea("unlock", A=[286+xDiff,211+yDiff,392+xDiff,232+yDiff])):
            #     continue   
            # print([338+xDiff,203+yDiff,389+xDiff,221+yDiff])
            ducatIconLocation= self.uwtask.hasImageInScreen("ducatInMarketBuy", A=[299+xDiff,215+yDiff,370+xDiff,230+yDiff])
            moneyScanArea=[ducatIconLocation[0]+13,ducatIconLocation[1],ducatIconLocation[0]+63,ducatIconLocation[1]+15] if ducatIconLocation else [299+xDiff,215+yDiff,370+xDiff,230+yDiff]
            price=self.uwtask.getNumberFromSingleLineInArea(A=moneyScanArea)
            #269,137,326,155
            #logic re food type
            #typeOcr=self.uwtask.getSingleLineWordsInArea(A=[274+xDiff,140+yDiff,371+xDiff,162+yDiff])

            if not price:
                continue
            if(price>300 and self.uwtask.hasSingleLineWordsInArea("food", A=[274+xDiff,140+yDiff,371+xDiff,162+yDiff])):
                continue

            buyList.append((index-1, price))

        #sort by price high to low
        buyList=sorted(buyList, key=lambda student: student[1], reverse=True)
        print(buyList)

        #Click from list and buy
        for buyObj in buyList:
            index=buyObj[0]
            if(self.checkMaxBought(xDiff,yDiff)):
                break
            xDiff=int(index%4*225.5)
            yDiff=int(index/4)*134
            self.uwtask.print("buy item "+str(index))
            wait(lambda: self.instance.clickPointV2(self.transactClick[0]+xDiff,self.transactClick[1]+yDiff),0.2,disableWait=True)
        
        wait(lambda: self.instance.clickPointV2(1306,845),1)
        wait(lambda: self.instance.clickPointV2(*self.transactOKBtn),5)
        self.bargin()
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,0)
        self.uwtask.print("buy fin")

    def sellGoodsWithMargin(self,simple=False,types=None):
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(46,153), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=self.uwtask.titleArea),2,2)
        def sellItemsInScreen():
            #Loop through and find what can be bought
            #xDiff 225.5
            #yDiff 134
            index=0
            while (index<12):
                xDiff=int(index%4*225.5)
                yDiff=int(index/4)*134
                index+=1
                if(simple is False):
                    # print([310+xDiff,214+yDiff,397+xDiff,230+yDiff])
                    if(self.uwtask.hasSingleLineWordsInArea("-", A=[310+xDiff,214+yDiff,397+xDiff,230+yDiff], ocrType=2)):
                        continue
                if(isArray(types)):
                    typeOcr=self.uwtask.getSingleLineWordsInArea(A=[274+xDiff,140+yDiff,371+xDiff,162+yDiff])
                    if(hasOneArrayStringInStringAndNotVeryDifferent(typeOcr,types)):
                        wait(lambda: self.instance.clickPointV2(self.transactClick[0]+xDiff,self.transactClick[1]+yDiff),0.2,disableWait=True)
                if(types is None):
                    wait(lambda: self.instance.clickPointV2(self.transactClick[0]+xDiff,self.transactClick[1]+yDiff),0.2,disableWait=True)
            wait(lambda: self.instance.clickPointV2(1306,845),1)
            wait(lambda: self.instance.clickPointV2(*self.transactOKBtn),5)
            self.bargin()
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,0)

        self.uwtask.print("sell items")
        sellItemsInScreen()
        # if(not(self.uwtask.hasSingleLineWordsInArea("sell", A=[706,471,737,494]))):
        #     sellItemsInScreen()
        ducatIconLocation= self.uwtask.hasImageInScreen("ducatInMarket", A=[891,5,985,50])
        moneyScanArea=[ducatIconLocation[0]+18,ducatIconLocation[1]-2,ducatIconLocation[0]+123,ducatIconLocation[1]+16] if ducatIconLocation else [1007,11,1119,39]
        savingOcr=self.uwtask.getSingleLineWordsInArea(A=moneyScanArea,ocrType=2)
        self.uwtask.sendMessage("UW","current saving is: "+(savingOcr if savingOcr else "undefined"))
        self.uwtask.print("sell fin")

    def checkMaxBought(self,xDiff,yDiff):
        if(self.marketMode==1):
            return self.uwtask.isPositionColorSimilarTo(362+xDiff,173+yDiff,(225,215,204))
        return (self.uwtask.getNumberFromSingleLineInArea(A=[1300,105,1353,126])>1000 and self.uwtask.isPositionColorSimilarTo(362+xDiff,173+yDiff,(225,215,204)))
    
    def buyProductsInMarket(self,products):
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.purchaseBtn), lambda: self.uwtask.hasSingleLineWordsInArea("purchase", A=self.uwtask.titleArea), 2,2)
        print(products)
        boughtTick=0

        #xDiff 261
        #yDiff 131
        index=0
        #Loop through and find what can be bought
        self.uwtask.print("buy items")
        while (index<9):
            xDiff=int(index%4*225.5)
            yDiff=int(index/4)*134
            index+=1
            #red check area 260,203,346,221
            # if(self.uwtask.hasSingleLineWordsInArea("unlock", A=[286+xDiff,211+yDiff,392+xDiff,232+yDiff])):
            #     continue   
            productName=self.uwtask.getSingleLineWordsInArea(A=[273+xDiff,117+yDiff,414+xDiff,139+yDiff])
            if(not(productName)):
                continue
            if(stringhasStartsWithOneArrayString(productName, products)):
                # beforeBuyQty=self.uwtask.getNumberFromSingleLineInArea(A=[237+xDiff,160+yDiff,264+xDiff,176+yDiff])
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(self.transactClick[0]+xDiff,self.transactClick[1]+yDiff),2,0.2,disableWait=True)
                boughtTick+=1
                if(self.checkMaxBought(xDiff,yDiff)):
                    self.uwtask.print("maxed out")
                    self.uwtask.tradeRouteBuyFin=True
                    break

        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1306,845),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[757,689,816,712]),1,1,timeout=5)
        wait(lambda: self.instance.clickPointV2(*self.transactOKBtn),1)
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
            number=self.uwtask.getNumberFromSingleLineInArea(A=[893,78,910,96])
            if(number and int(number)>=25):
                break
            else:
                time.sleep(60)
                wait(lambda: self.instance.clickPointV2(*self.randomPoint),3)

        self.buyProductsInMarket(products)

    def bargin(self):
        if(self.uwtask.hasSingleLineWordsInArea("es", A=[981,768,1177,817])):
            time.sleep(1)
            #click yes
            wait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),2)
            #wait for dialog, click no regardless of successful.
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(1076,715),6, 0.5)

    def shouldBuyBlackMarket(self,city):
        with open('src/UW/blackMarket.json', 'r') as f:
            boughtCities = json.load(f)
        # time=self.uwtask.getTime()
        if((city in hasBMCities) and (city not in boughtCities)): #and (time<6 or time>12)):
            return True

    def buyInBlackMarket(self,city):
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(74,210), lambda: self.uwtask.hasSingleLineWordsInArea("blackmarket", A=self.uwtask.titleArea),2,1)

        #must rule  rosewood must,
        #ducat rule  value >400000 no, 
        #else gem
        def clickBuy(x,y):
            wait(lambda: self.instance.clickPointV2(x,y),0.2,disableWait=True)
            wait(lambda: self.uwtask.clickWithImage("calculator", A=[801,547,860,663]),0,disableWait=True)
            if(self.uwtask.hasSingleLineWordsInArea("max", A=[941,567,1022,602])):
                wait(lambda: self.instance.clickPointV2(972,584),0.2,disableWait=True)
                wait(lambda: self.instance.clickPointV2(1078,564),0.2,disableWait=True)
            #quick purchase
            wait(lambda: self.instance.clickPointV2(765,689),1)
            # if(self.uwtask.hasSingleLineWordsInArea("purchase", A=[613,236,699,258])):
            #     wait(lambda: self.instance.clickPointV2(719,482))
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(74,210),2,0.2,disableWait=True)

        index=0
        self.uwtask.print("buy BM items")
        while (index<20):
            xDiff=int(index%4*225.3)
            yDiff=int(int(index/4)*134)
            index+=1
            productName=self.uwtask.getMultiLineWordsInArea(A=[275+xDiff,119+yDiff,415+xDiff,183+yDiff])
            if(not(productName) or productName==''):
                continue 
            if(
                 ("intermediatetrade" in productName and "appointment" not in productName) or
                 productName.startswith("intermediatecombatappointment") or
                "teak" in productName or "largegunport" in productName or
                "specialenhanced" in productName or "silverastrolabe" in productName or
                "rosewoodmast" in productName or #"beech" in productName
                 "lightsha" in productName or "tanjaq" in productName or #"improvedmedium" in productName
                "lareale" in productName or# "heavycarrack" in productName or "largeschoo" in productName or
                ("bgradeprocessed" in productName and "lumber" not in productName and "metal" not in productName)
            ):
                clickBuy(267+xDiff,165+yDiff)
                continue

            def ducatCase():
                #Ducat case
                price=self.uwtask.getNumberFromSingleLineInArea(A=[260+xDiff,212+yDiff,373+xDiff,231+yDiff])
                if(
                    "dye" in productName or "emblem" in productName or "lowest" in productName or
                    "mediumkeel" in productName or "decoration" in productName or
                    "golden" in productName or "pine" in productName or (productName.startswith("mediumgunport"))
                ):
                    return False
                itemType=self.uwtask.getSingleLineWordsInArea(A=[276+xDiff,141+yDiff,412+xDiff,163+yDiff])
                if("decoration" in itemType or "design" in itemType):
                    return False
                if(price and price>938):
                    clickBuy(267+xDiff,165+yDiff)
            
            gemLocation= self.uwtask.hasImageInScreen("gemInBM2", A=[274+xDiff,213+yDiff,351+xDiff,231+yDiff])
            if(gemLocation):
                # gemInBM2 pixel: 11x10
                gemScanArea=[gemLocation[0]-5,gemLocation[1]-5,gemLocation[0]+11+5,gemLocation[1]+10+5]
                gemAreaOCR=self.uwtask.getNumberFromSingleLineInArea(A=[gemScanArea[0]-3,gemScanArea[1],gemScanArea[2]+5,gemScanArea[3]])
                if(self.uwtask.hasImageInScreen("gemInBM2",A=gemScanArea) and (not gemAreaOCR or gemAreaOCR==1 or gemAreaOCR==3)):
                    #Gem case
                    continue
                else:
                    if(not ducatCase()):
                        continue
            else:
                if(not ducatCase()):
                    continue
        screenshotBlob = self.instance.outputWindowScreenshotV2()
        self.uwtask.saveImageToFile(screenshotBlob, relaPath="\\..\\..\\assets\\screenshots\\UW\\"+self.today,filename=city+".jpg")
    
    def buyBlackMarket(self,city):
        timeout=0
        timeout2=0
        def recursiveVisitBM():
            nonlocal timeout2
            while(self.uwtask.getTime()>5 and self.uwtask.getTime()<20):
                time.sleep(30)
                timeout2+=1
                if(timeout2>360):
                    return
            if(not self.uwtask.clickInMenu("temshop","temshop")):
                nonlocal timeout
                timeout+=1
                if(timeout>5):
                    return
                recursiveVisitBM()
                
            if(not self.uwtask.hasSingleLineWordsInArea("blackmarket", A=[19,198,161,231])):
                timeout+=1
                if(timeout>5):
                    return
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
        

            