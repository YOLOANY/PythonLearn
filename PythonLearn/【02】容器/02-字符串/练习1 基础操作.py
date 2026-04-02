#s = "  Hello, Python World!  "
# 1. 去掉两端空格
# 2. 全部转小写
# 3. 全部转大写
# 4. 将 "Python" 替换为 "AI"
s = "  Hello, Python World!  "
s.strip()     #移除开头和结尾的指定字符（未输入则为移除空格）
print(s)

s1=s.upper()
print(f"转换为大写:{s1}")

s2=s.lower()
print(f"转换为小写:{s2}")

s3=s.replace("Python","AI")    #replace  替换
print(f"替换后:{s3}")
