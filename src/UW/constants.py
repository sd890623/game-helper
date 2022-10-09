# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
cityNames=[]

#Liquer+
# "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","cheese"],
# "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],

# Shared object
northEuropeHot={
    # ,"tourmaline","amber", "jewllery""glassbead"
    "buyProducts": ["gobelin","steel","vodka","aquavit","gin","whisky","westerncann","saffron"],
    # "gda", "hamburg"
    # Feb alchohol+
    # "buyCities":["saint","riga","copenhag","groningen","amsterda","london","dover","calais","plymouth","groningen","amsterda","london","dover","calais","plymouth"],
    # Feb alchohol+-
    "buyCities":["saint","riga","copenhag","groningen","amsterda","london","dover","calais","plymouth","groningen","amsterda","london","dover","calais","plymouth","laga","seville","lisboa"],
    "buySupplyCities":["copenhag"],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"diu","types":None}],
}
northEuropeStd={
    # ,"tourmaline","amber", "jewllery""glassbead"
    "buyProducts": ["tapestry","gobelin","steel","vodka","aquavit","gin","whisky","westerncann","saffron","almond"],
    # "gda", "hamburg"
    # Feb alchohol+
    # Feb alchohol+-
    "buyCities":["saint","stockhol","visby","riga","copenhag","bremen","groningen","amsterda","london","dover","antwerp","calais","plymouth","nantes","laga","seville","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga"],
    "buySupplyCities":["copenhag"],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"diu","types":None}],
}
northEuropeLightSea={
    # "jewllery","tourmaline" ,"handcanno", "flannel","chrysoberyl"
    "buyProducts": ["gobelin","steel","vodka","aquavit","gin","whisky","glassbead","tapestry","amber","silverplate","westerncann","saffron","almond","matchlockgun"],
    "buyCities":["saint","beck","copenhag","bremen","groningen","amsterda","london","dover","antwerp","calais","plymouth","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga","lisboa","seville","laga"],
    "buySupplyCities":[],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["ceuta","bathurst","luanda","cape","mozambiqu","kochi"],
    "sellCities":[{"name":"diu","types":None}],
}

northEuropeBM={
    # ,"tourmaline","amber", "jewllery""glassbead",     "tapestry","aquavit", "almond"
    "buyProducts": ["gobelin","steel","vodka","gin","whisky","westerncann","saffron"],
    # "gda", "hamburg"
    # Feb alchohol+
    # Feb alchohol+-
    "buyCities":["saint","stockhol","visby","beck","copenhag","oslo","hamburg","bremen","amsterda",
    "london","dover","antwerp","calais","plymouth","nantes","bordeaux","porto","laga","seville","lisboa"],
    "buySupplyCities":[],
    "dumpCrewCities": ["kochi"],
    "buyStrategy":"once",
    "supplyCities":["ceuta","bathurst","elmina","luanda","cape","sofala","mozambiqu","zanzibar","manbasa","mozambiqu","kochi"],
    "sellCities":[{"name":"diu","types":None}],
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
            "sellCities":[{"name":"beck","types":["perfume"]},{"name":"kokkola","types":None}],
        },
    ],
        #5 saint<->hindu, double buy
    [
        northEuropeHot,
        {
            "buyProducts": ["musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine","taffeta","lapislazu","frankincens","diamond","gold","geraniu","platinum"],
            #
            "buyCities":["diu","goa","kozhikod","kochi"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "dumpCrewCities": ["mozambiqu"],
            "supplyCities":["kochi","mozambiqu","cape","tom","bathurst","ceuta","london"],
            #{"name":"beck","types":["perfume"]},{"name":"riga","types":["jewelry"]}
            "sellCities":[{"name":"kokkola","types":None}],
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
            "sellCities":[{"name":"beck","types":["perfume"]},{"name":"kokkola","types":None}],
        },
    ],
]
