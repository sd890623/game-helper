# cityNames = ["pisa", "genoa", "calvi", "marseille", "barcelona", "valencia", "malaga", "seville", "ceuta", "cagliari","sassari"]
# NorthEuropeCitynames=["london","antwerp","calais","antwerp","helder","amsterda","groningen","bremen","hamburg"]
# cityNames=["amsterda","bremen","hamburg","groningen"]
cityNames=["london","dover","calais","amsterda","hamburg","groningen"]

#saint<->east land
#light season
routeList2=[
    {
        "sellCity":"saint",
        "buyProducts": ["amber","vodka","felt","tourmaline","aquavit","gin","glassbead","brandy","printed"],
        #light season
        # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],
        "buyCities":["saint","visby","gda","groningen","helder","amsterda"],
        "buySupplyCities":[],
        #light seaso3n
        # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
        "supplyCities":["helder","faro","syracuse"]
    },
    {
        "sellCity":"candia",
        "buyProducts": ["civet","perfume","narcissus","oakmoss","marblestat"],
        "buyCities":["candia","alexandr","cairo","said","jaffa","beirut"],
        "buySupplyCities":[],
        "supplyCities":["syracuse","ceuta","helder"]
    },
]
#carrabean to north,winter
#need craft,alcohol,cloth,metal
routeList=[
    {
        "sellCity":"saint",
        #add felt later
        "buyProducts": ["amber","vodka","felt","tourmaline","aquavit","gin","glassbead","whisky","flannel","jewelry"],
        #light season
        # "buyProducts": ["amber", "vodka","felt","chrysoberyl","aquavit","feather","tourmaline","flax"],

        #gdahsk might suffer
        "buyCities":["saint","visby","gda","hamburg","groningen","amsterda","london"],
        "buySupplyCities":[],
        #light seaso3n
        # "buyCities":["kokkola","saint","stockholm","visby","gda","copenhagen","beck","oslo"],
        "supplyCities":["london","faro","ponta"]
    },
    # {
    #     "sellCity":"timbukt","
    #     "buyProducts": ["diamond","gold","goldwork","golddust","agate","malachite","pearl"],
    #     "buyCities":["timbukt","benin","tom","elmina"],
    #     "buySupplyCities":["benin"],
    #     "sulyCities":["abidjan","arguin","seville","antwerp","copenhagen"]
    # },
    {
        "sellCity":"juan",
        "buyProducts": ["opal","topaz","obsidianclu","gold","golddust","emerald","silver"],
        "buyCities":["juan","willemsta","maracaib","cartagen","santiago","santo"],
        "buySupplyCities":[],
        "supplyCities":["juan","ponta","helder"]
    },
]