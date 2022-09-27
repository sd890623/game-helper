# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
cityNames=[]

#Liquer+
# "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","cheese"],
# "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],

# Shared object
northEuropeStd={
    # ,"tourmaline","amber", "jewllery""glassbead"
    "buyProducts": ["gobelin","steel","vodka","aquavit","gin","whisky"],
    # "gda", "hamburg"
    # Feb alchohol+
    "buyCities":["saint","riga","copenhag","groningen","amsterda","london","dover","calais","plymouth","groningen","amsterda","london","dover","calais","plymouth"],
    # Light season
    # "buyCities":["saint","stockhol","visby","riga","copenhag","groningen","amsterda","london","dover","calais","plymouth","copenhag","groningen","amsterda","london","dover","calais","plymouth"],
    "buySupplyCities":["copenhag"],
    "dumpCrewCities": ["kochi"],
    "supplyCities":["london","ceuta","bissau","tom","karibi","cape","mozambiqu","kochi"],
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
        "supplyCities":["london","ceuta","bissau","tom","karibib","cape","mozambiqu","mogadish"],
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
            "supplyCities":["cape","tom","bissau","ceuta","london"],
            "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
        },
    ],
    #2 carrabean to north europe
    #need craft,alcohol,cloth,metal
    [
        {**northEuropeStd,
        "dumpCrewCities": [],
        "supplyCities":["london","ceuta","ponta","juan"],
        "sellCities":[{"name":"veracruz","types":None}],
        },
        {
            # obsidianclu golddust
            "buyProducts": ["opal","topaz","gold","emerald","silver","vanilla"],
            # "santiago"
            "buyCities":["santiago","juan","porlamar","caracas","willemsta","maracaib","cartagen","portobelo"],
            "buySupplyCities":[],
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
            "supplyCities":["london","ceuta","bissau"],
            "sellCities":[{"name":"abidj","types":None}],
        },
        {
            #"pearl","agate""malachit","pearl","goldwork"
            "buyProducts": ["pearl","agate","malachit","pearl","goldwork","golddust","orangeoi","ambergris","goldwork","lapislazu","frankincens","diamond","gold","tuberose","geraniu","platinum","emerald","pistachio"],
            "buyCities":["abidj","timbukt","benin","tom","elmina","abidj"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "supplyCities":["elmina","bissau","ceuta","london"],
            "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
        },
    ],
    #4 saint<->hindu
    [
        northEuropeStd,
        {
            #,"pepper","cashmere"
            "buyProducts": ["yogurt","musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine","taffeta","lapislazu","frankincens","diamond","gold","geraniu","platinum"],
            #
            "buyCities":["diu","goa","kozhikod","kochi","muscat","shiraz","hormuz"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "dumpCrewCities": ["mozambiqu"],
            "supplyCities":["kochi","mozambiqu","cape","tom","bissau","ceuta","london","copenhag"],
            "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
        },
    ],
        #5 saint<->hindu, double buy
    [
        northEuropeStd,
        {
            #"pepper","cashmere","yogurt",
            "buyProducts": ["musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine","taffeta","lapislazu","frankincens","diamond","gold","geraniu","platinum"],
            #
            "buyCities":["diu","goa","kozhikod","kochi"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "dumpCrewCities": ["mozambiqu"],
            "supplyCities":["kochi","mozambiqu","cape","tom","bissau","ceuta","london","copenhag"],
            "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
        },
    ]
]
