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

    #saint<->africa
    #light season
    [
        {
            "sellCity":"kokkola",
            # ,"tourmaline","amber","felt",
            "buyProducts": ["glassbead","steel","vodka","aquavit","gin","whisky"],
            #light season
            # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],
            # ,"hamburg","gda"
            "buyCities":["saint","stockhol","visby","riga","copenhag","groningen","amsterda","london","dover","plymouth","groningen","amsterda","london","dover","plymouth"],
            "buySupplyCities":[],

            #light seaso3n
            # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
            "supplyCities":["london","ceuta","bissau","tom","karibib","cape","mozambiqu","mogadish"]
        },
        {
            "sellCity":"massawa",
            # "pearl","agate""malachit","pearl","orangeoi"
            "buyProducts": ["lapislazu","frankincens","diamond","gold","goldwork","tuberose","geraniu","platinum","emerald","pistachio"],
            "buyCities":["aden","mogadish","malindi","manbasa","zanzibar","mozambiqu","queliman","sofala","natal","cape","karibi","benguel","luanda","tom","timbukt","tom","cape","karibi","benguel","luanda"],
            "buySupplyCities":[],
            "buyStrategy":"single",
            "supplyCities":["tom","bissau","ceuta","london","copenhag"]
        },
    ],
    #carrabean to north europe
    #need craft,alcohol,cloth,metal
    [
        #
        {
            "sellCity":"saint",
            # ,"tourmaline","glassbead"
            "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","glassbead","cheese"],
            # cities
            "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],
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
            "supplyCities":["juan","ponta","london"]
        },
    ]
]
