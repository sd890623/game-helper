import time
import json

print("Resetting daily BM data")
with open('src/UW/blackMarket.json', 'w') as json_file:
    json.dump([], json_file)
time.sleep(2)