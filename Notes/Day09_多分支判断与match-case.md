# Day09 Python多分支判断与match-case


# 1. elif 多分支判断

之前学习的：

```python
if 条件:
    执行代码
else:
    执行代码
```

只能处理两种情况。

如果需要判断多个情况，可以使用：

```python
if 条件1:
    执行代码1
elif 条件2:
    执行代码2
else:
    执行代码3
```


---

## 示例：判断数字正负

```python
num = float(input("请输入一个数字: "))

if num > 0:
    print("这是一个正数。")
elif num < 0:
    print("这是一个负数。")
else:
    print("这是零。")
```

判断流程：

```text
num > 0 ?
   ↓
是 → 正数

否
 ↓

num < 0 ?
   ↓
是 → 负数

否
 ↓

零
```


---

# 2. if嵌套

一个 `if` 中可以继续使用 `if`。

例如：

```python
if 条件1:
    if 条件2:
        执行代码
```

这种结构叫：

> if嵌套


---

# 3. 三角形判断案例

三条边能够组成三角形，需要满足：

```text
a + b > c
a + c > b
b + c > a
```

同时边长必须大于0。


Python：

```python
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
```

满足条件后，再进一步判断三角形类型。


---

## 等边三角形

三条边都相等：

```python
if a == b == c:
    print("这是一个等边三角形。")
```


---

## 等腰三角形

至少两条边相等：

```python
elif a == b or b == c or a == c:
    print("这是一个等腰三角形。")
```


---

## 不等边三角形

三条边都不相等：

```python
else:
    print("这是一个不等边三角形。")
```


整体逻辑：

```text
能否组成三角形？
        ↓
       是
        ↓
三边是否相等？
   ↓          ↓
  是          否
等边      是否有两边相等？
              ↓
          是       否
          ↓        ↓
        等腰     不等边
```


---

# 4. pass 占位语句

有时候已经确定需要编写一个代码块，但是暂时还没有想好具体内容。

可以使用：

```python
pass
```

例如：

```python
if condition:
    pass
```

`pass` 的作用：

> 什么都不做，仅用于占位。

注意：

`pass` 不会产生任何实际操作。


---

# 5. match-case 模式匹配

Python 3.10开始支持：

```python
match
case
```

可以用于根据某个变量的不同值执行不同代码。


基本结构：

```python
match 变量:
    case 值1:
        执行代码
    case 值2:
        执行代码
    case _:
        默认情况
```


其中：

```python
_
```

表示其他没有匹配到的情况。


---

# 6. match-case判断工作日

例如：

```python
day = input("请输入星期: ")

match day:
    case "星期一" | "星期二" | "星期三" | "星期四" | "星期五":
        print(f"{day} 是工作日。")

    case "星期六" | "星期日":
        print(f"{day} 是休息日。")

    case _:
        print("输入的值不合法")
```

其中：

```python
|
```

表示多个匹配条件。

例如：

```python
case "星期六" | "星期日":
```

表示：

匹配星期六或者星期日。


---

# 7. match-case中的条件判断

`case` 后面还可以增加条件。


例如：

```python
case "/" if num2 != 0:
```

表示：

当运算符是 `/`

并且：

```python
num2 != 0
```

时才执行该分支。


这可以避免：

```python
num1 / 0
```

导致除零错误。


---

# 8. match-case实现计算器

示例：

```python
num1 = float(input("请输入第一个数字: "))
oper = input("请输入运算符号: ")
num2 = float(input("请输入第二个数字: "))

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")

    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")

    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")

    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")

    case _:
        print("操作不支持")
```

程序流程：

```text
输入第一个数字
        ↓
输入运算符
        ↓
输入第二个数字
        ↓
match判断运算符
        ↓
执行对应计算
        ↓
输出结果
```


---

# 9. if 和 match-case 的区别

两者都可以实现分支判断，但是适用场景不同。


## if

适合：

- 范围判断
- 大小比较
- 复杂逻辑
- 多个条件组合

例如：

```python
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```


这种情况下使用 `if` 更合适。


---

## match-case

适合：

> 根据一个变量的多个固定值进行匹配。


例如：

```python
match oper:
    case "+":
        ...
    case "-":
        ...
    case "*":
        ...
```


这种情况下 `match-case` 比大量 `if-elif` 更直观。


---

# 10. 今日知识对比

|语法|主要用途|
|---|---|
|if|条件判断|
|elif|多个条件分支|
|else|其他情况|
|嵌套if|多层条件判断|
|pass|占位，不执行操作|
|match-case|固定值模式匹配|

---

# 今日总结

今天学习：

- `elif` 多分支判断
- `if` 嵌套
- `pass` 占位语句
- `match-case` 模式匹配
- `case _` 默认匹配
- `case` 条件判断
- `if` 和 `match-case` 的使用场景

重点：

### 多分支

```python
if 条件1:
    ...
elif 条件2:
    ...
else:
    ...
```


### 嵌套判断

```python
if 条件1:
    if 条件2:
        ...
```


### 模式匹配

```python
match value:
    case 1:
        ...
    case 2:
        ...
    case _:
        ...
```
