# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
# portgual reputation
cityNames=["funchal","lisboa","faro","casablanca","las"]

# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]

battleCity="narvik"
battleCity="hag"

#"piratefleet", "assau": ganzi, pillage: banzi, robber: paomen"rob",  ,"assa","rob" ,"assa"
#opponentNames=["lag","illag","llag","pil","assa","asau"]
opponentsInList=["pil","ass","asa","aas","ruthless","rob"]
# "golitsynpil","golitsynas","azubuikepi","azubuikeas","chenzuyipil","chenzuyias","kaikap","kaikaa"]
opponentNames=["pill","pil","ass","asa","duchunyong","rob","ruthless","nanima"] #add ducunyong as it's double lines, so quick hack,only checked in board
blackListForBattle=['piz','zpi','robeyn','masa','roberts']
# rob: "rob",
#hanyang chowta ass, chenziyu pirate fleet, shiyang ass
#hobe azubuike, chenzuyi assu, lalkaika fleet, chowta rob, zubuike pill

#Liquer+
# "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","cheese"],
# "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],

maticBarterTrade={
    "buyProducts": ["silverware","coffee","wine"],
    "villages": ["turk"],
    "buyCities":["nantes","arguin","genoa","tunis"],
    "enableVillageTrade": True,
    "sellCity": "suez"
}
NEEASupplySell={
    # "jewllery","tourmaline" ,"handcanno", "flannel","amber"
    "buyProducts": ["amber","twohand","felt","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
    "buyCities":["stockhol","visby","beck","copenhag","bergen","edinburgh","groningen","amsterda","london","dover","antwerp","calais","bristol","nantes","bordeaux","porto","seville","laga","marseil","genoa","seville","laga","marseil","genoa","seville","laga","marseil","genoa"],
    "buySupplyCities":[],
    "dumpCrewCities": [""],
    "enableVillageTrade": True,
    "villages": ["svear","sami","svea","sam"],
    "supplyCities":["seville","pisa","genoa","bathurst","sierra","luanda","cape","toamasina","pasay","hangzhou"],
    "useSkillCity":None,
    "checkInnCities": True,
    "sellCities":[{"name":"pasay","types":"BM"},
    # {"name":"malacca","types":"BM"},{"name":"palembang","types":"BM"},
    # {"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
    {"name":"hobe","types":"supply"},{"name":"yanyun","types":None}]
}
EADoubleBuy={
    #,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
    "buyProducts": ["gardenia","begonia","sweetolive","azalea","tiger'seye","chinesetea","agarwood","ylang-ylang"],
    # "buyProductsAfterSupply": [], flag on enabling buy after supply
    # "buyProductsAfterSupplyCities": [],
    "buyCities":["naha","hobe","hangzhou","chang","hanyang","jeju"],
    "buySupplyCities":[],
    "buyStrategy":"twice",
    "dumpCrewCities": [],
    "useSkillCity":"beck",
    "checkInnCities": ["dublin",'dover','london','macau',"edo",'sakai','hanyang','hobe',"plymouth","naha"],
    "sellFleet":2,
    "buyFleet":4,
    "supplyCities":["sakai","macau","pasay","toamasina","cape","soda","bathurst","dublin","plymouth","dover","london"],
    "sellCities":[{"name":"beck","types":None}],
}
EABuyBM={
    "buyFleet":4,
    "buyStrategy":"once",
    # , ,"shaoxingwine", "goryeoceladon","chinesepainting","easterncannon"
    "buyProducts": ["gardenia","begonia","sweetolive","azalea"],#,"tiger'seye"],
    "buyCities":["hanyang","dongnae","jeju","hangzhou","hobe"],#,"quanzhou","hobe","hangzhou","chang","hanyang","jeju","macau",],
    "deductBuyBM":True,
    "checkInnCities": ['sakai',"edo",'hanyang','hangzhou',"dongnae","jeju","hobe"],
    "buySupplyCities":[],
    "dumpCrewCities": [],
    "supplyCities":[],
    "sellCities":[],
}
apache={
    "villageName": "apache",
    "buys": [
        # sequence has to map in game display
        {"product":"platinum","cities":["natal","sofala","quelimane"],"targetNum":472},
        {"product":"tuberose","cities":["kilwa","zanzibar","mogadishu"],"targetNum":600}
    ],
    "buyCities": ["natal","sofala","quelimane","mozambique","kilwa","zanzibar","mogadishu"],
    "supplyCities": ["cape","ushuaia","lima","acapulco"],
    "buyProducts": ["platinum","tuberose"],
    "checkInnCities": True,
    "afterVillageSupplyCities":["acapulco"],
    # (index, val) array
    "tradeObjects": [(0,2),(1,2),(2,2)],
    "cleanupIndex": 2,
    "buyStrategy": "twice",
    "useGemCities": [],
    "supplyFleet":2,
    "barterFleet":2
}
# apache={
#     "villageName": "apache",
#     # "buys": [
#     #     # sequence has to map in game display
#     #     {"product":"silver","cities":[],"targetNum":402},
#     #     {"product":"coral","cities":[],"targetNum":600}
#     # ],
#     "buyCities": ["sofala","quelimane","cape","tom","praia","las","bahia","buenos","ushuaia","copia","guate","acapulco"],
#     "supplyCities": ["acapulco"],
#     "buyProducts": ["silver","coral"],
#     "checkInnCities": True,
#     "afterVillageSupplyCities":["acapulco"],
#     # (index, val) array
#     "tradeObjects": [(0,1),(1,1),(2,1)],
#     "cleanupIndex": 2,
#     "buyStrategy": "useGem",
#     "useGemCities": ["praia","las"],
#     "supplyFleet":2,
#     "barterFleet":2
# }
witoto={
    "villageName": "witoto",
    "buys": [
        # sequence has to map in game display
        {"product":"noni","cities":["kuching","jayakarta","makassar"],"targetNum":400},
        {"product":"mangosteen","cities":["prey","malacca","aceh"],"targetNum":200},
        {"product":"benzoin","cities":["prey","malacca","pasay"],"targetNum":400}
    ],
    "useFishing": True,
    "buyCities": ["prey","kuching","malacca","jayakarta","makassar","pasay","aceh"],
    "supplyCities": ["aceh","toamasina","cape","soda","pernambuco","cayenne"],
    "buyProducts": ["noni","mangosteen","benzoin"],
    "checkInnCities": True,
    "afterVillageSupplyCities":["cayenne"],
    # (index, val) array
    "tradeObjects": [(0,2),(1,2),(2,2)],
    "cleanupIndex": 2,
    "buyStrategy": "once",
    "useGemCities": [],
    "supplyFleet":2,
    "barterFleet":2
}
villageTradeList = {
    "turk": {
        "startCities": ['beck'],
        "villageName": "turk",
        "buyCities": ["nantes","arguin","genoa"],
        "checkInnCities": True,
        "supplyCities": ["antalya"],
        "buyProducts": ["silverware","coffee","wine"],
        # (index, val) array
        "tradeObjects": [(0,0),(1,0)],
        "cleanupIndex": 1,
        "buyStrategy": "useGem",
        "useGemCities": ["arguin"],
        "barterFleet":7
    },
    "apache": apache,
    "apach": apache,
    "apac": apache,
    "witoto": witoto,
    "witot": witoto,
    "varo": {
        "villageName": "varo",
        "buys": [
            {"product":"benzoin","cities":["sofala","quelimane"],"targetNum":500},
            {"product":"noni","cities":["kilwa","zanzibar","mogadishu"],"targetNum":500},
            {"product":"mangosteen","cities":["kilwa","zanzibar","mogadishu"],"targetNum":250}
        ],
        "buyCities": ["prey","kuching","jayakarta","malacca","pasay"],
        "supplyCities": ["aceh","toamasina","cape","soda","pernambuco","cayenne"],
        "buyProducts": ["benzoin","noni","mangosteen"],
        "afterVillageSupplyCities":["cayenne"],
        # (index, val) array
        "tradeObjects": [(0,2),(1,2),(2,2)],
        "cleanupIndex": 2,
        "buyStrategy": "twice",
        "useGemCities": [],
        "barterFleet":4
    },
    "svear": {
        "startCities": ['beck'],
        "villageName": "svear",
        "buyCities": ["santa","seville","dublin","amsterda"],
        "checkInnCities": True,
        "supplyCities": ["visby"],
        "buyProducts": ["candle", "matchlock","iron", "lron"],
        # (index, val) array
        "tradeObjects": [(0,0),(1,1),(2,1)],
        "cleanupIndex": 2,
        "buyStrategy": "",
        "useGemCities": ["santa"],
        "barterFleet":4
    },
    "svea": {
        "startCities": ['beck'],
        "villageName": "svea",
        "buyCities": ["santa","seville","dublin","amsterda"],
        "checkInnCities": True,
        "supplyCities": ["visby"],
        "buyProducts": ["candle", "matchlock","iron", "lron"],
        "tradeObjects": [(0,0),(1,1),(2,1)],
        "cleanupIndex": 2,
        "buyStrategy": "",
        "useGemCities": ["santa"],
        "barterFleet":4
    },
    "sami": {
        "startCities": ['beck'],
        "villageName": "sami",
        "shortVillageName": "s",
        "buyCities": ["santa","seville","dublin","amsterda"],
        "supplyCities": ["bergen"],
        "buyProducts": ["candle", "matchlock","iron", "lron"],
        "tradeObjects": [(0,0),(1,1),(2,1)],
        "cleanupIndex": 2,
        "buyStrategy": "",
        "useGemCities": ["santa"],
        "barterFleet":7
    },
    "sam": {
        "startCities": ['beck'],
        "villageName": "sam",
        "shortVillageName": "s",
        "buyCities": ["santa","seville","dublin","amsterda"],
        "supplyCities": ["bergen"],
        "buyProducts": ["candle", "matchlock","iron", "lron"],
        "tradeObjects": [(0,0),(1,1),(2,1)],
        "cleanupIndex": 2,
        "buyStrategy": "",
        "useGemCities": ["santa"],
        "barterFleet":7
    }
}

#Init option
#Route choice: Must-set 0: mar-May-spring(SEA-Carrebean),1: Jun-Aug-Summer(Carrebean-EA),2: Sep-Oct Aut, Carrebean-EA,3: Winter Nov-Feb, Carrebean-EA
#4 summer, 5autumn, 6winter 7 spring
# v1 trade mapping
monthToRoute = {
    "mar": 7,
    "apr": 7, "may": 7, "jun": 4,
    "jul": 4, "aug": 4, "sep": 5,
    "oct": 5, "nov": 5, "dec": 6,
    "jan": 6, "feb": 6
}
bartingMonthToRoute = {
    "mar": 8,
    "apr": 8, "may": 8, "jun": 8,
    "jul": 8, "aug": 8, "sep": 8,
    "oct": 8, "nov": 8, "dec": 8,
    "jan": 8, "feb": 8
}
dailyJobConf={
    "merchatQuestCity": "nantes",
    "buffCity": "davao",
    "landingFleet": 8,
    "landingCity": "hag",
    "battleFleet": 5,
    "endBattleCity": "davao"
}

checkInnCities=['lisboa','cape','toamasina','seville','bathurst','sierra',"genoa","pisa","saint","amsterda","hadiboh","aceh","ambon","ternate","natal","sofala","quelimane","mozambique","kilwa","zanzibar","mogadishu","cape","ushuaia","lima","acapulco","nantes","arguin","genoa","tunis","santa","seville","dublin","amsterda","hanyang","tainan","hobe","malacca","soda","pernambuco","cayenne"]

apacheRouteBase={
    "buyProducts": [],
    "buyFleet":4,
    "buyCities":["sofala"],
    "enableVillageTrade": True,
    "useFishingCities": ["ushuaia"],
    "villages": ["apac"],
    "afterVillageBuyCities": ["acapulco"],
    "supplyCities":[{"route":3,"target":"aden"}],
    "sellFleet":7,
    "useSkillCity":"suez",
    "checkInnCities": True,
    "sellPriceIndex": 0,
    "sellCityOptions":["suez","jeddah","massawa","aden","hadiboh","dhofar","muscat","hormuz","bidda","shiraz","basrah","baghdad","diu","goa","kozhi","kochi"],
    "secondSellOptions": [
        {
            "seqs":[
                {"type":"go","val":"suez"},
                {"type":"tunnel"},
                {"type":"goSellCity"},
                {"type":"sell"},
                {"type":"go","val":"said"},
                {"type":"tunnel"}
            ],
            "cities": ["alexandria","cairo","said","jaffa","beirut","lefkosa","antalya","candia","trabzon","benghazi"]
        },
        {
            "seqs":[
                {"type":"goSellCity"},
                {"type":"sell"}
            ],
            "cities": ["quelimane","mozambique","toamasina","kilwa","zanzibar","manbasa","malindi","mogadishu"]
        }
    ],
    "fashions": ["奢华","赞助"],  
    "waitForFashion":True,           
    "afterSellCities": ["suez"]
}
routeLists=[
    # northEu liquor Dec-Feb(Inc)Winter+, mar-May(Spring)STD, Jun-(Summer)-
    # EA: Perfume: Dec-Feb(Winter),STD, Mar-May(Spring)-, Jun-(Summer)Aug STD,Sep-Nov(Autumn)++
    # Carrebean: Nov-May: Liquor,Lux+    Jun-Oct: Dye,Gem+

    #0 SEA-Carrebean  mar-May-spring
    [
        #harvest
        {
            "buyFleet":4,
            "buyProducts": ["opal","tequila","pineapple","logwood"],
            "buyCities":["havana","southside","roya","santiago"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": [],
            "supplyCities":["juan","praia","elmina","luanda","cape","toamasina","pasay"],
            #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"pasay","types":None}],
            "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":"BM"},{"name":"macau","types":["placeholder"]},{"name":"chang","types":None},{"name":"hanyang","types":"BM"},{"name":"jeju","types":"BM"},{"name":"palembang","types":"BM"},{"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":["placeholder"]}],
            "sellFleet":2,
        },
        {	
            #blueprint 1 perfume to spice
            "buyFleet":4,
            "buyProducts": ["ebony","agarwood","ylang-ylang","musk","mace","kris","mangosteen"],
            "buyCities":["banda","ambon","ternate","jolo","makassar","banjarmasin","jayakarta","pasay","aceh"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": [],
            "supplyCities":["pasay","toamasina","cape","pernambuco","cayenne","caracas"],
            "useSkillCity":"rida",
            "sellCities":[{"name":"rida","types":["perfume","dye"]},{"name":"veracruz","types":"BM"},{"name":"southside","types":None}],
            "sellFleet":2,
        },
    ],
    #1 Summer Jun-Aug, Carrebean-EA, 
    [
        {
            "buyProducts": ["opal","tequila","pineapple","logwood"],
            "buyCities":["southside","roya","willemstad","porlamar","caracas","juan"],
            "buyStrategy":"twice",
            "buySupplyCities":[],
            "dumpCrewCities": [],
            "supplyCities":["juan","praia","elmina","luanda","cape","toamasina","pasay"],
            "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":"BM"},{"name":"palembang","types":"BM"},
            {"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
            {"name":"davao","types":["dye"]},{"name":"hobe","types":["placeholder"]},{"name":"chang","types":None}
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
            "supplyCities":["macau","pasay","toamasina","cape","pernambuco","cayenne","caracas"],
            "useSkillCity":"maracaibo",
            "sellCities":[{"name":"maracaibo","types":None},{"name":"veracruz","types":"BM"}],
        }
    ],

    #2 Autumn Sep-Oct, Carrebean-EA, EA-perfume+, Carrebean-dey+ (Nov EA+, carrebean dye-, luxury+)
    [
        {
            "buyProducts": ["opal","tequila","pineapple","logwood"],
            "buyCities":["southside","roya","willemstad","porlamar","caracas","juan"],
            "buyStrategy":"twice",
            "buySupplyCities":[],
            "dumpCrewCities": [],
            "supplyCities":["juan","praia","elmina","luanda","cape","toamasina","pasay"],
            "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":"BM"},{"name":"palembang","types":"BM"},
            {"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
            {"name":"davao","types":["dye","jewelry"]},{"name":"hobe","types":["placeholder"]},{"name":"chang","types":None}
            ]
        },
        EABuyBM,
        {
            **EADoubleBuy,
            #,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
            "buyProducts": ["gardenia","sweetolive","azalea","chinesetea","agarwood","ylang-ylang"],
            "buyCities":["naha","hangzhou","chang","hanyang"],
            "supplyCities":["macau","pasay","toamasina","cape","pernambuco","cayenne","caracas"],
            "useSkillCity":"maracaibo",
            "sellCities":[{"name":"maracaibo","types":None},{"name":"veracruz","types":"BM"}],
        },
    ],

    #3 Winter Nov-Feb, Carrebean-EA, EA-perfume->, Carrebean-luxury+ (Nov EA+, carrebean dye-, luxury+)
    [
        {
            "buyFleet":4,
            "buyProducts": ["opal","tequila","pineapple","logwood"],
            "buyCities":["havana","southside","roya","santiago"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": [],
            "sellFleet":2,
            "supplyCities":["juan","praia","elmina","luanda","cape","toamasina","pasay"],
            "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":"BM"},{"name":"palembang","types":"BM"},
            {"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
            {"name":"hobe","types":["placeholder"]},{"name":"chang","types":None}
            ]
        },
        EABuyBM,
        {
            **EADoubleBuy,
            "supplyCities":["macau","pasay","toamasina","cape","pernambuco","cayenne","caracas"],
            "useSkillCity":"maracaibo",
            "sellCities":[{"name":"maracaibo","types":None},{"name":"veracruz","types":"BM"}],
        }
    ],  
    #4 Summer Jun-Aug, NorthE-EA
    [
        {
            **NEEASupplySell,
            "buyFleet":4,
            "buyStrategy":"twice",
            "buyProducts": ["twohand","lilyof","felt","gobelin","woodenshoe","steel","vodka","aquavit","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
            "buyCities":["hamburg","bremen","london","dover","den","antwerp","bristol","bordeaux","seville","laga"],
            "sellFleet":2,
        },
        # EABuyBM,
        {
            **EADoubleBuy,
            "buyProductsAfterSupply": ["chinesepainting","shubrocade","candycraft","amethyst","yosegi","sweetolive"],
            "buyProductsAfterSupplyCities": ["chang","edo","nagasaki","sakai","hangzhou"]
        }
    ],
    #5 Autumn Sep-Nov, NE-EA, EA-perfume+
    [
        {
            **NEEASupplySell,
            "buyFleet":4,
            "buyStrategy":"twice",
            "buyProducts": ["twohand","lilyof","felt","gobelin","woodenshoe","steel","vodka","aquavit","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
            "buyCities":["bremen","london","dover","den","antwerp","bristol","bordeaux","seville","laga"],
            "sellFleet":2,
        },
        # EABuyBM,
        {
            **EADoubleBuy,
            "buyProducts": ["gardenia","sweetolive","azalea","chinesetea","agarwood","ylang-ylang"],
            "buyProductsAfterSupply": [],
            "buyCities":["naha","hangzhou","chang","hanyang"],
        }
    ],
    #6 Winter Dec-Feb, NE-EA, EA-perfume->, liquor+
    [
        {
            **NEEASupplySell,
            "buyFleet":4,
            "buyStrategy":"twice",
            "buyProducts": ["twohand","lilyof","gobelin","steel","vodka","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
            "buyCities":["saint","stockhol","visby","riga","edinburgh","groningen","amsterda","london","dover"],
            "sellFleet":2,
        },
        # EABuyBM,
        {
            **EADoubleBuy,
            "buyProductsAfterSupply": ["chinesepainting","shubrocade","candycraft","amethyst","yosegi","sweetolive"],
            "buyProductsAfterSupplyCities": ["chang","edo","nagasaki","sakai","hangzhou"]
        }
    ],
    #7 Spring Dec-Feb, NE-EA, EA-perfume->, liquor+
    [
        {
            **NEEASupplySell,
            "buyFleet":4,
            "buyStrategy":"twice",
            "buyProducts": ["twohand","lilyof","gobelin","steel","vodka","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
            "buyCities":["saint","stockhol","visby","riga","edinburgh","groningen","amsterda","london","dover","santa"],
            "sellFleet":2,
        },
        # EABuyBM,
        {
            **EADoubleBuy,
            "buyProducts": ["begonia","tiger'seye","gardenia","sweetolive","azalea","chinesetea","agarwood","ylang-ylang","chinesepainting","shubrocade","easterncannon","goryeo"],
            "buyProductsAfterSupply": ["horseback","japanesepainting","candycraft","amethyst","nishijin","yosegi","sweetolive"],
            "buyProductsAfterSupplyCities": ["edo","nagasaki","sakai","hangzhou"]
        }
    ],
    [
        {
            **apacheRouteBase,
            "villages": ["apache"],
            "buyCities":["natal"],
            "afterSellCities": ["hadiboh","aceh"]
        },
        {
            "buyProducts": [],
            "buyFleet":4,
            "buyCities":["prey","deokwon"],
            "enableVillageTrade": True,
            "useFishingCities": [],
            "villages": ["witoto"],
            "afterVillageBuyCities": [],
            "supplyCities":["pernambuco","cape","toamasina","pasay","dongnae"],
            "sellFleet":7,
            # "useSkillCity":"suez",
            "checkInnCities": True,
            "sellPriceIndex": 0,
            "sellCityOptions":["hanyang","jeju","dongnae","yeongil","deokwon"],
            "fashions": ["赞助"],
            "waitForFashion":True,           
            "afterSellCities": ["hanyang","tainan","malacca","mogadishu"]
        },
        {
            **apacheRouteBase,
            "villages": ["apac"],
            "buyCities":["sofala","aden"],
            "afterSellCities": ["suez"]
        },
        {
            "buyCities":["suez"],
            "mode": "tunnel",
            "supplyCities":["barcelona"],
        },
        # {"mode": "landing"},
        {
            "mode": "merchantQuest",
            "supplyCities":["hadiboh","aceh","ambon","ternate"],
            "checkInnCities": True
        },
        {
            "mode": "battle",
            "buyCities":["ternate"],
        },
        {
            "buyProducts": [],
            "buyFleet":4,
            "buyCities":["kuching"],
            "enableVillageTrade": True,
            "useFishingCities": [],
            "villages": ["witot"],
            "afterVillageBuyCities": [],
            "supplyCities":["pernambuco","cape","toamasina","pasay","dongnae"],
            "sellFleet":7,
            # "useSkillCity":"suez",
            "checkInnCities": True,
            "sellPriceIndex": 0,
            "sellCityOptions":["hanyang","jeju","dongnae","yeongil","deokwon"],
            "fashions": ["赞助"],
            "waitForFashion":True,           
            "afterSellCities": ["hanyang","tainan","malacca","mogadishu"]
        }
        # {
        #     **NEEASupplySell,
        #     "buyFleet":4,
        #     "villages": ["svear"],
        #     "buyStrategy":"twice",
        #     "buyProducts": ["twohand","lilyof","gobelin","steel","vodka","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
        #     "buyCities":["saint","stockhol","visby","riga","edinburgh","groningen","amsterda","london","dover"],
        #     "sellFleet":2,
        #     "useSkillCity": None,
        #     "sellCityOptions":["macau","quanzhou","hobe","hangzhou","yanyun","peking","hanyang","jeju","chang","chongqing"],
        #     "fashions": ["奢华","赞助"],  
        #     "sellPriceIndex":0,
        #     "waitForFashion":False,    
        #     "afterSellCities": [{"route":4,"target":"mogadishu"}]
        # },
        # {
        #     **NEEASupplySell,
        #     "buyFleet":4,
        #     "villages": ["varo"],
        #     "buyStrategy":"twice",
        #     "buyProducts": [],
        #     "buyCities":[],
        #     "supplyCities":[{"route":4,"target":"dongnae"}],
        #     "sellFleet":2,
        #     "afterSellCities": ["aden"]
        # }

        # check passed day or pause
    ]

    #x NE valuable cities: liquor ok- saint-stockhol-visby-hamburg-bremen
    #liquor bad route: hamburg,bremen,helder,antwerp,calais,
]
