import random

class dog():
    dict1 = {"name": "小黑", "agr": 15, "blo": 80}
    dict2 = {"name": "笨笨", "agr": 15, "blo": 80}
    dict3 = {"name": "二哈", "agr": 15, "blo": 80}
    list1 = [dict1,dict2,dict3]
    def attack(self):
        for i in range(100):
            x1=random.randrange(0,3)
            if not self.list1[x1]["blo"]==0: 
                return self.list1[x1]["name"],self.list1[x1]["agr"]
    def behit(self,x):
        for i in range(100):
            x1=random.randrange(0,3)
            if not x==0 and not self.list1[x1]["agr"]==0:
                self.list1[x1]["agr"]-=3
                self.list1[x1]["blo"]-=x
                return x1,self.list1[x1]["name"]
            elif not self.list1[x1]["blo"]==0:
                if self.list1[x1]["blo"]>x:
                    self.list1[x1]["blo"]-=x
                else:
                    self.list1[x1]["blo"]=0
                return x1,self.list1[x1]["name"]
        
    def fail(self):
        for i in self.list1:
            if not i["blo"]==0:
                return 1
        else:
            return 0

