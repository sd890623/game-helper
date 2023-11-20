import sys
import time
sys.path.append("src")
from windows import getAllWindowsWithTitle
from UWTask import UWTask
from utils import doMoreTimesWithWait,doAndWaitUntilBy,continueWithUntilByWithBackup,wait

def importMarket():
    from Market import Market
    return Market

allWindowsWithTitle = getAllWindowsWithTitle("神盾虚拟机 NP版 - VMware Workstation")
if (len(allWindowsWithTitle) > 0):
    hwndObject = allWindowsWithTitle[0]

task = UWTask(hwndObject["hwnd"], "uw")
simuInstance=task.simulatorInstance

class Investment:
    goBM = False
    #Better do winter
    investmentCities = [
        "saint","riga","visby","beck","copenhag","bergen","bremen","dublin","ceuta","marseille","pisa","calvi","syracuse","zadar","ragusa","candia","antalya","beirut","cairo","casablanca","las","bathurst","douala","cape","natal","manbasa","aden","suez","jeddah","massawa","hadiboh","dhofar","bidda","shiraz","hormuz","diu","kotte","aceh","pasay","malacca","palembang","lopburi","brunei","kuching","jayakarta","surabaya","pinjarra","pirie","hobart","gari","kaka","ambon","banda","makassar","davao","manila","quanzhou","naha","hangzhou","chongqing","yanyun","chang","peking","macau","pasay","toamasina","cape","bahia","aires","ushuaia","valpara","lima","tumbes","acapulco","guatemala","panama","copiap","ushuaia","rio","pernambuco","maracaibo",
        "nassau","nutak","arviat","reykjav","narvik","edinburgh"
    ]
    investmentCities3 = [
        #"saint","riga","visby","beck","copenhag","bergen","dublin","ceuta","marseille","pisa","calvi","syracuse","candia","antalya","beirut","cairo","casablanca","las","douala","cape","manbasa","aden","suez","jeddah","massawa","hadiboh","dhofar","bidda","shiraz","kotte","aceh","malacca","palembang","kuching","jayakarta","surabaya","pinjarra","pirie","hobart","gari","kaka","ambon","makassar","davao","manila","quanzhou","naha","hangzhou","chongqing","yanyun","chang","peking","macau","pasay","toamasina","cape","bahia","aires","ushuaia","valpara","lima","tumbes","acapulco","guatemala","panama",
        "copiap","ushuaia","rio","pernambuco","maracaibo","nassau","nutak","arviat","reykjav","edinburgh"
    ]
    investmentCities4 = [
        #"unalaska","tacoma",
        "ohlone","acapulco","guatemala","panama"
    ]
    # investmentCities=investmentCitiesArray[investmentRoute]
    supplyCities = [
        "toamasina"
    ]
    shippartsCities = [
        "visby","beirut","cape","suez","malacca","jayakarta","rio","aires","lima","valpara"
    ]
    buyCities = [
        "saint","riga","visby","beck","copenhag","bergen","dublin","pisa","candia","antalya","beirut"
        "quanzhou","naha","hangzhou","chongqing","yanyun","chang","peking"
    ]
    buyGoods = [
        "vodka","felt","feather","amber","aquavit","twohand","whisky","velvet","western","oakmoss","narcissus","civet","damascus",
        "chinesetea","huzhoubrush","ancientbone","gardenia","bingata","ramiefabric","sweetolive","shaoxingwine","blueandwhite","blackvineg","musa","staranise","beanpaste","chinesepainting","guqin","sanjiegun","firelance"
    ]
    sellCities = [
        "quanzhou","nassau"
    ]
    #before going to a city
    changeFleet = ["nutak"]

    def investOnce(self,max=False):
        doAndWaitUntilBy(lambda: simuInstance.clickPointV2(1248,238), lambda: task.hasImageInScreen("investBtn", A=[643,430,779,726]),2,2)
        investBtn= task.hasImageInScreen("investBtn", A=[643,430,779,726])
        if(investBtn):
            wait(lambda: simuInstance.clickPointV2(709,261),1)
            if(max):
                wait(lambda: simuInstance.clickPointV2(786,532),1)
            wait(lambda: simuInstance.clickPointV2(investBtn[0]+30,investBtn[1]+5))
            wait(lambda: simuInstance.clickPointV2(1278,853),1)

    def investInCity(self):
        task.print("去投资")
        doMoreTimesWithWait(lambda: simuInstance.clickPointV2(*task.rightCatePoint2),1, 1)
        task.clickInMenu("bureau","bureau",startIndex=5)
        doAndWaitUntilBy(lambda: simuInstance.clickPointV2(39,84), lambda: task.hasSingleLineWordsInArea("lnvest", A=task.titleArea), 2,2)
        while(task.getNumberFromSingleLineInArea(A=[260,807,285,823])<750 and task.hasSingleLineWordsInArea("p", A=[284,807,295,823])):
            self.investOnce(True)
        self.investOnce()
        # doAndWaitUntilBy(lambda: simuInstance.clickPointV2(46,153), lambda: UWTask.hasSingleLineWordsInArea("sel", A=task.titleArea),2,2)
        # wait(lambda: simuInstance.clickPointV2(),1)
        continueWithUntilByWithBackup(lambda: simuInstance.clickPointV2(*task.rightTopTownIcon), lambda: task.inCityList(self.investmentCities),3,30)

    def runInvestmentTrip(self):
        for index,city in enumerate(self.investmentCities):
            if(city in self.changeFleet):
                task.changeFleet(3)
            task.gotoCity(city,self.investmentCities)
            if(not city in self.supplyCities):
                self.investInCity()
            if(city in self.sellCities):
                task.sellInCity(city)
            if(city in self.buyCities):
                task.buyInCity(self.investmentCities, products=self.buyGoods)
            if(self.goBM):
                task.buyBlackMarket(city)
            task.checkSB()
            task.checkReachCity()
            # if index is the last of the array
            if(index is len(self.investmentCities)-1):
                # stop the python program
                sys.exit()


investment=Investment()
task.allCityList=investment.investmentCities
while(True):
    # task.setCurrentCityFromScreen()
    if(not task.inCityList(investment.investmentCities)):
        task.print("没有在长途城市列表中，中断")
        wait(lambda: simuInstance.rightClickPointV2(*task.randomPoint))
        time.sleep(5)
        continue
    investment.runInvestmentTrip()
