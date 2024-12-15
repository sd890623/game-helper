import sys
import os
import copy

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

from guiUtils import win
from utils import removeArrayElementFromArray,wait,isStringSameOrSimilar,hasOneArrayStringInString,doMoreTimesWithWait,doAndWaitUntilBy,hasOneArrayStringInStringAndNotVeryDifferent,isArray,stringhasStartsWithOneArrayString,continueWithUntilBy,isArrayAnyInArray
import os
import json
import time
from datetime import date
from UWTask import UWTask
from Fashion import Fashion

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

hasBMCities=["kokkola","saint","stockhol","visby","beck","copenhag","oslo","hamburg","bremen","london","antwerp","calais","plymouth","amsterda",
# "bristol","dublin","edinburgh","nantes","bordeaux","porto","lisboa","faro","seville","ceuta","laga","bathurst","elmina","luanda","town","sofala","mozambiqu",
# "zanzibar","toamasina","mombasa","socotra","aden","jeddah","muscat","hormuz","basrah","baghdad","goa","kozhikod",
# "algiers","valencia","barcelona","montpellie","marseille","geona","pisa","calvi","tunis","syracuse","ragusa",
# "alexandria","cairo","candia","athens","thessaloni","constantino",
# "roya","santiago","caracas","trujil","veracruz","rida","santo","portobelo",
# "malacca","palembang","banjarmasin","surabaya","jakarta",
"pasay","macau","quanzhou","tamsui","hangzhou","peking","hanyang","jeju","chang","chongqing","edo","nagasaki","dongnae"]
capitals=["london","amsterda","lisboa","seville","constantino","hanyang","peking","edo"]
coinPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"coinInBuy"+".bmp")
BMfile=os.path.abspath(__file__ + "\\..\\blackMarket.json")
class Market:
    randomPoint=851,668
    buySellWholeArea=[187,99,949,395]
    errorMsgTitleArea=[654,285,783,303]
    today=None
    transactPurchaseBtn=1306,845
    transactClick=307,177
    marketTransactOKBtn=781,700
    purchaseBtn=55,90

    @staticmethod
    def deductSellBMFromCities(cities):
        with open(BMfile, 'r') as f:
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
        self.fashion=Fashion(self.instance,self.uwtask)

    def deductBuyBMFromRouteObj(self,routeObject):
        # if(not self.uwtask.goBM):
        #     return []
        cities=routeObject["buyCities"]
        if(not routeObject.get("deductBuyBM")):
            return cities
        with open(BMfile, 'r') as f:
            boughtCities = json.load(f)
        def filterCallback(city):
            return (city not in boughtCities)
        return list(filter(filterCallback, cities))
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
        
        wait(lambda: self.instance.clickPointV2(*self.transactPurchaseBtn),1)
        wait(lambda: self.instance.clickPointV2(*self.marketTransactOKBtn),5)
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
            if(not simple):
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
            else:
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(1033,856),3,0)
            wait(lambda: self.instance.clickPointV2(*self.transactPurchaseBtn),1)
            wait(lambda: self.instance.clickPointV2(*self.marketTransactOKBtn),5)
            self.bargin(True)
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),3,0)

        self.uwtask.print("sell items")
        sellItemsInScreen()
        if(not(self.uwtask.hasSingleLineWordsInArea("sel", A=[690,467,736,496]))):
            sellItemsInScreen()
        ducatIconLocation= self.uwtask.hasImageInScreen("ducatInMarket", A=[891,5,985,50])
        moneyScanArea=[ducatIconLocation[0]+18,ducatIconLocation[1]-2,ducatIconLocation[0]+123,ducatIconLocation[1]+16] if ducatIconLocation else [1007,11,1119,39]
        savingOcr=self.uwtask.getSingleLineWordsInArea(A=moneyScanArea,ocrType=2)
        self.uwtask.sendMessage("UW","current saving is: "+(savingOcr if savingOcr else "undefined"))
        self.uwtask.print("sell fin")

    def checkMaxBought(self,xDiff,yDiff):
        if(self.marketMode==1):
            return self.uwtask.isPositionColorSimilarTo(362+xDiff,173+yDiff,(225,215,204))
        goodsNumber=self.uwtask.getNumberFromSingleLineInArea(A=[1300,105,1353,126])
        if(not goodsNumber):
            return True
        return (goodsNumber>1000 and self.uwtask.isPositionColorSimilarTo(362+xDiff,173+yDiff,(225,215,204)))
    
    def buyProductsInMarket(self,products,buyNotProducts=None):
        if(buyNotProducts is None):
            buyNotProducts=[]
        if(self.uwtask.hasSingleLineWordsInArea("skip", A=[1330,5,1384,39])):
            doAndWaitUntilBy(lambda: self.instance.clickPointV2(1373,23), lambda: self.uwtask.hasSingleLineWordsInArea("market", A=self.uwtask.titleArea), 2,2)

        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.purchaseBtn), lambda: self.uwtask.hasSingleLineWordsInArea("purchase", A=self.uwtask.titleArea), 2,2)
        print(products)
        boughtTick=0

        #xDiff 261
        #yDiff 131
        index=0
        #Loop through and find what can be bought
        self.uwtask.print("buy items")
        while (index<12):
            xDiff=int(index%4*225.5)
            yDiff=int(index/4)*134
            index+=1
            #red check area 260,203,346,221
            # if(self.uwtask.hasSingleLineWordsInArea("unlock", A=[286+xDiff,211+yDiff,392+xDiff,232+yDiff])):
            #     continue   
            productName=self.uwtask.getSingleLineWordsInArea(A=[273+xDiff,117+yDiff,418+xDiff,139+yDiff])
            if(not(productName)):
                continue
            if(hasOneArrayStringInString(productName,buyNotProducts)):
                continue
            if(stringhasStartsWithOneArrayString(productName, products)):
                # beforeBuyQty=self.uwtask.getNumberFromSingleLineInArea(A=[237+xDiff,160+yDiff,264+xDiff,176+yDiff])
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(self.transactClick[0]+xDiff,self.transactClick[1]+yDiff),2,0.2,disableWait=True)
                boughtTick+=1
                if(self.checkMaxBought(xDiff,yDiff)):
                    self.uwtask.print("maxed out")
                    self.uwtask.tradeRouteBuyFin=True
                    break

        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.transactPurchaseBtn),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[757,689,816,712]),1,1,timeout=5)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.marketTransactOKBtn),lambda: not self.uwtask.hasSingleLineWordsInArea("ok", A=[757,689,816,712]),1,1,timeout=5)
        self.bargin()
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),2,0)
        self.uwtask.print("buy fin")
        return boughtTick

    def buyProductsInCityTwice(self,products,returnResultsLambda=None):
        boughtTick=self.buyProductsInMarket(products)
        if(self.uwtask.tradeRouteBuyFin):
            return
        # if(boughtTick==0):
        #     return
        times=0
        prev_number = 30
        while(times<80):
            number=self.uwtask.getNumberFromSingleLineInArea(A=[893,78,910,96])
            if(number and int(number)>=25):
                break
            elif prev_number == 0 and number and number != 0:
                break
            else:
                prev_number = int(number) if number else 0
                time.sleep(30)
                times+=1
                wait(lambda: self.instance.clickPointV2(*self.randomPoint),3)

        self.buyProductsInMarket(products)
        if(returnResultsLambda):
            return returnResultsLambda()


    def buyProductsInCityTwiceWithGem(self,products):
        self.buyProductsInMarket(products)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1000,83), lambda: self.uwtask.hasSingleLineWordsInArea("stock", A=[730,271,797,297]),2,1)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(767,611), lambda: not self.uwtask.hasSingleLineWordsInArea("stock", A=[730,271,797,297]),2,1)
        self.buyProductsInMarket(products)

    def bargin(self,multiTimes=False):
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.randomPoint),5,0)
        if(self.uwtask.hasSingleLineWordsInArea("es", A=[981,768,1177,817])):
            time.sleep(1)
            if(multiTimes):
                #click yes
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(*self.uwtask.inScreenConfirmYesButton),self.uwtask.getDailyConfValByKey("negoTimes") or 5,1)
            #wait for dialog, click no regardless of successful.
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(1076,715),6, 0.5)

    def shouldBuyBlackMarket(self,city):
        with open(BMfile, 'r') as f:
            boughtCities = json.load(f)
        # time=self.uwtask.getTime()
        if((city in hasBMCities) and (city not in boughtCities)): #and (time<6 or time>12)):
            return True

    def buyInBlackMarket(self,city):
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(74,210), 
        lambda: self.uwtask.hasSingleLineWordsInArea("blackmarket", A=self.uwtask.titleArea),2,1)
        #must rule  rosewood must,
        #ducat rule  value >400000 no
        #else gem
        index=0
        self.uwtask.print("buy BM items")
        while (index<20):
            xDiff=int(index%4*225.3)
            yDiff=int(int(index/4)*134)
            index+=1
            productName=self.uwtask.getMultiLineWordsInArea(A=[275+xDiff,118+yDiff,418+xDiff,163+yDiff])
            # for case of smaller text a grade material not recognized, 2nd round of recog
            if(productName in ["material", "manual"]):
                productName=self.uwtask.getSingleLineWordsInArea(A=[275+xDiff,118+yDiff,419+xDiff,136+yDiff])
            if(not(productName) or productName==''):
                continue
            if(
                 (isStringSameOrSimilar("ntermediatetrade",productName) and "appointment" not in productName) or
                 productName.startswith("intermediatecombatappointment") or
                ("wooden" in productName and "astro" in productName) or "lowcombat" in productName or
                "ebony" in productName or
                 ("highcombat" in productName and "highest" not in productName) or
                #  "tanjaq" in productName or
                #  "largefrigate" in productName or "hind" in productName or "bermuda" in productName or
                #  "junk" in productName or "higaki" in productName or
                # "teak" in productName or "largegunport" in productName or
                # "largekeel" in productName or
                # "silverastrolabe" in productName or
                "goldastrolabe" in productName or
                #"rosewoodmast" in productName or #"beech" in productName
                #"lightsha" in productName or "tanjaq" in productName or #"improvedmedium" in productName
                # "lareale" in productName or# "heavycarrack" in productName or "largeschoo" in productName or
                (isStringSameOrSimilar("agrade",productName) and "processed" in productName and "parts" not in productName) or # and "lumber" not in productName and "metal" not in productName) or
                "abcccc" in productName
            ):
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(267+xDiff,165+yDiff),2,0.2,disableWait=True)
                continue

            def ducatCase():
                #Ducat case
                price=self.uwtask.getNumberFromSingleLineInArea(A=[260+xDiff,212+yDiff,373+xDiff,231+yDiff])
                if(
                    "dye" in productName or "emblem" in productName or
                    "deco" in productName or#"mediumkeel" in productName or "lowest" in productName or 
                    "redseal" in productName or
                    "blueprint" in productName or
                    "golden" in productName #or "pine" in productName or (productName.startswith("mediumgunport"))
                ):
                    return False
                itemType=self.uwtask.getSingleLineWordsInArea(A=[276+xDiff,141+yDiff,412+xDiff,163+yDiff])
                if("deco" in itemType or "design" in itemType or "town" in itemType):
                    return False
                if(price and price>938):
                    doMoreTimesWithWait(lambda: self.instance.clickPointV2(267+xDiff,165+yDiff),2,0.2,disableWait=True)
            
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
        #quick purchase
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.transactPurchaseBtn),lambda: self.uwtask.hasSingleLineWordsInArea("ok", A=[755,653,815,677]),1,1,timeout=5)
        if(self.uwtask.hasSingleLineWordsInArea("ok",A=[755,653,815,677])):
            wait(lambda: self.instance.clickPointV2(780,671),1)
        else:
            wait(lambda: self.instance.clickPointV2(1304,606),1)

        # use red gem to buy
        # if(self.uwtask.hasSingleLineWordsInArea("purchase", A=[613,236,699,258])):
        #     wait(lambda: self.instance.clickPointV2(719,482))
        doMoreTimesWithWait(lambda: self.instance.clickPointV2(74,210),2,1)
        screenshotBlob = self.instance.outputWindowScreenshotV2()
        self.uwtask.saveImageToFile(screenshotBlob, relaPath="\\..\\..\\..\\assets\\screenshots\\UW\\"+self.today,filename=city+".jpg")
    
    def buyBlackMarket(self,city):
        timeout=0
        timeout2=0
        def recursiveVisitBM():
            nonlocal timeout2
            while(self.uwtask.getTime()>5 and self.uwtask.getTime()<20):
                time.sleep(30)
                timeout2+=1
                if(timeout2>30):
                    return
            if(not self.uwtask.clickInMenu("temshop",["temshop"],startIndex=3)):
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
            self.uwtask.clickInMenu("temshop",["temshop"],startIndex=3)
        else:
            recursiveVisitBM()
        if(self.uwtask.hasSingleLineWordsInArea("temshop", A=self.uwtask.titleArea)):
            self.buyInBlackMarket(city)
                
        with open(BMfile, 'r') as f:
            boughtCities = json.load(f)
        boughtCities.append(city)
        with open(BMfile, 'w') as json_file:
            json.dump(boughtCities, json_file)
        
    def barterInVillage(self, villageObject):
        def cleanupGoods():
            index=4
            #first 540,475
            #2th 614,480
            while (index>=0):
                xDiff=int(index*74)
                # yDiff=int(index/4)*134
                index-=1
                wait(lambda: self.instance.rightClickPointV2(*self.randomPoint),0)
                # doMoreTimesWithWait(lambda: self.instance.clickPointV2(540+xDiff,475),2,1)
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(540+xDiff,475),lambda: self.uwtask.hasSingleLineWordsInArea("discardgoods", A=self.errorMsgTitleArea),1,1,timeout=5)
                # do not drop some items
                if(villageObject.get("leaveGoods") and self.uwtask.hasArrayStringInSingleLineWords(villageObject.get("leaveGoods"), A=[651,423,786,448])):
                    doAndWaitUntilBy(lambda: self.instance.clickPointV2(650,600),lambda: not self.uwtask.hasSingleLineWordsInArea("discardgoods", A=self.errorMsgTitleArea),1,1,timeout=5)
                    continue
                if(self.uwtask.hasArrayStringInSingleLineWords(villageObject.get("buyProducts"),A=[651,423,786,448])):
                    doAndWaitUntilBy(lambda: self.instance.clickPointV2(786,600),lambda: not self.uwtask.hasSingleLineWordsInArea("discardgoods", A=self.errorMsgTitleArea),1,1,timeout=5)

        if(self.uwtask.isPositionColorSimilarTo(273,784,(147,140,132))):
            buffer=0 
        else:
            buffer=villageObject.get("barterFirstRoundCount") or 3
        for (index, val) in villageObject.get("tradeObjects"):
            def tradeOnce():
                doAndWaitUntilBy(
                    lambda: self.instance.clickPointV2(44, 93),
                    lambda: self.uwtask.hasSingleLineWordsInArea("explore", A=self.uwtask.titleArea),
                )
                doAndWaitUntilBy(
                    lambda: self.instance.clickPointV2(44, 343),
                    lambda: self.uwtask.hasSingleLineWordsInArea("barter", A=self.uwtask.titleArea),
                )
                doMoreTimesWithWait(lambda: self.instance.clickPointV2(227+val*76,201),2,0)
                num=self.uwtask.getNumberFromSingleLineInArea(A=[1153,154,1183,170])
                if(num and num<1100):
                    doAndWaitUntilBy(lambda: self.instance.clickPointV2(1259,303), lambda: self.uwtask.hasSingleLineWordsInArea("negotiation", A=[694,245,802,268]),2,2,timeout=5)
                    nogoTimes=11
                    while(self.uwtask.isPositionColorSimilarTo(1019,317,(190,255,76)) and nogoTimes>0):
                        wait(lambda: self.instance.clickPointV2(553,628),0)
                        nogoTimes-=1
                    doAndWaitUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.enterCityButton), lambda: not self.uwtask.hasSingleLineWordsInArea("negotiation", A=[694,245,802,268]),2,2,timeout=5)

                doAndWaitUntilBy(lambda: self.instance.clickPointV2(1267,851), lambda: self.uwtask.hasSingleLineWordsInArea("barter", A=[630,287,705,308]),2,2,timeout=5)
                # position tba
                if(self.uwtask.hasSingleLineWordsInArea("trusting",A=[725,511,815,536]) and not self.uwtask.hasSingleLineWordsInArea("favor",A=[613,512,718,537])):
                    doAndWaitUntilBy(lambda: self.instance.clickPointV2(667,594), lambda: not self.uwtask.hasSingleLineWordsInArea("barter", A=[630,287,705,308]),2,2,timeout=5)
                    return False
                continueWithUntilBy(lambda: self.instance.clickPointV2(772,592), lambda: not self.uwtask.hasSingleLineWordsInArea("barter", A=[630,287,705,308]),2,timeout=10)
                if(self.uwtask.hasSingleLineWordsInArea("insufficient", A=[612,215,714,236])):
                    if(index==villageObject.get("cleanupIndex")):
                        self.uwtask.print("clean up goods, last round")
                        cleanupGoods()
                    doAndWaitUntilBy(lambda: self.instance.clickPointV2(712,668), lambda: not self.uwtask.hasSingleLineWordsInArea("sufficient", A=[610,215,716,236]) or self.uwtask.hasSingleLineWordsInArea("notice", A=[681,284,757,304]),2,2,timeout=5)
                    if(self.uwtask.hasSingleLineWordsInArea("notice", A=[681,284,757,304])):
                        doAndWaitUntilBy(lambda: self.instance.clickPointV2(789,593), lambda: not self.uwtask.hasSingleLineWordsInArea("notice", A=[681,284,757,304]),2,2)
                return True
            times=0
            while(self.uwtask.isPositionColorSimilarTo(273+(index+buffer)*81,784,(147,140,132)) and times<3):
                self.uwtask.print("empty slot in "+str(index+buffer)+", barter, times "+ str(times))
                if(not tradeOnce()):
                    break
                wait(lambda: None)
                times+=1

    def cleanupGoods(self, goods, leaveGoods=[]):
        continueWithUntilBy(lambda: self.instance.clickPointV2(*self.uwtask.rightTopTownIcon), lambda: self.uwtask.hasSingleLineWordsInArea("company", A=[156,22,227,39]),2,15,firstWait=2)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1390,94),lambda: self.uwtask.hasSingleLineWordsInArea("storage", A=self.uwtask.titleArea),1,1,timeout=10)#storage
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(42,339), lambda: self.uwtask.hasSingleLineWordsInArea("storage", A=self.uwtask.titleArea),2,1)
        index=5
        #first 242,264
        #5th 567,264
        while (index>=0):
            xDiff=int(index*81.25)
            # yDiff=int(index/4)*134
            index-=1
            wait(lambda: self.instance.rightClickPointV2(*self.randomPoint),0)
            wait(lambda: self.instance.clickPointV2(242+xDiff,264),2)
            # do not drop some items
            if(self.uwtask.hasArrayStringInSingleLineWords(leaveGoods, A=[627,245,810,272])):
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(1202,837),lambda: not self.uwtask.hasSingleLineWordsInArea("cargo", A=self.errorMsgTitleArea),1,1,timeout=5)
                continue
            if(self.uwtask.hasArrayStringInSingleLineWords(goods,A=[627,245,810,272])):
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(570,670),lambda: self.uwtask.hasSingleLineWordsInArea("discardgoods", A=self.errorMsgTitleArea),1,1,timeout=5)
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(786,602),lambda: not self.uwtask.hasSingleLineWordsInArea("discardgoods", A=self.errorMsgTitleArea),1,1,timeout=5)
            else:
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(1202,837),lambda: not self.uwtask.hasSingleLineWordsInArea("discardgoods", A=self.errorMsgTitleArea),1,1,timeout=5)
        
    def buyInCityByConf(self, buyCities, buyProducts, buyFin, buysConf, buyStrategy=None):
        def getUpdatedBuyResults():
            result=copy.copy(buyFin)
            for (index,element) in enumerate(buysConf):
                xDiff=1145+index*83
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(xDiff,178),lambda: self.uwtask.hasSingleLineWordsInArea("cargo", A=[671,209,730,232]),1,1,timeout=5)
                boughtQty=self.uwtask.getNumberFromSingleLineInArea(A=[640,294,677,311])
                if(boughtQty and boughtQty>element["targetNum"]):
                    result[element["product"]]=True
                wait(lambda: self.instance.clickPointV2(1051,668),1)
            return result
        def getUpdatedBuyProducts():
            result=list(buyProducts)
            for product in buyProducts:
                if(buyFin and buyFin.get(product)):
                    result.remove(product)
            return result

        return self.uwtask.buyInCity(buyCities, getUpdatedBuyProducts(), buyStrategy=buyStrategy,returnResultsLambda=getUpdatedBuyResults)

    def getBestPriceCity(self,routeObject,cities):
        sellPriceIndex=0
        sellPriceIndexByName=routeObject.get("sellPriceIndexByName")
        self.uwtask.print("find city with best price")
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(1409,201), lambda: self.uwtask.hasSingleLineWordsInArea("worldmap", A=self.uwtask.titleArea), 2,1,timeout=15)
        doAndWaitUntilBy(lambda: self.instance.clickPointV2(39,97), lambda: self.uwtask.hasSingleLineWordsInArea("search", A=[131,68,203,90]), 2,1,timeout=15)
        highestCity={"city":cities[0],"price":0}
        def findPriceIndex():
            area = [1152,226,1251,249]
            index = 0
            while index < 4:
                yDiff = index *45
                if(self.uwtask.hasSingleLineWordsInArea(sellPriceIndexByName,A=[area[0], area[1] + yDiff, area[2], area[3] + yDiff])):
                    return index  
                index += 1
            return 0
        
        # init
        def initClick(city):
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(259,76),1,0)
            wait(lambda: self.instance.typewrite(city),0)
            wait(lambda: self.instance.send_enter(),0)
            continueWithUntilBy(lambda: self.instance.clickPointV2(114,109),lambda: (self.uwtask.hasSingleLineWordsInArea("city",A=[1221,67,1263,95])),frequency=1,timeout=10)
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(1226,159),2,0)
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(1270,196),2,0)
            sellPriceIndex=findPriceIndex()
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(259,73),2,0)
            self.instance.send_backspaces()
            return sellPriceIndex
        sellPriceIndex=initClick("aden")
        sellPriceIndex=initClick("seville")

        for city in cities:
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(259,76),1,0)
            wait(lambda: self.instance.typewrite(city),0)
            wait(self.instance.send_enter,0)
            continueWithUntilBy(lambda: self.instance.clickPointV2(114,109),lambda: (self.uwtask.hasSingleLineWordsInArea("city",A=[1221,67,1263,95])),frequency=1,timeout=10)
            yDiff=sellPriceIndex*45
            ducatIconLocation= self.uwtask.hasImageInScreen("ducatInMap", A=[1331,227+yDiff,1370,250+yDiff])
            moneyScanArea=[ducatIconLocation[0]+13,ducatIconLocation[1]-2,ducatIconLocation[0]+66,ducatIconLocation[1]+15] if ducatIconLocation else [1350,224+yDiff,1410,251+yDiff]
            price=self.uwtask.getNumberFromSingleLineInArea(A=moneyScanArea)
            if(price and price>highestCity["price"]):
                highestCity["city"]=city
                highestCity["price"]=price
            doMoreTimesWithWait(lambda: self.instance.clickPointV2(259,73),1,0)
            wait(self.instance.send_backspaces,1)
            if(not self.uwtask.hasSingleLineWordsInArea("search", A=[131,68,203,90])):
                doAndWaitUntilBy(lambda: self.instance.clickPointV2(39,97), lambda: self.uwtask.hasSingleLineWordsInArea("search", A=[131,68,203,90]), 2,1,timeout=15)
                wait(lambda: self.instance.clickPointV2(259,73),1)
                wait(self.instance.send_backspaces,1)

        return highestCity.get("city")

    def buyUntilByConf(self,villageObject, routeObject):
        buyProducts=villageObject.get("buyProducts")
        buyCities=villageObject.get("buyCities")
        buyFin={}
        def getUpdateBuyCities():
            updatedCities=list(buyCities)
            for element in villageObject.get("buys"):
                if(buyFin and buyFin.get(element["product"])):
                   updatedCities=removeArrayElementFromArray(updatedCities,element["cities"])
            return updatedCities
        
        while(len(getUpdateBuyCities())>1):
            for city in getUpdateBuyCities():
                if(city not in getUpdateBuyCities()):
                    break
                fishing=routeObject.get("useFishingCities") and city in routeObject.get("useFishingCities")
                self.uwtask.gotoCity(city,self.uwtask.allCityList,express=True,fishing=fishing)
                buyFin=self.buyInCityByConf(buyCities, buyProducts, buyFin, villageObject.get("buys"), buyStrategy=villageObject.get("buyStrategy"))
                self.uwtask.checkInn(city, villageObject)
        
    def shouldWaitForFashion(self,fashions,cities,hours=3):
        fashionsR=self.fashion.getFashionsByCity(cities[0],hours)
        for fashion in fashionsR:
            if(isArrayAnyInArray(fashion["fashions"],fashions)):
                return fashion["hour"]
        return 0