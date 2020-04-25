import random

class people():
    dict1 = {"name": "张三", "agr": 10, "blo": 100}
    dict2 = {"name": "李四", "agr": 10, "blo": 100}
    list1 = [dict1,dict2]
    def attack(self):
        for i in range(100):
            x1=random.randrange(0,2)
            if not self.list1[x1]["blo"]==0: 
                return self.list1[x1]["name"],self.list1[x1]["agr"]
    def behit(self,x):
        for i in range(100):
            x1=random.randrange(0,2)
            if not x==0 and not self.list1[x1]["agr"]==0:
                self.list1[x1]["agr"]-=2
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

