import json
import os
from utils import isStringSameOrSimilar

if __name__ == "__main__":
    a = ["亚丁", "开普敦", "乌斯怀亚", "利马"]
    print(isStringSameOrSimilar("马赛A", "马赛B"))
    print(a[::-1])
    filePath = os.path.abspath(__file__ + "\\..\\dailyConfFile.json")

    with open(filePath, "r") as f:
        villageTrade = json.load(f)
    print(villageTrade.get("samir"))
    villageTrade["samir"] = True
    villageTrade["samir2"] = False

    with open(filePath, "w") as json_file:
        json.dump(villageTrade, json_file)
