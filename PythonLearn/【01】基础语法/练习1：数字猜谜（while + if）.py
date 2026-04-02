import random

result=random.randint(1,50)
chance=5

print("猜数字游戏（1-50）")
print(f"你有{chance}次机会")

while chance>0:
   n = int(input(f"还有{chance}次机会，请输入您猜测的数:"))
   if n<1 or n>50:
      print("请输入1-50之间的整数!")
      continue
   if n>result:
      print(f"太大了")
      chance-=1
   elif n < result:
      print(f"太小了")
      chance -= 1
   else:
      print(f"恭喜！你用了{6-chance}次猜中")
      print(f"正确答案就是{result}")
if chance==0:
   print(f"机会用完了，正确答案是{result}")