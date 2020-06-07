class Dog:
    count=0
    def __init__(self,color,name):
        self.color=color
        self.name=name
        self.__class__.count+=1
    def wolf(self):
        if(self.name=="秋田"):
            print("汪汪汪汪")
        elif (self.name=="哈士奇"):
            print("wowowowwowowowowo")
    @staticmethod
    def count1():
        print("一共有{}条狗".format(Dog.count))

a=Dog("黄色","哈士奇")
b=Dog("白色","秋田")
a.wolf()
Dog.count1()
            
