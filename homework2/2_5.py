#5  写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
def check(arg):
    dic = {}
    for key,value in arg.items():
        if len(value) > 2:
            dic[key] = value[0:2]
        else:
            dic[key] = value
    return  dic
arg = {"key1": "vasvzx", "ke2": ["q","w","e"],"key3":(11,12,13,14)}
print(check(arg))