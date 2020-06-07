# 定义列表，并使用内置函数求最大、最小元素、长度等信息
# 使用循环计算列表元素和
score = [80, 79, 93, 54, 74, 67, 98, 82, 47, 78]
sum = 0
for i in range(len(score)):
    sum += score[i]

print('最高分:', max(score))
print('最低分:', min(score))
print('总分:', sum)
print('平均分:', sum / len(score))