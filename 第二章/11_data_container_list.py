# 列表操作
# 定义列表 - list
s = [56, 90, 88, 65, 90, "A", "Hello", True]

print(type(s))

# 访问列表元素
# 获取
print(s[0])  # 正向索引，从0开始
print(s[-8]) # 反向索引，从-1开始

print(s[2])
print(s[-6])

# 修改
s[5] = "ABC"
print(s)

# 注意: 如果指定的索引，超出范围，将会报错
# s[10] = "DEF"
# print(s)

# 删除
del s[6]
print(s)

# 遍历
for i in s:
    print(i)



# --------------------------- 列表 list 切片 ---------------------------
# 定义列表
s = ["A", "C", "H", "K", "L", "B", "D", "X", "C", "U"]

# 切片操作 s[开始索引:结束索引:步长]
print(s[0:5:1])
print(type(s[0:5:1]))

print(s[0:5:1])
print(type(s[0:5:1]))

print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[0:5:2])
print(s[0:-2:1])



# --------------------------- 列表 list 常用方法 ---------------------------
# 列表定义
s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
print(s)

# append(): 在列表尾部追加元素
s.append(188)
print(s)

# insert(): 在指定索引之前，插入元素
s.insert(__index=2, __object=80)
print(s)

# remove(): 移除列表中第一个匹配到的元素
s.remove(90)
print(s)

# pop(): 删除列表中指定索引位置的元素并返回(如果未指定，默认删除最后一个)
e = s.pop(1)
print(e)

e = s.pop()
print(e)

print(s)

# sort(): 排序
s.sort()
print(s)

# reverse(): 反转列表元素
s.reverse()
print(s)
