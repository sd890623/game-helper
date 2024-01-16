import sys
import os

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

from datetime import datetime, timedelta
from guiUtils import win
import os
import time
from utils import *
from datetime import date
from UWTask import UWTask

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))
sys.path.append(os.path.abspath(__file__ + "\\..\\"))

class Fashion:
    cityMapList=[
        {'name': '阿拉伯西印度群岛',"cities":["suez","jeddah","massawa","aden","hadiboh","dhofar","muscat","hormuz","bidda","shiraz","basrah","baghdad"]},
        {'name': '东地中海',"cities":["alexandria","cairo","said","jaffa","beirut","lefkosa","antalya","candia","trabzon","benghazi"]},
        {'name': '东非',"cities":["quelimane","mozambique","toamasina","kilwa","zanzibar","manbasa","malindi","mogadishu"]}
    ]
    mapList = [
        {'name': '北海', 'zone': 0, 'show': True, 'flag': 0},
        {'name': '东地中海', 'zone': -1, 'show': True, 'flag': 0, "zoneMinutes":1},
        {'name': '大西洋&西地中海', 'zone': -2, 'show': True, 'flag': 0},
        {'name': '西非', 'zone': -3, 'show': True, 'flag': 0},
        {'name': '南非', 'zone': -4, 'show': True, 'flag': 0},
        {'name': '东非', 'zone': -5, 'show': True, 'flag': 0, "zoneMinutes":1},
        {'name': '阿拉伯西印度群岛', 'zone': -6, 'show': True, 'flag': 0,"zoneMinutes":3},
        {'name': '东印度群岛&印度支那', 'zone': -7, 'show': True, 'flag': 0},
        {'name': '南亚', 'zone': -8, 'show': True, 'flag': 0},
        {'name': '东亚', 'zone': -9, 'show': True, 'flag': 0},
        {'name': '远东亚洲', 'zone': -10, 'show': True, 'flag': 0},
        {'name': '南太平洋', 'zone': -11, 'show': True, 'flag': 0},
        {'name': '南美洲、西美', 'zone': 0, 'show': True, 'flag': 1},
        {'name': '北美、东美、加勒比', 'zone': -1, 'show': True, 'flag': 1}
    ]
    fashionInfoDict = [
        {'name': '奢华', 'detail': ['工艺品', '辛香料', '香料'], 'interval': 19, 'sn': [8, 3], 'show': True},
        {'name': '繁荣', 'detail': ['贵金属', '艺术作品', '宝石'], 'interval': 17, 'sn': [4, 1], 'show': True},
        {'name': '开发', 'detail': ['工业制品', '矿石', '酒类或家畜'], 'interval': 13, 'sn': [2, 3], 'show': True},
        {'name': '赞助', 'detail': ['嗜好品', '工艺品', '艺术作品'], 'interval': 11, 'sn': [2, 5], 'show': True},
        {'name': '战争', 'detail': ['家畜', '武器', '枪支'], 'interval': 7, 'sn': [2, 2], 'show': True},
        {'name': '洪水', 'detail': ['食品', '工业制品', '织物'], 'interval': 5, 'sn': [1, 0], 'show': True},
        {'name': '传染病', 'detail': ['杂货', '药品', '纤维'], 'interval': 3, 'sn': [0, 2], 'show': True},
        {'name': '节庆', 'detail': ['食品', '调味品', '染料'], 'interval': 2, 'sn': [1, 1], 'show': True}
    ]

    def __init__(self, instance: win, uwtask:UWTask) -> None:
        self.instance=instance
        self.uwtask=uwtask
        self.today=date.today().strftime("%d-%m-%Y")

    def isDst(self):
        return bool(time.localtime().tm_isdst)

    def get_hour(self):
        # 设置目标时间（注意Python中时区的处理方式）
        target = datetime(2023, 1, 24, 0, 0, 0) + timedelta(hours=1)+ (timedelta(hours=1) if self.isDst() else timedelta(hours=0))  # 假设目标时间为GMT+9
        # 获取当前时间
        today = datetime.now()
        # 计算时间差，并转换为小时
        hours_difference = (today - target).total_seconds() / 3600
        return int(hours_difference)
    
    def getFashionByHour(self,hour,flags,t='name'):
        r=[]
        for element in self.fashionInfoDict:
            if (len(r)>=2):
                break
            if (hour % element['interval'] == element['sn'][flags]):
                r.append(element[t])
        return r
    
    def getFashionsByMap(self,name, hours):
        map = next((map_item for map_item in self.mapList if map_item['name'] == name), None)
        if not map:
            print(f"Map not found: {name}")
            return []
        iHour=self.get_hour()
        fashions=[]

        for i in range(hours):
            hour = iHour + i + map['zone']
            fashion = self.getFashionByHour(hour, map['flag'])
            fashions.append({"hour": i, "fashions": fashion})
        return fashions

    def getMapNameByCity(self,cityName):
        for map in self.cityMapList:
            if(cityName in map['cities']):
                return map['name']
        return None
    
    def getFashionsByCity(self,cityName,hours):
        mapName=self.getMapNameByCity(cityName)
        if(mapName==None):
            return []
        return self.getFashionsByMap(mapName,hours)    
    
    def getExtraMinutesByCity(self,cityName):
        mapName=self.getMapNameByCity(cityName)
        if(mapName==None):
            return 0
        map = next((map_item for map_item in self.mapList if map_item['name'] == mapName), None)
        if not map:
            return 0
        return map['zoneMinutes']

if __name__ == '__main__':
    print(getCentralTime())
    fashion=Fashion(None,None)
    print(fashion.getFashionsByCity("suez",5))