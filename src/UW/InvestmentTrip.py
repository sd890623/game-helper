import sys
sys.path.append("src")
from windows import getAllWindowsWithTitle
from UWTask import UWTask
from utils import doMoreTimesWithWait,doAndWaitUntilBy,continueWithUntilByWithBackup

allWindowsWithTitle = getAllWindowsWithTitle("神盾虚拟机 NP版 - VMware Workstation")
if (len(allWindowsWithTitle) > 0):
    hwndObject = allWindowsWithTitle[0]

task = UWTask(hwndObject["hwnd"], "uw")
simuInstance=task.simulatorInstance

class Investment:
    #Better do winter
    investmentCities = [
        "saint","riga","visby","beck","copenhag","bergen","dublin","ceuta","marseille","pisa","calvi","syracuse","candia","antalya","beirut","cairo","casablanca","las","douala","cape","manbasa","aden","suez","jeddah","massawa","hadiboh","dhofar","bidda","shiraz","kotte","aceh","malacca","palembang","kuching","jayakarta","surabaya","pinjarra","pirie","hobart","gari","kaka","ambon","makassar","davao","manila","quanzhou","naha","hangzhou","chongqing","yanyun","chang","peking","macau","pasay","toamasina","cape","bahia","aires","ushuaia","valpara","lima","tumbes","copiap","ushuaia","rio","pernambuco","maracaibo","nassau","nutak","arviat","reykjav","edinburgh"
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
        "chinesetea","huzhoubrush","ancientbone","gardenia","bingata","ramiefabric","sweetolive","shaoxingwine","blackvineg","staranise","beanpaste","chinesepainting","guqin","sanjiegun","firelance"
    ]
    sellCities = [
        "quanzhou","maracaibo"
    ]
    changeFleet = ["nassau"]

    def investInCity(self):
        task.print("去投资")
        doMoreTimesWithWait(lambda: simuInstance.clickPointV2(*task.rightCatePoint2),1, 1)
        task.clickInMenu("bureau","bureau",startIndex=6)
        continueWithUntilByWithBackup(lambda: simuInstance.clickPointV2(*task.rightTopTownIcon), lambda: task.inCityList(self.investmentCities),3,30)

    def runInvestmentTrip(self):
        for index,city in enumerate(self.investmentCities):
            task.gotoCity(city,self.investmentCities)
            self.investInCity()


investment=Investment()
investment.runInvestmentTrip()
