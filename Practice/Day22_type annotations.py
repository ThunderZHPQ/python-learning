def supermarket(     
    *args,
    coupon=0,
    score=0,
    freight=0
):
    '''
    根据商品信息、优惠券、积分和运费计算订单总金额

    :param args:
        商品信息（商品名、价格、数量）

    :param coupon:
        优惠券金额

    :param score:
        积分数量

    :param freight:
        运费

    :return:
        订单最终金额
    '''

    # 1.计算所有商品金额
    total_price = [goods[1] * goods[2] for goods in args]

    # 商品总金额
    goods_total = sum(total_price)

    # 最终需要支付的金额
    total_cost = goods_total

    # 2.扣减优惠券
    if goods_total >= 5000 and coupon <= goods_total:
        total_cost = total_cost - coupon

    # 3.扣减积分
    score_money = score // 100

    if goods_total >= 5000 and score_money <= goods_total:
        total_cost = total_cost - score_money

    # 4.减去运费
    total_cost = total_cost - freight

    return total_cost

cost = supermarket(
    ("鼠标", 188, 20),
    ("键盘", 388, 30),
    coupon=1000,
    score=100000,
    freight=9.9
)

print(cost)


# 类型注解是Python中的一种语法特性，用于明确标识变量、函数参数和返回值的数据类型，从而使代码更清晰、更安全、更易维护。

a:int = 695
score:float = 98.5
hobby:str = "Python"
flag: bool = True
pic:None = None
names:list[str]= ["A","B","C"]
phones:set[str] = {"13309091111","15209109121"}
options:dict[str,int] = {"count":0,"total":0}
goods:tuple[str,int,int] = ("手机",5999,1)


# 1，类型注解的写法:变量：数据类型（如a：int)
# 2．常见类型的写法
# int、float、bool、str、None、list、set、tuple、dict,str|int
# 3.为什么要使用类型注解，有什么好处呢？
# 代码结构更清晰、代码逻辑更安全、易维护
# 更准确的代码自动提示
# 提前发现代码潜在问题


# 为函数添加类型注解，其实主要就是为函数的参数和返回值添加类型注解，具体语法如下：
def calc(scores: list[int]) -> float:
    return sum(scores)/len(scores)

def calc_data(scores: list[int]) -> tuple[int,int,float]:
    max_V = max(scores)
    min_v = min(scores)
    avg_V =sum(scores)/ len(scores)
    return max_V, min_v, avg_V
