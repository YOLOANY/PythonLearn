# for循环：遍历输入的字符串
msg = input("请输入需要遍历的字符串：")

for s in msg:  # s 表示遍历出来的元素； msg 表示需要遍历的数据
    print(f"元素：{s}")
else:
    print("遍历结束！")


# 案例1：计算 1-100 之间所有的奇数之和
total = 0  # 记录累加之和

# 原始写法
# for i in range(1, 101):
#     if i % 2 == 1: # 奇数
#         total += i

# 简化写法
for i in range(1, 101, 2):
    total += i

print("1-100之间的奇数累加之和：", total)


# 案例2：计算 100-500 之间所有3的倍数的数字之和
total = 0  # 记录累加之和

for i in range(100, 501):
    if i % 3 == 0: # i 是3的倍数
        total += i

print("100-500 之间所有3的倍数的数字之和：", total)

