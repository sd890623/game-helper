# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
cityNames=["london","dover","calais","amsterda","hamburg","groningen"]

#saint<->east land
routeList=[
    {
        "sellCity":"saint",
        "buyProducts": ["amber","vodka","felt","chrysoberyl","tourmaline","aquavit"],
        #light season
        # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],
        "buyCities":["saint","visby","gda","beck","copenhagen"],
        "buySupplyCities":[],
        #light seaso3n
        # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
        "supplyCities":["helder","ceuta","syracuse"]
    },
    {
        "sellCity":"candia",
        "buyProducts": ["civet","perfume","narcissus","oakmoss","marblestat"],
        "buyCities":["candia","alexandr","cairo","said","jaffa","beirut"],
        "buySupplyCities":[],
        "supplyCities":["syracuse","ceuta","helder"]
    },
]

routeList2=[
    {
        "sellCity":"saint",
        #add felt later
        "buyProducts": ["amber","vodka","felt","chrysoberyl","tourmaline","aquavit"],
        #light season
        # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],

        #gdahsk might suffer
        "buyCities":["saint","visby","gda","beck","copenhagen"],
        "buySupplyCities":[],
        #light seaso3n
        # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
        "supplyCities":["helder","ceuta","syracuse"]
    },
    # {
    #     "sellCity":"timbukt","
    #     "buyProducts": ["diamond","gold","goldwork","golddust","agate","malachite","pearl"],
    #     "buyCities":["timbukt","benin","tom","elmina"],
    #     "buySupplyCities":["benin"],
    #     "supplyCities":["abidjan","arguin","seville","antwerp","copenhagen"]
    # },
    {
        "sellCity":"candia",
        "buyProducts": ["civet","perfume","narcissus","oakmoss","marblestat"],
        "buyCities":["candia","alexandr","cairo","said","jaffa","beirut"],
        "buySupplyCities":[],
        "supplyCities":["syracuse","ceuta","helder"]
    },
]