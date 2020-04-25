# -*- encoding: utf-8 -*-
"""
@File : 6_3.py
@Time : 2020/04/17 15:03:07
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
"""

# here put the import lib
"""
三、定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
"""
class dictclass():
    def __init__(self,dict1):
        self.dict=dict1
    
    def del_dict(self,key):
        if key in self.dict.keys():
            del self.dict[key]
        else:
            return "not found"

    def get_dict(self,key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return "not found"

    def get_key(self):
        return list(self.dict.keys())

    def update_dict(self,dict1):
        for key in dict1.keys():
            self.dict[key]=dict1[key]
        return list(self.dict.values())

    def printdict(self):
        print("操作后的字典：",self.dict)


mydict={"品种":"哈士奇","color":"黑色","num":9}
dict1=dictclass(mydict)
dict1.del_dict("颜色")
dict1.del_dict("color")
dict1.printdict()
print(dict1.get_dict("价格"))
print(dict1.get_dict("品种"))
print("返回键值列表：",dict1.get_key())
updict={"price":200}
print(dict1.update_dict(updict))
dict1.printdict()