# Day21 函数进阶：函数参数、lambda与递归

## 一、函数也可以作为参数

Python中的函数除了可以接收普通数据作为参数之外，也可以把另一个函数作为参数传递。

普通参数可以是：

```text
数字
字符串
布尔值
列表
元组
集合
字典
```

函数本身也可以作为参数传递。

例如先定义两个函数：

```python
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y
```

再定义一个计算函数：

```python
def calc(x, y, oper):
    return oper(x, y)
```

调用：

```python
result = calc(10, 20, add)

print(result)
```

这里：

```python
calc(10, 20, add)
```

把：

```python
add
```

这个函数本身作为实参传递给了：

```python
oper
```

因此：

```python
return oper(x, y)
```

实际上相当于：

```python
return add(10, 20)
```

最终得到：

```text
30
```

如果传入：

```python
result = calc(10, 20, subtract)
```

实际上执行：

```python
subtract(10, 20)
```

得到：

```text
-10
```

注意：

```python
calc(10, 20, add)
```

这里写的是：

```python
add
```

而不是：

```python
add()
```

因为需要传递的是函数本身，而不是立即调用函数。

---

## 二、高阶函数

如果一个函数：

```text
接收另一个函数作为参数
```

或者：

```text
返回一个函数
```

通常称为高阶函数。

例如：

```python
def calc(x, y, oper):
    return oper(x, y)
```

其中：

```python
oper
```

接收另一个函数，因此 `calc()` 就具有高阶函数的特点。

可以理解为：

```text
add()
   ↓
作为参数
   ↓
calc()
   ↓
通过oper接收
   ↓
oper(x, y)
   ↓
执行add(x, y)
```

---

## 三、匿名函数 lambda

匿名函数指的是没有正式函数名称的简单函数。

Python使用：

```python
lambda
```

创建匿名函数。

基本格式：

```python
lambda 参数: 表达式
```

普通函数：

```python
def add(x, y):
    return x + y
```

使用lambda可以简写为：

```python
add = lambda x, y: x + y
```

调用：

```python
print(add(10, 20))
```

输出：

```text
30
```

---

## 四、无参数的lambda

lambda也可以不接收参数。

例如：

```python
out_line = lambda: print("---------------------")
```

调用：

```python
out_line()
```

相当于普通函数：

```python
def out_line():
    print("---------------------")
```

---

## 五、lambda的返回值

匿名函数如果需要返回一个结果，不需要写 `return`。

例如：

```python
add = lambda x, y: x + y
```

其中：

```python
x + y
```

这个表达式的结果会自动作为lambda函数的返回值。

相当于：

```python
def add(x, y):
    return x + y
```

因此：

```text
普通函数
    ↓
return x + y

lambda
    ↓
lambda x, y: x + y
```

---

## 六、什么时候使用lambda

如果函数逻辑比较简单，并且只有一个简单表达式，可以考虑使用lambda。

尤其适合：

```text
函数逻辑简单
只在一个地方使用
作为其他函数的参数
```

例如：

```python
lambda x: x * 2
```

如果逻辑比较复杂，包含大量：

```text
if
for
while
多步计算
```

通常使用普通的 `def` 函数会更加清晰。

---

## 七、lambda配合sort()排序

练习：

按照字符串的字符数量，从短到长进行排序。

原始列表：

```python
data_list = [
    "C++",
    "C",
    "Python",
    "Jack",
    "PHP",
    "Java",
    "Go",
    "JavaScript",
    "Rust"
]
```

普通排序：

```python
data_list.sort()
```

默认是按照字符串本身进行排序。

如果想按照：

```text
字符串长度
```

进行排序，可以使用 `key`。

```python
data_list.sort(
    key=lambda item: len(item)
)
```

完整代码：

```python
data_list = [
    "C++",
    "C",
    "Python",
    "Jack",
    "PHP",
    "Java",
    "Go",
    "JavaScript",
    "Rust"
]

print(data_list)

data_list.sort(
    key=lambda item: len(item)
)

print(data_list)
```

---

## 八、sort()中的key参数

`sort()`中的：

```python
key=
```

可以指定：

```text
按照什么规则进行排序
```

例如：

```python
key=lambda item: len(item)
```

执行过程可以理解为：

```text
"C++"
 ↓
len("C++")
 ↓
3

"C"
 ↓
len("C")
 ↓
1

"Python"
 ↓
len("Python")
 ↓
6
```

最终根据这些长度：

```text
3
1
6
...
```

进行排序。

所以：

```python
data_list.sort(
    key=lambda item: len(item)
)
```

意思就是：

> 根据列表中每个字符串的长度进行排序。

---

## 九、递归调用

递归调用指的是：

> 一个函数在自己的函数内部再次调用自己。

例如计算数字的阶乘。

阶乘：

```text
3! = 3 × 2 × 1
```

可以写成：

```text
3! = 3 × 2!
2! = 2 × 1!
1! = 1
```

因此可以使用递归：

```python
def stratum(n):

    if n == 1:
        return 1

    else:
        return n * stratum(n - 1)
```

调用：

```python
print(stratum(3))
```

---

## 十、递归执行过程

执行：

```python
stratum(3)
```

首先：

```text
stratum(3)
```

因为：

```text
3 != 1
```

所以执行：

```python
3 * stratum(2)
```

继续：

```text
stratum(2)
```

得到：

```python
2 * stratum(1)
```

最后：

```python
stratum(1)
```

满足：

```python
if n == 1:
```

返回：

```text
1
```

开始逐层返回：

```text
stratum(1)
    ↓
1

stratum(2)
    ↓
2 × 1
    ↓
2

stratum(3)
    ↓
3 × 2
    ↓
6
```

最终：

```text
3! = 6
```

---

## 十一、递归必须有终止条件

递归函数中非常重要的一点是：

```text
必须存在递归终止条件
```

本例中的终止条件：

```python
if n == 1:
    return 1
```

如果没有终止条件：

```python
def test():
    test()
```

函数就会不断调用自己：

```text
test()
 ↓
test()
 ↓
test()
 ↓
test()
 ↓
……
```

最终超过Python允许的最大递归深度并报错。

因此递归函数通常包含：

```text
终止条件
+
递归调用
```

例如：

```python
def stratum(n):

    if n == 1:
        return 1

    return n * stratum(n - 1)
```

---

## 十二、阶乘函数需要注意的地方

当前写法：

```python
def stratum(n):
    if n == 1:
        return 1

    return n * stratum(n - 1)
```

适用于：

```text
n >= 1
```

如果以后考虑：

```text
0!
```

数学规定：

```text
0! = 1
```

可以写成：

```python
def stratum(n):

    if n == 0 or n == 1:
        return 1

    return n * stratum(n - 1)
```

现阶段先理解：

```text
递归调用
+
终止条件
```

是最重要的。

---

## 十三、综合案例：超市订单金额计算

要求定义一个函数，根据：

```text
商品信息
优惠券
积分抵扣
运费
```

计算订单最终金额。

商品信息包括：

```text
商品名
价格
数量
```

例如：

```python
("鼠标", 188, 20)
```

其中：

```text
"鼠标" → 商品名称

188 → 商品单价

20 → 商品数量
```

一个订单可以同时包含多个商品：

```python
("鼠标", 188, 20)

("键盘", 388, 30)
```

---

## 十四、订单计算函数的参数设计

函数：

```python
def supermarket(
    *args,
    coupon=0,
    score=0,
    freight=0
):
    pass
```

这里综合使用了Day20学习的参数知识。

### *args

```python
*args
```

接收所有商品信息。

调用：

```python
supermarket(
    ("鼠标", 188, 20),
    ("键盘", 388, 30)
)
```

那么 `args` 可以理解为：

```python
(
    ("鼠标", 188, 20),
    ("键盘", 388, 30)
)
```

因此：

```text
args是元组
    ↓
里面的每一个元素
    ↓
又是一个商品元组
```

---

## 十五、默认参数

函数还定义了：

```python
coupon=0
score=0
freight=0
```

分别表示：

```text
coupon  → 优惠券金额

score   → 积分数量

freight → 运费
```

因为都有默认值：

```text
0
```

所以调用函数时可以选择不传。

例如：

```python
supermarket(
    ("鼠标", 188, 20)
)
```

此时：

```text
coupon = 0

score = 0

freight = 0
```

---

## 十六、计算每种商品的总价

商品信息：

```python
("鼠标", 188, 20)
```

通过索引：

```python
goods[0]
```

得到商品名称：

```text
鼠标
```

通过：

```python
goods[1]
```

得到商品价格：

```text
188
```

通过：

```python
goods[2]
```

得到数量：

```text
20
```

所以单项商品总价：

```python
goods[1] * goods[2]
```

即：

```text
价格 × 数量
```

---

## 十七、列表推导式计算所有商品金额

可以使用之前学习过的列表推导式：

```python
total_price = [
    goods[1] * goods[2]
    for goods in args
]
```

例如：

```python
args = (
    ("鼠标", 188, 20),
    ("键盘", 388, 30)
)
```

最终：

```python
total_price
```

相当于：

```python
[
    188 * 20,
    388 * 30
]
```

得到每一种商品的总金额。

然后：

```python
goods_total = sum(total_price)
```

得到整个订单的商品总金额。

---

## 十八、优惠券规则

规则：

```text
商品总金额满5000元才可以使用优惠券

优惠券金额不能超过商品总金额
```

可以判断：

```python
if goods_total >= 5000 and coupon <= goods_total:
    total_cost = total_cost - coupon
```

这里使用：

```python
and
```

同时判断两个条件。

只有两个条件都满足，优惠券才可以使用。

---

## 十九、积分抵扣规则

规则：

```text
商品总金额满5000元才可以使用积分

100积分抵扣1元

积分只能整百抵扣
```

例如：

```text
100积分  → 1元

500积分  → 5元

1500积分 → 15元
```

因此可以使用：

```python
score // 100
```

计算可以抵扣的金额。

例如：

```python
score = 1050
```

那么：

```python
score // 100
```

得到：

```text
10
```

也就是：

```text
1050积分可以抵扣10元
```

剩下50积分不参与本次抵扣。

---

## 二十、订单最终金额

订单计算规则：

```text
最终金额
=
商品总金额
- 优惠券
- 积分抵扣
- 运费
```

## 二十一、超市订单案例完整整理

```python
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
Day21 函数进阶：函数参数、lambda与递归    total_price = [
        goods[1] * goods[2]
        for goods in args
    ]

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

    # 4.添加运费
    total_cost = total_cost - freight

    return total_cost
```

调用：

```python
cost = supermarket(
    ("鼠标", 188, 20),
    ("键盘", 388, 30),
    coupon=1000,
    score=100000,
    freight=9.9
)

print(cost)
```

---

## 二十二、为什么统计优惠条件时使用goods_total

题目的规则是：

```text
商品总金额满5000才可以使用优惠券和积分
```

因此最好先保存：

```python
goods_total = sum(total_price)
```

代表：

```text
原始商品总金额
```

然后另外创建：

```python
total_cost = goods_total
```

代表：

```text
经过优惠、积分和运费计算后的最终金额
```

这样：

```text
goods_total
    ↓
判断是否满足优惠条件

total_cost
    ↓
不断计算最终付款金额
```

两个变量的作用更加清楚。

---

## 二十三、Day21综合使用到的旧知识

今天的超市案例综合使用了很多之前学习过的知识：

```text
函数
    ↓
封装订单计算逻辑

*args
    ↓
接收多个商品

默认参数
    ↓
coupon、score、freight

元组
    ↓
保存单个商品信息

列表推导式
    ↓
计算所有商品金额

sum()
    ↓
计算商品总金额

if
    ↓
判断优惠条件

and
    ↓
同时判断多个条件

//
    ↓
积分整百抵扣

return
    ↓
返回最终订单金额
```

---

## 二十四、今日重点

### 函数作为参数

```python
def calc(x, y, oper):
    return oper(x, y)
```

调用：

```python
calc(10, 20, add)
```

注意传入的是：

```python
add
```

而不是：

```python
add()
```

---

### lambda基本格式

```python
lambda 参数: 表达式
```

例如：

```python
lambda x, y: x + y
```

---

### lambda作为排序规则

```python
data_list.sort(
    key=lambda item: len(item)
)
```

表示：

```text
根据每个元素的长度进行排序
```

---

### 递归

```python
def stratum(n):

    if n == 1:
        return 1

    return n * stratum(n - 1)
```

递归一定要有：

```text
终止条件
```

---

### 不定长商品参数

```python
def supermarket(*args):
    pass
```

可以接收：

```python
supermarket(
    ("鼠标", 188, 20),
    ("键盘", 388, 30)
)
```

---

### 订单计算

```text
订单最终金额
=
商品总金额
- 优惠券
- 积分抵扣
+ 运费
```

---

## Day21总结

今天继续学习Python函数的进阶内容：

- 学习了函数本身也可以作为参数传递
- 初步理解了高阶函数的概念
- 学习了匿名函数 `lambda`
- 理解了lambda不需要显式写 `return`
- 学习了什么时候适合使用lambda
- 学习了使用 `lambda` 配合 `sort(key=...)` 自定义排序规则
- 学习了按照字符串长度进行排序
- 学习了递归函数的基本概念
- 理解了递归函数必须设置终止条件
- 通过阶乘案例理解了递归调用和逐层返回过程
- 综合使用了 `*args` 和默认参数设计订单计算函数
- 使用元组保存商品信息
- 使用列表推导式计算每项商品金额
- 使用优惠券、积分和运费计算订单最终金额
- 进一步综合练习了 `if`、`and`、`//`、`sum()` 和 `return`