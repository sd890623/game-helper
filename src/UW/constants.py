# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
# portgual reputation
cityNames = ["funchal", "lisboa", "faro", "casablanca", "las"]

# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]

battleCity = "narvik"
battleCity = "hag"

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
# hobe azubuike, chenzuyi assu, lalkaika fleet, chowta rob, zubuike pill

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
    "supplyCities": ["seville", "pisa", "genoa", "bathurst", "sierra", "luanda", "cape", "toamasina", "pasay", "hangzhou"],
    "useSkillCity": None,
    "checkInnCities": True,
    "sellCities": [{"name": "pasay", "types": "BM"},
                   # {"name":"malacca","types":"BM"},{"name":"palembang","types":"BM"},
                   # {"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
                   {"name": "hobe", "types": "supply"}, {"name": "yanyun", "types": None}]
}
EADoubleBuy = {
    # ,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
    "buyProducts": ["gardenia", "begonia", "sweetolive", "azalea", "tiger'seye", "chinesetea", "agarwood", "ylang-ylang"],
    # "buyProductsAfterSupply": [], flag on enabling buy after supply
    # "buyProductsAfterSupplyCities": [],
    "buyCities": ["naha", "hobe", "hangzhou", "chang", "hanyang", "jeju"],
    "buySupplyCities": [],
    "buyStrategy": "twice",
    "dumpCrewCities": [],
    "useSkillCity": "beck",
    "checkInnCities": ["dublin", 'dover', 'london', 'macau', "edo", 'sakai', 'hanyang', 'hobe', "plymouth", "naha"],
    "sellFleet": 2,
    "buyFleet": 4,
    "supplyCities": ["sakai", "macau", "pasay", "toamasina", "cape", "soda", "bathurst", "dublin", "plymouth", "dover", "london"],
    "sellCities": [{"name": "beck", "types": None}],
}
EABuyBM = {
    "buyFleet": 4,
    "buyStrategy": "once",
    # , ,"shaoxingwine", "goryeoceladon","chinesepainting","easterncannon"
    # ,"tiger'seye"],
    "buyProducts": ["gardenia", "begonia", "sweetolive", "azalea"],
    # ,"quanzhou","hobe","hangzhou","chang","hanyang","jeju","macau",],
    "buyCities": ["hanyang", "dongnae", "jeju", "hangzhou", "hobe"], 
    "deductBuyBM": True,
    "checkInnCities": ['sakai', "edo", 'hanyang', 'hangzhou', "dongnae", "jeju", "hobe"],
    "buySupplyCities": [],
    "dumpCrewCities": [],
    "supplyCities": [],
    "sellCities": [],
}
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
    "supplyCities": ["cape", "ushuaia", "lima", "acapulco"],
    "buyProducts": ["platinum", "tuberose"],
    "checkInnCities": True,
    "afterVillageSupplyCities": ["acapulco"],
    # (index, val) array
    "tradeObjects": [(0, 2), (1, 2), (2, 2)],
    "cleanupIndex": 2,
    "buyStrategy": "twice",
    "useGemCities": [],
    "supplyFleet": 2,
    "barterFleet": 3
}

apachewine = {
    "villageName": "apache",
    # "buys": [
    #     # sequence has to map in game display
    #     {"product":"silver","cities":[],"targetNum":402},
    #     {"product":"coral","cities":[],"targetNum":600}
    # ],
    "buyCities": ["sofala", "quelimane", "cape", "tom", "praia", "las", "santo", "trujillo", "portobelo", "santo", "bahia", "tom", "praia", "las", "bahia", "buenos", "ushuaia", "copia", "guate", "acapulco"],
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
    "villageName": "varo",
    "buys": [
        # sequence has to map in game display
        {"product": "noni", "cities": [
            "kuching", "jayakarta", "makassar"], "targetNum": 400},
        {"product": "mangosteen", "cities": [
            "malacca", "aceh"], "targetNum": 200},
        {"product": "benzoin", "cities": [
            "prey", "malacca", "pasay"], "targetNum": 450}
    ],
    "useFishing": True,
    "buyCities": ["prey", "kuching", "malacca", "jayakarta", "makassar", "pasay", "aceh"],
    "supplyCities": ["aceh", "toamasina", "cape", "soda", "pernambuco", "cayenne"],
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
    "buyCities": ["kuching", "aceh","mogadishu","zanzibar","mozambique","cape","buenos","ushuaia", "valpara", "copia", "tumbes", "lima"],
    "supplyCities": ["lima"],
    "buyProducts": ["coal", "silver","gold"],
    "buyNotProducts": ["dust","goldware"],
    "checkInnCities": True,
    # "afterVillageSupplyCities": ["acapulco"],
    # (index, val) array
    "tradeObjects": [(0, 0), (1, 0), (2, 0)],
    "cleanupIndex": 2,
    "buyStrategy": "useGem",
    "useGemCities": ["kuching","copia"],
    "supplyFleet": 2,
    "barterFleet": 3
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
    "tradeObjects": [(0, 0), (1, 1), (2, 1)],
    "cleanupIndex": 2,
    "buyStrategy": "",
    "useGemCities": ["santa"],
    "barterFleet": 3
}
yaruruOrKalkaOri="kalkat"
def getYawuruOrKalka(secondVillage=False):
    if(secondVillage):
        return yaruruOrKalkaOri[:-1]
    return yaruruOrKalkaOri

yawuru= {
    "villageName": getYawuruOrKalka(),
    "checkInnCities": True,
    "buys": [
        # sequence has to map in game display
        {"product": "lumber", "cities": [], "targetNum": 170},
        {"product": "gold", "cities": [
         "samarai", "pinjarra"], "targetNum": 260},
        {"product": "kris", "cities": [
            "jayakarta", "surabaya"], "targetNum": 260}
    ],
    "buyProducts": ["kris", "gold","lumber"],
    "buyCities": ["samarai", "pinjarra","jayakarta", "surabaya"],
    "supplyCities": ["kakatuwah"],
    "tradeObjects": [(0, 1), (1, 1), (2, 1)],
    "cleanupIndex": 2,
    "buyStrategy": "twice",
    "useGemCities": ["samarai"],
    "barterFleet": 3
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
    "barterFleet": 7
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
    "apach": apache,
    "apac": apache,
    "apachewine": apachewine,
    "apachwine": apachewine,
    "apacwine": apachewine,
    "witoto": witoto,
    "witot": witoto,
    "quechuas": quechuas,
    "quechua": quechuas,
    "varo": {
        "villageName": "varo",
        "buys": [
            {"product": "benzoin", "cities": [
                "sofala", "quelimane"], "targetNum": 500},
            {"product": "noni", "cities": [
                "kilwa", "zanzibar", "mogadishu"], "targetNum": 500},
            {"product": "mangosteen", "cities": [
                "kilwa", "zanzibar", "mogadishu"], "targetNum": 250}
        ],
        "buyCities": ["prey", "kuching", "jayakarta", "malacca", "pasay"],
        "supplyCities": ["aceh", "toamasina", "cape", "soda", "pernambuco", "cayenne"],
        "buyProducts": ["benzoin", "noni", "mangosteen"],
        "afterVillageSupplyCities": ["cayenne"],
        # (index, val) array
        "tradeObjects": [(0, 2), (1, 2), (2, 2)],
        "cleanupIndex": 2,
        "buyStrategy": "twice",
        "useGemCities": [],
        "barterFleet": 4
    },
    "svear": svear,
    "svea": {
        **svear,
        "villageName": "svea"
    },
    "svearWLumber": svearWLumber,
    "sveaWLumber": {
        **svearWLumber,
        "villageName": "svea"
    },
    "sami": sami,
    "sam": {
        **sami,
        "villageName": "sam"
    },
    "yawuru": yawuru,
    "yawur": {
        **yawuru,
        "villageName": getYawuruOrKalka(True)
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
    "landingFleet": 8,
    "landingCity": "cohasset",
    "battleFleet": 5,
    "endBattleCity": "davao",
    "landingTimes": 90,
    "reportAndAdvQuestCity": "edo",
    "battleQuest": True,
    "gotoBattlecity": ["kakatuwah", "gari"],
    "leaveBattlecity": ["gari", "kakatuwah"]
}

checkInnCities = ['bathurst', "elmina", "aden", 'sierra', "barcelona", "marseille", "pisa", "saint", "plymouth","beck","amsterda","dover","visby", "santo", "portobelo","cohasset" "trujillo", "hadiboh", "aceh", "pasay", "banjarmasin","jayakarta", "natal", "sofala", "quelimane", "mozambique", "kilwa", "zanzibar", "mogadishu", "ushuaia", "copia", "tumbes", "acapulco", "nantes", "arguin", "genoa", "pisa", "algiers", "tunis", "santa","ceuta", "dublin", "amsterda", "bremen", "hanyang", "nagasaki","edo", "hangzhou", "quanzhou","tainan","macau", "hobe", "malacca","manila","brunei","surabaya", "kotte","gari", "pinjarra","samarai","hobart", "suva","mahina","atuona","soda", "pernambuco", "cayenne"]

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
    "sellPriceIndex": 0,
    "sellCityOptions": ["hangzhou", "macau", "quanzhou", "hobe", "tainan", "yanyun", "peking", "chang", "chongqing"],
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
    "supplyCities":["bremen","nantes","tunis","said","tunnel",{"route": 2, "target": "hangzhou"}],
    "sellFleet": 2,
    "useSkillCity": False,
    "checkInnCities": True,
    "sellPriceIndex": 1,
    "sellCityOptions": ["hangzhou", "macau", "quanzhou", "hobe", "tainan", "yanyun", "peking", "chang", "chongqing"],
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
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": []
}

yawuruRouteBase={
    "buyProducts": [],
    "buyFleet": 4,
    "buyCities": ["jayakarta"],
    "villages": ["yawuru"],
    "enableVillageTrade": True,
    "useFishingCities": ["panama"],
    "afterVillageBuyCities": [],
    "sellFleet": 2,
    "supplyCities":["samarai","mahina","atuona","panama","tunnel","santo"],
    "useSkillCity": "portobelo",
    "checkInnCities": True,
    "sellPriceIndex": 0,
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
    "supplyCities":["bremen","seville","tunis"],
    "sellFleet": 7,
    "useSkillCity": False,
    "checkInnCities": True,
    "sellPriceIndex": 0,
    "sellCityOptions": ["hangzhou", "macau", "quanzhou", "hobe", "tainan", "yanyun", "peking", "chang", "chongqing"],
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
    "sellFleet": 7,
    "useSkillCity": "suez",
    "checkInnCities": True,
    "sellPriceIndex": 0,
    "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "cities": ["alexandria", "cairo", "said", "jaffa", "beirut", "lefkosa", "antalya", "candia", "trabzon", "benghazi"]
        },
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "goToCityForTrade": "mozambique",
            "cities": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "manbasa", "malindi", "mogadishu"]
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
    "useFishingCities": ["ushuaia","cape"],
    "villages": ["quechuas"],
    # "afterVillageBuyCities": ["acapulco"],
    "supplyCities": ['ushuaia', 'cape', 'aden'],
    "sellFleet": 2,
    "useSkillCity": False,
    "checkInnCities": True,
    "sellPriceIndex": 0,
    "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "cities": ["alexandria", "cairo", "said", "jaffa", "beirut", "lefkosa", "antalya", "candia", "trabzon", "benghazi"]
        },
        {
            "seqs": [
                {"type": "goSellCity"},
                {"type": "sell"}
            ],
            "cities": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "manbasa", "malindi", "mogadishu"]
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
    "villages": ["varo"],
    "afterVillageBuyCities": [],
    "supplyCities": ["elmina", "cape", "toamasina", "pasay", "dongnae"],
    "sellFleet": 7,
    # "useSkillCity":"suez",
    "checkInnCities": True,
    "sellPriceIndex": 0,
    "sellCityOptions": ["hanyang", "jeju", "dongnae", "yeongil", "deokwon", "edo", "nagasaki", "sakai"],
    "fashions": ["赞助"],
    "waitForFashion": True,
    "waitHour": 1,
    "afterSellCities": ["hanyang", "tainan", "malacca", "mogadishu"]
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
            "supplyCities": ["juan", "praia", "elmina", "luanda", "cape", "toamasina", "pasay"],
            # "sellCities":[{"name":"malacca","types":["liquor"]},{"name":"pasay","types":None}],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malacca", "types": "BM"}, {"name": "macau", "types": ["placeholder"]}, {"name": "chang", "types": None}, {"name": "hanyang", "types": "BM"}, {"name": "jeju", "types": "BM"}, {"name": "palembang", "types": "BM"}, {"name": "jayakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {"name": "banjarmasin", "types": ["placeholder"]}],
            "sellFleet": 2,
        },
        {
            # blueprint 1 perfume to spice
            "buyFleet": 4,
            "buyProducts": ["ebony", "agarwood", "ylang-ylang", "musk", "mace", "kris", "mangosteen"],
            "buyCities": ["banda", "ambon", "ternate", "jolo", "makassar", "banjarmasin", "jayakarta", "pasay", "aceh"],
            "buySupplyCities": [],
            "buyStrategy": "twice",
            "dumpCrewCities": [],
            "supplyCities": ["pasay", "toamasina", "cape", "pernambuco", "cayenne", "caracas"],
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
            "supplyCities": ["juan", "praia", "elmina", "luanda", "cape", "toamasina", "pasay"],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malacca", "types": "BM"}, {"name": "palembang", "types": "BM"},
                           {"name": "jayakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {
                               "name": "banjarmasin", "types": "BM"},
                           {"name": "davao", "types": ["dye"]}, {"name": "hobe", "types": [
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
            "supplyCities": ["macau", "pasay", "toamasina", "cape", "pernambuco", "cayenne", "caracas"],
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
            "supplyCities": ["juan", "praia", "elmina", "luanda", "cape", "toamasina", "pasay"],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malacca", "types": "BM"}, {"name": "palembang", "types": "BM"},
                           {"name": "jayakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {
                               "name": "banjarmasin", "types": "BM"},
                           {"name": "davao", "types": ["dye", "jewelry"]}, {
                               "name": "hobe", "types": ["placeholder"]}, {"name": "chang", "types": None}
                           ]
        },
        EABuyBM,
        {
            **EADoubleBuy,
            # ,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
            "buyProducts": ["gardenia", "sweetolive", "azalea", "chinesetea", "agarwood", "ylang-ylang"],
            "buyCities": ["naha", "hangzhou", "chang", "hanyang"],
            "supplyCities": ["macau", "pasay", "toamasina", "cape", "pernambuco", "cayenne", "caracas"],
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
            "supplyCities": ["juan", "praia", "elmina", "luanda", "cape", "toamasina", "pasay"],
            "sellCities": [{"name": "pasay", "types": "BM"}, {"name": "malacca", "types": "BM"}, {"name": "palembang", "types": "BM"},
                           {"name": "jayakarta", "types": "BM"}, {"name": "surabaya", "types": "BM"}, {
                               "name": "banjarmasin", "types": "BM"},
                           {"name": "hobe", "types": ["placeholder"]}, {
                "name": "chang", "types": None}
            ]
        },
        EABuyBM,
        {
            **EADoubleBuy,
            "supplyCities": ["macau", "pasay", "toamasina", "cape", "pernambuco", "cayenne", "caracas"],
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
            "afterSellCities": ["hanyang", "nagasaki","quanzhou", "manila", "kotte","toamasina", "cape", "soda", "bathurst"]
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
            "supplyCities": ["hadiboh", "manila"],
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
            "afterSellCities": ["hanyang", "nagasaki","quanzhou", "manila", "toamasina", "cape", "soda", "bathurst"]
        }
    ],
    # wine+witoto #9
    [
        # apache wine replacement
        {
            **apacheRouteBase,
            "villages": ["apachewine"],
            "sellFleet": 7,
            "buyCities": ["natal"],
            "afterSellCities": ["hadiboh"],
            "useSkillCity": False,
            "sellCityOptions": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "manbasa", "malindi", "mogadishu"],
            "waitForFashion": False
        },
        # {
        #     **witotoRouteBase,
        #     "buyCities": ["prey", "deokwon","santa"],
        #     "villages": ["witoto"],
        #     "afterSellCities": ["hanyang", "nagasaki", "quanzhou", "manila", "kotte"]
        # },
        {
            **apacheRouteBase,
            "sellFleet": 7,
            "villages": ["apacwine"],
            "buyCities": ["sofala", "ushuaia"],
            "sellCityOptions": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "manbasa", "malindi", "mogadishu"],
            "afterSellCities": ["suez"]
        },
        {
            "buyCities": ["said","edo"],
            "mode": "tunnel",
            "supplyCities": ["barcelona"],
        },
        {
            "buyCities": ["cohasset"],
            "mode": "newlanding",
        },
        {
            "buyCities": ["nantes","seville","santa","jayakarta"],
            "mode": "merchantQuest",
            "supplyCities": ["hadiboh", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "hag"],
        },
        # {"mode": "reportAndAdvQuest",
        #     "buyCities": ["edo","tainan"],
        #  },
        {
            **witotoRouteBase,
            "buyCities": ["kuching","mozambique","ponta","jayakarta"],
            "villages": ["witot"],
            "afterSellCities": ["hanyang", "nagasaki", "quanzhou", "banjarmasin", "manila", "kotte"]
        }
        # check passed day or pause
    ],
    # 10 crafts+witoto
    [
        {
            **apacheRouteBase,
            "villages": ["apache"],
            "buyCities": ["natal"],
            "afterSellCities": ["hadiboh", "aceh"]
        },
        {
            **witotoRouteBase,
            "buyCities": ["prey", "deokwon"],
            "villages": ["witoto"],
            "afterSellCities": ["hanyang", "nagasaki", "quanzhou", "banjarmasin", "malacca", "kotte"]
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
            "supplyCities": ["kotte", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "hag"],
        },
        {"mode": "reportAndAdvQuest",
            "buyCities": ["edo"]
         },
        {
            **witotoRouteBase,
            "buyCities": ["kuching"],
            "villages": ["witot"],
            "afterSellCities": ["hanyang", "nagasaki", "quanzhou", "banjarmasin", "malacca", "kotte"]
        }
        # check passed day or pause
    ],
    # 11 crafts+bark+chocolate+pipe
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
            "afterSellCities":["dover"]
        },
        {
            **svearRouteBase,
            "buyCities": ["santa"],
            "villages": ["svear"],
            "supplyCities":["bremen","seville","tunis"],
            "useSkillCity": False,
            "forceUseSequenceOptions": True,
            "waitForFashion": False,
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
        },
        {
            **apacheRouteBase,
            "sellFleet": 2,
            "villages": ["apac"],
            "supplyCities": ['lima', 'ushuaia', 'cape', 'aden'],
            "useFishingCities": ["ushuaia","cape"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "manbasa", "malindi", "mogadishu"]
                }
            ],
            "buyCities": ["sofala"],
            "afterSellCities": ["suez"]
        },
        {
            "buyCities": ["suez"],
            "mode": "tunnel"
        },
        {
            "buyCities": ["nantes"],
            "mode": "merchantQuest",
            "supplyCities": ["kotte", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "hag"],
            #"supplyCities": ["malacca", "aden","suez"],
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo","tainan"],
            "supplyCities": ["malacca", "kotte","suez"],
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
            "buyCities": ["ponta"],
            "villages": ["sami"],
            "forceUseSequenceOptions": True,
            "waitForFashion": False,
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
        #     "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "supplyCities":["bremen","nantes","ceuta","tunis"],
            "useSkillCity": False,
            "forceUseSequenceOptions": True,
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
        },
        {
            **apacheRouteBase,
            "sellFleet": 2,
            "villages": ["apac"],
            "supplyCities": ['lima', 'ushuaia', 'cape', 'aden'],
            "useFishingCities": ["ushuaia","cape"],
            "secondSellOptions": [
                {
                    "seqs": [
                        {"type": "goSellCity"},
                        {"type": "sell"}
                    ],
                    "cities": ["quelimane", "mozambique", "toamasina", "kilwa", "zanzibar", "manbasa", "malindi", "mogadishu"]
                }
            ],
            "buyCities": ["sofala"],
            "afterSellCities": ["kotte", "manila", "davao"]
        },

        # {
        #     "mode": "buff",
        #     "buyCities": ["davao"],
        # },
        {
            "mode": "battle",
            "buyCities": ["davao", "hag"],
            # "supplyCities": ["nagasaki","hangzhou","macau","malacca", "kotte","suez"],
            "checkInnCities": True
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo","tainan"],
            "checkInnCities": True,
            "supplyCities": ["nagasaki","hangzhou","macau","brunei","surabaya", "kotte","suez"],
        },
        # {
        #     "buyCities": ["suez"],
        #     "mode": "tunnel"
        # },
        # {
        #     "buyCities": ["nantes"],
        #     "mode": "merchantQuest",
        #     "supplyCities": [],
        #     "checkInnCities": True
        # },
        {
            "buyCities": ["said"],
            "mode": "tunnel",
            "supplyCities": ["ceuta"],
        },
        {
            "buyCities": ["cohasset"],
            "mode": "newlanding",
        },
        {
            **samiRouteBase,
            "buyCities": ["ponta"],
            "villages": ["sam"],
            "supplyCities":["bremen","ceuta","tunis"],
            "forceUseSequenceOptions": True,
            "useSkillCity": False,
            "waitForFashion": False,
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "afterSellCities": ["mogadishu"]
        },
        # {
        #     "mode": "tunnel"
        # },
        # {
        #     **samiRouteBase,
        #     "buyCities": ["seville"],
        #     "villages": ["sam"],
        #     "forceUseSequenceOptions": True,
        #     "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "supplyCities": ["kotte", "manila", "ambon", "ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities": ["davao", "hag"],
            #"supplyCities": ["malacca", "aden","suez"],
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo","tainan"],
            "supplyCities": ["brunei","surabaya", "kotte","suez"],
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
            "buyCities": ["ponta"],
            "villages": ["sami"],
            "forceUseSequenceOptions": True,
            "useSkillCity": True,
            "waitForFashion": False,
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "sellCityOptions": ["suez", "jeddah", "massawa", "aden", "hadiboh", "dhofar", "muscat", "hormuz", "bidda", "shiraz", "basrah", "baghdad"],
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
            "villages": ["svearWLumber"]
        },
        yawuruRouteBase,
        {
            **svearWLumberRouteBase,
            "buyCities": ["ponta"],
            "villages": ["sveaWLumber"]
        },
        {
            "mode": "buff",
            "buyCities": ["davao"],
        },
        {
            **yawuruRouteBase,
            "villages": ["yawur"],
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
            "supplyCities": ["kotte", "brunei","surabaya"],
            "checkInnCities": True
        },
        # {
        #     "buyCities": ["nantes"],
        #     "mode": "merchantQuest",
        #     "supplyCities": ["kotte", "manila", "ambon", "ternate"],
        #     "checkInnCities": True
        # },
        {
            "mode": "battle",
            "buyCities": ["hag"],
            # "supplyCities": ["nagasaki","hangzhou","macau","malacca", "kotte","suez"],
            "checkInnCities": True
        },
        {
            "mode": "reportAndAdvQuest",
            "buyCities": ["edo","tainan"],
            # "supplyCities": ["nagasaki","hangzhou","macau","malacca", "kotte","suez"],
            "supplyCities": ["nagasaki","hangzhou","macau","brunei","surabaya","kotte"],
            "checkInnCities": True
        },
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
            "afterSellCities":["dover"]
        }
        # {
        #     "mode": "tunnel"
        # }
    ]
]
