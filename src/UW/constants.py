# Short trips
# cityNames = ["比萨", "热那亚", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
# portgual reputation
cityNames = ["funchal", "lisboa", "faro", "casablanca", "las"]

# cityNames = ["比萨", "热那亚", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]

battleCity = "纳尔维克"
battleCity = "关岛"

# "piratefleet", "assau": ganzi, pillage: banzi, robber: paomen"rob",  ,"assa","rob" ,"assa"
# opponentNames=["lag","illag","llag","pil","assa","asau"]
opponentsInList = ["奇袭","掠夺","强盗"]
# "golitsynpil","golitsynas","azubuikepi","azubuikeas","chenzuyipil","chenzuyias","kaikap","kaikaa"]
# add ducunyong as it's double lines, so quick hack,only checked in board
opponentNames = ["奇袭","掠夺","强盗"]
blackListForBattle = ['piz', 'zpi', 'robeyn', 'masa', 'roberts']
# rob: "rob",
# 汉阳 chowta ass, chenziyu pirate fleet, shiyang ass
# 淡水 azubuike, chenzuyi assu, lalkaika fleet, chowta rob, zubuike pill

# Liquer+
# "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","cheese"],
# "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],

maticBarterTrade = {
    "buyProducts": ["silverware", "coffee", "wine"],
    "villages": ["turk"],
    "buyCities": ["南特", "arguin", "marseille", "热那亚", "algiers", "tunis"],
    "enableVillageTrade": True,
    "sellCity": "塞得港"
}
NEEASupplySell = {
    # "jewllery","tourmaline" ,"handcanno", "flannel","amber"
    "buyProducts": ["amber", "twohand", "felt", "gobelin", "steel", "vodka", "aquavit", "gin", "whisky", "tapestry", "western", "westerncann", "saffron", "azulejo", "almond"],
    "buyCities": ["stockhol", "visby", "beck", "copenhag", "bergen", "edinburgh", "groningen", "amsterda", "london", "dover", "antwerp", "calais", "bristol", "南特", "bordeaux", "porto", "seville", "laga", "marseil", "热那亚", "seville", "laga", "marseil", "热那亚", "seville", "laga", "marseil", "热那亚"],
    "buySupplyCities": [],
    "dumpCrewCities": [""],
    "enableVillageTrade": True,
    "villages": ["日耳曼", "sami", "svea", "sam"],
    "supplyCities": ["seville", "比萨", "热那亚", "bathurst", "sierra", "luanda", "capetown", "塔玛塔夫", "pasay", "杭州"],
    "useSkillCity": None,
    "checkInnCities": True,
    "sellCities": [{"name": "pasay", "types": "BM"},
                   # {"name":"malacca","types":"BM"},{"name":"palembang","types":"BM"},
                   # {"name":"jakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
                   {"name": "淡水", "types": "supply"}, {"name": "燕云", "types": None}]
}
EADoubleBuy = {
    # ,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
    "buyProducts": ["gardenia", "begonia", "sweetolive", "azalea", "tiger'seye", "chinesetea", "agarwood", "ylang-ylang"],
    # "buyProductsAfterSupply": [], flag on enabling buy after supply
    # "buyProductsAfterSupplyCities": [],
    "buyCities": ["naha", "淡水", "杭州", "长安", "汉阳", "济州"],
    "buySupplyCities": [],
    "buyStrategy": "twice",
    "dumpCrewCities": [],
    "useSkillCity": "beck",
    "checkInnCities": ["dublin", 'dover', 'london', '澳门', "江户", '堺', '汉阳', '淡水', "plymouth", "naha"],
    "sellFleet": 2,
    "buyFleet": 4,
    "supplyCities": ["堺", "澳门", "pasay", "塔玛塔夫", "开普敦", "soda", "bathurst", "dublin", "plymouth", "dover", "london"],
    "sellCities": [{"name": "beck", "types": None}],
}
EABuyBM = {
    "buyFleet": 4,
    "buyStrategy": "once",
    # , ,"shaoxingwine", "goryeoceladon","chinesepainting","easterncannon"
    # ,"tiger'seye"],
    "buyProducts": ["gardenia", "begonia", "sweetolive", "azalea"],
    # ,"泉州","淡水","杭州","长安","汉阳","济州","澳门",],
    "buyCities": ["汉阳", "东莱", "济州", "杭州", "淡水"], 
    "deductBuyBM": True,
    "checkInnCities": ['堺', "江户", '汉阳', '杭州', "东莱", "济州", "淡水"],
    "buySupplyCities": [],
    "dumpCrewCities": [],
    "supplyCities": [],
    "sellCities": [],
}

## yawuru or kalkat
yaruruOrKalkaOri="yawuru"
def getYawuruOrKalka(secondVillage=False):
    if(secondVillage):
        return yaruruOrKalkaOri[:-1]
    return yaruruOrKalkaOri

## witoto or varo
witotoOrVaro="witoto"
def getWitotoOrVaro(secondVillage=False):
    if(secondVillage):
        return witotoOrVaro[:-1]
    return witotoOrVaro

apache = {
    "villageName": "阿帕奇",
    "buys": [
        # sequence has to map in game display
        {"product": "白金", "cities": [
            "纳塔尔", "索法拉", "克利马内"], "targetNum": 542},
        {"product": "夜来香", "cities": [
            "基尔瓦", "桑给巴尔", "摩加迪沙"], "targetNum": 600}
    ],
    "buyCities": ["纳塔尔", "索法拉", "克利马内", "莫桑比克", "基尔瓦", "桑给巴尔", "摩加迪沙"],
    "supplyCities": ["开普敦", "乌斯怀亚", "利马", "阿卡普尔科"],
    "buyProducts": ["白金", "夜来香"],
    "checkInnCities": True,
    "afterVillageSupplyCities": ["阿卡普尔科"],
    # (index, val) array
    "tradeObjects": [(0, 2), (1, 2), (2, 2),(3,2)],
    "cleanupIndex": 3,
    "buyStrategy": "twice",
    "useGemCities": [],
    "supplyFleet": 2,
    "barterFleet": 3,
    "barterFirstRoundCount":4
}

apachewine = {
    "villageName": "阿帕奇",
    # "buys": [
    #     # sequence has to map in game display
    #     {"product":"silver","cities":[],"targetNum":402},
    #     {"product":"coral","cities":[],"targetNum":600}
    # ],
    "buyCities": ["索法拉", "克利马内", "capetown", "tom","verde", "las", "santo", "trujillo", "portobelo", "santo", "bahia", "tom", "verde", "las", "bahia", "buenos", "乌斯怀亚", "copia", "guate", "阿卡普尔科"],
    "supplyCities": ["阿卡普尔科"],
    "buyProducts": ["silver", "coral"],
    "buyNotProducts": ["work"],
    "checkInnCities": True,
    "afterVillageSupplyCities": ["阿卡普尔科"],
    # (index, val) array
    "tradeObjects": [(0, 1), (1, 1), (2, 1)],
    "cleanupIndex": 2,
    "buyStrategy": "useGem",
    "useGemCities": ["tom"],
    "supplyFleet": 2,
    "barterFleet": 3
}
witoto = {
    "villageName": getWitotoOrVaro(),
    "buys": [
        # sequence has to map in game display
        {"product": "noni", "cities": [
            "kuching", "jakarta", "makassar"], "targetNum": 400},
        {"product": "mangosteen", "cities": [
            "malacca", "aceh"], "targetNum": 200},
        {"product": "benzoin", "cities": [
            "prey", "malacca", "pasay"], "targetNum": 450}
    ],
    "useFishing": True,
    "buyCities": ["prey", "kuching", "malacca", "jakarta", "makassar", "pasay", "aceh"],
    "supplyCities": ["aceh", "塔玛塔夫", "开普敦", "soda", "pernambuco", "cayenne"],
    "buyProducts": ["noni", "mangosteen", "benzoin"],
    "checkInnCities": True,
    "afterVillageSupplyCities": ["cayenne"],
    # (index, val) array
    "tradeObjects": [(0, 2), (1, 2), (2, 2)],
    "cleanupIndex": 2,
    "buyStrategy": "once",
    "useGemCities": [],
    "supplyFleet": 2,
    "barterFleet": 3
}
quechuas = {
    "villageName": "quechuas",
    "buyCities": ["kuching", "aceh","摩加迪沙","桑给巴尔","基尔瓦","莫桑比克","开普敦","buenos","乌斯怀亚","valpara", "copia", "tumbes", "利马"],
    # "buyCities": ["kuching", "aceh","摩加迪沙","桑给巴尔","基尔瓦","莫桑比克","摩加迪沙","桑给巴尔","基尔瓦","开普敦","bahia","rio","buenos","乌斯怀亚","valpara", "copia","阿卡普尔科","利马"],
    "supplyCities": ["利马"],
    "buyProducts": ["coal", "silver","gold"],
    "buyNotProducts": ["golddust","goldware"],
    "checkInnCities": True,
    "afterVillageSupplyCities": ["利马"],
    # (index, val) array
    "tradeObjects": [(0, 0), (1, 0), (2, 0),(3, 0)],
    "cleanupIndex": 3,
    "buyStrategy": "useGem",
    "useGemCities": ["kuching","copia"],
    "supplyFleet": 2,
    "barterFleet": 3,
    "barterFirstRoundCount":4
}

svear = {
    "villageName": "日耳曼",
    "buyCities": ["santa", "seville", "dublin", "amsterda"],
    "checkInnCities": True,
    "supplyCities": ["visby"],
    "buyProducts": ["candle", "matchlock", "iron", "lron"],
    # (index, val) array
    "tradeObjects": [(0, 0), (1, 1), (2, 1)],
    "cleanupIndex": 2,
    "buyStrategy": "",
    "useGemCities": ["santa"],
    "barterFleet": 3
}
svearWLumber = {
    "villageName": "日耳曼",
    "buyCities": ["santa", "barcelona","seville", "dublin", "amsterda","oslo","riga"],
    "checkInnCities": True,
    "supplyCities": ["visby"],
    "leaveGoods": ["lumber"],
    "buyProducts": ["candle", "matchlock", "iron", "lron", "birch","lumber"],
    # (index, val) array
    # "tradeObjects": [(0, 0), (1, 1), (2, 1)],
    "tradeObjects": [(0, 0), (1, 0), (2, 1),(3,1)],
    "cleanupIndex": 3,
    "buyStrategy": "",
    "useGemCities": ["santa"],
    "barterFleet": 3,
    "barterFirstRoundCount":4
}

yawuru= {
    "villageName": getYawuruOrKalka(),
    "checkInnCities": True,
    "buys": [
        # sequence has to map in game display
        {"product": "lumber", "cities": [], "targetNum": 170},
        {"product": "gold", "cities": [
         "萨马赖", "pinjarra"], "targetNum": 260},
        {"product": "kris", "cities": [
            "jakarta", "surabaya"], "targetNum": 260}
    ],
    "buyProducts": ["kris", "gold","lumber"],
    "buyCities": ["萨马赖", "pinjarra","jakarta", "surabaya"],
    "supplyCities": ["kakatuwah"],
    "tradeObjects": [(0, 1), (1, 1), (2, 1),(3, 1)],
    "cleanupIndex": 3,
    "buyStrategy": "twice",
    "useGemCities": ["萨马赖"],
    "barterFleet": 3,
    "barterFirstRoundCount":4
}
sami = {
    "villageName": "sami",
    "shortVillageName": "s",
    "buyCities": ["santa", "seville", "dublin", "amsterda"],
    "supplyCities": ["bergen"],
    "buyProducts": ["candle", "matchlock", "iron", "lron"],
    "tradeObjects": [(0, 0), (1, 0), (2, 1),(3,1)],
    "cleanupIndex": 3,
    "buyStrategy": "",
    "useGemCities": ["santa"],
    "barterFleet": 7,
    "barterFirstRoundCount":4
}
samiWLumber = {
    "villageName": "sami",
    "shortVillageName": "s",
    "buyCities": ["santa", "barcelona","seville", "dublin", "amsterda","oslo","riga"],
    "supplyCities": ["bergen"],
    "leaveGoods": ["lumber"],
    "buyProducts": ["candle", "matchlock", "iron", "lron", "birch","lumber"],
    "tradeObjects": [(0, 0), (1, 0), (2, 1),(3,1)],
    "cleanupIndex": 3,
    "buyStrategy": "",
    "useGemCities": ["santa"],
    "barterFleet": 7,
    "barterFirstRoundCount":4
}
villageTradeList = {
    "turk": {
        "villageName": "turk",
        "buyCities": ["南特", "arguin", "algiers", "热那亚", "比萨", "tunis"],
        "checkInnCities": True,
        "supplyCities": ["antalya"],
        "buyProducts": ["silverware", "coffee", "wine"],
        # (index, val) array
        "tradeObjects": [(0, 0), (1, 0)],
        "cleanupIndex": 1,
        "buyStrategy": "useGem",
        "useGemCities": ["arguin"],
        "barterFleet": 3
    },
    "apache": apache,
    "apach": {
        **apache,
        "tradeObjects": [(0, 2), (1, 2), (2, 2)],
        "cleanupIndex": 2
    },
    "apac": {
        **apache,
        "tradeObjects": [(0, 2), (1, 2), (2, 2)],
        "cleanupIndex": 2
    },
    "apachewine": apachewine,
    "apachwine": apachewine,
    "apacwine": apachewine,
    "witoto": witoto,
    "witot": {
        **witoto,
        "villageName": getWitotoOrVaro(True)
    },
    "quechuas": quechuas,
    "quechua": {
        **quechuas,
        "tradeObjects": [(0, 0), (1, 0), (2, 0)],
        "cleanupIndex": 2
    },
    "svear": svear,
    "svea": {
        **svear
    },
    "svearWLumber": svearWLumber,
    "sveaWLumber": {
        **svearWLumber,
        "tradeObjects": [(0, 0), (1, 1), (2, 1)],
        "cleanupIndex": 2
    },
    "sami": sami,
    "sam": {
        **sami,
        "villageName": "sam",
        "tradeObjects": [(0, 0), (1, 1), (2, 1)],
        "cleanupIndex": 2
    },
    "samiWLumber": samiWLumber,
    "samWLumber": {
        **samiWLumber,
        "villageName": "sam",
        "tradeObjects": [(0, 0), (1, 1), (2, 1)],
        "cleanupIndex": 2
    },
    "yawuru": yawuru,
    "yawur": {
        **yawuru,
        "villageName": getYawuruOrKalka(True),
        "tradeObjects": [(0, 1), (1, 1), (2, 1)],
        "cleanupIndex": 2,
    }
}

# Init option
# Route choice: Must-set 0: mar-May-spring(SEA-Carrebean),1: Jun-Aug-Summer(Carrebean-EA),2: Sep-Oct Aut, Carrebean-EA,3: Winter Nov-Feb, Carrebean-EA
# 4 summer, 5autumn, 6winter 7 spring
# v1 trade mapping
monthToRoute = {
    "3": 7,
    "4": 7, "5": 7, "6": 4,
    "7": 4, "8": 4, "9": 5,
    "10": 5, "11": 5, "12": 6,
    "1": 6, "2": 6
}
bartingMonthToRoute = {
    "3": 9,
    "4": 9, "5": 9, "6": 9,
    "7": 9, "8": 9, "9": 9,
    "10": 9, "11": 9, "12": 9,
    "1": 9, "2": 9
}
dailyJobConf = {
    "merchatQuestCity": "南特",
    "buffCity": "davao",
    "basicFleet":2,
    "landingFleet": 5,
    "preLandingCity": "cohasset",
    "landingCity": "cohasset",
    "battleFleet": 1,
    "endBattleCity": "江户",
    "landingTimes": 90,
    "landingRounds": 2,
    "reportAndAdvQuestCity": "江户",
    "battleQuest": True,
    "gotoBattlecity": ["kakatuwah", "gari"],
    "leaveBattlecity": ["gari", "kakatuwah"],
    "negoTimes": 35
}
checkInnCities=["比萨","热那亚"]
checkInnCitiesBack = ['bathurst', "elmina", "亚丁", 'sierra', "barcelona", "marseille", "palma","比萨","cairo","beirut", "saint", "plymouth","beck","amsterda","dover","visby", "santo", "royal","portobelo","cohasset" "trujillo","panama", "索科特拉", "aceh", "pasay", "banjarmasin","jakarta", "纳塔尔","塔玛塔夫","索法拉", "克利马内", "莫桑比克", "基尔瓦", "桑给巴尔", "摩加迪沙", "乌斯怀亚", "copia", "tumbes", "南特", "arguin", "热那亚", "比萨", "algiers", "tunis", "santa","ceuta", "dublin", "amsterda", "bremen", "汉阳","东莱","济州","堺", "长崎", "杭州", "泉州","安平","澳门", "淡水", "malacca","manila","brunei","surabaya", "ceylon","gari", "pinjarra","萨马赖","hobart", "suva","mahina","atuona","soda", "pernambuco", "cayenne"]

svearRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["santa", "seville", "杭州"],
    "enableVillageTrade": True,
    "useFishingCities": [],
    "villages": ["svear"],
    "afterVillageBuyCities": [],
    "supplyCities":["bremen","seville","tunis","塞得港","tunnel",{"route": 2, "target": "杭州"}],
    "sellFleet": 2,
    "useSkillCity": "苏伊士",
    "checkInnCities": True,
    "sellPriceIndexByName": "versl",
    "sellCityOptions": ["杭州", "澳门", "泉州", "淡水", "安平", "燕云", "北京", "长安", "重庆"],
    "forceUseSequenceOptions": False,
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["汉阳", "济州", "江户", "长崎", "东莱", "迎日", "德源", "堺"]
        }
    ],
    "sellCities": [{"name": "苏伊士", "types": None}],
    "fashions": ["赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": []
}

svearWLumberRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["santa"],
    "enableVillageTrade": True,
    "useFishingCities": [],
    "villages": ["svearWLumber"],
    "afterVillageBuyCities": [],
    "supplyCities":["beck","bremen","plymouth","南特","palma","热那亚","比萨","cairo","塞得港","tunnel",{"route": 2, "target": "杭州"}],
    "sellFleet": 2,
    "useSkillCity": False,
    "checkInnCities": True,
    "sellPriceIndexByName": "versl",
    "sellCityOptions": ["杭州", "澳门", "泉州", "淡水", "安平", "燕云", "北京", "长安", "重庆"],
    "forceUseSequenceOptions": False,
    "onlySellTypes": ["crafts"],
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["汉阳", "济州", "江户", "长崎", "东莱", "迎日", "德源", "堺"]
        }
    ],
    "fashions": ["赞助"],
    "waitForFashion": False,
    "waitHour": 1,
    "afterSellCities": []
}

yawuruRouteBase={
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["jakarta"],
    "villages": ["yawuru"],
    "enableVillageTrade": True,
    "useFishingCities": ["panama"],
    "afterVillageBuyCities": [],
    "sellFleet": 2,
    "supplyCities":["萨马赖","atuona","panama","tunnel","royal","santo"],
    "useSkillCity": "portobelo",
    "checkInnCities": True,
    "sellCityOptions": ["santo","veracruz","rida","trujillo","portobelo","cartagena","maracaibo","willemstad","caracas","porlamar","juan","santiago","royal","southside","havana","nassau"],
    "forceUseSequenceOptions": False,
    "fashions": ["赞助","繁荣"],
    "waitForFashion": True,
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "goToCityForTrade": "hamburg",
            "cities": ["beck","saint","kokkola","riga","stockhol", "gda","visby", "copenhag","oslo", "bergen", "edinburgh", "hamburg","bremen","groningen", "amsterda", "london", "dover", "antwerp"]
        }
    ],
    "waitHour": 1,
    "afterSellCities": ["santa"]
}

samiRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["santa", "seville", "杭州"],
    "enableVillageTrade": True,
    "useFishingCities": [],
    "villages": ["sami"],
    "afterVillageBuyCities": [],
    "supplyCities":["南特","热那亚","比萨","塞得港","tunnel",{"route": 2, "target": "杭州"}],
    "sellFleet": 7,
    "useSkillCity": False,
    "checkInnCities": True,
    "sellPriceIndexByName": "versl",
    "sellCityOptions": ["杭州", "澳门", "泉州", "淡水", "安平", "燕云", "北京", "长安", "重庆"],
    "forceUseSequenceOptions": False,
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["汉阳", "济州", "江户", "长崎", "东莱", "迎日", "德源", "堺"]
        }
    ],
    "sellCities": [{"name": "苏伊士", "types": None}],
    "fashions": ["赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": []
}
samiWLumberRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["santa"],
    "enableVillageTrade": True,
    "useFishingCities": [],
    "villages": ["samiWLumber"],
    "afterVillageBuyCities": [],
    "supplyCities":["南特","热那亚","比萨","塞得港","tunnel",{"route": 2, "target": "杭州"}],
    "sellFleet": 7,
    "useSkillCity": False,
    "checkInnCities": True,
    "sellPriceIndexByName": "versl",
    "sellCityOptions": ["杭州", "澳门", "泉州", "淡水", "安平", "燕云", "北京", "长安", "重庆"],
    "forceUseSequenceOptions": False,
    "onlySellTypes": ["crafts"],
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["汉阳", "济州", "江户", "长崎", "东莱", "迎日", "德源", "堺"]
        }
    ],
    "fashions": ["赞助"],
    "waitForFashion": False,
    "waitHour": 1,
    "afterSellCities": []
}
apacheRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["索法拉"],
    "enableVillageTrade": True,
    "useFishingCities": ["乌斯怀亚"],
    "villages": ["apache"],
    # "afterVillageBuyCities": ["阿卡普尔科"],
    "supplyCities": [{"route": 3, "target": "亚丁"}],
    "sellFleet": 2,
    "useSkillCity": "苏伊士",
    "checkInnCities": True,
    "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "goToCityForTrade": "莫桑比克",
            "cities": ["克利马内", "莫桑比克", "塔玛塔夫", "基尔瓦", "桑给巴尔", "蒙巴萨", "马林迪", "摩加迪沙"]
        }
    ],
    "fashions": ["奢华", "赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": ["苏伊士"]
}

quechuasRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["kuching"],
    "enableVillageTrade": True,
    "useFishingCities": ["乌斯怀亚","开普敦"],
    "villages": ["quechuas"],
    "supplyCities": ['乌斯怀亚', 'town', '亚丁'],
    "sellFleet": 2,
    "useSkillCity": True,
    "checkInnCities": True,
    "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "go", "val": "苏伊士"},
                {"type": "tunnel"},
                {"type": "goSellCity"},
                {"type": "sell"},
                {"type": "go", "val": "塞得港"},
                {"type": "tunnel"}
            ],
            "cities": ["亚历山德", "cairo", "塞得港", "jaffa", "beirut", "nicosia", "antalya", "candia", "trabzon", "benghazi"]
        },
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["克利马内", "莫桑比克", "塔玛塔夫", "基尔瓦", "桑给巴尔", "蒙巴萨", "马林迪", "摩加迪沙"]
        }
    ],
    "fashions": ["奢华", "赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": ["苏伊士"]
}
witotoRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["prey", "德源"],
    "enableVillageTrade": True,
    "useFishingCities": [],
    "villages": ["witoto"],
    "afterVillageBuyCities": [],
    "supplyCities": ["elmina", "开普敦", "塔玛塔夫", "pasay", "东莱"],
    "sellFleet": 2,
    # "useSkillCity":"苏伊士",
    "checkInnCities": True,
    "sellCityOptions": ["汉阳", "济州", "东莱", "迎日", "德源", "江户", "长崎", "堺"],
    "fashions": ["赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": ["汉阳", "安平", "malacca", "摩加迪沙"]
}
routeLists = [
    # northEu liquor Dec-Feb(Inc)Winter+, mar-May(Spring)STD, Jun-(Summer)-
    # EA: Perfume: Dec-Feb(Winter),STD, Mar-May(Spring)-, Jun-(Summer)Aug STD,Sep-Nov(Autumn)++
    # Carrebean: Nov-May: Liquor,Lux+    Jun-Oct: Dye,Gem+

    # 0 SEA-Carrebean  mar-May-spring
    [
        # harvest
        {
            "buyFleet": 4,
            "buyProducts": ["opal", "tequila", "pineapple", "logwood"],
            "buyCities": ["havana", "southside", "roya", "santiago"],
            "buySupplyCities": [],
            "buyStrategy": "twice",
            "dumpCrewCities": [],
            "supplyCities": ["juan", "verde", "elmina", "luanda", "capetown", "塔玛塔夫", "pasay"],
            # "sellCities":[{"name":"malacca","types":["liquor"]},{"name":"pasay","types":None}],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malacca", "types": "BM"}, {"name": "澳门", "types": ["placeholder"]}, {"name": "长安", "types": None}, {"name": "汉阳", "types": "BM"}, {"name": "济州", "types": "BM"}, {"name": "palembang", "types": "BM"}, {"name": "jakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {"name": "banjarmasin", "types": ["placeholder"]}],
            "sellFleet": 2,
        },
        {
            # blueprint 1 perfume to spice
            "buyFleet": 4,
            "buyProducts": ["ebony", "agarwood", "ylang-ylang", "musk", "mace", "kris", "mangosteen"],
            "buyCities": ["banda", "ambon", "ternate", "jolo", "makassar", "banjarmasin", "jakarta", "pasay", "aceh"],
            "buySupplyCities": [],
            "buyStrategy": "twice",
            "dumpCrewCities": [],
            "supplyCities": ["pasay", "塔玛塔夫", "开普敦", "pernambuco", "cayenne", "caracas"],
            "useSkillCity": "rida",
            "sellCities": [{"name": "rida", "types": ["perfume", "dye"]}, {"name": "veracruz", "types": "BM"}, {"name": "southside", "types": None}],
            "sellFleet": 2,
        },
    ],
    # 1 Summer Jun-Aug, Carrebean-EA,
    [
        {
            "buyProducts": ["opal", "tequila", "pineapple", "logwood"],
            "buyCities": ["southside", "roya", "willemstad", "porlamar", "caracas", "juan"],
            "buyStrategy": "twice",
            "buySupplyCities": [],
            "dumpCrewCities": [],
            "supplyCities": ["juan", "verde", "elmina", "luanda", "capetown", "塔玛塔夫", "pasay"],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malacca", "types": "BM"}, {"name": "palembang", "types": "BM"},
                           {"name": "jakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {
                               "name": "banjarmasin", "types": "BM"},
                           {"name": "davao", "types": ["dye"]}, {"name": "淡水", "types": [
                               "placeholder"]}, {"name": "长安", "types": None}
                           ]
        },
        # {
        #     **NEEASupplySell,
        #     "buyFleet":4,
        #     "buyStrategy":"twice",
        #     "buyProducts": ["twohand","lilyof","felt","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
        #     "buyCities":["hamburg","bremen","london","dover","calais","plymouth","bristol","bordeaux","seville","laga"],
        #     "sellFleet":2,
        # },
        EABuyBM,
        {
            **EADoubleBuy,
            "supplyCities": ["澳门", "pasay", "塔玛塔夫", "开普敦", "pernambuco", "cayenne", "caracas"],
            "useSkillCity": "maracaibo",
            "sellCities": [{"name": "maracaibo", "types": None}, {"name": "veracruz", "types": "BM"}],
        }
    ],

    # 2 Autumn Sep-Oct, Carrebean-EA, EA-perfume+, Carrebean-dey+ (Nov EA+, carrebean dye-, luxury+)
    [
        {
            "buyProducts": ["opal", "tequila", "pineapple", "logwood"],
            "buyCities": ["southside", "roya", "willemstad", "porlamar", "caracas", "juan"],
            "buyStrategy": "twice",
            "buySupplyCities": [],
            "dumpCrewCities": [],
            "supplyCities": ["juan", "verde", "elmina", "luanda", "capetown", "塔玛塔夫", "pasay"],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malacca", "types": "BM"}, {"name": "palembang", "types": "BM"},
                           {"name": "jakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {
                               "name": "banjarmasin", "types": "BM"},
                           {"name": "davao", "types": ["dye", "jewelry"]}, {
                               "name": "淡水", "types": ["placeholder"]}, {"name": "长安", "types": None}
                           ]
        },
        EABuyBM,
        {
            **EADoubleBuy,
            # ,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
            "buyProducts": ["gardenia", "sweetolive", "azalea", "chinesetea", "agarwood", "ylang-ylang"],
            "buyCities": ["naha", "杭州", "长安", "汉阳"],
            "supplyCities": ["澳门", "pasay", "塔玛塔夫", "开普敦", "pernambuco", "cayenne", "caracas"],
            "useSkillCity": "maracaibo",
            "sellCities": [{"name": "maracaibo", "types": None}, {"name": "veracruz", "types": "BM"}],
        },
    ],

    # 3 Winter Nov-Feb, Carrebean-EA, EA-perfume->, Carrebean-luxury+ (Nov EA+, carrebean dye-, luxury+)
    [
        {
            "buyFleet": 4,
            "buyProducts": ["opal", "tequila", "pineapple", "logwood"],
            "buyCities": ["havana", "southside", "roya", "santiago"],
            "buySupplyCities": [],
            "buyStrategy": "twice",
            "dumpCrewCities": [],
            "sellFleet": 2,
            "supplyCities": ["juan", "verde", "elmina", "luanda", "capetown", "塔玛塔夫", "pasay"],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malacca", "types": "BM"}, {"name": "palembang", "types": "BM"},
                           {"name": "jakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {
                               "name": "banjarmasin", "types": "BM"},
                           {"name": "淡水", "types": ["placeholder"]}, {
                "name": "长安", "types": None}
            ]
        },
        EABuyBM,
        {
            **EADoubleBuy,
            "supplyCities": ["澳门", "pasay", "塔玛塔夫", "开普敦", "pernambuco", "cayenne", "caracas"],
            "useSkillCity": "maracaibo",
            "sellCities": [{"name": "maracaibo", "types": None}, {"name": "veracruz", "types": "BM"}],
        }
    ],
    # 4 Summer Jun-Aug, NorthE-EA
    [
        {
            **NEEASupplySell,
            "buyFleet": 4,
            "buyStrategy": "twice",
            "buyProducts": ["twohand", "lilyof", "felt", "gobelin", "woodenshoe", "steel", "vodka", "aquavit", "gin", "whisky", "tapestry", "western", "westerncann", "saffron", "azulejo", "almond"],
            "buyCities": ["hamburg", "bremen", "london", "dover", "den", "antwerp", "bristol", "bordeaux", "seville", "laga"],
            "sellFleet": 2,
        },
        # EABuyBM,
        {
            **EADoubleBuy,
            "buyProductsAfterSupply": ["chinesepainting", "shubrocade", "candycraft", "amethyst", "yosegi", "sweetolive"],
            "buyProductsAfterSupplyCities": ["长安", "江户", "长崎", "堺", "杭州"]
        }
    ],
    # 5 Autumn Sep-Nov, NE-EA, EA-perfume+
    [
        {
            **NEEASupplySell,
            "buyFleet": 4,
            "buyStrategy": "twice",
            "buyProducts": ["twohand", "lilyof", "felt", "gobelin", "woodenshoe", "steel", "vodka", "aquavit", "gin", "whisky", "tapestry", "western", "westerncann", "saffron", "azulejo", "almond"],
            "buyCities": ["bremen", "london", "dover", "den", "antwerp", "bristol", "bordeaux", "seville", "laga"],
            "sellFleet": 2,
        },
        # EABuyBM,
        {
            **EADoubleBuy,
            "buyProducts": ["gardenia", "sweetolive", "azalea", "chinesetea", "agarwood", "ylang-ylang"],
            "buyProductsAfterSupply": [],
            "buyCities": ["naha", "杭州", "长安", "汉阳"],
        }
    ],
    # 6 Winter Dec-Feb, NE-EA, EA-perfume->, liquor+
    [
        {
            **NEEASupplySell,
            "buyFleet": 4,
            "buyStrategy": "twice",
            "buyProducts": ["twohand", "lilyof", "gobelin", "steel", "vodka", "gin", "whisky", "tapestry", "western", "westerncann", "saffron", "azulejo", "almond"],
            "buyCities": ["saint", "stockhol", "visby", "riga", "edinburgh", "groningen", "amsterda", "london", "dover"],
            "sellFleet": 2,
        },
        # EABuyBM,
        {
            **EADoubleBuy,
            "buyProductsAfterSupply": ["chinesepainting", "shubrocade", "candycraft", "amethyst", "yosegi", "sweetolive"],
            "buyProductsAfterSupplyCities": ["长安", "江户", "长崎", "堺", "杭州"]
        }
    ],
    # 7 Spring Dec-Feb, NE-EA, EA-perfume->, liquor+
    [
        {
            **NEEASupplySell,
            "buyFleet": 4,
            "buyStrategy": "twice",
            "buyProducts": ["twohand", "lilyof", "gobelin", "steel", "vodka", "gin", "whisky", "tapestry", "western", "westerncann", "saffron", "azulejo", "almond"],
            "buyCities": ["saint", "stockhol", "visby", "riga", "edinburgh", "groningen", "amsterda", "london", "dover", "santa"],
            "sellFleet": 2,
        },
        # EABuyBM,
        {
            **EADoubleBuy,
            "buyProducts": ["begonia", "tiger'seye", "gardenia", "sweetolive", "azalea", "chinesetea", "agarwood", "ylang-ylang", "chinesepainting", "shubrocade", "easterncannon", "goryeo"],
            "buyProductsAfterSupply": ["horseback", "japanesepainting", "candycraft", "amethyst", "nishijin", "yosegi", "sweetolive"],
            "buyProductsAfterSupplyCities": ["江户", "长崎", "堺", "杭州"]
        }
    ],
    # svear+witoto， #8
    [
        {
            **svearRouteBase,
            "buyCities": ["santa"],
            "villages": ["svear"],
            "afterSellCities": ["泉州"]
        },
        {
            **witotoRouteBase,
            "buyCities": ["prey", "德源"],
            "villages": ["witoto"],
            "afterSellCities": ["汉阳", "长崎","泉州", "manila", "ceylon","塔玛塔夫", "开普敦", "soda", "bathurst"]
        },
        {
            **svearRouteBase,
            "buyCities": ["seville", "杭州"],
            "villages": ["svea"],
            "afterSellCities": ["长崎","泉州", "manila", "亚丁", "苏伊士"]
        },
        {
            "buyCities": ["苏伊士"],
            "mode": "tunnel",
            "supplyCities": ["barcelona"],
        },
        # {"mode": "landing"},
        {
            "buyCities": ["南特"],
            "mode": "merchantQuest",
            "supplyCities": ["索科特拉", "manila"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao"],
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["江户"]
         },
        {
            **witotoRouteBase,
            "buyCities": ["kuching"],
            "villages": ["witot"],
            "afterSellCities": ["汉阳", "长崎","泉州", "manila", "塔玛塔夫", "开普敦", "soda", "bathurst"]
        }
    ],
    # wine+witoto #9
    [
        # apache wine replacement
        {
            **apacheRouteBase,
            "villages": ["apachewine"],
            "sellFleet": 2,
            "buyCities": ["纳塔尔","阿卡普尔科"],
            "afterSellCities": ["索科特拉"],
            "useSkillCity": False,
            "sellCityOptions": ["克利马内", "莫桑比克", "塔玛塔夫", "基尔瓦", "桑给巴尔", "蒙巴萨", "马林迪", "摩加迪沙"],
            "waitForFashion": False
        },
        {
            **witotoRouteBase,
            "buyCities": ["prey", "德源","santa","杭州","阿卡普尔科"],
            "villages": ["witoto"],
            "afterSellCities": ["汉阳", "长崎", "泉州", "manila", "ceylon"]
        },
        {
            **apacheRouteBase,
            "sellFleet": 2,
            "villages": ["apacwine"],
            "buyCities": ["索法拉", "乌斯怀亚"],
            "sellCityOptions": ["克利马内", "莫桑比克", "塔玛塔夫", "基尔瓦", "桑给巴尔", "蒙巴萨", "马林迪", "摩加迪沙"],
            "afterSellCities": ["ceylon", "manila", "davao"]
        },
        {
            "mode": "buff",
            "buyCities": ["davao"],
            "supplyCities": ["江户"],
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "关岛","切尔斯基","ezo"],
            # "supplyCities": ["长崎","杭州","澳门","malacca", "ceylon","苏伊士"],
            "checkInnCities": True
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["江户","安平","萨马赖"],
            "checkInnCities": True,
            "supplyCities": ["长崎","杭州","澳门","brunei","surabaya", "ceylon","苏伊士"],
        },
        {
            "buyCities": ["苏伊士"],
            "mode": "tunnel",
            "supplyCities": ["ceuta"],
        },
        {
            "buyCities": ["cohasset"],
            "mode": "newlanding",
            "supplyCities": ["ceuta","塞得港"]
        },
        {
            "buyCities": ["塞得港"],
            "mode": "tunnel",
            "supplyCities": ["ceylon"],
        },
        # {
        #     "buyCities": ["南特","seville","santa","jakarta"],
        #     "mode": "merchantQuest",
        #     "supplyCities": ["索科特拉", "manila", "ambon", "ternate"],
        #     "checkInnCities": True
        # },
        {
            **witotoRouteBase,
            "buyCities": ["kuching","莫桑比克","azores","jakarta","brunei"],
            "villages": ["witot"],
            "afterSellCities": ["汉阳", "长崎", "泉州", "banjarmasin", "manila", "ceylon"]
        }
        # check passed day or pause
    ],
    # 10 crafts+witoto
    [
        {
            **apacheRouteBase,
            "villages": ["apache"],
            "buyCities": ["纳塔尔"],
            "afterSellCities": ["索科特拉", "aceh"]
        },
        {
            **witotoRouteBase,
            "buyCities": ["prey", "德源"],
            "villages": ["witoto"],
            "afterSellCities": ["汉阳", "长崎", "泉州", "banjarmasin", "malacca", "ceylon"]
        },
        {
            **apacheRouteBase,
            "villages": ["apach"],
            "buyCities": ["索法拉", "乌斯怀亚"],
            "afterSellCities": ["苏伊士"]
        },
        {
            "buyCities": ["苏伊士"],
            "mode": "tunnel",
            "supplyCities": ["barcelona"],
        },
        # {"mode": "landing"},
        {
            "buyCities": ["南特"],
            "mode": "merchantQuest",
            "supplyCities": ["ceylon", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "关岛"],
        },
        {"mode": "reportAndAdvQuest",
            "buyCities": ["江户"]
         },
        {
            **witotoRouteBase,
            "buyCities": ["kuching"],
            "villages": ["witot"],
            "afterSellCities": ["汉阳", "长崎", "泉州", "banjarmasin", "malacca", "ceylon"]
        }
        # check passed day or pause
    ],
    # 11 pipe pipe
    [
        {
            **svearRouteBase,
            "buyCities": ["santa"],
            "useSkillCity": False,
            "forceUseSequenceOptions": True,
            "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "塞得港"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["苏伊士"]
                }
            ],
            "afterSellCities": ["ceylon"]
        },
        {
            **quechuasRouteBase,
            "buyCities": ["kuching"],
        },
        {
            **quechuasRouteBase,
            "buyCities": ["kuching"],
        },
        {
            "buyCities": ["苏伊士"],
            "mode": "tunnel"
        },
        {
            "buyCities": ["南特"],
            "mode": "merchantQuest",
            "supplyCities": ["ceylon", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "关岛"],
            #"supplyCities": ["malacca", "亚丁","苏伊士"],
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["江户","安平"],
            "supplyCities": ["malacca", "ceylon","苏伊士"],
        },

        {
            "mode": "tunnel"
        },
        {
            **samiRouteBase,
            "buyCities": ["azores"],
            "villages": ["sami"],
            "forceUseSequenceOptions": True,
            "waitForFashion": False,
            "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "塞得港"},
                        {"type": "tunnel","val": True},
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["苏伊士"]
                }
            ],
        },
        # {
        #     "mode": "tunnel"
        # },
        # {
        #     **samiRouteBase,
        #     "buyCities": ["seville"],
        #     "villages": ["sam"],
        #     "forceUseSequenceOptions": True,
        #     "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
        #     "secondSellOptions": [
        #         {
        #             "seqs": [
        #                 {"type": "go", "val": "塞得港"},
        #                 {"type": "tunnel","val": True},
        #                 # getBestPriceCity will use sellCityOptions to override the sell city
        #                 {"type": "getBestPriceCity"},
        #                 {"type": "goSellCity"},
        #                 {"type": "sell"}
        #             ],
        #             "cities": ["苏伊士"]
        #         }
        #     ]
        # }
        # check passed day or pause
    ],
    #12 express daily
     [
        {
            **apacheRouteBase,
            "sellFleet": 2,
            "supplyCities": ["panama"],
            "forceUseSequenceOptions": True,
            "sellCityOptions": ["beck","saint","kokkola","riga","stockhol", "gda","visby", "copenhag","oslo", "bergen", "edinburgh", "hamburg","bremen","groningen", "amsterda", "london", "dover", "antwerp"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "tunnel","val": True},
                        {"type": "go", "val": "santa"},
                        {"type": "go", "val": "plymouth"},
                        {"type": "go", "val": "beck"},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["beck"]
                }
            ],
            "villages": ["apache"],
            "buyCities": ["纳塔尔","阿卡普尔科"],
            "afterSellCities":["dover","南特"]
        },
        {
            **samiRouteBase,
            "buyCities": ["santa"],
            "villages": ["sami"],
            "useSkillCity": False,
            "forceUseSequenceOptions": True,
            "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "塞得港"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["苏伊士"]
                }
            ],
            "afterSellCities": ["摩加迪沙"]
        },
        {
            **apacheRouteBase,
            "sellFleet": 2,
            "villages": ["apach"],
            "supplyCities": ['利马', '乌斯怀亚', 'town', '亚丁'],
            "useFishingCities": ["乌斯怀亚","开普敦"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["克利马内", "莫桑比克", "塔玛塔夫", "基尔瓦", "桑给巴尔", "蒙巴萨", "马林迪", "摩加迪沙"]
                }
            ],
            "buyCities": ["索法拉"],
            "afterSellCities": ["ceylon", "manila", "davao"]
        },
        {
            "mode": "buff",
            "buyCities": ["davao"],
            "supplyCities": ["江户"],
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "关岛","ezo","切尔斯基"],
            # "supplyCities": ["长崎","杭州","澳门","malacca", "ceylon","苏伊士"],
            "checkInnCities": True
        },
        # {
        #     "buyCities": ["切尔斯基"],
        #     "mode": "landing",
        #     "checkInnCities": True
        # },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["江户","安平"],
            "checkInnCities": True,
            "supplyCities": ["堺","东莱","ceylon","苏伊士"],
        },
        {
            "buyCities": ["苏伊士"],
            "mode": "tunnel",
            "supplyCities": ["ceuta"],
        },
        # {
        #     "buyCities": ["南特"],
        #     "mode": "merchantQuest",
        #     "supplyCities": [],
        #     "checkInnCities": True
        # },
        {
            "buyCities": ["cohasset"],
            "mode": "newlanding",
        },
        {
            **samiRouteBase,
            "buyCities": ["azores"],
            "villages": ["samiWLumber"]
        },
        {
            **yawuruRouteBase,
            "buyCities": ["杭州"],
            "useSkillCity": False,
            "afterSellCities": ["santa","sierra","开普敦"]
        },
        # {
        #     **samiRouteBase,
        #     "buyCities": ["azores"],
        #     "villages": ["sam"],
        #     "forceUseSequenceOptions": True,
        #     "useSkillCity": False,
        #     "waitForFashion": False,
        #     "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
        #     "secondSellOptions": [
        #         {
        #             "seqs": [
        #                 {"type": "go", "val": "塞得港"},
        #                 {"type": "tunnel","val": True},
        #                 {"type": "getBestPriceCity"},
        #                 {"type": "goSellCity"},
        #                 {"type": "sell"}
        #             ],
        #             "cities": ["苏伊士"]
        #         }
        #     ],
        #     "afterSellCities": ["摩加迪沙"]
        # },
        # {
        #     **quechuasRouteBase,
        #     "buyCities": ["kuching"],
        #     "afterSellCities": ["ceylon"],
        #     "useSkillCity": True

        # },
        # {
        #     **quechuasRouteBase,
        #     "villages": ["quechua"],
        #     "buyCities": ["kuching"],
        #     "useSkillCity": False,
        #     "afterSellCities": ["摩加迪沙"]
        # },
        # {
        #     "mode": "tunnel"
        # },
        # {
        #     **samiRouteBase,
        #     "buyCities": ["seville"],
        #     "villages": ["sam"],
        #     "forceUseSequenceOptions": True,
        #     "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
        #     "secondSellOptions": [
        #         {
        #             "seqs": [
        #                 {"type": "go", "val": "塞得港"},
        #                 {"type": "tunnel","val": True},
        #                 # getBestPriceCity will use sellCityOptions to override the sell city
        #                 {"type": "getBestPriceCity"},
        #                 {"type": "goSellCity"},
        #                 {"type": "sell"}
        #             ],
        #             "cities": ["苏伊士"]
        #         }
        #     ]
        # }
        # check passed day or pause
    ],
    #13 svear sami
    [
        {
            **svearRouteBase,
            "buyCities": ["santa"],
            "villages": ["svear"],
            "supplyCities":["bremen","seville","tunis"],
            "useSkillCity": True,
            "forceUseSequenceOptions": True,
            "waitForFashion": False,
            "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "塞得港"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"},
                        {"type": "go", "val": "苏伊士"},
                        {"type": "tunnel"},
                        {"type": "go", "val": "tunis"}
                    ],
                    "cities": ["苏伊士"]
                }
            ],
        },
        {
            **svearRouteBase,
            "buyCities": ["santa"],
            "villages": ["svea"],
            "supplyCities":["bremen","seville","tunis"],
            "useSkillCity": False,
            "forceUseSequenceOptions": True,
            "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "塞得港"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"},
                        {"type": "go", "val": "苏伊士"},
                        {"type": "tunnel"},
                        {"type": "go", "val": "tunis"}
                    ],
                    "cities": ["苏伊士"]
                }
            ],
        },
        {
            "buyCities": ["南特"],
            "mode": "merchantQuest",
            "supplyCities": ["ceylon", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "关岛"],
            #"supplyCities": ["malacca", "亚丁","苏伊士"],
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["江户","安平"],
            "supplyCities": ["brunei","surabaya", "ceylon","苏伊士"],
        },
        # {
        #     **quechuasRouteBase,
        #     "buyCities": ["kuching"],
        # },
        {
            "mode": "tunnel"
        },
        {
            **samiRouteBase,
            "buyCities": ["azores"],
            "villages": ["sami"],
            "forceUseSequenceOptions": True,
            "useSkillCity": True,
            "waitForFashion": False,
            "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "塞得港"},
                        {"type": "tunnel","val": True},
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"},
                        {"type": "go", "val": "苏伊士"},
                        {"type": "tunnel"},
                        {"type": "go", "val": "tunis"}                    ],
                    "cities": ["苏伊士"]
                }
            ],
        },
        {
            **samiRouteBase,
            "buyCities": ["seville"],
            "villages": ["sam"],
            "forceUseSequenceOptions": True,
            "sellCityOptions": ["苏伊士", "吉达", "马萨瓦", "亚丁", "索科特拉", "杜法尔", "马斯喀特", "霍尔木兹", "多哈", "设拉子", "巴士拉", "巴格达"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "塞得港"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"},
                        {"type": "go", "val": "苏伊士"},
                        {"type": "tunnel"},
                        {"type": "go", "val": "tunis"}                        ],
                    "cities": ["苏伊士"]
                }
            ]
        }
        # check passed day or pause
    ],
    #14 svear + lumber -> bark painting
    [
        {
            **samiWLumberRouteBase,
            "buyCities": ["santa"],
            "villages": ["samiWLumber"],
            "useSkillCity": True
        },
        {
            **yawuruRouteBase,
            "buyCities": ["杭州"],
            "useSkillCity": True
        },
        {
            **samiWLumberRouteBase,
            "buyCities": ["azores"],
            "villages": ["samWLumber"],
            "useSkillCity": True
        },
        {
            "mode": "buff",
            "buyCities": ["davao"],
        },
        {
            **yawuruRouteBase,
            "buyCities": ["萨马赖"],
            "villages": ["yawur"],
            "afterSellCities": ["santa"],
            "useSkillCity": True
        },
        {
            "buyCities": ["cohasset"],
            "mode": "newlanding",
            "supplyCities": ["ceuta","塞得港"],
            "checkInnCities": True
        },
        {
            "buyCities": ["塞得港"],
            "mode": "tunnel",
            "supplyCities": ["ceylon", "brunei","surabaya","江户"],
            "checkInnCities": True
        },
        # {
        #     "buyCities": ["南特"],
        #     "mode": "merchantQuest",
        #     "supplyCities": ["ceylon", "manila", "ambon", "ternate"],
        #     "checkInnCities": True
        # },
        {
            "mode": "battle",
            "buyCities": ["切尔斯基"],
            # "supplyCities": ["江户","杭州","澳门","malacca", "ceylon","苏伊士"],
            "checkInnCities": True
        },
        # {
        #     "buyCities": ["切尔斯基"],
        #     "mode": "landing",
        #     "checkInnCities": True
        # },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["江户","安平"],
            "supplyCities": ["堺","malacca"],
            # "supplyCities": ["长崎","杭州","澳门","brunei","surabaya","ceylon"],
            "checkInnCities": True
        },
        {
            **quechuasRouteBase,
            "buyCities": ["kuching"],
            "afterSellCities": ["ceylon"],
            "useSkillCity": True

        },
        {
            **quechuasRouteBase,
            "villages": ["quechua"],
            "buyCities": ["brunei"],
            "useSkillCity": True
        },
        # {
        #     **apacheRouteBase,
        #     "sellFleet": 2,
        #     "supplyCities": ["panama"],
        #     "forceUseSequenceOptions": True,
        #     "sellCityOptions": ["beck","saint","kokkola","riga","stockhol", "gda","visby", "copenhag","oslo", "bergen", "edinburgh", "hamburg","bremen","groningen", "amsterda", "london", "dover", "antwerp"],
        #     "secondSellOptions": [
        #         {
        #             "seqs": [
        #                 {"type": "tunnel","val": True},
        #                 {"type": "go", "val": "santa"},
        #                 {"type": "go", "val": "plymouth"},
        #                 {"type": "go", "val": "beck"},
        #                 # getBestPriceCity will use sellCityOptions to override the sell city
        #                 {"type": "getBestPriceCity"},
        #                 {"type": "goSellCity"},
        #                 {"type": "sell"}
        #             ],
        #             "cities": ["beck"]
        #         }
        #     ],
        #     "villages": [阿帕奇],
        #     "buyCities": ["纳塔尔"],
        #     "afterSellCities":["dover"]
        # }
        {
            "buyCities": ["苏伊士"],
            "mode": "tunnel"
        },
    ]
]
