# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
# portgual reputation
cityNames = ["funchal", "lisboa", "faro", "casablanca", "las"]

# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]

battleCity = "narvik"
battleCity = "guam"

# "piratefleet", "assau": ganzi, pillage: banzi, robber: paomen"rob",  ,"assa","rob" ,"assa"
# opponentNames=["lag","illag","llag","pil","assa","asau"]
opponentsInList = ["pil", "ass", "asa", "aas", "ruthless","rob"]
# "golitsynpil","golitsynas","azubuikepi","azubuikeas","chenzuyipil","chenzuyias","kaikap","kaikaa"]
# add ducunyong as it's double lines, so quick hack,only checked in board
opponentNames = ["pill", "pil", "ass", "asa",
                 "duchunyong", "rob", "ruthless", "nanima"]
blackListForBattle = ['piz', 'zpi', 'robeyn', 'masa', 'roberts']
# rob: "rob",
# hanyang chowta ass, chenziyu pirate fleet, shiyang ass
# tamsui azubuike, chenzuyi assu, lalkaika fleet, chowta rob, zubuike pill

# Liquer+
# "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","cheese"],
# "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],

maticBarterTrade = {
    "buyProducts": ["silverware", "coffee", "wine"],
    "villages": ["turk"],
    "buyCities": ["nantes", "arguin", "marseille", "genoa", "algiers", "tunis"],
    "enableVillageTrade": True,
    "sellCity": "said"
}
NEEASupplySell = {
    # "jewllery","tourmaline" ,"handcanno", "flannel","amber"
    "buyProducts": ["amber", "twohand", "felt", "gobelin", "steel", "vodka", "aquavit", "gin", "whisky", "tapestry", "western", "westerncann", "saffron", "azulejo", "almond"],
    "buyCities": ["stockhol", "visby", "beck", "copenhag", "bergen", "edinburgh", "groningen", "amsterda", "london", "dover", "antwerp", "calais", "bristol", "nantes", "bordeaux", "porto", "seville", "laga", "marseil", "genoa", "seville", "laga", "marseil", "genoa", "seville", "laga", "marseil", "genoa"],
    "buySupplyCities": [],
    "dumpCrewCities": [""],
    "enableVillageTrade": True,
    "villages": ["svear", "sami", "svea", "sam"],
    "supplyCities": ["seville", "pisa", "genoa", "bathurst", "sierra", "luanda", "capetown", "toamasina", "pasay", "hangzhou"],
    "useSkillCity": None,
    "checkInnCities": True,
    "sellCities": [{"name": "pasay", "types": "BM"},
                   # {"name":"malaca","types":"BM"},{"name":"palembang","types":"BM"},
                   # {"name":"jakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
                   {"name": "tamsui", "types": "supply"}, {"name": "yanyun", "types": None}]
}
EADoubleBuy = {
    # ,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
    "buyProducts": ["gardenia", "begonia", "sweetolive", "azalea", "tiger'seye", "chinesetea", "agarwood", "ylang-ylang"],
    # "buyProductsAfterSupply": [], flag on enabling buy after supply
    # "buyProductsAfterSupplyCities": [],
    "buyCities": ["naha", "tamsui", "hangzhou", "chang", "hanyang", "jeju"],
    "buySupplyCities": [],
    "buyStrategy": "twice",
    "dumpCrewCities": [],
    "useSkillCity": "beck",
    "checkInnCities": ["dublin", 'dover', 'london', 'macau', "edo", 'sakai', 'hanyang', 'tamsui', "plymouth", "naha"],
    "sellFleet": 2,
    "buyFleet": 4,
    "supplyCities": ["sakai", "macau", "pasay", "toamasina", "town", "soda", "bathurst", "dublin", "plymouth", "dover", "london"],
    "sellCities": [{"name": "beck", "types": None}],
}
EABuyBM = {
    "buyFleet": 4,
    "buyStrategy": "once",
    # , ,"shaoxingwine", "goryeoceladon","chinesepainting","easterncannon"
    # ,"tiger'seye"],
    "buyProducts": ["gardenia", "begonia", "sweetolive", "azalea"],
    # ,"quanzhou","tamsui","hangzhou","chang","hanyang","jeju","macau",],
    "buyCities": ["hanyang", "dongnae", "jeju", "hangzhou", "tamsui"], 
    "deductBuyBM": True,
    "checkInnCities": ['sakai', "edo", 'hanyang', 'hangzhou', "dongnae", "jeju", "tamsui"],
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
    "villageName": "apache",
    "buys": [
        # sequence has to map in game display
        {"product": "platinum", "cities": [
            "natal", "sofala", "quelimane"], "targetNum": 522},
        {"product": "tuberose", "cities": [
            "kilwa", "zanzibar", "mogadishu"], "targetNum": 600}
    ],
    "buyCities": ["natal", "sofala", "quelimane", "mozambique", "kilwa", "zanzibar", "mogadishu"],
    "supplyCities": ["town", "ushuaia", "lima", "acapulco"],
    "buyProducts": ["platinum", "tuberose"],
    "checkInnCities": True,
    "afterVillageSupplyCities": ["acapulco"],
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
    "villageName": "apache",
    # "buys": [
    #     # sequence has to map in game display
    #     {"product":"silver","cities":[],"targetNum":402},
    #     {"product":"coral","cities":[],"targetNum":600}
    # ],
    "buyCities": ["sofala", "quelimane", "capetown", "tom","verde", "las", "santo", "trujillo", "portobelo", "santo", "bahia", "tom", "verde", "las", "bahia", "buenos", "ushuaia", "copia", "guate", "acapulco"],
    "supplyCities": ["acapulco"],
    "buyProducts": ["silver", "coral"],
    "buyNotProducts": ["work"],
    "checkInnCities": True,
    "afterVillageSupplyCities": ["acapulco"],
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
            "malaca", "aceh"], "targetNum": 200},
        {"product": "benzoin", "cities": [
            "prey", "malaca", "pasay"], "targetNum": 450}
    ],
    "useFishing": True,
    "buyCities": ["prey", "kuching", "malaca", "jakarta", "makassar", "pasay", "aceh"],
    "supplyCities": ["aceh", "toamasina", "town", "soda", "pernambuco", "cayenne"],
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
    # "buyCities": ["kuching", "aceh","mogadishu","zanzibar","kilwa","mozambique","town","buenos","ushuaia","valpara", "copia", "tumbes", "lima"],
    "buyCities": ["kuching", "aceh","mogadishu","zanzibar","kilwa","mozambique","mogadishu","zanzibar","kilwa","town","bahia","rio","buenos","ushuaia","valpara", "copia","acapulco","lima"],
    "supplyCities": ["lima"],
    "buyProducts": ["coal", "silver","gold"],
    "buyNotProducts": ["golddust","goldware"],
    "checkInnCities": True,
    "afterVillageSupplyCities": ["lima"],
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
    "villageName": "svear",
    "buyCities": ["santa", "seville", "dublin", "amsterda"],
    "checkInnCities": True,
    "supplyCities": ["visby"],
    "buyProducts": ["candle", "matchlock", "iron", "lron", "birch"],
    # (index, val) array
    "tradeObjects": [(0, 0), (1, 1), (2, 1)],
    "cleanupIndex": 2,
    "buyStrategy": "",
    "useGemCities": ["santa"],
    "barterFleet": 3
}
svearWLumber = {
    "villageName": "svear",
    "buyCities": ["santa", "seville", "dublin", "amsterda","oslo","riga"],
    "checkInnCities": True,
    "supplyCities": ["visby"],
    "leaveGoods": ["lumber"],
    "buyProducts": ["candle", "matchlock", "iron", "lron", "birch","lumber"],
    # (index, val) array
    # "tradeObjects": [(0, 0), (1, 1), (2, 1)],
    "tradeObjects": [(0, 0), (1, 0), (2, 1),(3,1)],
    "cleanupIndex": 2,
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
         "samarai", "pinjarra"], "targetNum": 260},
        {"product": "kris", "cities": [
            "jakarta", "surabaya"], "targetNum": 260}
    ],
    "buyProducts": ["kris", "gold","lumber"],
    "buyCities": ["samarai", "pinjarra","jakarta", "surabaya"],
    "supplyCities": ["kakatuwah"],
    "tradeObjects": [(0, 1), (1, 1), (2, 1),(3, 1)],
    "cleanupIndex": 3,
    "buyStrategy": "twice",
    "useGemCities": ["samarai"],
    "barterFleet": 3,
    "barterFirstRoundCount":4
}
sami = {
    "villageName": "sami",
    "shortVillageName": "s",
    "buyCities": ["santa", "seville", "dublin", "amsterda"],
    "supplyCities": ["bergen"],
    "buyProducts": ["candle", "matchlock", "iron", "lron"],
    "tradeObjects": [(0, 0), (1, 1), (2, 1)],
    "cleanupIndex": 2,
    "buyStrategy": "",
    "useGemCities": ["santa"],
    "barterFleet": 7,
    "barterFirstRoundCount":3
}
villageTradeList = {
    "turk": {
        "villageName": "turk",
        "buyCities": ["nantes", "arguin", "algiers", "genoa", "pisa", "tunis"],
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
        **svear,
        "villageName": "svea"
    },
    "svearWLumber": svearWLumber,
    "sveaWLumber": {
        **svearWLumber,
        "villageName": "svea",
        "tradeObjects": [(0, 0), (1, 1), (2, 1)],
        "cleanupIndex": 2,
    },
    "sami": sami,
    "sam": {
        **sami,
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
    "mar": 7,
    "apr": 7, "may": 7, "jun": 4,
    "jul": 4, "aug": 4, "sep": 5,
    "oct": 5, "nov": 5, "dec": 6,
    "jan": 6, "feb": 6
}
bartingMonthToRoute = {
    "mar": 9,
    "apr": 9, "may": 9, "jun": 9,
    "jul": 9, "aug": 9, "sep": 9,
    "oct": 9, "nov": 9, "dec": 9,
    "jan": 9, "feb": 9
}
dailyJobConf = {
    "merchatQuestCity": "nantes",
    "buffCity": "davao",
    "basicFleet":2,
    "landingFleet": 5,
    "preLandingCity": "cohasset",
    "landingCity": "cohasset",
    "battleFleet": 1,
    "endBattleCity": "edo",
    "landingTimes": 90,
    "landingRounds": 2,
    "reportAndAdvQuestCity": "edo",
    "battleQuest": True,
    "gotoBattlecity": ["kakatuwah", "gari"],
    "leaveBattlecity": ["gari", "kakatuwah"],
    "negoTimes": 4
}
checkInnCities=[]
checkInnCitiesBack = ['bathurst', "elmina", "aden", 'sierra', "barcelona", "marseille", "palma","pisa","cairo","beirut", "saint", "plymouth","beck","amsterda","dover","visby", "santo", "royal","portobelo","cohasset" "trujillo","panama", "socotra", "aceh", "pasay", "banjarmasin","jakarta", "natal","toamasina","sofala", "quelimane", "mozambique", "kilwa", "zanzibar", "mogadishu", "ushuaia", "copia", "tumbes", "nantes", "arguin", "genoa", "pisa", "algiers", "tunis", "santa","ceuta", "dublin", "amsterda", "bremen", "hanyang","dongnae","jeju","sakai", "nagasaki", "hangzhou", "quanzhou","tainan","macau", "tamsui", "malaca","manila","brunei","surabaya", "ceylon","gari", "pinjarra","samarai","hobart", "suva","mahina","atuona","soda", "pernambuco", "cayenne"]

svearRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["santa", "seville", "hangzhou"],
    "enableVillageTrade": True,
    "useFishingCities": [],
    "villages": ["svear"],
    "afterVillageBuyCities": [],
    "supplyCities":["bremen","seville","tunis","said","tunnel",{"route": 2, "target": "hangzhou"}],
    "sellFleet": 2,
    "useSkillCity": "suez",
    "checkInnCities": True,
    "sellPriceIndexByName": "versl",
    "sellCityOptions": ["hangzhou", "macau", "quanzhou", "tamsui", "tainan", "yanyun", "peking", "chang", "chongqing"],
    "forceUseSequenceOptions": False,
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["hanyang", "jeju", "edo", "nagasaki", "dongnae", "yeongil", "deokwon", "sakai"]
        }
    ],
    "sellCities": [{"name": "suez", "types": None}],
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
    "supplyCities":["beck","bremen","plymouth","nantes","palma","genoa","pisa","cairo","said","tunnel",{"route": 2, "target": "hangzhou"}],
    "sellFleet": 2,
    "useSkillCity": False,
    "checkInnCities": True,
    "sellPriceIndexByName": "versl",
    "sellCityOptions": ["hangzhou", "macau", "quanzhou", "tamsui", "tainan", "yanyun", "peking", "chang", "chongqing"],
    "forceUseSequenceOptions": False,
    "onlySellTypes": ["crafts"],
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["hanyang", "jeju", "edo", "nagasaki", "dongnae", "yeongil", "deokwon", "sakai"]
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
    "supplyCities":["samarai","atuona","panama","tunnel","royal","santo"],
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
    "buyCities": ["santa", "seville", "hangzhou"],
    "enableVillageTrade": True,
    "useFishingCities": [],
    "villages": ["sami"],
    "afterVillageBuyCities": [],
    "supplyCities":["nantes","ceuta","palma","genoa","pisa","cairo"],
    "sellFleet": 7,
    "useSkillCity": False,
    "checkInnCities": True,
    "sellPriceIndexByName": "versl",
    "sellCityOptions": ["hangzhou", "macau", "quanzhou", "tamsui", "tainan", "yanyun", "peking", "chang", "chongqing"],
    "forceUseSequenceOptions": False,
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["hanyang", "jeju", "edo", "nagasaki", "dongnae", "yeongil", "deokwon", "sakai"]
        }
    ],
    "sellCities": [{"name": "suez", "types": None}],
    "fashions": ["赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": []
}

apacheRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["sofala"],
    "enableVillageTrade": True,
    "useFishingCities": ["ushuaia"],
    "villages": ["apac"],
    # "afterVillageBuyCities": ["acapulco"],
    "supplyCities": [{"route": 3, "target": "aden"}],
    "sellFleet": 2,
    "useSkillCity": "suez",
    "checkInnCities": True,
    "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "go", "val": "suez"},
                {"type": "tunnel"},
                {"type": "goSellCity"},
                {"type": "sell"},
                {"type": "go", "val": "said"},
                {"type": "tunnel"}
            ],
            "cities": ["alexandria", "cairo", "said", "jaffa", "beirut", "nicosia", "antalya", "candia", "trabzon", "benghazi"]
        },
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "goToCityForTrade": "mozambique",
            "cities": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "mombasa", "malindi", "mogadishu"]
        }
    ],
    "fashions": ["奢华", "赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": ["suez"]
}

quechuasRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["kuching"],
    "enableVillageTrade": True,
    "useFishingCities": ["ushuaia","town"],
    "villages": ["quechuas"],
    "supplyCities": ['ushuaia', 'town', 'aden'],
    "sellFleet": 2,
    "useSkillCity": True,
    "checkInnCities": True,
    "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
    "secondSellOptions": [
        {
            "seqs": [
                {"type": "go", "val": "suez"},
                {"type": "tunnel"},
                {"type": "goSellCity"},
                {"type": "sell"},
                {"type": "go", "val": "said"},
                {"type": "tunnel"}
            ],
            "cities": ["alexandria", "cairo", "said", "jaffa", "beirut", "nicosia", "antalya", "candia", "trabzon", "benghazi"]
        },
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "mombasa", "malindi", "mogadishu"]
        }
    ],
    "fashions": ["奢华", "赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": ["suez"]
}
witotoRouteBase = {
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["prey", "deokwon"],
    "enableVillageTrade": True,
    "useFishingCities": [],
    "villages": ["witoto"],
    "afterVillageBuyCities": [],
    "supplyCities": ["elmina", "town", "toamasina", "pasay", "dongnae"],
    "sellFleet": 2,
    # "useSkillCity":"suez",
    "checkInnCities": True,
    "sellCityOptions": ["hanyang", "jeju", "dongnae", "yeongil", "deokwon", "edo", "nagasaki", "sakai"],
    "fashions": ["赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": ["hanyang", "tainan", "malaca", "mogadishu"]
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
            "supplyCities": ["juan", "verde", "elmina", "luanda", "capetown", "toamasina", "pasay"],
            # "sellCities":[{"name":"malaca","types":["liquor"]},{"name":"pasay","types":None}],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malaca", "types": "BM"}, {"name": "macau", "types": ["placeholder"]}, {"name": "chang", "types": None}, {"name": "hanyang", "types": "BM"}, {"name": "jeju", "types": "BM"}, {"name": "palembang", "types": "BM"}, {"name": "jakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {"name": "banjarmasin", "types": ["placeholder"]}],
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
            "supplyCities": ["pasay", "toamasina", "town", "pernambuco", "cayenne", "caracas"],
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
            "supplyCities": ["juan", "verde", "elmina", "luanda", "capetown", "toamasina", "pasay"],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malaca", "types": "BM"}, {"name": "palembang", "types": "BM"},
                           {"name": "jakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {
                               "name": "banjarmasin", "types": "BM"},
                           {"name": "davao", "types": ["dye"]}, {"name": "tamsui", "types": [
                               "placeholder"]}, {"name": "chang", "types": None}
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
            "supplyCities": ["macau", "pasay", "toamasina", "town", "pernambuco", "cayenne", "caracas"],
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
            "supplyCities": ["juan", "verde", "elmina", "luanda", "capetown", "toamasina", "pasay"],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malaca", "types": "BM"}, {"name": "palembang", "types": "BM"},
                           {"name": "jakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {
                               "name": "banjarmasin", "types": "BM"},
                           {"name": "davao", "types": ["dye", "jewelry"]}, {
                               "name": "tamsui", "types": ["placeholder"]}, {"name": "chang", "types": None}
                           ]
        },
        EABuyBM,
        {
            **EADoubleBuy,
            # ,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
            "buyProducts": ["gardenia", "sweetolive", "azalea", "chinesetea", "agarwood", "ylang-ylang"],
            "buyCities": ["naha", "hangzhou", "chang", "hanyang"],
            "supplyCities": ["macau", "pasay", "toamasina", "town", "pernambuco", "cayenne", "caracas"],
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
            "supplyCities": ["juan", "verde", "elmina", "luanda", "capetown", "toamasina", "pasay"],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malaca", "types": "BM"}, {"name": "palembang", "types": "BM"},
                           {"name": "jakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {
                               "name": "banjarmasin", "types": "BM"},
                           {"name": "tamsui", "types": ["placeholder"]}, {
                "name": "chang", "types": None}
            ]
        },
        EABuyBM,
        {
            **EADoubleBuy,
            "supplyCities": ["macau", "pasay", "toamasina", "town", "pernambuco", "cayenne", "caracas"],
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
            "buyProductsAfterSupplyCities": ["chang", "edo", "nagasaki", "sakai", "hangzhou"]
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
            "buyCities": ["naha", "hangzhou", "chang", "hanyang"],
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
            "buyProductsAfterSupplyCities": ["chang", "edo", "nagasaki", "sakai", "hangzhou"]
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
            "buyProductsAfterSupplyCities": ["edo", "nagasaki", "sakai", "hangzhou"]
        }
    ],
    # svear+witoto， #8
    [
        {
            **svearRouteBase,
            "buyCities": ["santa"],
            "villages": ["svear"],
            "afterSellCities": ["quanzhou"]
        },
        {
            **witotoRouteBase,
            "buyCities": ["prey", "deokwon"],
            "villages": ["witoto"],
            "afterSellCities": ["hanyang", "nagasaki","quanzhou", "manila", "ceylon","toamasina", "town", "soda", "bathurst"]
        },
        {
            **svearRouteBase,
            "buyCities": ["seville", "hangzhou"],
            "villages": ["svea"],
            "afterSellCities": ["nagasaki","quanzhou", "manila", "aden", "suez"]
        },
        {
            "buyCities": ["suez"],
            "mode": "tunnel",
            "supplyCities": ["barcelona"],
        },
        # {"mode": "landing"},
        {
            "buyCities": ["nantes"],
            "mode": "merchantQuest",
            "supplyCities": ["socotra", "manila"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao"],
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo"]
         },
        {
            **witotoRouteBase,
            "buyCities": ["kuching"],
            "villages": ["witot"],
            "afterSellCities": ["hanyang", "nagasaki","quanzhou", "manila", "toamasina", "town", "soda", "bathurst"]
        }
    ],
    # wine+witoto #9
    [
        # apache wine replacement
        {
            **apacheRouteBase,
            "villages": ["apachewine"],
            "sellFleet": 2,
            "buyCities": ["natal"],
            "afterSellCities": ["socotra"],
            "useSkillCity": False,
            "sellCityOptions": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "mombasa", "malindi", "mogadishu"],
            "waitForFashion": False
        },
        {
            **witotoRouteBase,
            "buyCities": ["prey", "deokwon","santa","hangzhou"],
            "villages": ["witoto"],
            "afterSellCities": ["hanyang", "nagasaki", "quanzhou", "manila", "ceylon"]
        },
        {
            **apacheRouteBase,
            "sellFleet": 2,
            "villages": ["apacwine"],
            "buyCities": ["sofala", "ushuaia"],
            "sellCityOptions": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "mombasa", "malindi", "mogadishu"],
            "afterSellCities": ["ceylon", "manila", "davao"]
        },
        {
            "mode": "buff",
            "buyCities": ["davao"],
            "supplyCities": ["edo"],
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "guam","chersky","ezo"],
            # "supplyCities": ["nagasaki","hangzhou","macau","malaca", "ceylon","suez"],
            "checkInnCities": True
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo","tainan","samarai"],
            "checkInnCities": True,
            "supplyCities": ["nagasaki","hangzhou","macau","brunei","surabaya", "ceylon","suez"],
        },
        {
            "buyCities": ["suez"],
            "mode": "tunnel",
            "supplyCities": ["ceuta"],
        },
        {
            "buyCities": ["cohasset"],
            "mode": "newlanding",
            "supplyCities": ["ceuta","said"]
        },
        {
            "buyCities": ["said"],
            "mode": "tunnel",
            "supplyCities": ["ceylon"],
        },
        # {
        #     "buyCities": ["nantes","seville","santa","jakarta"],
        #     "mode": "merchantQuest",
        #     "supplyCities": ["socotra", "manila", "ambon", "ternate"],
        #     "checkInnCities": True
        # },
        {
            **witotoRouteBase,
            "buyCities": ["kuching","mozambique","azores","jakarta"],
            "villages": ["witot"],
            "afterSellCities": ["hanyang", "nagasaki", "quanzhou", "banjarmasin", "manila", "ceylon"]
        }
        # check passed day or pause
    ],
    # 10 crafts+witoto
    [
        {
            **apacheRouteBase,
            "villages": ["apache"],
            "buyCities": ["natal"],
            "afterSellCities": ["socotra", "aceh"]
        },
        {
            **witotoRouteBase,
            "buyCities": ["prey", "deokwon"],
            "villages": ["witoto"],
            "afterSellCities": ["hanyang", "nagasaki", "quanzhou", "banjarmasin", "malaca", "ceylon"]
        },
        {
            **apacheRouteBase,
            "villages": ["apac"],
            "buyCities": ["sofala", "ushuaia"],
            "afterSellCities": ["suez"]
        },
        {
            "buyCities": ["suez"],
            "mode": "tunnel",
            "supplyCities": ["barcelona"],
        },
        # {"mode": "landing"},
        {
            "buyCities": ["nantes"],
            "mode": "merchantQuest",
            "supplyCities": ["ceylon", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "guam"],
        },
        {"mode": "reportAndAdvQuest",
            "buyCities": ["edo"]
         },
        {
            **witotoRouteBase,
            "buyCities": ["kuching"],
            "villages": ["witot"],
            "afterSellCities": ["hanyang", "nagasaki", "quanzhou", "banjarmasin", "malaca", "ceylon"]
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
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "said"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["suez"]
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
            "buyCities": ["suez"],
            "mode": "tunnel"
        },
        {
            "buyCities": ["nantes"],
            "mode": "merchantQuest",
            "supplyCities": ["ceylon", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "guam"],
            #"supplyCities": ["malaca", "aden","suez"],
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo","tainan"],
            "supplyCities": ["malaca", "ceylon","suez"],
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
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "said"},
                        {"type": "tunnel","val": True},
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["suez"]
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
        #     "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
        #     "secondSellOptions": [
        #         {
        #             "seqs": [
        #                 {"type": "go", "val": "said"},
        #                 {"type": "tunnel","val": True},
        #                 # getBestPriceCity will use sellCityOptions to override the sell city
        #                 {"type": "getBestPriceCity"},
        #                 {"type": "goSellCity"},
        #                 {"type": "sell"}
        #             ],
        #             "cities": ["suez"]
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
            "buyCities": ["natal"],
            "afterSellCities":["dover","nantes"]
        },
        {
            **samiRouteBase,
            "buyCities": ["santa"],
            "villages": ["sami"],
            "useSkillCity": False,
            "forceUseSequenceOptions": True,
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "said"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["suez"]
                }
            ],
            "afterSellCities": ["mogadishu"]
        },
        {
            **apacheRouteBase,
            "sellFleet": 2,
            "villages": ["apac"],
            "supplyCities": ['lima', 'ushuaia', 'town', 'aden'],
            "useFishingCities": ["ushuaia","town"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "mombasa", "malindi", "mogadishu"]
                }
            ],
            "buyCities": ["sofala"],
            "afterSellCities": ["ceylon", "manila", "davao"]
        },
        {
            "mode": "buff",
            "buyCities": ["davao"],
            "supplyCities": ["edo"],
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "guam","ezo","chersky"],
            # "supplyCities": ["nagasaki","hangzhou","macau","malaca", "ceylon","suez"],
            "checkInnCities": True
        },
        # {
        #     "buyCities": ["chersky"],
        #     "mode": "landing",
        #     "checkInnCities": True
        # },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo","tainan"],
            "checkInnCities": True,
            "supplyCities": ["sakai","nagasaki","hanyang","macau","brunei","surabaya", "ceylon","suez"],
        },
        {
            "buyCities": ["suez"],
            "mode": "tunnel",
            "supplyCities": ["ceuta"],
        },
        # {
        #     "buyCities": ["nantes"],
        #     "mode": "merchantQuest",
        #     "supplyCities": [],
        #     "checkInnCities": True
        # },
        {
            "buyCities": ["cohasset"],
            "mode": "newlanding",
        },
        {
            **svearWLumberRouteBase,
            "buyCities": ["azores"],
            "villages": ["svearWLumber"]
        },
        {
            **yawuruRouteBase,
            "buyCities": ["hangzhou"],
            "useSkillCity": False,
            "afterSellCities": ["santa","sierra","town"]
        },
        # {
        #     **samiRouteBase,
        #     "buyCities": ["azores"],
        #     "villages": ["sam"],
        #     "forceUseSequenceOptions": True,
        #     "useSkillCity": False,
        #     "waitForFashion": False,
        #     "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
        #     "secondSellOptions": [
        #         {
        #             "seqs": [
        #                 {"type": "go", "val": "said"},
        #                 {"type": "tunnel","val": True},
        #                 {"type": "getBestPriceCity"},
        #                 {"type": "goSellCity"},
        #                 {"type": "sell"}
        #             ],
        #             "cities": ["suez"]
        #         }
        #     ],
        #     "afterSellCities": ["mogadishu"]
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
        #     "afterSellCities": ["mogadishu"]
        # },
        # {
        #     "mode": "tunnel"
        # },
        # {
        #     **samiRouteBase,
        #     "buyCities": ["seville"],
        #     "villages": ["sam"],
        #     "forceUseSequenceOptions": True,
        #     "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
        #     "secondSellOptions": [
        #         {
        #             "seqs": [
        #                 {"type": "go", "val": "said"},
        #                 {"type": "tunnel","val": True},
        #                 # getBestPriceCity will use sellCityOptions to override the sell city
        #                 {"type": "getBestPriceCity"},
        #                 {"type": "goSellCity"},
        #                 {"type": "sell"}
        #             ],
        #             "cities": ["suez"]
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
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "said"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"},
                        {"type": "go", "val": "suez"},
                        {"type": "tunnel"},
                        {"type": "go", "val": "tunis"}
                    ],
                    "cities": ["suez"]
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
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "said"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"},
                        {"type": "go", "val": "suez"},
                        {"type": "tunnel"},
                        {"type": "go", "val": "tunis"}
                    ],
                    "cities": ["suez"]
                }
            ],
        },
        {
            "buyCities": ["nantes"],
            "mode": "merchantQuest",
            "supplyCities": ["ceylon", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "guam"],
            #"supplyCities": ["malaca", "aden","suez"],
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo","tainan"],
            "supplyCities": ["brunei","surabaya", "ceylon","suez"],
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
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "said"},
                        {"type": "tunnel","val": True},
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"},
                        {"type": "go", "val": "suez"},
                        {"type": "tunnel"},
                        {"type": "go", "val": "tunis"}                    ],
                    "cities": ["suez"]
                }
            ],
        },
        {
            **samiRouteBase,
            "buyCities": ["seville"],
            "villages": ["sam"],
            "forceUseSequenceOptions": True,
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "socotra", "dhofar", "muscat", "hormuz", "doha", "shiraz", "basrah", "baghdad"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "go", "val": "said"},
                        {"type": "tunnel","val": True},
                        # getBestPriceCity will use sellCityOptions to override the sell city
                        {"type": "getBestPriceCity"},
                        {"type": "goSellCity"},
                        {"type": "sell"},
                        {"type": "go", "val": "suez"},
                        {"type": "tunnel"},
                        {"type": "go", "val": "tunis"}                        ],
                    "cities": ["suez"]
                }
            ]
        }
        # check passed day or pause
    ],
    #14 svear + lumber -> bark painting
    [
        {
            **svearWLumberRouteBase,
            "buyCities": ["santa"],
            "villages": ["svearWLumber"],
            "useSkillCity": True
        },
        {
            **yawuruRouteBase,
            "buyCities": ["hangzhou"],
            "useSkillCity": True
        },
        {
            **svearWLumberRouteBase,
            "buyCities": ["azores"],
            "villages": ["sveaWLumber"],
            "useSkillCity": True
        },
        {
            "mode": "buff",
            "buyCities": ["davao"],
        },
        {
            **yawuruRouteBase,
            "buyCities": ["samarai"],
            "villages": ["yawur"],
            "afterSellCities": ["santa"],
            "useSkillCity": True
        },
        {
            "buyCities": ["cohasset"],
            "mode": "newlanding",
            "supplyCities": ["ceuta","said"],
            "checkInnCities": True
        },
        {
            "buyCities": ["said"],
            "mode": "tunnel",
            "supplyCities": ["ceylon", "brunei","surabaya","edo"],
            "checkInnCities": True
        },
        # {
        #     "buyCities": ["nantes"],
        #     "mode": "merchantQuest",
        #     "supplyCities": ["ceylon", "manila", "ambon", "ternate"],
        #     "checkInnCities": True
        # },
        {
            "mode": "battle",
            "buyCities": ["chersky"],
            # "supplyCities": ["edo","hangzhou","macau","malaca", "ceylon","suez"],
            "checkInnCities": True
        },
        # {
        #     "buyCities": ["chersky"],
        #     "mode": "landing",
        #     "checkInnCities": True
        # },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo","tainan"],
            "supplyCities": ["sakai","nagasaki","dongnae","jeju","hanyang","macau","malaca"],
            # "supplyCities": ["nagasaki","hangzhou","macau","brunei","surabaya","ceylon"],
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
            "buyCities": ["kuching"],
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
        #     "villages": ["apache"],
        #     "buyCities": ["natal"],
        #     "afterSellCities":["dover"]
        # }
        {
            "buyCities": ["suez"],
            "mode": "tunnel"
        },
    ]
]
