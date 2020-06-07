list1=[(101,"sda",73),
       (102,"rwq",84),
       (103,"xdsz",37),
       (104,"ls",69),
       (105,"xcw",20),
       (106,"sd",93),
       (107,"rq",77),
       (108,"ohg",46),
       (109,"sgc",52),
       (110,"vxz",81)]
print("学号 ","姓名 ","成绩")
list1.sort(key=lambda nos:nos[2])
for i in list1:
    print(i)