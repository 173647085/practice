j=0
def createCounter():
    global j
    j=0
    def f():
        global j
        j+=1
        return j
    return f
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

def count():
    fs = []
    for i in range(1, 4):
        fs.append(i) 
    return fs

a=count()
print(a)