# Day15 字符串

## 一、字符串的基本特点

字符串是一种字符容器，可以存放任意数量的字符。

例如：

    s1 = "Python"
    s2 = 'Python'

字符串的主要特点：

- 不可变性：字符串创建后，不能直接修改其中的某一个字符
- 有序性：字符串中的字符按照一定顺序排列
- 可迭代性：可以使用 `for` 循环依次访问其中的字符

字符串中的每一个字符都有对应的索引。


## 二、字符串索引

字符串可以通过索引获取指定位置的字符。

例如：

    s = "hello_world"

    print(s[4])
    print(s[-6])

正向索引从 `0` 开始：

    h e l l o _ w o r l d
    0 1 2 3 4 5 6 7 8 9 10

反向索引从 `-1` 开始：

    h  e  l  l  o  _  w  o  r  l  d
   -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


## 三、字符串切片

字符串支持切片操作。

基本语法：

    字符串[开始索引:结束索引:步长]

注意：

- 开始索引包含
- 结束索引不包含
- 开始索引省略时默认为0
- 结束索引省略时默认到字符串末尾
- 步长省略时默认为1

例如：

    s = "hello_world"

    print(s[0:5])

结果：

    hello

也可以省略开始或结束索引：

    print(s[6:])

表示从索引6开始，一直到字符串末尾。


## 四、反向切片

切片的步长可以设置为负数，从而实现反向读取。

例如：

    s = "hello_world"

    print(s[-1:-6:-1])

也可以使用：

    s[::-1]

将整个字符串反转。

例如：

    s = "Python"

    print(s[::-1])

结果：

    nohtyP


## 五、字符串常用方法

### 1. find()

查找子字符串第一次出现的位置。

    s = "Hello-Python-Hello-World"

    print(s.find("Python"))

如果找不到，返回 `-1`。


### 2. count()

统计指定子字符串出现的次数。

    s = "Hello-Python-Hello-World"

    print(s.count("l"))


### 3. upper()

将字符串中的英文字母全部转换为大写。

    s = "Hello Python"

    print(s.upper())


### 4. lower()

将字符串中的英文字母全部转换为小写。

    s = "Hello Python"

    print(s.lower())


### 5. split()

按照指定的分隔符，将字符串拆分成列表。

    s = "Hello-Python-Hello-World"

    print(s.split("-"))

结果：

    ["Hello", "Python", "Hello", "World"]


### 6. strip()

去除字符串两端的空白字符，也可以指定需要去除的字符。

    s = "    Hello Python    "

    print(s.strip())

也可以：

    s = "***Hello Python***"

    print(s.strip("*"))

注意：`strip()`只处理字符串两端，不会删除中间的字符。


### 7. replace()

将字符串中的指定内容替换成新的内容。

    s = "Hello-Python-Hello-World"

    print(s.replace("-", "_"))

结果：

    Hello_Python_Hello_World


### 8. startswith()

判断字符串是否以指定内容开头。

返回值为 `True` 或 `False`。

    s = "Hello Python"

    print(s.startswith("Hello"))


### 9. endswith()

判断字符串是否以指定内容结尾。

返回值为 `True` 或 `False`。

    s = "Hello Python"

    print(s.endswith("Python"))


## 六、字符串不可变性

字符串属于不可变类型。

例如：

    s = "Python"

不能直接通过索引修改：

    s[0] = "p"

这种操作会产生错误。

如果需要得到修改后的字符串，需要创建一个新的字符串。

例如：

    s = "Python"
    s = "python"

这里实际上是让变量 `s` 指向了一个新的字符串。


## 七、邮箱格式判断

可以利用字符串的 `count()` 和 `in` 来进行简单的邮箱格式判断。

例如要求：

- 必须有且只有一个 `@`
- 至少包含一个 `.`

写法一：

    mail = input("请输入邮箱")

    if mail.count("@") == 1 and mail.count(".") >= 1:
        print(f"{mail}为合法邮箱")
    else:
        print(f"{mail}为非法邮箱")

也可以使用：

    if mail.count("@") == 1 and "." in mail:
        print(f"{mail}为合法邮箱")
    else:
        print(f"{mail}为非法邮箱")

这里：

    in

可以判断某个元素是否存在于字符串中。


## 八、判断回文字符串

回文是指正向读取和反向读取结果相同的字符串。

例如：

    上海自来水来自海上

判断方法：

    s1 = input("请输入语句：")
    s2 = s1[::-1]

    if s1 == s2:
        print("该段语句为回文")
    else:
        print("该段语句不是回文")

核心思路：

    原字符串
        ↓
    使用 [::-1] 反转
        ↓
    与原字符串进行比较
        ↓
    相同 → 回文
    不同 → 不是回文


## 九、字符串反转与大小写转换

可以先将字符串反转，再转换成大写。

    str_list1 = input("请输入任意字符串：")

    str_list2 = str_list1[::-1]

    str_list3 = [str_list2, str_list2.upper()]

    print(str_list3)

    for i in str_list3:
        print(i)

这里综合使用了：

    [::-1]       → 字符串反转
    upper()      → 转换为大写
    []           → 创建列表
    for          → 遍历列表


## 十、今日重点

### 字符串基本特点

    不可变
    有序
    可迭代

### 索引

    正向索引 → 从0开始
    反向索引 → 从-1开始

### 切片

    s[开始:结束:步长]

反转字符串：

    s[::-1]

### 常用字符串方法

    find()       → 查找子字符串
    count()      → 统计出现次数
    upper()      → 转换为大写
    lower()      → 转换为小写
    split()      → 分割成列表
    strip()      → 去除两端字符
    replace()    → 替换字符串
    startswith() → 判断开头
    endswith()   → 判断结尾


## 今日总结

今天学习了字符串这种数据容器，掌握了字符串的索引、切片和反向切片操作，并学习了常用的字符串处理方法。

通过邮箱格式判断、回文判断以及字符串反转等练习，将字符串的索引、切片、条件判断、列表和循环等知识进行了综合运用。