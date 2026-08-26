# 全局变量：在函数之外定义的变量,称之为全局变量,在整个文件中（包括函数内)都可以使用（通常定义在文件的顶部)
# 局部变量：在函数内部定义的变量,称之为局部变量,只能在该函数内部使用,外部无法访问（函数执行完毕后,会自动销毁其内部局部变量)。
# global关键字用于明确的告诉Python解释器,在函数中要使用全局变量,使得可以在函数内部修改全局变量的值。一定要先声明,再调用

#全局变量：在函数外部或函数的内部都是可以访问的；
# num=100

# 定义函数
# def circle_area(r):
# #布局变量：只能在函数内部使用
#     pi=3.14
#     area=pi*r*r
#     global  num
#     num = 10000

#     print("num =",num)# 10000
#     return area

# # 调用函数
# c_area = circle_area(10)

# print(c_area)

# print("num =",num) #10000

# 传参方式指的是,在调用函数时,传递实参的方式。
# 1:位置参数：调用函数时根据函数定义时的位置来传递参数。要求：调用函数时参数顺序与定义函数时参数顺序完全一致
# 2:关键字参数：调用函数时以函数定义时形参名称作为关键字,以"键=值”的形式来传递参数（不要求顺序)。如果位置参数与关键字参数混用,关键字参数必须在位置参数之后（关键字参数之间,没有顺序要求)
# 位置参数简介,关键性参数可读性强,方便维护,但是繁琐
# 参数数量较少切不容易混淆时,建议使用位置参数。参数数量多并且容易混淆时,建议使用关键字参数

# def reg_stu(name, age, gender, city):
#     print(f"注册成功,姓名：{name},年龄：{age},性别：{gender},城市：{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}

# #位置参数
# stu =reg_stu("张三",18,"男","北京")
# print(stu)

# #关键字参数
# stu = reg_stu(name="王林",age=28,gender="男",city="北京")
# print(stu)
# stu1=reg_stu(age=20,gender="女",city="北京",name="李慕婉")
# print(stu1)

# #位置+关键字混合参数
# stu3 = reg_stu("李慕婉",20,gender="女",city="北京")
# print(stu3)

# 默认参数也称为缺省参数,可以不传递有默认值的参数
# 默认参数必须放在没有默认值的参数列表的后面,一个函数在定义时是可以设置多个默认参数的。
# 函数调用时,如果为默认参数传递了值,则会修改默认的参数值；如果没有传递该参数,则直接使用默认值。

# def reg_stu(name, age, gender, city="北京"):
#     print(f"注册成功,姓名：{name},年龄：{age},性别：{gender},城市：{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}

# stu = reg_stu(name="王林",age=28,gender="男",)
# print(stu)
# stu1=reg_stu(age=20,gender="女",city="上海",name="李慕婉")
# print(stu1)

# 传递的所有匹配的位置参数都会被（*不定长参数)变量收集,这些参数会合并封装为一个元组,args是元组类型（注意并不会封装关键字参数)。
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args)/ len(args)
#     return min_data, max_data, round(avg_data,1)

# #调用函数
# data = calc_data(10,20,30,40,50,60,70,80,90,100)
# print(data)
# data = calc_data(100,200,300,400,500)
# print(data)

# 不定长参数-关键字传递(**关键字)。参数是以“键=值"形式传递的关键字参数，这些"键=值"参数都会被kwargs接受，并合并封装为一个字典类型。
def calc_data(*args,**kwargs):
    '''
    根据传入的这批数据，计算这批数据的最小值，最大值，平均值
    :paramargs:不定长位置参数，需要计算的这批数据
    :paramkwargs:不定长关键字参数
        round:保留的小数位个数
        print:是否打印输出
    :return:最小值,最大值,平均值
    '''
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/ len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值：{min_data}，最大值：{max_data}，平均值:{avg_data}")
    
    return min_data, max_data, avg_data

#调用函数
data = calc_data(10.25,20,33,44,56,68,77,85,94,111,round=2,print = True)
print(data)
data = calc_data(156,278.697,357,431,511,round=2,print = True)
print(data)