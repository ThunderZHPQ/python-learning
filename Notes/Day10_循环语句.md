# Day10 Python循环语句


# 1. while循环

`while` 用于在条件满足时重复执行代码。

基本语法：

```python
while 条件:
    执行代码
```

例如：

```python
i = 0

while i < 10:
    print("while循环语法")
    i += 1
```

执行过程：

```text
i = 0
 ↓
判断 i < 10
 ↓
条件成立
 ↓
执行循环体
 ↓
i += 1
 ↓
再次判断
 ↓
...
```

当：

```python
i < 10
```

变成 `False` 时，循环结束。


---

# 2. while循环中的计数器

使用 `while` 循环时，如果希望循环最终结束，通常需要改变判断条件中的变量。

例如：

```python
i = 0

while i < 10:
    print(i)
    i += 1
```

这里：

```python
i += 1
```

非常重要。

如果没有这一句：

```python
i
```

一直保持 `0`，那么：

```python
i < 10
```

永远成立，程序就会陷入无限循环。

所以使用 `while` 时要特别注意：

> 必须保证循环条件最终有机会变成 `False`。


---

# 3. while-else

Python中的 `while` 可以和 `else` 配合使用。

```python
while 条件:
    循环代码
else:
    循环结束后执行的代码
```

例如：

```python
i = 0

while i < 10:
    print("while循环语法")
    i += 1
else:
    print("循环结束")
```

当 `while` 正常结束后，会执行 `else`。


---

# 4. while计算1~100的偶数和

```python
total = 0
num = 1

while num <= 100:

    if num % 2 == 0:
        total += num

    num += 1

print(f"1~100之间的偶数和为{total}")
```

这里使用：

```python
num % 2 == 0
```

判断数字是否为偶数。

其中：

```python
%
```

是取余运算符。

如果一个数字除以2余数为0：

```text
偶数
```

否则：

```text
奇数
```


---

# 5. for循环

`for` 循环主要用于：

> 遍历一个已知的数据集，或者执行指定次数的循环。

基本语法：

```python
for 变量 in 数据:
    执行代码
```

例如遍历字符串：

```python
msg = input("请输入需要遍历的字符串")

for i in msg:
    print(f"遍历元素{i}")
```

如果输入：

```text
Python
```

会依次得到：

```text
P
y
t
h
o
n
```

也就是说：

> `for` 会依次取出数据中的每一个元素。


---

# 6. for-else

`for` 也可以和 `else` 配合：

```python
for i in data:
    执行代码
else:
    print("遍历结束")
```

当 `for` 循环正常结束后，会执行 `else`。


---

# 7. while和for的区别

## while

关注：

> 条件是否满足。

适合：

- 循环次数未知
- 根据某个条件持续执行
- 用户输入验证
- 持续运行的程序

例如：

```python
while password != correct_password:
    password = input("请输入密码")
```


## for

关注：

> 遍历每一个元素。

适合：

- 遍历字符串
- 遍历列表
- 遍历字典
- 遍历其他数据
- 已知循环次数

例如：

```python
for item in data:
    print(item)
```


简单理解：

```text
while → 满足条件就一直做

for   → 把数据一个一个拿出来处理
```


---

# 8. range()

`range()` 用于生成指定规则的整数序列。

基本形式：

```python
range(end)
range(start, end)
range(start, end, step)
```

注意：

> `end` 不包含在结果中。


---

## range(end)

例如：

```python
range(5)
```

生成：

```text
0
1
2
3
4
```

不包含 `5`。


---

## range(start, end)

例如：

```python
range(1, 5)
```

生成：

```text
1
2
3
4
```

不包含 `5`。


---

## range(start, end, step)

例如：

```python
range(1, 10, 2)
```

生成：

```text
1
3
5
7
9
```

其中：

```text
start = 1
end = 10
step = 2
```

表示从1开始，每次增加2。


注意：

`range()` 的三个参数分别是：

```text
开始值
结束值
步长
```

结束值始终不包含。


---

# 9. for + range()

`range()` 经常和 `for` 一起使用。

例如：

```python
for i in range(5):
    print(i)
```

结果：

```text
0
1
2
3
4
```


这种写法经常用于：

> 执行固定次数的循环。


例如：

```python
for i in range(10):
    print("Hello")
```

会输出10次 `Hello`。


---

# 10. 计算1~100的奇数和

```python
total = 0

for i in range(1, 100, 2):
    total += i

print(f"1-100之间的奇数和为{total}")
```

这里：

```python
range(1, 100, 2)
```

生成：

```text
1
3
5
7
...
99
```

所以可以直接遍历所有奇数。


---

# 11. 计算100~500之间所有3的倍数

```python
total = 0

for i in range(100, 501):

    if i % 3 == 0:
        total += i

print(f"100-500之间所有3的倍数的和是{total}")
```

这里：

```python
i % 3 == 0
```

用于判断 `i` 是否能够被3整除。

注意：

这里使用：

```python
range(100, 501)
```

而不是：

```python
range(100, 500)
```

因为 `range()` 不包含结束值。

如果想让500也参与判断，就需要写：

```python
range(100, 501)
```


---

# 12. 今日知识总结

今天学习了：

- `while` 循环
- `while-else`
- `for` 循环
- `for-else`
- `range()`
- `range(start, end)`
- `range(start, end, step)`
- 循环条件
- 循环计数器
- 使用循环进行累加计算


## while

```python
while 条件:
    执行代码
```

特点：

> 根据条件循环，循环次数通常不确定。


## for

```python
for i in 数据:
    执行代码
```

特点：

> 遍历数据或者执行指定次数的循环。


## range

```python
range(start, end, step)
```

注意：

> `end` 不包含。


---

# 今日重点

### while

```python
i = 0

while i < 10:
    print(i)
    i += 1
```


### for

```python
for i in data:
    print(i)
```


### range

```python
for i in range(1, 10):
    print(i)
```
