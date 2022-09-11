# Short trips
# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
cityNames=[]

routeLists=[
    #saint<->eastland
    [
        {
            "sellCity":"kokkola",
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
            "buyProducts": ["cowhide","amber","felt","tourmaline","glassbead","steel","jewelry","vodka","aquavit","gin","whisky"],
            #light season
            # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],
            "buyCities":["saint","visby","gda","copenhag","hamburg","groningen","amsterda","london"],
            "buySupplyCities":[],
            #light seaso3n
            # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
            "supplyCities":["london","faro","bissau"]
        },
        {
            "sellCity":"tom",
            "buyProducts": ["diamond","gold","goldwork","golddust","agate","pearl","malachit","geraniu"],
            "buyCities":["timbukt","tom","luanda","benguel","karibi"],
            "buySupplyCities":["tom"],
            "supplyCities":["tom","bissau","faro","london"]
        },
    ],
    #carrabean to north europe
    #need craft,alcohol,cloth,metal
    [
        #
        {
            "sellCity":"saint",
            #add felt later
            "buyProducts": ["cowhide","amber","felt","tourmaline","glassbead","steel","jewelry","vodka","aquavit","gin","whisky"],
            #light season
            # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],

            #gdahsk might suffer
            "buyCities":["saint","visby","gda","copenhag","hamburg","groningen","amsterda","london"],
            "buySupplyCities":[],
            #light seaso3n
            # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
            "supplyCities":["london","faro","ponta","juan"]
        },
        # gold down, jewllery up
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
