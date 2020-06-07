import time

def outer(func):
    def inner(*s):
        t1=time.time()
        func(*s)
        t2=time.time()
        print("%.f"%(t2-t1))
    return inner
@outer
def add(a,b):
    print (a+b)

add(1,2)