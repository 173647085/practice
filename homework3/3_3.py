#编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
f=open(r"D:\text\3_3.1.txt","rt",encoding='UTF-8')
str_1="\n"
str1=sorted(f.read().splitlines(),key=lambda s: s.split()[2],reverse=1)
print(str_1.join(str1))
f.close()