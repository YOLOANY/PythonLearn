#fruits = ["苹果", "香蕉", "橙子"]
# 1. 在末尾添加 "葡萄"
# 2. 在第二个位置插入 "芒果"
# 3. 删除 "香蕉"
# 4. 打印最终列表

fruits=["苹果", "香蕉", "橙子"]
fruits.append("葡萄")   #在末尾添加
fruits.insert(1,"芒果")   #在某个位置的的前面添加什么
#del fruits[2]           #删除下标为2的元素（香蕉)
fruits.remove("香蕉")    #删除 "香蕉"

print(fruits)