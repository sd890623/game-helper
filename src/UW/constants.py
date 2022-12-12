# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
# portgual reputation
#cityNames=["funchal","faro","lisboa","porto"]

cityNames=["funchal","faro","lisboa","porto"]

battleCity="pasay"
#"piratefleet", "assau": ganzi, pillage: banzi, robber: paomen"rob",
opponentNames=["assa","lag","illag","llag","pil"]

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
    "buyCities":["saint","stockhol","visby","riga","groningen","amsterda","edinburgh","london","dover","calais","plymouth","bristol","bordeaux","seville","laga","marseil","genoa"],
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
    "buyCities":["saint","stockhol","visby","riga","groningen","amsterda","edinburgh","london","dover","calais","plymouth","bristol","bordeaux","seville","laga","marseil","genoa","seville","laga","marseil","genoa","seville","laga","marseil","genoa"],
    "buySupplyCities":["copenhag"],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","elmina","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}
northEuropeLightSea={
    # "jewllery","tourmaline" ,"handcanno", "flannel","amber"
    "buyProducts": ["amber","twohandedswor","felt","gobelin","steel","vodka","aquavit","gin","whisky","tapestry","silverplate","westernarmo","westerncann","saffron","azulejo","almond"],
    "buyCities":["saint","stockhol","visby","copenhag","helder","edinburgh","london","dover","antwerp","calais","plymouth","bristol","nantes","bordeaux","porto","seville","laga","marseil","genoa","seville","laga","marseil","genoa","seville","laga","marseil","genoa"],
    "buySupplyCities":[],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"kochi","types":None}],
}

northEuropeBM={
    # ,"tourmaline","amber", "jewllery""glassbead",     
    "buyProducts": ["twohandedswor","azulejo","gobelin","steel","vodka","gin","whisky","westerncann","saffron","tapestry","aquavit","almond"],
    # "gda", "hamburg"
    # Feb alchohol+
    # Feb alchohol+-
    #
    "buyCities":["saint","stockhol","visby","beck","copenhag","oslo","hamburg","bremen","amsterda","london","dover","antwerp","calais","plymouth","nantes","bordeaux","porto","faro","laga","seville","lisboa"],
    "buySupplyCities":[],
    "dumpCrewCities": ["kochi"],
    "buyStrategy":"once",
    "supplyCities":["ceuta","bathurst","elmina","luanda","cape","sofala","zanzibar","manbasa","aden","hadiboh","muscat"],
    "sellCities":[{"name":"kochi","types":None}],
}

routeLists=[
    #0 saint<->eastland
    [
        {
            #
            "buyProducts": ["amber","felt","tourmaline","glassbead","jewelry","vodka","aquavit","gin","whisky"],
            # light season
            "buyCities":["saint","stockhol","visby","riga","gda","copenhag","hamburg","groningen","amsterda","london","dover","calais","plymouth","copenhag","hamburg","groningen","amsterda","london","dover","calais","plymouth"],
            "buySupplyCities":[],
            #light seaso3n
            "supplyCities":["london","ceuta","syracuse"],
            "sellCities":[{"name":"athens","types":None}],
        },
        {
            # marblestatu, marble
            "buyProducts": ["narcissu","civet","perfume","oakmos"],
            "buyCities":["alexandr","cairo","said","jaffa","beirut","athens","candia"],
            "buySupplyCities":[],
            "supplyCities":["syracuse","ceuta","london"],
            "sellCities":[{"name":"saint","types":None}],
        },
    ],

    #1 saint<->east africa
    [
        {**northEuropeStd,
        "supplyCities":["london","ceuta","bathurst","tom","karibib","cape","mozambiqu","mogadish"],
        "sellCities":[{"name":"massawa","types":None}],
        "dumpCrewCities": [],
        },
        {
            # "pearl","agate","malachit","pearl","orangeoi","goldwork"
            "buyProducts": ["lapislazu","frankincens","diamond","gold","tuberose","geraniu","platinum","emerald","pistachio"],
            #,"malindi","manbasa"
            "buyCities":["aden","mogadish","zanzibar","mozambiqu","queliman","sofala","natal","mogadish","zanzibar","mozambiqu","queliman","sofala","natal","cape","karibi","benguel","luanda","tom","timbukt","tom","cape","karibi","benguel","luanda"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "dumpCrewCities": [],
            "supplyCities":["cape","tom","bathurst","ceuta","london"],
            "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
        },
    ],
    #2 carrabean to north europe
    #need craft,alcohol,cloth,metal
    [
        {**northEuropeStd,
        "dumpCrewCities": ["juan"],
        "supplyCities":["london","ceuta","ponta","juan"],
        "sellCities":[{"name":"veracruz","types":None}],
        },
        {
            # obsidianclu golddust
            "buyProducts": ["opal","topaz","gold","emerald","silver","vanilla"],
            # "santiago"
            "buyCities":["santiago","juan","porlamar","caracas","willemsta","maracaib","cartagen","portobelo"],
            "buySupplyCities":[],
            "dumpCrewCities": ["ponta"],
            "supplyCities":["juan","ponta","london"],
            "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
        },
    ],
    #3 saint<->west africa
    [
        {
            # "tourmaline",
            "buyProducts": ["glassbead","steel","vodka","aquavit","gin","whisky","amber","felt"],
            "buyCities":["saint","stockhol","visby","riga","gda","copenhag","hamburg","groningen","amsterda","london","dover","plymouth","copenhag","hamburg","groningen","amsterda","london","dover","plymouth"],
            "buySupplyCities":[],
            "supplyCities":["london","ceuta","bathurst"],
            "sellCities":[{"name":"abidj","types":None}],
        },
        {
            #"pearl","agate""malachit","pearl","goldwork"
            "buyProducts": ["pearl","agate","malachit","pearl","goldwork","golddust","orangeoi","ambergris","goldwork","lapislazu","frankincens","diamond","gold","tuberose","geraniu","platinum","emerald","pistachio"],
            "buyCities":["abidj","timbukt","benin","tom","elmina","abidj"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "supplyCities":["elmina","bathurst","ceuta","london"],
            "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
        },
    ],
    #4 saint<->hindu
    [
        northEuropeHot,
        {
            #,"pepper","cashmere"
            "buyProducts": ["yogurt","musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine","taffeta","lapislazu","frankincens","diamond","gold","geraniu","platinum"],
            #
            "buyCities":["diu","goa","kozhikod","kochi","muscat","shiraz","hormuz"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "dumpCrewCities": ["mozambiqu"],
            "supplyCities":["kochi","mozambiqu","cape","tom","bathurst","ceuta","london"],
            "sellCities":[{"name":"kokkola","types":None}],
        },
    ],
        #5 saint<->hindu, double buy
    [
        northEuropeHot,
        {
            #,"blacktea"
            "buyProducts": ["musk","turquoise","ruby","sapphire","aventurin","jasmine","taffeta","lapislazu","frankincens","diamond","gold","geraniu","platinum"],
            #
            "buyCities":["diu","goa","kozhikod","kochi"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": ["mozambiqu"],
            "supplyCities":["kochi","mozambiqu","cape","tom","bathurst","ceuta","london"],
            #{"name":"beck","types":["perfume"]},{"name":"riga","types":["jewelry"]}
            "sellCities":[{"name":"beck","types":["perfume"]},{"name":"gda","types":None}],
        },
    ],
    #6 saint<->hindu BM every day
    [
        northEuropeBM,
        {
            #,"pepper","cashmere"
            "buyProducts": ["musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine","taffeta","lapislazu","frankincens","diamond","gold","geraniu","platinum"],
            #
            "buyCities":["diu","goa","kozhikod","kochi","muscat","baghdad","basrah","hormuz"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "dumpCrewCities": ["mozambiqu"],
            "supplyCities":["kochi","mozambiqu","cape","tom","bathurst","ceuta","london"],
            "sellCities":[{"name":"kokkola","types":None}],
        },
    ],
    #7 carrebean<->SEA
    [
        # #light
        # {
        #     # obsidianclu golddust cacao
        #     "buyProducts": ["opal","topaz","tequila","obsidianclu","tobacco","pineapple","logwood","allspice"],
        #     "buyCities":["southside","royal","juan","porlamar","caracas","willemstad","trujil"],
        #     "buySupplyCities":[],
        #     "dumpCrewCities": [],
        #     "supplyCities":["juan","praia","elmina","luanda","cape","mozambiqu","toamasina","aceh"],
        #     #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
        #     "sellCities":[{"name":"malacca","types":["liquor"]},{"name":"palembang","types":None}],
        # },
        #harvest
        {
            # obsidianclu golddust cacao ,"allspice"]
            "buyProducts": ["opal","topaz","tequila","pineapple","logwood"],
            "buyCities":["havana","southside","royal","santiago","porlamar"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": [],
            "supplyCities":["juan","praia","elmina","luanda","cape","toamasina","aceh"],
            #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
            "sellCities":[{"name":"malacca","types":["liquor"]},{"name":"palembang","types":None}],
        },
        {
            "buyProducts": ["mangosteen","agarwood","ylang-ylang","benzoin","musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine"],
            "buyCities":["aceh","pasay","malacca"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": ["mozambiqu"],
            "supplyCities":["aceh","toamasina","cape","tom","bathurst","cayenne","caracas","trujil"],
            "sellCities":[{"name":"rida","types":None}],
        },
    ],
    #8 carrebean<->NorthEu<->SEA
    [
        {
            # obsidianclu golddust cacao
            "buyProducts": ["gold","opal","topaz","tequila","obsidianclu","tobacco","pineapple","logwood","allspice","gold","emerald","silver","vanilla"],
            "buyCities":["havana","southside","royal","santiago","porlamar","caracas","willemstad"],
            "buySupplyCities":[],
            "dumpCrewCities": [],
            "supplyCities":["juan","ponta","london"],
            "sellCities":[{"name":"saint","types":None}],
        },
        {**northEuropeHot,
            "supplyCities":["ceuta","bathurst","elmina","luanda","cape","mozambiqu","toamasina","aceh"],
            "sellCities":[{"name":"malacca","types":["liquor"]},{"name":"palembang","types":None}],
        },
        {
            "buyProducts": ["mangosteen","agarwood","ylang-ylang","benzoin","musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine"],
            "buyCities":["aceh","pasay","malacca"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": ["mozambiqu"],
            "supplyCities":["aceh","toamasina","mozambiqu","cape","tom","bathurst","cayenne","caracas","trujil"],
            "sellCities":[{"name":"rida","types":None}],
        },
    ],
    #9 carrebean<->SEA 80area
    [
        #light
        {
            # obsidianclu golddust cacao "obsidianclu" "topaz" vanilla,"allspice" "tobacco"
            "buyProducts": ["opal","tequila","pineapple","logwood"],
            "buyCities":["southside","royal","willemstad","porlamar","caracas","juan"],
            "buyStrategy":"twice",
            "buySupplyCities":[],
            "dumpCrewCities": [],
            "supplyCities":["juan","praia","elmina","luanda","cape","toamasina","aceh"],
            #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
            "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":["liquor"]},{"name":"palembang","types":"BM"},{"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},{"name":"banda","types":None}],
        },
        # #harvest
        # {
        #     # obsidianclu golddust cacao ,"allspice"]
        #     "buyProducts": ["opal","tequila","pineapple","logwood"],
        #     "buyCities":["havana","southside","royal","santiago"],
        #     "buySupplyCities":[],
        #     "buyStrategy":"twice",
        #     "dumpCrewCities": [],
        #     "supplyCities":["juan","praia","elmina","luanda","cape","toamasina","aceh"],
        #     #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
        #     "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":["liquor"]},{"name":"palembang","types":"BM"},{"name":"jayakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},{"name":"banda","types":None}],
        # },
        {
            #,"clove" ,"benzoin"  ,"feathercrafts"  
            "buyProducts": ["ebony","agarwood","ylang-ylang","musk","mace","nutmeg","mangosteen"],
            "buyCities":["banda","ambon","ternate","jolo","brunei","jayakarta","pasay","aceh"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": [],
            "supplyCities":["aceh","toamasina","cape","pernambuco","cayenne","caracas","trujil"],
            "useSkillCity":"trujil",
            "sellCities":[{"name":"rida","types":["perfume","dye"]},{"name":"veracruz","types":"BM"},{"name":"southside","types":None},{"name":"santiago","types":"BM"},{"name":"santo","types":"BM"}],
        },
    ],
]
