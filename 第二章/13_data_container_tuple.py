# 元组基本操作 - tuple ---> 元素可以重复，有序，不可修改
# 定义
t1 = (80, 95, 78, 50, 76, 80, 85, 20)

print(t1)
print(type(t1))

# 索引访问
print(t1[0])
print(t1[-1])

# 切片
print(t1[0:5:1])

#方法
#count() 统计元素出现的次数
print(t1.count(80))

#index() 查找元素的索引位置(第一个元素的位置)
print(t1.index(80))

# 注意点：如果定义单元素的元组，单个元素之后需要加上逗号，比如 (100,)
t2 = ()
print(t2)
print(type(t2))

t3 = (100,)  # 定义单元素元组
print(t3)
print(type(t3))



# ----------------------------- 元组 tuple 组包与解包 -----------------------------
# 组包操作
t1 = (5, 7, 9, 10, 2, 23, 12)
t2 = 5, 7, 9, 10, 2, 23, 12

print(t1)
print(t2)

# 解包操作
# 基础解包(变量数量与容器的元素个数一致)
a,b,c,d,e,f,g = t1
print(a,b,c,d,e,f,g)

# * 扩展解包 (* 收集剩余的所有元素，封装列表list中)
first,second,*other,last = t1
print(first,second)
print(other)
print(last)

*other,last2,last1 = t1
print(other)
print(last2)
print(last1)


# 案例1：现有两个变量，分别为: a = 10, b = 20，现需要将这两个变量值交换，然后输出到控制台。
a = 10
b = 20

# 组包
# t = b,a
# # 解包
# a,b = t

# 合并
a,b = b,a

print(a) # 20
print(b) # 10


# 案例2：现有三个变量，分别为: a = 100, b = 200, c = 300，现需要将这三个变量值进行交换，将a,b,c的值分别赋值给c,a,b，并将其输出到控制台。
a = 100
b = 200
c = 300

c,a,b = a,b,c

print(a)
print(b)
print(c)

