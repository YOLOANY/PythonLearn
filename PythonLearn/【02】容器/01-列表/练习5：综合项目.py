# 有一个待办列表
#todos = ["学Python", "写作业", "做项目"]
# 1. 用 enumerate 打印带序号的待办（从1开始）
# 2. 删除第 2 个待办
# 3. 检查 "学Python" 是否在列表中
todos = ["学Python", "写作业", "做项目"]
for index,todo in enumerate(todos,start=1):
    print(f"{index}.{todo}")

todos.pop(1)                        #pop删除索引，remove删除索引对应的值
print(todos)

result="学Python" in todos
print(result)