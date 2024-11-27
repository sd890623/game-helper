import re
import sys
import os
sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

from utils import doMoreTimesWithWait, doAndWaitUntilBy, continueWithUntilByWithBackup, wait,continueWithUntilBy,isStringSameOrSimilar
from UWTask import UWTask
from windows import getAllWindowsWithTitle
import time
sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))


def importMarket():
    from Market import Market
    return Market


allWindowsWithTitle = getAllWindowsWithTitle("神盾虚拟机 NP版 - VMware Workstation")
if (len(allWindowsWithTitle) > 0):
    hwndObject = allWindowsWithTitle[0]

task = UWTask(hwndObject["hwnd"], "uw")
task.initMarket()
simuInstance = task.simulatorInstance


class Investment:
    goBM = False
    inn = True
    # Better do winter
    investmentCities = [
        "saint", "kokkola","stock", "visby","riga","gda", "beck", "copenhag", "oslo","bergen","edinburgh","hamburg","bremen", "dublin", "nantes","bordeaux","santa","ceuta", "montpell","marseille","genoa","pisa", "calvi","sassari","cagliari","naples", "syracuse","ancona", "venice","trieste","zadar", "ragusa", "candia", "varna","odesa","kerch","taganrog","antalya", "nicosia","beirut","jaffa", "said","cairo", "benghazi","tripoli","tunis","casablanca","las","arguin","verde", "bathurst","bissau", "sierra","abidjan","elmina","benin","douala", "tom","luanda","benguela","karibib","verde", "natal", "sofala","quelimane","mozambique","kilwa", "zanzibar","mombasa","malindi","mogadishu","aden","massawa","suez", "jeddah", "socotra", "dhofar","muscat", "doha", "basrah","baghdad","shiraz", "hormuz", "diu", "goa","kozhi","kochi","ceylon","pondi", "masuli","kolkata","pegu","aceh", "pasay", "malaca","palembang", "pangk", "lopburi", "prey", "brunei", "kuching", "jakarta", "surabaya","banjarmasin", "pinjarra","pirie", "hobart", "gari",
        "kaka", "dili", "banda", "ambon", "makassar", "ternate", "davao","jolo", "manila", "hanoi","quanzhou", "naha",  "hangzhou", "chongqing", "yanyun", "chang", "peking", "tamsui",
        "tainan","macau", "pasay", "toamasina", "town", "bahia", "aires", "ushuaia", "valpara", "lima", "tumbes", "acapulco", "guatemala", "panama", "copiap", "ushuaia", "rio", "pernambuco", "cayenne","porlamar","caracas","willemstad","maracaibo","cartagena","portobelo","trujillo","rida","veracruz","havana","southside","royal","santiago","santo","juan","nassau", "cohasset","nutak", "arviat", "nutak", "reykjav", "narvik","edinburgh"
    ]
    investmentCitiesy = [
        'peking',
        'yanyun',
        'chang',
        'chongqing',
        'hangzhou',
        'quanzhou',
        'tamsui',
        'macau',
        'jolo',
        'davao',
        'ternate',
        'ambon',
        'banda',
        'dili',
        'makassar',
        'surabaya',
        'banjarmasin',
        'pangk',
        'brunei',
        'lopburi',
        'aceh',
        'masuli',
        "kochi",
        'socotra',
        'aden',
        'toamasina'
    ]
    investmentCities4 = [
        # "unalaska","tacoma",
        "ohlone", "acapulco", "guatemala", "panama"
    ]
    # investmentCities=investmentCitiesArray[investmentRoute]
    supplyCities = [
    ]
    shippartsCities = [
        "visby", "beirut", "town", "suez", "malaca", "jakarta", "rio", "aires", "lima", "valpara"
    ]
    buyCities = [
        "saint", "riga", "visby", "beck", "copenhag", "bergen", "dublin", "pisa", "candia", "antalya", "beirut"
        "quanzhou", "naha", "hangzhou", "chongqing", "yanyun", "chang", "peking"
    ]
    buyGoods = [
        "vodka", "felt", "paper", "feather", "amber", "aquavit", "twohand", "whisky", "velvet", "western", "oakmoss", "narcissus", "civet", "damascus",
        "chinesetea", "huzhoubrush", "ancientbone", "gardenia", "bingata", "ramiefabric", "sweetolive", "shaoxingwine", "blueandwhite", "blackvineg", "musa", "staranise", "beanpaste", "chinesepainting", "guqin", "sanjiegun", "firelance","shu"
    ]
    sellCities = [
        "quanzhou", "nassau"
    ]
    # before going to a city
    changeFleet = ["cohasset"]

    def investOnce(self, domax=False):
        doAndWaitUntilBy(lambda: simuInstance.clickPointV2(
            1248, 238), lambda: task.hasImageInScreen("investBtn", A=[643, 430, 779, 726]), 2, 2)
        investBtn = task.hasImageInScreen("investBtn", A=[643, 430, 779, 726])
        if (investBtn):
            wait(lambda: simuInstance.clickPointV2(709, 261), 1)
            if (domax):
                doMoreTimesWithWait(lambda: simuInstance.clickPointV2(865,388),11,0)
            wait(lambda: simuInstance.clickPointV2(
                investBtn[0]+30, investBtn[1]+5))
            wait(lambda: simuInstance.clickPointV2(1278, 853), 1)

    def investInCity(self):
        task.print("去投资")
        doMoreTimesWithWait(lambda: simuInstance.clickPointV2(
            *task.rightCatePoint2), 1, 1)
        if(not task.clickInMenu(["bureau"], ["bureau"], startIndex=5)):
            continueWithUntilBy(lambda: simuInstance.clickPointV2(
            *task.rightTopTownIcon), lambda: task.inCityList(self.investmentCities), 3, 30)
            task.clickInMenu(["bureau"], ["bureau"], startIndex=5)

        doAndWaitUntilBy(lambda: simuInstance.clickPointV2(
            39, 84), lambda: task.hasSingleLineWordsInArea("invest", A=task.titleArea), 2,2,timeout=5)
        self.investOnce()
        while (True):
            xxxp = task.getSingleLineWordsInArea(A=[259,791,311,809],ocrType=3)
            # if (num and num < 800 and task.hasSingleLineWordsInArea("p", A=[284,786,296,802])):
            if (not xxxp):
                break
            match = re.search(r'\d+', xxxp)
            if (match and int(match.group()) and int(match.group()) < 800):
                self.investOnce(True)
                continue
            break
            

        # doAndWaitUntilBy(lambda: simuInstance.clickPointV2(46,153), lambda: UWTask.hasSingleLineWordsInArea("sel", A=task.titleArea),2,2)
        # wait(lambda: simuInstance.clickPointV2(),1)
        continueWithUntilByWithBackup(lambda: simuInstance.clickPointV2(
            *task.rightTopTownIcon), lambda: task.inCityList(self.investmentCities), 3, 30)

    def runInvestmentTrip(self):
        for index, city in enumerate(self.investmentCities):
            if (city in self.changeFleet):
                task.changeFleet(7)
            task.gotoCity(city, self.investmentCities,express=True)
            if(isStringSameOrSimilar(city, "varna")):
                task.sendNotification("reached checkpoint")
            if (not city in self.supplyCities):
                self.investInCity()
            # if (city in self.sellCities):
                # task.sellInCity(city)
            # if (city in self.buyCities):
                # task.buyInCity(self.investmentCities, products=self.buyGoods)
            if (self.goBM):
                task.buyBlackMarket(city)
            if (self.inn):
                task.checkInn(city, {"checkInnCities": self.investmentCities})
            task.checkSB()
            task.checkReachCity()

            # if index is the last of the array
            if (index is len(self.investmentCities)-1):
                task.sendNotification("investment finished")
                # stop the python program
                sys.exit()


investment = Investment()
task.allCityList = investment.investmentCities
while (True):
    # task.setCurrentCityFromScreen()
    if (not task.inCityList(investment.investmentCities)):
        task.print("没有在长途城市列表中，中断")
        wait(lambda: simuInstance.rightClickPointV2(*task.randomPoint))
        time.sleep(5)
        continue
    investment.runInvestmentTrip()
