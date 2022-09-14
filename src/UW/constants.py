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
            "sellCity":"saint",
            # ,"tourmaline"
            "buyProducts": ["amber","felt","glassbead","steel","jewelry","vodka","aquavit","gin","whisky","cheese"],
            #light season
            # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],
            "buyCities":["saint","stockhol","visby","gda","copenhag","hamburg","groningen","amsterda","london","dover","plymouth"],
            "buySupplyCities":[],

            #light seaso3n
            # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
            "supplyCities":["london","faro","bissau","tom","karibi"]
        },
        {
            "sellCity":"cape",
            # "pearl","agate"
            "buyProducts": ["diamond","gold","goldwork","golddust","malachit","geraniu","orangeoi","ambergris","pearl"],
            "buyCities":["cape","karibi","benguel","luanda","tom","timbukt"],
            "buySupplyCities":["tom","karibi"],
            "buyStrategy":"single",
            "supplyCities":["tom","bissau","faro","london","copenhag"]
        },
    ],
    #carrabean to north europe
    #need craft,alcohol,cloth,metal
    [
        #
        {
            "sellCity":"saint",
            # ,"tourmaline","glassbead"
            "buyProducts": ["amber","felt","steel","vodka","aquavit","gin","whisky","cheese"],
            # cities
            "buyCities":["saint","stockhol","visby","copenhag","groningen","amsterda","london","dover","plymouth"],
            "buySupplyCities":["copenhag"],
            # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
            "supplyCities":["london","faro","ponta","juan"]
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
