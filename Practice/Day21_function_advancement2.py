# 普通参数：数字、布尔、字符串、列表、元组、集合、字典等。
# 特殊参数：函数

# def add (x, y):
#     return x+y

# def subtract (x, y):
#     return x-y

# def calc(x,y,oper):
#     return oper(x,y)

# result = calc(10,20,add)
# print(result)

# 匿名函数指的是没有名称的函数,需要通过lambda表达式来声明函数,可以简化简单函数的编写（单行表达式）。
# out_line = lambda:print("---------------------")
# add = lambda x,y:x+y

# out_line()
# print(add(10,20))

# 函数逻辑比较简单（单行表达式）且只在一个地方使用时,可以考虑使用匿名函数,简化书写（通常作为高阶函数的参数使用）。
# 匿名函数中可以返回结果,也可以不返回结果。返回结果时,不需要写return,表达式的运行结果就是要返回的结果。

#完成如下列表的排序操作,按照每一个元素的字符个数,从小到大排序；
# data_list =["C++","C","Python","Jack","PHP","Java", "Go","JavaScript","Rust"]
# print(data_list)
# data_list.sort(key=lambda item :len(item))
# print(data_list)

# 定义一个函数，根据传入的数字，计算该数字阶乘的结果。

# 递归调用：指的是在函数中自己调用自己的情况，一定要用终结点
# def stratum(n):
#     if n== 1:
#         return 1
#     else:
#         return n*stratum(n-1)

# print(stratum(3))

# 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
# 具体规则如下：
# 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。

def supermarket(*args,coupon = 0,score = 0,freight = 0):
    '''
    :param *args:商品信息（商品名、价格、数量）
    :param coupon:优惠券
    :param score:积分
    :param freight:运费
    :param return:订单总价格
    '''

# 订单的总金额=商品总金额-优惠券-积分抵扣-运费

#1．计算商品总金额

    #单项产品总价格
    total_price= [goods[1] * goods[2] for goods in args]
    #订单总金额
    total_cost = sum(total_price)

# 2．扣减优惠券

    if total_cost >= 5000 and coupon <= total_cost:
        total_cost = total_cost - coupon

# 3，扣减积分抵扣
    if total_cost >= 5000 and score//100 <= total_cost:
        total_cost = total_cost - score//100

# 4，添加运费
    total_cost = total_cost - freight

    return total_cost

cost = supermarket(("鼠标",188,20),("键盘",388,30),coupon=1000,score=100000,freight=9.9)
print(cost)
