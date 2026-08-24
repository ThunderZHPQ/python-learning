# Day18 字典（dict）

## 一、字典的基本概念

Python中的字典（dict）是一种用于存储键值对（key:value）的数据容器，可以根据key找到对应的value。

字典的主要特点：

- 以 `key:value` 键值对的形式存储数据
- key不能重复，如果重复，后面的value会覆盖前面的value
- 字典没有索引下标，不能像列表一样通过索引获取数据
- 可以通过key获取对应的value
- 字典可以修改
- value可以是任意类型的数据
- key不能使用可变类型，例如list、set、dict

例如：

```python
dict1 = {
    "zhang": 670,
    "wang": 684,
    "li": 703,
    "zhang": 750
}

print(dict1)
print(dict1["wang"])
```

因为 `"zhang"` 重复，所以后面的750会覆盖前面的670。


## 二、创建字典

普通字典：

```python
dict1 = {
    "小智": 675,
    "李思": 608
}
```

创建空字典：

```python
dict2 = {}
dict3 = dict()
```


## 三、根据key获取value

可以直接通过key获取value：

```python
dict1 = {
    "小智": 675,
    "李思": 608
}

print(dict1["小智"])
```

也可以使用 `get()`：

```python
print(dict1.get("小智"))
```

两种方式的区别：

- `dict1[key]`：key不存在时会产生 `KeyError`
- `dict1.get(key)`：key不存在时默认返回 `None`

因此在不确定key是否存在时，可以使用：

```python
dict1.get(key)
```


## 四、字典的添加和修改

字典添加和修改元素使用相同的语法：

```python
字典[key] = value
```

如果key不存在，则添加：

```python
dict1["小张"] = 687
```

如果key已经存在，则修改value：

```python
dict1["小张"] = 666
```

可以理解为：

```text
key不存在 → 添加

key存在 → 修改
```


## 五、字典的删除

### 1. pop()

删除指定key，并返回该key对应的value：

```python
score = dict1.pop("小张")

print(dict1)
print(score)
```

### 2. del

直接删除指定的键值对：

```python
del dict1["小智"]
```

区别：

```text
pop() → 删除并可以得到返回值

del   → 直接删除，没有返回值
```


## 六、字典常用方法

### keys()

获取所有key：

```python
dict1.keys()
```

### values()

获取所有value：

```python
dict1.values()
```

### items()

获取所有key-value键值对：

```python
dict1.items()
```

例如：

```python
dict1 = {
    "小智": 675,
    "李思": 608
}

print(dict1.keys())
print(dict1.values())
print(dict1.items())
```


## 七、遍历字典

可以使用 `items()` 同时遍历key和value：

```python
dict1 = {
    "小智": 675,
    "李思": 608
}

for k, v in dict1.items():
    print(f"{k},{v}")
```

其中：

```text
k → key
v → value
```

也可以只遍历key：

```python
for k in dict1.keys():
    print(k)
```


## 八、判断key是否存在

使用 `in` 判断key是否存在：

```python
if "小智" in dict1:
    print("key存在")
```

使用 `not in` 判断key是否不存在：

```python
if "小张" not in dict1:
    print("key不存在")
```

注意：

```python
"小智" in dict1
```

判断的是字典中的 **key**，不是value。


## 九、字典value的解包

字典中的value可以是列表。

例如：

```python
shopping = {
    "香蕉": [10, 1.98]
}
```

使用 `items()` 遍历时，可以直接进行解包：

```python
for name, [quantity, cost] in shopping.items():
    print(f"商品名称：{name}")
    print(f"商品数量：{quantity}")
    print(f"商品价格：{cost}")
```

`shopping.items()` 中的一条数据可以理解为：

```python
("香蕉", [10, 1.98])
```

经过解包后：

```text
name = "香蕉"

quantity = 10

cost = 1.98
```


## 十、嵌套字典

字典中的value还可以是另一个字典。

例如：

```python
shopping = {
    "香蕉": {
        "price": 1.98,
        "num": 10
    }
}
```

获取香蕉的全部商品信息：

```python
print(shopping["香蕉"])
```

得到：

```python
{
    "price": 1.98,
    "num": 10
}
```

继续获取价格：

```python
print(shopping["香蕉"]["price"])
```

获取数量：

```python
print(shopping["香蕉"]["num"])
```

嵌套字典相比：

```python
"香蕉": [10, 1.98]
```

这种写法更加清楚，因为：

```python
"price"
"num"
```

可以直接表示数据的含义。


## 十一、购物车管理系统

本次练习使用嵌套字典保存购物车信息：

```python
shopping = {
    "香蕉": {
        "price": 1.98,
        "num": 10
    }
}
```

需要实现：

1. 添加商品
2. 修改商品
3. 删除商品
4. 查询商品
5. 退出购物车


### 1. 添加商品

首先输入商品名称：

```python
name = input("请输入需要添加的商品名称：")
```

判断商品是否存在：

```python
if name in shopping:
    print("该商品已存在")
    continue
```

如果不存在，则添加：

```python
quantity = input("请输入商品的数量：")
cost = input("请输入商品的价格：")

shopping[name] = {
    "price": cost,
    "num": quantity
}

print("商品添加成功")
```

这里：

```python
shopping[name] = {...}
```

实际上是在向外层字典添加一个新的键值对。


### 2. 修改商品

```python
name = input("请输入需要修改的商品名称：")

if name in shopping:
    quantity = input("请输入商品的数量：")
    cost = input("请输入商品的价格：")

    shopping[name] = {
        "price": cost,
        "num": quantity
    }

    print("商品修改成功")
else:
    print("库存中没有该商品")
```

因为key已经存在：

```python
shopping[name] = {...}
```

此时执行的是修改操作。


### 3. 删除商品

```python
name = input("请输入需要删除的商品名称：")

if name in shopping:
    del shopping[name]
    print("商品已删除")
else:
    print("库存中没有该商品")
```


### 4. 查询商品

可以先遍历商品名称：

```python
for name in shopping.keys():
    shopping_info = shopping[name]

    print(
        f"商品名称：{name},"
        f"商品数量：{shopping_info['num']},"
        f"商品价格：{shopping_info['price']}"
    )
```

这里：

```python
shopping_info = shopping[name]
```

获取到的是内层字典：

```python
{
    "price": 1.98,
    "num": 10
}
```

然后：

```python
shopping_info["num"]
shopping_info["price"]
```

分别获取数量和价格。

也可以直接使用 `items()`：

```python
for name, shopping_info in shopping.items():
    print(
        f"商品名称：{name},"
        f"商品数量：{shopping_info['num']},"
        f"商品价格：{shopping_info['price']}"
    )
```


## 十二、购物车案例中用到的旧知识

本次购物车案例不仅使用了字典，还综合使用了之前学习的内容：

```text
while True
    ↓
保持购物车程序持续运行

match-case
    ↓
根据用户输入选择不同功能

if
    ↓
判断商品是否存在

in
    ↓
判断字典中是否存在指定key

continue
    ↓
结束本次循环，重新选择操作

break
    ↓
退出购物车程序

for
    ↓
遍历购物车中的商品
```


## 十三、今日重点

字典基本格式：

```python
dict1 = {
    key: value
}
```

根据key获取value：

```python
dict1[key]
dict1.get(key)
```

添加和修改：

```python
dict1[key] = value
```

删除：

```python
dict1.pop(key)

del dict1[key]
```

获取字典数据：

```python
dict1.keys()
dict1.values()
dict1.items()
```

判断key：

```python
key in dict1

key not in dict1
```

遍历：

```python
for key, value in dict1.items():
    print(key, value)
```

嵌套字典：

```python
shopping = {
    "香蕉": {
        "price": 1.98,
        "num": 10
    }
}
```


## Day18总结

今天学习了Python字典 `dict`：

- 理解了字典的key-value键值对结构
- 学习了字典的创建方式
- 学习了根据key获取value
- 学习了字典的添加、修改和删除
- 学习了 `keys()`、`values()`、`items()` 等常用方法
- 学习了字典的遍历
- 学习了使用 `in` 和 `not in` 判断key是否存在
- 学习了字典value的解包
- 学习了嵌套字典
- 使用字典完成了购物车管理系统
- 综合练习了 `while`、`match-case`、`if`、`for`、`continue` 和 `break`