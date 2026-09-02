"""
#输入一个数字，判断是否为正数、负数或零
num = float(input("请输入一个数字: "))
if num > 0:
    print("这是一个正数。")
elif num < 0:
    print("这是一个负数。")
else:
    print("这是零。")



#输入三边长，判断能否构成三角形，并输出三角形的类型
a = float(input("请输入第一条边长: "))
b = float(input("请输入第二条边长: "))
c = float(input("请输入第三条边长: "))

#如果if嵌套时，暂时不想编写里面的代码，可以使用pass占位，表示什么都不做
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    if a==b==c:
        print("这是一个等边三角形。")
    elif a==b or b==c or a==c:
        print("这是一个等腰三角形。")
    else:
        print("这是一个不等边三角形。")
else:
    print(f"边长 {a}, {b}, {c} 无法构成三角形。")


#输入一个值，判断是否是工作日
day = input("请输入一个值（例如：星期一、星期二、星期三、星期四、星期五、星期六、星期日）: ")
match day:
    case "星期一" | "星期二" | "星期三" | "星期四" | "星期五":
        print(f"{day} 是工作日。")
    case "星期六" | "星期日":
        print(f"{day} 是休息日。")
    case _:
        print("输入的值不合法，请输入有效的星期值。")
"""

#实现基于match-case的计算器功能
try:
    num1 = float(input("请输入第一个数字: "))
    oper = input("请输入运算符号:")
    num2 = float(input("请输入第二个数:"))
except ValueError:
    raise SystemExit("输入不是有效的数字，程序退出。")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1+num2}")
    case "-":
        print(f"{num1} - {num2} = {num1-num2}")
    case "*":
        print(f"{num1} * {num2} = {num1*num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1/num2}")
    case "/":
        print("错误：除数不能为0")
    case _:
        print(f"不支持的运算符：{oper}")

#match.·.case应用场景
# match：基于某个变量的多个固定值进行分支判断时，可以使用match模式匹配
# if：条件判断涉及复杂的逻辑判定、范围比较及组合条件时