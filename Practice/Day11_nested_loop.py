#嵌套循环的应用
#根据输入的数值，打印出一个长度为M，宽为N的长方形

"""
m = int(input("请输入长："))
n = int(input("请输入宽："))

for i in range(m):
    for x in range(n):
        print("*",end=" ")
    print()
"""

#打印9*9算数表

for i in range(1,10):
    for n in range(1,i+1):
        print(f"{n}*{i}={n*i}",end=" ")
    print()
