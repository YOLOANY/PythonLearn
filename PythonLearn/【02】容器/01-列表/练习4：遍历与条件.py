#scores = [85, 92, 78, 60, 45]
# 1. 打印所有分数
# 2. 打印所有及格（>=60）的分数
# 3. 计算平均分
scores = [85, 92, 78, 60, 45]

#打印所有分数-1
for i in range(len(scores)):
    print(scores[i],end=" ")
print()
#打印所有分数-2
print(scores)

#打印所有及格（>=60）的分数
for i in range(len(scores)):
    if scores[i]>=60:
        print(scores[i],end=" ")
print()

#计算平均分
sum=0
for i in range(len(scores)):
    sum+=scores[i]
average = sum/len(scores)
print(average)
