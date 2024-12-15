routeList=[

     # #0 saint<->eastland
    # [
    #     {
    #         #
    #         "buyProducts": ["amber","felt","tourmaline","glassbead","jewelry","vodka","aquavit","gin","whisky"],
    #         # light season
    #         "buyCities":["saint","stockhol","visby","riga","gda","copenhag","hamburg","groningen","amsterda","london","dover","calais","plymouth","copenhag","hamburg","groningen","amsterda","london","dover","calais","plymouth"],
    #         "buySupplyCities":[],
    #         #light seaso3n
    #         "supplyCities":["london","ceuta","syracuse"],
    #         "sellCities":[{"name":"athens","types":None}],
    #     },
    #     {
    #         # marblestatu, marble
    #         "buyProducts": ["narcissu","civet","perfume","oakmos"],
    #         "buyCities":["alexandr","cairo","said","jaffa","beirut","athens","candia"],
    #         "buySupplyCities":[],
    #         "supplyCities":["syracuse","ceuta","london"],
    #         "sellCities":[{"name":"saint","types":None}],
    #     },
    # ],

    # #1 saint<->east africa
    # [
    #     {**northEuropeStd,
    #     "supplyCities":["london","ceuta","bathurst","tom","karibib","town","mozambiqu","mogadish"],
    #     "sellCities":[{"name":"massawa","types":None}],
    #     "dumpCrewCities": [],
    #     },
    #     {
    #         # "pearl","agate","malachit","pearl","orangeoi","goldwork"
    #         "buyProducts": ["lapislazu","frankincens","diamond","gold","tuberose","geraniu","platinum","emerald","pistachio"],
    #         #,"malindi","mombasa"
    #         "buyCities":["aden","mogadish","zanzibar","mozambiqu","queliman","sofala","natal","mogadish","zanzibar","mozambiqu","queliman","sofala","natal","town","karibi","benguel","luanda","tom","timbukt","tom","town","karibi","benguel","luanda"],
    #         "buySupplyCities":[],
    #         "buyStrategy":"single",
    #         "dumpCrewCities": [],
    #         "supplyCities":["town","tom","bathurst","ceuta","london"],
    #         "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
    #     },
    # ],
    # #2 carrabean to north europe
    # #need craft,alcohol,cloth,metal
    # [
    #     {**northEuropeStd,
    #     "dumpCrewCities": ["juan"],
    #     "supplyCities":["london","ceuta","azores","juan"],
    #     "sellCities":[{"name":"veracruz","types":None}],
    #     },
    #     {
    #         # obsidianclu golddust
    #         "buyProducts": ["opal","topaz","gold","emerald","silver","vanilla"],
    #         # "santiago"
    #         "buyCities":["santiago","juan","porlamar","caracas","willemsta","maracaib","cartagen","portobelo"],
    #         "buySupplyCities":[],
    #         "dumpCrewCities": ["azores"],
    #         "supplyCities":["juan","azores","london"],
    #         "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
    #     },
    # ],
    # #3 saint<->west africa
    # [
    #     {
    #         # "tourmaline",
    #         "buyProducts": ["glassbead","steel","vodka","aquavit","gin","whisky","amber","felt"],
    #         "buyCities":["saint","stockhol","visby","riga","gda","copenhag","hamburg","groningen","amsterda","london","dover","plymouth","copenhag","hamburg","groningen","amsterda","london","dover","plymouth"],
    #         "buySupplyCities":[],
    #         "supplyCities":["london","ceuta","bathurst"],
    #         "sellCities":[{"name":"abidj","types":None}],
    #     },
    #     {
    #         #"pearl","agate""malachit","pearl","goldwork"
    #         "buyProducts": ["pearl","agate","malachit","pearl","goldwork","golddust","orangeoi","ambergris","goldwork","lapislazu","frankincens","diamond","gold","tuberose","geraniu","platinum","emerald","pistachio"],
    #         "buyCities":["abidj","timbukt","benin","tom","elmina","abidj"],
    #         "buySupplyCities":[],
    #         "buyStrategy":"single",
    #         "supplyCities":["elmina","bathurst","ceuta","london"],
    #         "sellCities":[{"name":"riga","types":["jewelry"]},{"name":"saint","types":None}],
    #     },
    # ],
    # #4 saint<->hindu
    # [
    #     northEuropeHot,
    #     {
    #         #,"pepper","cashmere"
    #         "buyProducts": ["yogurt","musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine","taffeta","lapislazu","frankincens","diamond","gold","geraniu","platinum"],
    #         #
    #         "buyCities":["diu","goa","kozhikod","kochi","muscat","shiraz","hormuz"],
    #         "buySupplyCities":[],
    #         "buyStrategy":"single",
    #         "dumpCrewCities": ["mozambiqu"],
    #         "supplyCities":["kochi","mozambiqu","town","tom","bathurst","ceuta","london"],
    #         "sellCities":[{"name":"kokkola","types":None}],
    #     },
    # ],
    #     #5 saint<->hindu, double buy
    # [
    #     northEuropeHot,
    #     {
    #         #,"blacktea"
    #         "buyProducts": ["musk","turquoise","ruby","sapphire","aventurin","jasmine","taffeta","lapislazu","frankincens","diamond","gold","geraniu","platinum"],
    #         #
    #         "buyCities":["diu","goa","kozhikod","kochi"],
    #         "buySupplyCities":[],
    #         "buyStrategy":"twice",
    #         "dumpCrewCities": ["mozambiqu"],
    #         "supplyCities":["kochi","mozambiqu","town","tom","bathurst","ceuta","london"],
    #         #{"name":"beck","types":["perfume"]},{"name":"riga","types":["jewelry"]}
    #         "sellCities":[{"name":"beck","types":["perfume"]},{"name":"gda","types":None}],
    #     },
    # ],
    # #6 saint<->hindu BM every day
    # [
    #     northEuropeBM,
    #     {
    #         #,"pepper","cashmere"
    #         "buyProducts": ["musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine","taffeta","lapislazu","frankincens","diamond","gold","geraniu","platinum"],
    #         #
    #         "buyCities":["diu","goa","kozhikod","kochi","muscat","baghdad","basrah","hormuz"],
    #         "buySupplyCities":[],
    #         "buyStrategy":"single",
    #         "dumpCrewCities": ["mozambiqu"],
    #         "supplyCities":["kochi","mozambiqu","town","tom","bathurst","ceuta","london"],
    #         "sellCities":[{"name":"kokkola","types":None}],
    #     },
    # ],
    # #7 carrebean<->SEA
    # [
    #     # #light
    #     # {
    #     #     # obsidianclu golddust cacao
    #     #     "buyProducts": ["opal","topaz","tequila","obsidianclu","tobacco","pineapple","logwood","allspice"],
    #     #     "buyCities":["southside","royal","juan","porlamar","caracas","willemstad","trujil"],
    #     #     "buySupplyCities":[],
    #     #     "dumpCrewCities": [],
    #     #     "supplyCities":["juan","verde","elmina","luanda","town","mozambiqu","toamasina","aceh"],
    #     #     #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
    #     #     "sellCities":[{"name":"malacca","types":["liquor"]},{"name":"palembang","types":None}],
    #     # },
    #     #harvest
    #     {
    #         # obsidianclu golddust cacao ,"allspice"]
    #         "buyProducts": ["opal","topaz","tequila","pineapple","logwood"],
    #         "buyCities":["havana","southside","royal","santiago","porlamar"],
    #         "buySupplyCities":[],
    #         "buyStrategy":"twice",
    #         "dumpCrewCities": [],
    #         "supplyCities":["juan","verde","elmina","luanda","town","toamasina","aceh"],
    #         #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
    #         "sellCities":[{"name":"malacca","types":["liquor"]},{"name":"palembang","types":None}],
    #     },
    #     {
    #         "buyProducts": ["mangosteen","agarwood","ylang-ylang","benzoin","musk","blacktea","turquoise","ruby","sapphire","aventurin","jasmine"],
    #         "buyCities":["aceh","pasay","malacca"],
    #         "buySupplyCities":[],
    #         "buyStrategy":"twice",
    #         "dumpCrewCities": ["mozambiqu"],
    #         "supplyCities":["aceh","toamasina","town","tom","bathurst","cayenne","caracas","trujil"],
    #         "sellCities":[{"name":"rida","types":None}],
    #     },
    # ],

#x triangle
    [
        {**northEuropeQuick,
            "supplyCities":["azores","juan"],
        },
        #light
        {
            "buyFleet":3,
            # obsidianclu golddust cacao "obsidianclu" "topaz" vanilla,"allspice" "tobacco"
            "buyProducts": ["opal","tequila","pineapple","logwood"],
            "buyCities":["southside","royal","willemstad","porlamar","caracas","juan"],
            "buyStrategy":"twice",
            "buySupplyCities":[],
            "dumpCrewCities": [],
            "supplyCities":["juan","verde","elmina","luanda","town","toamasina","aceh"],
            #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
            "sellCities":[{"name":"pasay","types":"BM"},{"name":"palembang","types":"BM"},
            {"name":"jakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},
            {"name":"davao","types":"dye"},{"name":"hanyang","types":None}]
        },
        # #harvest
        # {
        #     # obsidianclu golddust cacao ,"allspice"]
        #     "buyProducts": ["opal","tequila","pineapple","logwood"],
        #     "buyCities":["havana","southside","royal","santiago"],
        #     "buySupplyCities":[],
        #     "buyStrategy":"twice",
        #     "dumpCrewCities": [],
        #     "supplyCities":["juan","verde","elmina","luanda","town","toamasina","aceh"],
        #     #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
        #     "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":"BM"},{"name":"hanoi","types":None},{"name":"palembang","types":"BM"},{"name":"jakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"}],
        # },
        {**EABuyBM},
        {
            #,"goryeoceladon","chinesepainting","easterncannon" ,"tiger'seye",
            "buyProducts": ["gardenia","begoniaflower","sweetolive","azalea","tiger'seye","chinesetea","agarwood","ylang-ylang"],
            "buyCities":["shuri","tamsui","hangzhou","xi'an","hanyang","jeju"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": [],
            "sellFleet":2,
            "supplyCities":["macau","pasay","toamasina","town","bathurst","lisboa","london"],
            "useSkillCity":"beck",
            "sellCities":[{"name":"beck","types":"perfume"},{"name":"riga","types":None}],
        },
    ],
    #x carrebean<->SEA 80area
    # 2: harvest/liquor Nov-May(inclu)  3: Light/Dye
    [
        #light
        {
            # obsidianclu golddust cacao "obsidianclu" "topaz" vanilla,"allspice" "tobacco"
            "buyProducts": ["opal","tequila","pineapple","logwood"],
            "buyCities":["southside","royal","willemstad","porlamar","caracas","juan"],
            "buyStrategy":"twice",
            "buySupplyCities":[],
            "dumpCrewCities": [],
            "supplyCities":["juan","verde","elmina","luanda","town","toamasina","aceh"],
            #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
            "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":["liquor"]},{"name":"palembang","types":"BM"},{"name":"jakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"},{"name":"ambon","types":None}],
        },
        # #harvest
        # {
        #     # obsidianclu golddust cacao ,"allspice"]
        #     "buyProducts": ["opal","tequila","pineapple","logwood"],
        #     "buyCities":["havana","southside","royal","santiago"],
        #     "buySupplyCities":[],
        #     "buyStrategy":"twice",
        #     "dumpCrewCities": [],
        #     "supplyCities":["juan","verde","elmina","luanda","town","toamasina","aceh"],
        #     #"sellCities":[{"name":"malacca","types":["liquor"]},{"name":"aceh","types":None}],
        #     "sellCities":[{"name":"pasay","types":"BM"},{"name":"malacca","types":"BM"},{"name":"hanoi","types":None},{"name":"palembang","types":"BM"},{"name":"jakarta","types":"BM"},{"name":"surabaya","types":"BM"},{"name":"banjarmasin","types":"BM"}],
        # },
        {
            #,"clove" ,"benzoin"  ,"feathercrafts"  ,"nutmeg"
            "buyProducts": ["ebony","agarwood","ylang-ylang","musk","mace","mangosteen"],
            "buyCities":["banda","ambon","ternate","jolo","makassar","banjarmasin","jakarta","pasay","aceh"],
            "buySupplyCities":[],
            "buyStrategy":"twice",
            "dumpCrewCities": [],
            "supplyCities":["aceh","toamasina","town","pernambuco","cayenne","caracas","trujil"],
            "useSkillCity":"rida",
            "sellCities":[{"name":"rida","types":["perfume","dye"]},{"name":"veracruz","types":"BM"},{"name":"southside","types":None},{"name":"santiago","types":"BM"}],
        },
    ]
]

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
    "supplyCities":["ceuta","bathurst","elmina","luanda","town","sofala","zanzibar","mombasa","aden","socotra","muscat"],
    "sellCities":[{"name":"kochi","types":None}],
}