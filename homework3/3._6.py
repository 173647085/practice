#在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
import string
f1=open(r"D:\practice\Blowing in the wind.txt","r")
f2=open(r"D:\practice\1.txt","r")
str1=f1.read()
str1=str1.lower()
str2=f2.read()
str2=str2.lower()
f1.close()
f2.close()
words1={}
words2={}
list1={}
list2={}
def check(s,w,l):
    for i in s:
        if not ("a" <= i and i <= "z"):
            s=s.replace(i," ")
    strs=s.split(" ")
    l=list(strs)
    for k in l:
        if k in w:
            w[k] += 1     
        else:
            w[k] = 1
    if "" in w:
        del w[""]
check(str1,words1,list1)
check(str2,words2,list2)
dict1= sorted(words1.items(), key=lambda d:d[1], reverse = True)
dict2= sorted(words2.items(), key=lambda d:d[1], reverse = True)
dict1=dict1[:10]
dict2=dict2[:10]
print(dict1)
print(dict2)
p=0
for i in dict1:
    if i in dict2:
        p+=1
        print(i)
print("相似度{}0%".format(p))
        