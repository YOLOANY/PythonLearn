#s = "hello@example.com"
# 1. 判断是否以 "hello" 开头
# 2. 判断是否以 ".com" 结尾
# 3. 找到 "@" 的位置
# 4. 提取 "@" 后面的部分

s = "hello@example.com"
n1=s.startswith("hello")
n2=s.endswith(".com")
print(f"是否以'hello'开头：{n1}")
print(f"是否以'.com'结尾：{n1}")
position=s.find("@")
s1=s[position+1:]     #只是position的话会把@带上
print(f"@的位置是：{position}")
print(f"@后面的部分是：{s1}")