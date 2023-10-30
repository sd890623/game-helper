# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
# portgual reputation
#cityNames=["funchal","faro","lisboa","porto"]

cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]

battleCity="edo"
# battleCity="ezo"

#"piratefleet", "assau": ganzi, pillage: banzi, robber: paomen"rob",  ,"assa","rob" ,"assa"
#opponentNames=["lag","illag","llag","pil","assa","asau"]
opponentsInList=["pil","ass","asa","aas","ruthless"
]
# "golitsynpil","golitsynas","azubuikepi","azubuikeas","chenzuyipil","chenzuyias","kaikap","kaikaa"]
opponentNames=["pill","pil","ass","asa","duchunyong","rob","ruthless","nanima"] #add ducunyong as it's double lines, so quick hack,only checked in board
blackListForBattle=['piz','zpi','robeyn','masa']
# rob: "rob",
#hanyang chowta ass, chenziyu pirate fleet, shiyang ass
#hobe azubuike, chenzuyi assu, lalkaika fleet, chowta rob, zubuike pill

#Liquer+
# "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","cheese"],
# "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],

# Shared object
northEuropeHot={
    # ,"tourmaline","amber", "jewllery""glassbead","aquavit"
    "buyProducts": ["twohand","gobelin","steel","vodka","gin","whisky","westerncann","saffron","western"],
    # "gda", "hamburg"
    # Feb alchohol+
    # "buyCities":["saint","riga","copenhag","groningen","amsterda","london","dover","calais","plymouth","groningen","amsterda","london","dover","calais","plymouth"],
    # Feb alchohol+-
    "buyCities":["saint","stockhol","visby","riga","bergen","edinburgh","groningen","amsterda","london","dover","bristol","bristol","bordeaux","seville","laga","marseil","genoa"],
    "buySupplyCities":["copenhag"],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}
northEuropeStd={
    # ,"tourmaline","amber", "jewllery""glassbead"
    "buyProducts": ["twohand","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","westerncann","western","saffron","azulejo","almond"],
    # "gda", "hamburg"
    # Feb alchohol+
    # Feb alchohol+-
    "buyCities":["saint","stockhol","visby","copenhag","bergen","edinburgh","groningen","amsterda","london","dover","calais","plymouth","bristol","bristol","bordeaux","seville","laga","marseil","genoa","seville","laga","marseil","genoa","seville","laga","marseil","genoa"],
    "buySupplyCities":["copenhag"],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","elmina","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}
northEuropeLightSea={
    # "jewllery", ,"handcanno", "flannel",
    "buyProducts": ["amber","chrysoberyl","tourmaline","twohand","felt","feather","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","silverplate","western","westerncann","saffron","azulejo","almond"],
    "buyCities":["saint","stockhol","visby","copenhag","london"],
    "buySupplyCities":[],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}
northEuropeQuick={
    # "jewllery","tourmaline" ,"handcanno", "flannel","amber"
    "buyProducts": ["amber","twohand","felt","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
    "buyCities":["stockhol","visby","beck","copenhag","bergen","edinburgh","groningen","amsterda","london","dover","antwerp","calais","bristol","nantes","bordeaux","porto","seville","laga","marseil","genoa","seville","laga","marseil","genoa","seville","laga","marseil","genoa"],
    "buySupplyCities":[],
    "buyStrategy":"once",
    "dumpCrewCities": [""],
    "supplyCities":["lisboa","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}

NEEASupplySell={
    # "jewllery","tourmaline" ,"handcanno", "flannel","amber"
    "buyProducts": ["amber","twohand","felt","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
    "buyCities":["stockhol","visby","beck","copenhag","bergen","edinburgh","groningen","amsterda","london","dover","antwerp","calais","bristol","nantes","bordeaux","porto","seville","laga","marseil","genoa","seville","laga","marseil","genoa","seville","laga","marseil","genoa"],
    "buySupplyCities":[],
    "dumpCrewCities": [""],
    "supplyCities":["lisboa","bathurst","luanda","cape","toamasina","pasay"],
    "sellCities":[{"name":"pasay","types":"BM"},
    # {"name":"malacca","types":"BM"},{"name":"palembang","types":"BM"},
    # {"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
    {"name":"hobe","types":"supply"},{"name":"chang","types":None}]
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
    "sellFleet":2,
    "supplyCities":["macau","pasay","toamasina","cape","soda","bathurst","lisboa","london"],
    "useSkillCity":"beck",
    "sellCities":[{"name":"beck","types":None},{"name":"saint","types":"BM"}],
}
EABuyBM={
    "buyFleet":4,
    "buyStrategy":"once",
    # , ,"shaoxingwine", "goryeoceladon","chinesepainting","easterncannon"
    "buyProducts": ["gardenia","begonia","sweetolive","azalea"],#,"tiger'seye"],
    "buyCities":["peking","hanyang","dongnae","jeju","chongqing","hangzhou","quanzhou","hobe"],#,"quanzhou","hobe","hangzhou","chang","hanyang","jeju","macau",],
    "deductBuyBM":True,
    "buySupplyCities":[],
    "dumpCrewCities": [],
    "supplyCities":[],
    "sellCities":[],
}

routeLists=[
    # northEu liquor Dec-Feb(Inc)Winter+, mar-May(Spring)STD, Jun-(Summer)-
    # EA: Perfume: Dec-Feb(Winter),STD, Mar-May(Spring)-, Jun-(Summer)Aug STD,Sep-Nov(Autumn)++
    # Carrebean: Nov-May: Liquor,Lux+    Jun-Oct: Dye,Gem+

    #0 SEA-Carrebean  mar-May-spring, 
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
        EABuyBM,
        {
            **EADoubleBuy,
            "buyProductsAfterSupply": ["horseback","japanesepainting","candycraft","amethyst","nishijin","yosegi","sweetolive"],
            "buyProductsAfterSupplyCities": ["edo","nagasaki","sakai","hangzhou"]
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
        EABuyBM,
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
        EABuyBM,
        {
            **EADoubleBuy,
            "buyProductsAfterSupply": ["horseback","japanesepainting","candycraft","amethyst","nishijin","yosegi","sweetolive"],
            "buyProductsAfterSupplyCities": ["edo","nagasaki","sakai","hangzhou"]
        }
    ],
    #7 Spring Dec-Feb, NE-EA, EA-perfume->, liquor+
    [
        {
            **NEEASupplySell,
            "buyFleet":4,
            "buyStrategy":"twice",
            "buyProducts": ["twohand","lilyof","gobelin","steel","vodka","gin","whisky","tapestry","western","westerncann","saffron","azulejo","almond"],
            "buyCities":["saint","stockhol","visby","riga","edinburgh","groningen","amsterda","london","dover"],
            "sellFleet":2,
        },
        EABuyBM,
        {
            **EADoubleBuy,
            "buyProducts": ["begonia","tiger'seye","gardenia","sweetolive","azalea","chinesetea","agarwood","ylang-ylang","chinesepainting","shubrocade","cannon","celadon"],
            "buyProductsAfterSupply": ["horseback","japanesepainting","candycraft","amethyst","nishijin","yosegi","sweetolive"],
            "buyProductsAfterSupplyCities": ["edo","nagasaki","sakai","hangzhou"]
        }
    ]

    #x NE valuable cities: liquor ok- saint-stockhol-visby-hamburg-bremen
    #liquor bad route: hamburg,bremen,helder,antwerp,calais,
]
