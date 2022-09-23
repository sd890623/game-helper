# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
cityNames=[]

#Liquer+
# "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","cheese"],
# "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],

routeLists=[
    #saint<->eastland
    [
        {
            "sellCity":"saint",
            # "vodka","aquavit","gin","whisky"
            "buyProducts": ["cowhide","amber","felt","tourmaline","glassbead","steel","jewelry","vodka","aquavit","gin","whisky"],
            #light season
            # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],
            "buyCities":["saint","visby","gda","copenhag","hamburg","groningen","amsterda","london"],
            "buySupplyCities":[],
            #light seaso3n
            # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
            "supplyCities":["london","ceuta","syracuse"]
        },
        {
            "sellCity":"athens",
            #marblestatu
            "buyProducts": ["narcissu","civet","perfume","oakmos"],
            "buyCities":["alexandr","cairo","said","jaffa","beirut","athens","candia"],
            "buySupplyCities":[],
            "supplyCities":["syracuse","ceuta","london","copenhag"]
        },
    ],

    #saint<->east africa
    #light season
    [
        {
            "sellCity":"saint",
            # ,"tourmaline",,"amber", "jewllery"
            "buyProducts": ["glassbead","steel","vodka","aquavit","gin","whisky","felt"],
            #light season
            # ,,"gda"
            "buyCities":["saint","stockhol","visby","riga","copenhag","groningen","amsterda","london","dover","plymouth","copenhag","groningen","amsterda","london","dover","plymouth"],
            "buySupplyCities":["copenhag"],

            #light seaso3n
            # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
            "supplyCities":["london","ceuta","bissau","tom","karibib","cape","mozambiqu","mogadish"]
        },
        {
            "sellCity":"massawa",
            # "pearl","agate""malachit","pearl","orangeoi","goldwork"
            "buyProducts": ["lapislazu","frankincens","diamond","gold","tuberose","geraniu","platinum","emerald","pistachio"],
            #,"malindi","manbasa"
            "buyCities":["aden","mogadish","zanzibar","mozambiqu","queliman","sofala","natal","mogadish","zanzibar","mozambiqu","queliman","sofala","natal","cape","karibi","benguel","luanda","tom","timbukt","tom","cape","karibi","benguel","luanda"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "dumpCrewCities": [],
            "supplyCities":["cape","tom","bissau","ceuta","london","copenhag"]
        },
    ],
    #carrabean to north europe
    #need craft,alcohol,cloth,metal
    [
        #
        {
            "sellCity":"saint",
            # ,"tourmaline",
            "buyProducts": ["glassbead","steel","vodka","aquavit","gin","whisky","amber","felt"],
            #light season
            # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],
            # ,
            "buyCities":["saint","stockhol","visby","riga","gda","copenhag","hamburg","groningen","amsterda","london","dover","plymouth","copenhag","hamburg","groningen","amsterda","london","dover","plymouth"],
            "buySupplyCities":["copenhag"],
            # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
            "supplyCities":["london","ceuta","ponta","juan"]
        },
        {
            "sellCity":"veracruz",
            # obsidianclu golddust
            "buyProducts": ["opal","topaz","gold","emerald","silver","vanilla"],
            # "santiago"
            "buyCities":["santiago","juan","porlamar","caracas","willemsta","maracaib","cartagen","portobelo"],
            "buySupplyCities":[],
            "supplyCities":["juan","ponta","london","copenhag"]
        },
    ],
    #saint<->west africa
    [
        {
            "sellCity":"saint",
            # ,"tourmaline",
            "buyProducts": ["glassbead","steel","vodka","aquavit","gin","whisky","amber","felt"],
            #light season
            # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],
            # ,
            "buyCities":["saint","stockhol","visby","riga","gda","copenhag","hamburg","groningen","amsterda","london","dover","plymouth","copenhag","hamburg","groningen","amsterda","london","dover","plymouth"],
            "buySupplyCities":[],

            #light seaso3n
            # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
            "supplyCities":["london","ceuta","bissau","tom"]
        },
        {
            "sellCity":"cape",
            # "pearl","agate""malachit","pearl","goldwork"
            "buyProducts": ["golddust","orangeoi","ambergris","goldwork","lapislazu","frankincens","diamond","gold","tuberose","geraniu","platinum","emerald","pistachio"],
            "buyCities":["cape","karibib","benguel","luanda","tom","timbukt"],
            "buySupplyCities":["tom"],
            "buyStrategy":"single",
            "supplyCities":["tom","bissau","ceuta","london","copenhag"]
        },
    ]
]
