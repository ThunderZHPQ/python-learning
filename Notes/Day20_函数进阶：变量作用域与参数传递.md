# Day20 函数进阶：变量作用域与参数传递

## 一、全局变量和局部变量

Python中的变量根据定义的位置，可以分为：

- 全局变量
- 局部变量

### 1. 全局变量

在函数外部定义的变量称为全局变量。

全局变量通常定义在文件顶部，在当前文件中的函数外部和函数内部都可以读取。

例如：

```python
num = 100

def test():
    print(num)

test()

print(num)
```

这里的：

```python
num = 100
```

是在函数外部定义的，因此是全局变量。

函数内部可以读取：

```python
print(num)
```

函数外部也可以读取：

```python
print(num)
```

---

### 2. 局部变量

在函数内部定义的变量称为局部变量。

局部变量只能在当前函数内部使用。

例如：

```python
def circle_area(r):
    pi = 3.14

    area = pi * r * r

    return area
```

其中：

```python
pi
area
```

都是局部变量。

它们只属于 `circle_area()` 函数。

函数外部不能直接访问：

```python
print(pi)
```

否则会报错。

可以理解为：

```text
全局变量
    ↓
整个文件中都可以使用

局部变量
    ↓
只能在当前函数内部使用
```

---

## 二、global关键字

函数内部可以直接读取全局变量。

但是如果想要在函数内部修改全局变量，需要使用：

```python
global
```

例如：

```python
num = 100

def circle_area(r):
    pi = 3.14

    area = pi * r * r

    global num

    num = 10000

    print("num =", num)

    return area
```

调用：

```python
c_area = circle_area(10)

print(c_area)

print("num =", num)
```

执行函数后：

```python
num
```

已经从：

```text
100
```

修改成：

```text
10000
```

### global基本格式

```python
global 变量名
```

必须先声明：

```python
global num
```

然后再对它重新赋值：

```python
num = 10000
```

注意：

如果只是读取全局变量，通常不需要使用 `global`。

例如：

```python
num = 100

def test():
    print(num)
```

只有当函数内部需要对全局变量进行赋值修改时，才需要使用：

```python
global num
```

---

## 三、函数参数的传递方式

调用函数时，需要将实际的数据传递给函数。

本次主要学习了：

```text
位置参数
关键字参数
默认参数
不定长位置参数
不定长关键字参数
```

---

## 四、位置参数

位置参数是根据函数定义时参数的位置和顺序传递数据。

例如：

```python
def reg_stu(name, age, gender, city):
    print(
        f"注册成功,"
        f"姓名：{name},"
        f"年龄：{age},"
        f"性别：{gender},"
        f"城市：{city}"
    )

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "city": city
    }
```

使用位置参数调用：

```python
stu = reg_stu("张三", 18, "男", "北京")

print(stu)
```

对应关系为：

```text
name   = "张三"

age    = 18

gender = "男"

city   = "北京"
```

位置参数最重要的是：

```text
实参顺序必须和形参顺序对应
```

例如：

```python
reg_stu("张三", 18, "男", "北京")
```

不能随意改变参数顺序，否则数据的含义就会发生变化。

---

## 五、关键字参数

关键字参数通过：

```python
形参名=值
```

的方式传递数据。

例如：

```python
stu = reg_stu(
    name="王林",
    age=28,
    gender="男",
    city="北京"
)
```

关键字参数不需要按照函数定义时的顺序传递。

例如：

```python
stu1 = reg_stu(
    age=20,
    gender="女",
    city="北京",
    name="李慕婉"
)
```

依然可以正常执行。

因为Python会根据参数名称进行匹配。

### 位置参数和关键字参数的区别

位置参数：

```python
reg_stu("张三", 18, "男", "北京")
```

优点：

```text
代码简洁
```

缺点：

```text
参数较多时容易混淆
```

关键字参数：

```python
reg_stu(
    name="张三",
    age=18,
    gender="男",
    city="北京"
)
```

优点：

```text
可读性更强
不容易混淆参数含义
方便维护
```

如果：

```text
参数数量较少，并且不容易混淆
```

可以使用位置参数。

如果：

```text
参数数量较多，并且容易混淆
```

可以使用关键字参数。

---

## 六、位置参数和关键字参数混合使用

位置参数和关键字参数可以同时使用。

例如：

```python
stu3 = reg_stu(
    "李慕婉",
    20,
    gender="女",
    city="北京"
)
```

这里：

```text
"李慕婉"
20
```

属于位置参数。

而：

```python
gender="女"
city="北京"
```

属于关键字参数。

需要注意：

```text
位置参数必须写在关键字参数前面
```

正确：

```python
reg_stu(
    "李慕婉",
    20,
    gender="女",
    city="北京"
)
```

不能把普通的位置参数放在关键字参数之后。

---

## 七、默认参数

默认参数也称为缺省参数。

定义函数时，可以提前给某些参数设置默认值。

例如：

```python
def reg_stu(name, age, gender, city="北京"):
    print(
        f"注册成功,"
        f"姓名：{name},"
        f"年龄：{age},"
        f"性别：{gender},"
        f"城市：{city}"
    )

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "city": city
    }
```

这里：

```python
city="北京"
```

就是默认参数。

---

## 八、默认参数的使用

如果调用函数时没有传递 `city`：

```python
stu = reg_stu(
    name="王林",
    age=28,
    gender="男"
)
```

那么：

```python
city
```

会自动使用默认值：

```text
北京
```

如果主动传递新的值：

```python
stu1 = reg_stu(
    age=20,
    gender="女",
    city="上海",
    name="李慕婉"
)
```

那么：

```python
city
```

使用的是：

```text
上海
```

而不是默认的北京。

可以理解为：

```text
不传参数
    ↓
使用默认值

传入参数
    ↓
使用本次传入的值
```

---

## 九、默认参数的位置

默认参数必须放在没有默认值参数的后面。

正确：

```python
def reg_stu(name, age, gender, city="北京"):
    pass
```

这里：

```text
name
age
gender
```

没有默认值。

```text
city
```

有默认值，因此放在后面。

一个函数可以设置多个默认参数。

例如：

```python
def test(name, age=18, city="北京"):
    pass
```

---

## 十、不定长位置参数 *args

有时候无法提前确定函数调用时会传入多少个数据。

这时可以使用：

```python
*args
```

接收不定数量的位置参数。

例如：

```python
def calc_data(*args):
    min_data = min(args)

    max_data = max(args)

    avg_data = sum(args) / len(args)

    return min_data, max_data, round(avg_data, 1)
```

调用时可以传入任意数量的位置参数：

```python
data = calc_data(
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100
)

print(data)
```

也可以传入：

```python
data = calc_data(
    100,
    200,
    300,
    400,
    500
)

print(data)
```

函数都可以正常接收。

---

## 十一、args的类型

使用：

```python
*args
```

接收到的所有位置参数，会自动封装成一个：

```text
元组 tuple
```

例如：

```python
def test(*args):
    print(args)
    print(type(args))

test(10, 20, 30)
```

可以理解为：

```python
args = (10, 20, 30)
```

因此可以直接使用之前学习过的：

```python
min(args)
max(args)
sum(args)
len(args)
```

例如：

```python
avg_data = sum(args) / len(args)
```

计算平均值。

---

## 十二、不定长关键字参数 **kwargs

如果传入的是：

```python
键=值
```

形式的关键字参数，可以使用：

```python
**kwargs
```

进行接收。

例如：

```python
def test(**kwargs):
    print(kwargs)
```

调用：

```python
test(
    name="张三",
    age=18,
    city="北京"
)
```

这些关键字参数会被封装成一个字典。

可以理解为：

```python
kwargs = {
    "name": "张三",
    "age": 18,
    "city": "北京"
}
```

因此：

```text
*args
    ↓
接收位置参数
    ↓
元组 tuple


**kwargs
    ↓
接收关键字参数
    ↓
字典 dict
```

---

## 十三、同时使用 *args 和 **kwargs

一个函数中可以同时使用：

```python
*args
```

和：

```python
**kwargs
```

例如：

```python
def calc_data(*args, **kwargs):
    min_data = min(args)

    max_data = max(args)

    avg_data = sum(args) / len(args)

    return min_data, max_data, avg_data
```

调用：

```python
data = calc_data(
    10.25,
    20,
    33,
    44,
    56,
    68,
    77,
    85,
    94,
    111,
    round=2,
    print=True
)
```

其中：

```text
10.25
20
33
44
...
111
```

这些属于位置参数，被：

```python
args
```

接收。

因此：

```python
args
```

相当于：

```python
(
    10.25,
    20,
    33,
    44,
    56,
    68,
    77,
    85,
    94,
    111
)
```

而：

```python
round=2
print=True
```

属于关键字参数，被：

```python
kwargs
```

接收。

相当于：

```python
kwargs = {
    "round": 2,
    "print": True
}
```

---

## 十四、通过kwargs获取参数

因为 `kwargs` 是字典，所以可以使用字典的方法。

例如：

```python
kwargs.get("round")
```

获取：

```text
round
```

对应的value。

又例如：

```python
kwargs.get("print")
```

获取：

```text
print
```

对应的value。

---

## 十五、判断关键字参数是否传入

在本次案例中：

```python
if kwargs.get("round") is not None:
    avg_data = round(
        avg_data,
        kwargs.get("round")
    )
```

意思是：

```text
获取kwargs中的"round"
        ↓
如果不是None
        ↓
说明传入了round参数
        ↓
按照指定的小数位进行四舍五入
```

例如：

```python
calc_data(
    10,
    20,
    30,
    round=2
)
```

那么：

```python
kwargs.get("round")
```

得到：

```text
2
```

于是执行：

```python
avg_data = round(avg_data, 2)
```

---

## 十六、根据kwargs决定是否输出结果

代码：

```python
if kwargs.get("print"):
    print(
        f"计算出来的最小值：{min_data}，"
        f"最大值：{max_data}，"
        f"平均值:{avg_data}"
    )
```

如果调用：

```python
calc_data(
    10,
    20,
    30,
    print=True
)
```

则：

```python
kwargs.get("print")
```

得到：

```text
True
```

因此执行打印。

如果没有传：

```python
print=True
```

那么：

```python
kwargs.get("print")
```

默认得到：

```text
None
```

条件不成立，因此不会执行打印。

---

## 十七、综合案例：计算一批数据

完整函数：

```python
def calc_data(*args, **kwargs):
    '''
    根据传入的这批数据，计算这批数据的最小值、最大值、平均值

    :param args:
        不定长位置参数，需要计算的这批数据

    :param kwargs:
        不定长关键字参数

        round：保留的小数位个数
        print：是否打印输出

    :return:
        最小值、最大值、平均值
    '''

    min_data = min(args)

    max_data = max(args)

    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(
            avg_data,
            kwargs.get("round")
        )

    if kwargs.get("print"):
        print(
            f"计算出来的最小值：{min_data}，"
            f"最大值：{max_data}，"
            f"平均值:{avg_data}"
        )

    return min_data, max_data, avg_data
```

调用：

```python
data = calc_data(
    10.25,
    20,
    33,
    44,
    56,
    68,
    77,
    85,
    94,
    111,
    round=2,
    print=True
)

print(data)
```

再次调用：

```python
data = calc_data(
    156,
    278.697,
    357,
    431,
    511,
    round=2,
    print=True
)

print(data)
```

同一个函数可以接收不同数量的数据。

这就是不定长参数的重要作用。

---

## 十八、*args和**kwargs的区别

### *args

```python
def test(*args):
    pass
```

作用：

```text
接收任意数量的位置参数
```

最终封装为：

```text
tuple 元组
```

例如：

```python
test(10, 20, 30)
```

得到：

```python
args = (10, 20, 30)
```

---

### **kwargs

```python
def test(**kwargs):
    pass
```

作用：

```text
接收任意数量的关键字参数
```

最终封装为：

```text
dict 字典
```

例如：

```python
test(
    name="张三",
    age=18
)
```

得到：

```python
kwargs = {
    "name": "张三",
    "age": 18
}
```

因此可以记成：

```text
*args
↓
位置参数
↓
元组


**kwargs
↓
关键字参数
↓
字典
```

---

## 十九、参数类型总结

本次学习的参数可以整理为：

### 位置参数

```python
def test(a, b):
    pass

test(10, 20)
```

特点：

```text
按照位置传递
顺序非常重要
```

### 关键字参数

```python
test(
    a=10,
    b=20
)
```

特点：

```text
按照参数名称传递
可读性较强
顺序可以调整
```

### 默认参数

```python
def test(a, b=20):
    pass
```

特点：

```text
调用时可以不传
不传就使用默认值
```

### 不定长位置参数

```python
def test(*args):
    pass
```

特点：

```text
可以接收任意数量的位置参数
args是元组
```

### 不定长关键字参数

```python
def test(**kwargs):
    pass
```

特点：

```text
可以接收任意数量的关键字参数
kwargs是字典
```

---

## 二十、今日重点

### 全局变量

```python
num = 100
```

函数内部可以读取。

需要修改时：

```python
global num
num = 10000
```

### 局部变量

```python
def test():
    num = 100
```

只能够在当前函数内部使用。

### 位置参数

```python
test(10, 20)
```

### 关键字参数

```python
test(
    a=10,
    b=20
)
```

### 默认参数

```python
def test(a, b=20):
    pass
```

### 不定长位置参数

```python
def test(*args):
    pass
```

```text
args → tuple
```

### 不定长关键字参数

```python
def test(**kwargs):
    pass
```

```text
kwargs → dict
```

### 同时使用

```python
def test(*args, **kwargs):
    pass
```

其中：

```text
args
↓
接收位置参数

kwargs
↓
接收关键字参数
```

---

## Day20总结

今天继续学习Python函数的进阶内容：

- 学习了全局变量和局部变量的区别
- 学习了变量的作用范围
- 学习了使用 `global` 在函数内部修改全局变量
- 学习了位置参数的使用
- 学习了关键字参数的使用
- 学习了位置参数和关键字参数混合传递
- 学习了默认参数的定义和使用
- 理解了默认参数需要放在普通参数后面
- 学习了不定长位置参数 `*args`
- 理解了 `args` 会把位置参数封装成元组
- 学习了不定长关键字参数 `**kwargs`
- 理解了 `kwargs` 会把关键字参数封装成字典
- 学习了同时使用 `*args` 和 `**kwargs`
- 使用 `kwargs.get()` 获取可选参数
- 完成了可接收任意数量数据的最大值、最小值、平均值统计函数
- 实现了通过关键字参数控制小数位数和是否打印结果