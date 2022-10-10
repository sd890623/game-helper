with open('src/UW/reachCity.txt', 'r') as f:
    read=f.readline()
    if(read):
        print("found city")
        print(read)
        with open('src/UW/reachCity.txt', 'w') as f:
            f.write('')