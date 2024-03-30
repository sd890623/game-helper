import json
import os

if __name__ == '__main__':
    a=["aden","cape", "ushuaia", "lima"]
    print(a[::-1])
    filePath = os.path.abspath(__file__ + "\\..\\villageTrade.json")

    with open(filePath, 'r') as f:
        villageTrade = json.load(f)
    print(villageTrade.get("samir"))
    villageTrade["samir"]= True
    villageTrade["samir2"]= False

    with open(filePath, 'w') as json_file:
        json.dump(villageTrade, json_file)