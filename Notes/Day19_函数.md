# Day19 函数（function）

## 一、函数的基本概念

函数是组织好的、可重复使用的、用来实现特定功能的代码片段。

函数可以把一段需要重复执行的代码封装起来，在需要的时候直接调用。

函数的特点：

- 可以减少重复代码
- 可以提高代码的复用性
- 可以让程序结构更加清晰
- 一个函数通常负责完成一个具体功能
- 函数需要先定义，再调用

---

## 二、函数的定义和调用

Python中使用 `def` 定义函数。

基本格式：

```python
def 函数名():
    函数体
```

例如：

```python
def out_line():
    print("------------")
```

定义完成后，需要通过函数名进行调用：

```python
out_line()
```

完整示例：

```python
def out_line():
    print("------------")

out_line()
```

注意：

```text
定义函数 → 函数中的代码不会立即执行

调用函数 → 才会执行函数中的代码
```

因此函数一定是：

```text
先定义
  ↓
再调用
```

---

## 三、函数的参数

函数可以接收外部传入的数据。

例如计算圆的面积：

```python
def circle_area(r):
    area = 3.14 * r * r
    return area
```

调用：

```python
c_area = circle_area(3)

print(c_area)
```

这里：

```python
r
```

是函数定义时的参数。

而：

```python
3
```

是调用函数时实际传入的数据。

---

## 四、形参与实参

### 形参

定义函数时写在括号中的参数称为形参。

例如：

```python
def circle_area(r):
    return 3.14 * r * r
```

其中：

```python
r
```

就是形参。

### 实参

调用函数时实际传入的数据称为实参。

例如：

```python
circle_area(3)
```

其中：

```python
3
```

就是实参。

可以理解为：

```text
形参 → 定义函数时使用的变量

实参 → 调用函数时真正传进去的数据
```

通常情况下，形参与实参的数量需要对应。

例如：

```python
def rectangle_area(l, w):
    return l * w
```

调用时需要传入两个参数：

```python
rectangle_area(5, 10)
```

其中：

```text
l = 5
w = 10
```

---

## 五、return返回值

函数可以通过 `return` 将计算结果返回到函数外部。

例如：

```python
def circle_area(r):
    area = 3.14 * r * r

    return area
```

调用：

```python
c_area = circle_area(3)

print(c_area)
```

执行过程：

```text
circle_area(3)
      ↓
r = 3
      ↓
计算area
      ↓
return area
      ↓
返回给调用位置
      ↓
c_area接收结果
```

注意：

```text
print() → 把内容显示出来

return  → 把结果返回给调用函数的位置
```

两者作用不同。

---

## 六、使用函数计算长方形面积

定义一个函数，根据长和宽计算长方形面积：

```python
def rectangle_area(l, w):
    '''
    根据长宽计算长方形的面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形面积
    '''

    area = l * w

    return area
```

调用：

```python
r_rectangle = rectangle_area(5, 10)

print(r_rectangle)
```

其中：

```text
l = 5

w = 10
```

函数计算：

```text
5 × 10 = 50
```

然后通过 `return` 返回结果。

---

## 七、函数说明文档

函数中可以使用三引号添加说明文档。

例如：

```python
def rectangle_area(l, w):
    '''
    根据长宽计算长方形的面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形面积
    '''

    return l * w
```

其中：

```text
:param
```

用于说明参数。

```text
:return
```

用于说明返回值。

这种写法可以帮助理解函数的作用、参数以及返回结果。

---

## 八、函数返回多个值

一个函数可以同时返回多个值。

多个返回值之间使用逗号分隔：

```python
def circle_area_len(r):

    area = round(3.14 * r * r, 1)
    lens = round(2 * 3.14 * r, 1)

    return area, lens
```

调用：

```python
result = circle_area_len(10)

print(result)
```

当函数返回多个值时：

```python
return area, lens
```

Python会把多个返回值封装成一个元组。

例如可能得到：

```python
(314.0, 62.8)
```

因此：

```python
result = circle_area_len(10)
```

这里的 `result` 是一个元组。

---

## 九、解包函数的多个返回值

函数返回多个值后，可以使用之前学习的解包进行接收。

例如：

```python
area, lens = circle_area_len(10)

print(area)
print(lens)
```

相当于将：

```python
(314.0, 62.8)
```

解包成：

```text
area = 314.0

lens = 62.8
```

因此：

```python
return 值1, 值2
```

可以搭配：

```python
变量1, 变量2 = 函数()
```

直接获取多个结果。

---

## 十、函数的嵌套调用

函数的嵌套调用指的是：

> 在一个函数中又调用另一个函数。

例如：

```python
def function_a():
    print("a ... before")

    function_b()

    print("a ... after")


def function_b():
    print("b ... before")

    function_c()

    print("b ... after")


def function_c():
    print("c ...")


function_a()
```

调用过程：

```text
function_a()
     ↓
执行a before
     ↓
调用function_b()
     ↓
执行b before
     ↓
调用function_c()
     ↓
执行c
     ↓
function_c结束
     ↓
继续function_b
     ↓
执行b after
     ↓
function_b结束
     ↓
继续function_a
     ↓
执行a after
```

---

## 十一、函数调用的栈结构

函数调用遵循栈结构。

特点：

```text
后进先出
```

英文：

```text
LIFO
Last In First Out
```

也就是：

> 最后被调用的函数，会最先执行完成并返回。

例如：

```text
function_a
    ↓
function_b
    ↓
function_c
```

调用顺序：

```text
a → b → c
```

返回顺序：

```text
c → b → a
```

---

## 十二、练习：计算三角形面积

要求：

根据传入的底和高计算三角形面积。

公式：

```text
三角形面积 = 底 × 高 ÷ 2
```

定义函数：

```python
def triangle(l, d):

    return round(l * d / 2, 1)
```

调用：

```python
area_triangle = triangle(3, 6)

print(area_triangle)
```

计算结果：

```text
3 × 6 ÷ 2 = 9
```

---

## 十三、练习：统计字符串中的元音字母

要求：

计算传入字符串中元音字母的数量。

元音字母包括：

```text
a e i o u
A E I O U
```

代码：

```python
def strings(s):

    num = 0

    for i in s:

        if i in "aeiouAEIOU":
            num += 1

    return num
```

调用：

```python
vowel = strings(input("请输入字符串："))

print(f"元音字母的数量为：{vowel}")
```

执行思路：

```text
传入字符串
    ↓
for遍历每一个字符
    ↓
判断字符是否在"aeiouAEIOU"中
    ↓
如果是元音
    ↓
num += 1
    ↓
遍历完成
    ↓
return num
```

这里综合使用了之前学习的：

```text
函数
for循环
if判断
in
字符串
变量累加
return
```

---

## 十四、练习：统计班级成绩

要求：

计算传入的班级成绩列表中的：

- 最高分
- 最低分
- 平均分
- 平均分保留1位小数

定义函数：

```python
def calc_score(score_list):
    '''
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
    :param score_list: 分数列表
    :return: 最高分, 最低分, 平均分
    '''

    max_s = max(score_list)

    min_s = min(score_list)

    avg_s = round(
        sum(score_list) / len(score_list),
        1
    )

    return max_s, min_s, avg_s
```

准备成绩列表：

```python
s_list = [
    589,
    609,
    605,
    643,
    677,
    455,
    477,
    489,
    503
]
```

调用函数并进行解包：

```python
max_score, min_score, avg_score = calc_score(s_list)

print(max_score, min_score, avg_score)
```

这里：

```python
return max_s, min_s, avg_s
```

实际上返回的是一个包含三个元素的元组。

然后：

```python
max_score, min_score, avg_score = calc_score(s_list)
```

使用解包分别接收三个结果。

---

## 十五、成绩统计案例中使用的知识

获取最高分：

```python
max(score_list)
```

获取最低分：

```python
min(score_list)
```

获取总分：

```python
sum(score_list)
```

获取人数：

```python
len(score_list)
```

计算平均分：

```python
sum(score_list) / len(score_list)
```

保留1位小数：

```python
round(
    sum(score_list) / len(score_list),
    1
)
```

最终通过：

```python
return max_s, min_s, avg_s
```

一次返回三个结果。

---

## 十六、函数的基本结构

一个比较完整的函数通常包含：

```python
def 函数名(参数):
    # 函数中的代码

    return 返回值
```

例如：

```python
def add(a, b):

    result = a + b

    return result
```

调用：

```python
num = add(10, 20)

print(num)
```

可以理解为：

```text
定义函数
   ↓
传入参数
   ↓
函数处理数据
   ↓
return返回结果
   ↓
调用位置接收结果
```

---

## 十七、今日重点

### 定义函数

```python
def 函数名():
    函数体
```

### 调用函数

```python
函数名()
```

### 带参数的函数

```python
def 函数名(参数):
    函数体
```

调用：

```python
函数名(实参)
```

### 返回一个结果

```python
def test():
    return 结果
```

接收：

```python
result = test()
```

### 返回多个结果

```python
def test():
    return 值1, 值2, 值3
```

接收：

```python
a, b, c = test()
```

### 函数嵌套调用

```python
def a():
    b()


def b():
    print("b")


a()
```

调用遵循：

```text
LIFO
后进先出
```

---

## Day19总结

今天开始学习Python中的函数：

- 了解了函数的基本概念和作用
- 学习了使用 `def` 定义函数
- 学习了函数需要先定义再调用
- 学习了函数的调用方法
- 学习了形参和实参
- 学习了通过参数向函数传递数据
- 学习了使用 `return` 返回函数执行结果
- 学习了函数返回多个值
- 学习了多个返回值会组成元组
- 学习了使用解包接收多个返回值
- 学习了函数说明文档的基本写法
- 学习了函数之间的嵌套调用
- 了解了函数调用的栈结构和LIFO后进先出
- 完成了三角形面积计算函数
- 完成了字符串元音字母统计函数
- 完成了班级成绩最高分、最低分和平均分统计函数
- 综合复习了 `for`、`if`、`in`、列表、字符串、`max()`、`min()`、`sum()`、`len()` 和 `round()`