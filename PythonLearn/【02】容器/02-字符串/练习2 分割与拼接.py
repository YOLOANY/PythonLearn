#s = "apple,banana,orange"
# 1. 用逗号分割成列表
# 2. 用 "-" 将列表拼接成字符串
s = "apple,banana,orange"

s1=s.split(",")     #split 分割
print(f"分割后:{s1}")

s2="_".join(s1)     #join  拼接     “以什么符号”.join（拼接什么列表）
print(f"拼接后:{s2}")