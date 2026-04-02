# 创建一个字典 student，包含键值对：
#   "name": "张三"
#   "age": 20
#   "major": "计算机"
# 1. 打印姓名
# 2. 修改年龄为 21
# 3. 添加键值对 "grade": 85
# 4. 删除 "major"
# 5. 打印最终的字典
student={"name":"张三","age":20,"major":"计算机"}
print(f"姓名是:{student["name"]}")
student["name"]=21
print(f"修改后的年龄是:{student["age"]}")
student["grade"]=85
print(f"修改后studnet是：:{student}")
del student["major"]
print(f"删除后studnet是：:{student}")
