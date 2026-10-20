# 注意：函数定义的时候并不会执行，只有在调用函数的时候，函数体的逻辑才会执行；函数必须先定义，后调用；
# 函数定义
def out_line():  
    print("------------------------------------------------")
    print("------------------------------------------------")

# 函数调用
out_line()



# 函数的参数与返回值
# 函数1：计算圆的面积 -- 半径
def circle_area(r):  
    area = 3.14 * r ** 2
    return area

area = circle_area(10)
print(area)  # 调用函数并打印返回值

# 函数2：计算长方形的面积 -- 长，宽
def rectangle_area(l,w):  
    """计算长方形的面积
    :param l: 长
    :param w: 宽
    :return: 面积
    """
    area = l * w
    return area

help(rectangle_area)  # 查看函数的帮助文档
print(rectangle_area(l=20, w=10))

# 函数3：计算圆的面积，周长 -- 半径 ----> 如果返回值有多个，多个返回值之间逗号分隔 ----> 多个返回值会封装到元组之中
def circle_area_len(r):  
    """
    计算圆的面积和周长
    :param r: 半径
    :return: 面积和周长
    """
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(10)
print(al)
print(type(al))

area, len = circle_area_len(10) # 解包
print(area)
print(len)

