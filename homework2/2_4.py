#4 函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
s=input("请输入字符串:")
count={"字母":0,"数字":0,"空格":0,"其他":0}
def lei(l):
    for i in l :
        if i.isalpha():        
            count["字母"]+=1
        elif i.isdigit():
            count["数字"]+=1
        elif i.isspace():
            count["空格"]+=1
        else:
            count["其他"]+=1
    return count
print(lei(s))