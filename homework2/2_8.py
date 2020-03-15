#8  请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
import string
str1="hrtftdghed"
str2=string.ascii_letters#生成所有字母
def count():
    dict1={}
    for letter in str2:
        dict1[letter]=0
    print(dict1)
    for i in str1:
        dict1[i]+=1
    for count in str2:
        if dict1[count]!=0:
            print("%s:%d"%(count,dict1[count]))

count()