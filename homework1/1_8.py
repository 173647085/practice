#设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  将这10个员工，按照工资从高到低打印输出；
list1=[(101,"sda",5,5500),
       (102,"rwq",11,10000),
       (103,"xdsz",3,4500),
       (104,"ls",8,7500),
       (105,"xcw",1,3000),
       (106,"sd",15,12000),
       (107,"rq",21,14000),
       (108,"ohg",4,5000),
       (109,"sgc",7,6000),
       (110,"vxz",9,8000)]
print("工号 ","姓名 ","工龄","工资")
list1.sort(key=lambda nos:nos[3])
list1.reverse()
for i in list1:
    print(i)