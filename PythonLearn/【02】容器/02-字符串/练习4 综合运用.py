#text = "  我 爱 Python 编程  "
# 1. 去掉两端空格
# 2. 将中间多个空格替换为单个空格（提示：split + join）
# 3. 统计字符数（不含空格）

text = "  我  爱 Python  编程  "
text1=text.strip(" ")    #strip 删除前后的内容
print(f"去掉两端的空格：{text1}")

text2=text.split()
text3=" ".join(text2)
print(f"替换为单个空格后：{text3}")

n=len(text.replace(" ",""))
print(f"字符数（不含空格）:{n}")
