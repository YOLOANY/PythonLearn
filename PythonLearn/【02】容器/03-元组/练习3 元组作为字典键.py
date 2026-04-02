# 创建一个空字典 cache
# 将元组 ("user", 1) 作为键，值设为 "张三"
# 将元组 ("user", 2) 作为键，值设为 "李四"
# 打印 cache
# 通过键 ("user", 1) 获取对应的值
cache={}                            #创建空字典
cache[("user",1)]="张三"             #类比数组：arr[1]=...
cache[("user",2)]="李四"
print(cache)

value=cache[("user",1)]
print(value)


