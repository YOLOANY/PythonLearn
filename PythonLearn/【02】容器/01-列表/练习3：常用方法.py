#numbers = [3, 1, 4, 1, 5, 9, 2]
# 1. 统计 1 出现了几次
# 2. 找出 5 的索引位置
# 3. 对列表排序（升序）
# 4. 反转列表
# 5. 清空列表
numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"1的出现次数:{numbers.count(5)}")    #count   统计出现次数

print(f"5的索引位置:{numbers.index(5)}")    #index   找到位置

numbers.sort()                            #sort    排序(原地操作———先排序再输出)
print(f"排序后:{numbers}")

numbers.reverse()                         #reverse 反转(原地操作———先排序再输出)
print(f"反转后:{numbers}")

print(f"清空后:{numbers.clear()}")                    #clear     清空


