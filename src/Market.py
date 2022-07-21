from guiUtils import win
from utils import *
import os

coinPath = os.path.abspath(__file__ + "\\..\\..\\assets\\UWClickons\\"+"coinInBuy"+".bmp")

class Market:
    def __init__(self, instance: win, uwtask) -> None:
        self.instance=instance
        self.uwtask=uwtask
    
    def buyV1(self):
        count=11
        wait(lambda: self.instance.click_point(54,88),1)
        doAndWaitUntilBy(lambda: self.instance.click_point(54,88), lambda: self.uwtask.hasSingleLineWordsInArea("purch", A=[54,17,142,55]), 1)        
        while(count>0):
            if(self.uwtask.hasSingleLineWordsInArea("max", A=[1212,126,1265,139])):
                break
            position=self.instance.window_capture_v2(coinPath, A=[172,99,1192,370])
            count-=1
            if(position):
                print("buy item x")
                wait(lambda: self.instance.click_point(position[0], position[1]),0.2)  
                wait(lambda: self.instance.click_point(1398,808),1)
                wait(lambda: self.instance.click_point(809,658))
                self.uwtask.bargin()
                doMoreTimesWithWait(lambda: self.instance.click_point(809,658),3,1) 

    def sellV1(self):
        count=11
        wait(lambda: self.instance.click_point(40,146),1)
        doAndWaitUntilBy(lambda: self.instance.click_point(40,146), lambda: self.uwtask.hasSingleLineWordsInArea("sel", A=[54,17,142,55]), 1)
        while(count>0):
            position=self.instance.window_capture_v2(coinPath, A=[172,99,1192,370])
            if(self.uwtask.hasSingleLineWordsInArea("noitemtosell", A=[623,444,737,469])):
                break
            else:
                print("sell item x")
                count-=1
                wait(lambda: self.instance.click_point(position[0], position[1]),0.2)
                if(self.uwtask.hasSingleLineWordsInArea("-", A=[1401,761,1469,782])):
                    self.uwtask.clickWithImage("crossInSell", A=[1203,94,1274,131])
                    continue  
                wait(lambda: self.instance.click_point(1398,808),1)
                wait(lambda: self.instance.click_point(809,658))
                self.uwtask.bargin()
                doMoreTimesWithWait(lambda: self.instance.click_point(809,658),3,1)         

    #move by slot and choose wisely to buy
    def buyV2(self):
        self.uwtask.print("")