f=open(r"D:\text\a.txt","rt",encoding='UTF-8')
f1=open(r"D:\text\b.txt","w+",encoding='UTF-8')
str_1="\n"
str1=sorted(f.read().splitlines(),key=lambda s: s.split()[2],reverse=1)
f1.write(str_1.join(str1))
print(str1)
f.close()
f1.close()
# f=open(r"D:\text\a.txt","r",encoding='UTF-8')
# f1=open(r"D:\text\b.txt","w",encoding='UTF-8')
# for i in range(0,4):
#     w[i]=w[i].split( )
# w1=w[1:4]
# del w[1:4]
# w1=sorted(w1,key=lambda s:s[2], reverse=True)
# for i in w1:
#     w.append(i)
# strs=""
# str1=""
# for i in w:
#     for j in i:
#         str1+=j
#         str1+="\t"
#     strs+=str1
#     strs+="\n"
#     str1=""
# f1.write(strs)
# f.close()
# f1.close()