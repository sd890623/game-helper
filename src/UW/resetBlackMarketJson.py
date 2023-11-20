import time
import os
import json

print("Resetting daily data")
filePath1 = os.path.abspath(__file__ + "\\..\\blackMarket.json")
filePath2 = os.path.abspath(__file__ + "\\..\\villageTrade.json")

with open(filePath1, 'w') as json_file:
    json.dump([], json_file)
with open(filePath2, 'w') as json_file:
    json.dump({}, json_file)
time.sleep(2)