# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
# portgual reputation
#cityNames=["funchal","faro","lisboa","porto"]

cityNames=["funchal","faro","lisboa","porto"]

battleCity="xi"
#"piratefleet", "assau": ganzi, pillage: banzi, robber: paomen"rob",  ,"assa","rob" ,"assa"
opponentNames=["lag","illag","llag","pil","rob"]

#Liquer+
# "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","cheese"],
# "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],

# Shared object
northEuropeHot={
    # ,"tourmaline","amber", "jewllery""glassbead","aquavit"
    "buyProducts": ["twohandedswor","gobelin","steel","vodka","gin","whisky","westerncann","saffron","westernarmo"],
    # "gda", "hamburg"
    # Feb alchohol+
    # "buyCities":["saint","riga","copenhag","groningen","amsterda","london","dover","calais","plymouth","groningen","amsterda","london","dover","calais","plymouth"],
    # Feb alchohol+-
    "buyCities":["saint","stockhol","visby","riga","bergen","edinburgh","groningen","amsterda","london","dover","bristol","bordeaux","seville","laga","marseil","genoa"],
    "buySupplyCities":["copenhag"],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}
northEuropeStd={
    # ,"tourmaline","amber", "jewllery""glassbead"
    "buyProducts": ["twohandedswor","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","westerncann","westernarmo","saffron","azulejo","almond"],
    # "gda", "hamburg"
    # Feb alchohol+
    # Feb alchohol+-
    "buyCities":["saint","stockhol","visby","copenhag","bergen","edinburgh","groningen","amsterda","london","dover","calais","plymouth","bristol","bordeaux","seville","laga","marseil","genoa","seville","laga","marseil","genoa","seville","laga","marseil","genoa"],
    "buySupplyCities":["copenhag"],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","elmina","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}
northEuropeLightSea={
    # "jewllery", ,"handcanno", "flannel",
    "buyProducts": ["amber","chrysoberyl","tourmaline","twohandedswor","felt","feather","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","silverplate","westernarmo","westerncann","saffron","azulejo","almond"],
    "buyCities":["saint","stockhol","visby","copenhag","london"],
    "buySupplyCities":[],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}
northEuropeQuick={
    # "jewllery","tourmaline" ,"handcanno", "flannel","amber"
    "buyProducts": ["amber","twohandedswor","felt","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","westernarmo","westerncann","saffron","azulejo","almond"],
    "buyCities":["stockhol","visby","beck","copenhag","bergen","edinburgh","groningen","amsterda","london","dover","antwerp","calais","bristol","nantes","bordeaux","porto","seville","laga","marseil","genoa","seville","laga","marseil","genoa","seville","laga","marseil","genoa"],
    "buySupplyCities":[],
    "buyStrategy":"once",
    "dumpCrewCities": [""],
    "supplyCities":["lisboa","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}

NEEASupplySell={
    # "jewllery","tourmaline" ,"handcanno", "flannel","amber"
    "buyProducts": ["amber","twohandedswor","felt","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","westernarmo","westerncann","saffron","azulejo","almond"],
    "buyCities":["stockhol","visby","beck","copenhag","bergen","edinburgh","groningen","amsterda","london","dover","antwerp","calais","bristol","nantes","bordeaux","porto","seville","laga","marseil","genoa","seville","laga","marseil","genoa","seville","laga","marseil","genoa"],
    "buySupplyCities":[],
    "dumpCrewCities": [""],
    "supplyCities":["laga","lisboa","bathurst","luanda","cape","toamasina","aceh"],
    #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
    "sellCities":[{"name":"pasay","types":"BM"},{"name":"palembang","types":"BM"},
    {"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
    {"name":"hobe","types":["placeholder"]},{"name":"hanyang","types":None}]
}
EADoubleBuy={
    #,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
    "buyProducts": ["gardenia","begoniaflower","sweetolive","azalea","tiger'seye","chinesetea","agarwood","ylang-ylang"],
    "buyCities":["shuri","hobe","hangzhou","xi'an","hanyang","jeju"],
    "buySupplyCities":[],
    "buyStrategy":"twice",
    "dumpCrewCities": [],
    "sellFleet":2,
    "supplyCities":["macau","pasay","toamasina","cape","bathurst","lisboa","london"],
    "useSkillCity":"beck",
    "sellCities":[{"name":"beck","types":["perfume"]},{"name":"riga","types":None},{"name":"saint","types":"BM"}],
}
EABuyBM={
    "buyFleet":4,
    "buyStrategy":"once",
    # , ,"shaoxingwine", "goryeoceladon","chinesepainting","easterncannon"
    "buyProducts": ["gardenia","begoniaflower","sweetolive","azalea"],#,"tiger'seye"],
    "buyCities":["hobe","hanyang","jeju"],#,"quanzhou","hobe","hangzhou","xi'an","peking","hanyang","jeju","macau",],
    "deductBuyBM":True,
    "buySupplyCities":[],
    "dumpCrewCities": [],
    "supplyCities":[],
    "sellCities":[],
}

routeLists=[
    # northEu liquor Dec-Feb(Inc)Winter+, mar-May(Spring)STD, Jun-(Summer)-
    # EA: Perfume: Dec-Jan(Winter),STD, Feb-May(Spring)-, Jun-(Summer)STD,
    # Carrebean: Dec-May: Liquor,Lux+    Jun-Nov: Dye,Gem+

    #0 SEA-Carrebean  mar-May-spring, 
    [
        #harvest
        {
            "buyFleet":2,
            "buyProducts": ["opal","tequila","pineapple","logwood"],
            "buyCities":["havana","southside","royal","santiago"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": [],
            "supplyCities":["juan","praia","elmina","luanda","cape","toamasina","aceh"],
            #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
            "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":"BM"},{"name":"macau","types":["placeholder"]},{"name":"hanyang","types":None},{"name":"palembang","types":"BM"},{"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"}],
        },
        {
            "buyProducts": ["ebony","agarwood","ylang-ylang","musk","mace","mangosteen"],
            "buyCities":["banda","ambon","ternate","jolo","makassar","banjarmasin","jayakarta","pasay","aceh"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": [],
            "supplyCities":["aceh","toamasina","cape","pernambuco","cayenne","caracas","trujil"],
            "useSkillCity":"rida",
            "sellCities":[{"name":"rida","types":["perfume","dye"]},{"name":"veracruz","types":"BM"},{"name":"southside","types":None}],
        },
    ],
    #1 Summer Jun-Aug, NorthE-EA, 
    [
        {
            **NEEASupplySell,
            "buyFleet":4,
            "buyStrategy":"twice",
            "buyProducts": ["twohandedswor","lilyofthevalley","felt","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","westernarmo","westerncann","saffron","azulejo","almond"],
            "buyCities":["hamburg","bremen","london","dover","calais","plymouth","bordeaux","laga","seville"],
            "sellFleet":2,
        },
        EABuyBM,
        EADoubleBuy,
    ],

    #2 Autumn Sep-Nov, NorthE-EA, EA-perfume+, NE-perfume+
    [
        {
            **NEEASupplySell,
            "buyFleet":4,
            "buyStrategy":"twice",
            "buyProducts": ["twohandedswor","lilyofthevalley","felt","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","westernarmo","westerncann","saffron","azulejo","almond"],
            "buyCities":["hamburg","bremen","london","dover","hamburg","bremen","london","dover","laga","seville"],
            "sellFleet":2,
        },
        EABuyBM,
        {
            **EADoubleBuy,
            #,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
            "buyProducts": ["gardenia","begoniaflower","sweetolive","azalea","chinesetea","agarwood","ylang-ylang"],
            "buyCities":["shuri","hobe","hangzhou","xi'an","hanyang"]
        },
    ],

    #3 Winter Dec-Feb, NorthE-EA, NE-liquor+
    [
        {
            **NEEASupplySell,
            "buyStrategy":"twice",
            "buyProducts": ["twohandedswor","lilyofthevalley","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","westernarmo","westerncann","saffron","azulejo","almond"],
            "buyCities":["saint","stockhol","visby","riga","groningen","amsterda","london","dover"],
            "sellFleet":2,
        },
        EABuyBM,
        EADoubleBuy,
    ],

    #4 Summer Dec-Feb, NorthE-EA, NE-liquor-, temp for Korea
    [
        {
            **NEEASupplySell,
            "buyFleet":4,
            "buyProducts": ["twohandedswor","lilyofthevalley","gobelin","steel","vodka","felt","aquavit","gin","whisky","tapestry","westernarmo","westerncann","saffron","azulejo","almond"],
            "buyCities":["hamburg","bremen","london","dover","calais","plymouth","bordeaux","laga","seville"],
            "sellFleet":2,
        },
        EABuyBM,
        EADoubleBuy
    ],
        
    #x NE valuable cities: liquor ok- saint-stockhol-visby-hamburg-bremen
    #liquor bad route: hamburg,bremen,helder,antwerp,calais,
]
