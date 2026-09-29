# 常见数据类型 ---> type() 获取指定的字面量或变量的类型
print("Hello")
print(type("Hello"))  # str

print(type(10))      # int
print(type(3.14))    # float
print(type(True))    # bool
print(type(False))   # bool
print(type(None))    # NoneType

num = -100
print(type(num)) #int


# 常见数据类型 ---> isinstance(数据, 类型) ---> bool值 ---> 判定数据是否是指定的类型，如果是: True, 否则: False
print(isinstance(num, int))    #True
print(isinstance(num, float))  #False
print(isinstance(num, bool))   #False


# 字符串
# 定义字符串的三种方式
s1 = "Hello"  # 双引号定义
s2 = 'Python'  # 单引号定义
s3 = """
Hello:
欢迎大家进入到Python课程的学习！
大家记得一键三连哦 ~
"""  # 三引号定义（多行字符串）

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))


# 定义字符串 ---> It's very good
# 转义字符 \'  \"  \n  \t
msg = 'It\'s very good'
print(msg)

msg2 = "It's very good"
print(msg2)

msg3 = "Hello 的意思就是 \"您好\""
print(msg3)

msg4 = 'Hello 的意思就是 \"您好\"'
print(msg4)

print("\t欢迎大家进入到Python课程的学习！\n\t大家记得一键三连哦 ~") # \n换行 \t制表符缩进
