#给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
words={}
str=input()
str=str.lower()
for i in str:
    if not ("a" <= i and i <= "z"):
        str=str.replace(i," ")
strs=str.split(" ")
list1=list(strs)
for k in list1:
    if k in words:
        words[k] += 1     
    else:
        words[k] = 1
if "" in words:
    del words[""]
print(words)