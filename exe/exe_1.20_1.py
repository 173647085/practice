def jisuan(x,y,a,j,r,e):
    print(a(x,y))
    print(j(x,y))
    print(r(x,y))
    print(e(x,y))

def add(x,y):
    return "{}+{}={}".format(x,y,x+y)

def jian(x,y):
    return "{}-{}={}".format(x,y,x-y)

def cheng(x,y):
    return "{}*{}={}".format(x,y,x*y)

def chu(x,y):
    return "{}/{}={}".format(x,y,x/y)

jisuan(6,2,add,jian,cheng,chu)