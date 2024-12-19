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
        # "saint", "kokkola","stock", "visby","riga","gda", "beck", "copenhag", "oslo","bergen","edinburgh","hamburg","bremen", "dublin", "南特","bordeaux","santa","ceuta", "montpell","marseille","热那亚","比萨", "calvi","sassari","cagliari","naples", "syracuse","ancona", "venice","trieste","zadar", "ragusa", "candia", "varna","odesa","kerch","taganrog","antalya", "nicosia","beirut","jaffa", "塞得港","cairo", "benghazi","tripoli","tunis","casablanca","las","arguin","verde", "bathurst","bissau", "sierra","abidjan","elmina","benin","douala", "tom","luanda","benguela","karibib","verde", "纳塔尔", "索法拉","克利马内","莫桑比克","基尔瓦", "桑给巴尔","蒙巴萨","马林迪","摩加迪沙","亚丁","马萨瓦","苏伊士", "吉达", "索科特拉", "杜法尔","马斯喀特", "多哈", "巴士拉","巴格达","设拉子", "霍尔木兹", "diu", "goa","kozhi","kochi",
        "ceylon","pondi", "masuli","kolkata","pegu","aceh", "pasay", "malacca","palembang", "pangk", "lopburi", "prey", "brunei", "kuching", "jakarta", "surabaya","banjarmasin", "pinjarra","pirie", "hobart", "gari","kaka", "dili", "banda", "ambon", "makassar", "ternate", "davao","jolo", "manila", "hanoi","泉州", "naha",  "杭州", "重庆", "燕云", "长安", "北京", "淡水",
        "安平","澳门", "pasay", "塔玛塔夫", "town", "bahia", "aires", "乌斯怀亚", "valpara", "利马", "tumbes", "阿卡普尔科", "guatemala", "panama", "copiap", "乌斯怀亚", "rio", "pernambuco", "cayenne","porlamar","caracas","willemstad","maracaibo","cartagena","portobelo","trujillo","rida","veracruz","havana","southside","royal","santiago","santo","juan","nassau", "cohasset","nutak", "arviat", "nutak", "reykjav", "纳尔维克","edinburgh"
    ]
    investmentCitiesy = [
        '北京',
        '燕云',
        '长安',
        '重庆',
        '杭州',
        '泉州',
        '淡水',
        '澳门',
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
        '索科特拉',
        '塔玛塔夫',
        '亚丁',
        '苏伊士',
        'tunnel',
        'nicosia',
        'montpell'
    ]
    investmentCities4 = [
        # "unalaska","tacoma",
        "ohlone", "阿卡普尔科", "guatemala", "panama"
    ]
    # investmentCities=investmentCitiesArray[investmentRoute]
    supplyCities = [
    ]
    shippartsCities = [
        "visby", "beirut", "town", "苏伊士", "malacca", "jakarta", "rio", "aires", "利马", "valpara"
    ]
    buyCities = [
        "saint", "riga", "visby", "beck", "copenhag", "bergen", "dublin", "比萨", "candia", "antalya", "beirut"
        "泉州", "naha", "杭州", "重庆", "燕云", "长安", "北京"
    ]
    buyGoods = [
        "vodka", "felt", "paper", "feather", "amber", "aquavit", "twohand", "whisky", "velvet", "western", "oakmoss", "narcissus", "civet", "damascus",
        "chinesetea", "huzhoubrush", "ancientbone", "gardenia", "bingata", "ramiefabric", "sweetolive", "shaoxingwine", "blueandwhite", "blackvineg", "musa", "staranise", "beanpaste", "chinesepainting", "guqin", "sanjiegun", "firelance","shu"
    ]
    sellCities = [
        "泉州", "nassau"
    ]
    # before going to a city
    changeFleet = ["cohasset"]

    def investOnce(self, domax=False):
        # doAndWaitUntilBy(lambda: simuInstance.clickPointV2(
        #     1267,400), lambda: task.hasImageInScreen("investBtn", A=[643, 430, 779, 726]), 2, 2)
        # investBtn = task.hasImageInScreen("investBtn", A=[643, 430, 779, 726])
        # if (investBtn):
        #     wait(lambda: simuInstance.clickPointV2(709, 261), 1)
        #     if (domax):
        #         doMoreTimesWithWait(lambda: simuInstance.clickPointV2(865,388),11,0)
        #     wait(lambda: simuInstance.clickPointV2(
        #         investBtn[0]+30, investBtn[1]+5))
        #     wait(lambda: simuInstance.clickPointV2(1278, 853), 1)
        doAndWaitUntilBy(lambda: simuInstance.clickPointV2(1267,400), lambda:task.hasSingleLineWordsInArea("investment", A=[705,221,799,243]), 2,2,timeout=5)
        if (domax):
            doMoreTimesWithWait(lambda: simuInstance.clickPointV2(860,373),3,0)
        wait(lambda: simuInstance.clickPointV2(758,664))
        doAndWaitUntilBy(lambda: simuInstance.clickPointV2(*task.randomPoint), lambda:not task.hasSingleLineWordsInArea("investment", A=[705,221,799,243]), 2,2,timeout=5)


    def investInCity(self):
        task.print("去投资")
        doMoreTimesWithWait(lambda: simuInstance.clickPointV2(
            *task.rightCatePoint2), 1, 1)
        if(not task.clickInMenu(["bureau"], ["bureau"], startIndex=5)):
            continueWithUntilBy(lambda: simuInstance.clickPointV2(
            *task.rightTopTownIcon), lambda: task.inCityList(self.investmentCities), 3, 30)
            task.clickInMenu(["bureau"], ["bureau"], startIndex=5)

        doAndWaitUntilBy(lambda: simuInstance.clickPointV2(
            39, 81), lambda: task.hasSingleLineWordsInArea("invest", A=task.titleArea), 2,2,timeout=5)
        self.investOnce()
        while (True):
            xxxp = task.getSingleLineWordsInArea(A=[234,803,290,818],ocrType=3)
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
            if(city=="tunnel"):
                task.crossTunnel(goods=False)
                continue
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
