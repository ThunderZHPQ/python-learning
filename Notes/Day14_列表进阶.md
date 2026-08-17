# Day14 列表进阶

## 一、列表的数据统计

可以使用列表配合 `min()`、`max()`、`sum()`、`len()` 对数据进行统计。

例如：

    num_list = [10, 20, 30, 40, 50]

    print(min(num_list))
    print(max(num_list))
    print(sum(num_list))
    print(len(num_list))

分别表示：

    min() → 获取最小值
    max() → 获取最大值
    sum() → 计算所有元素的总和
    len() → 获取元素数量

平均值可以通过：

    sum(num_list) / len(num_list)

计算。


## 二、通过循环向列表中添加数据

可以先创建一个空列表，然后通过 `append()` 不断添加用户输入的数据。

    num_list = []

    for i in range(10):
        num = int(input("请输入数字"))
        num_list.append(num)

    print(num_list)

这种方式可以将用户输入的多个数据保存到同一个列表中。


## 三、列表排序

使用 `sort()` 可以对列表中的元素进行排序。

    num_list.sort()

默认按照从小到大的顺序排列。

例如：

    num_list = [5, 2, 8, 1, 3]
    num_list.sort()

结果：

    [1, 2, 3, 5, 8]


## 四、列表合并

可以使用 `+` 将两个列表合并。

    num_list1 = [1, 2, 3]
    num_list2 = [4, 5, 6]

    num_list3 = num_list1 + num_list2

结果：

    [1, 2, 3, 4, 5, 6]


## 五、列表解包

解包是将一个容器中的元素拆开，变成一个一个独立的元素。

例如：

    num_list1 = [1, 2, 3]
    num_list2 = [4, 5, 6]

    num_list = [*num_list1, *num_list2]

结果：

    [1, 2, 3, 4, 5, 6]

其中 `*` 可以将列表中的元素解包出来。


## 六、列表去重

列表本身允许存在重复元素。

例如：

    num_list = [1, 2, 2, 3, 3, 4]

可以通过遍历列表，判断元素是否已经存在于新列表中，从而实现去重：

    new_list = []

    for num in num_list:
        if num not in new_list:
            new_list.append(num)

    print(new_list)

结果：

    [1, 2, 3, 4]

其中：

    num not in new_list

用于判断元素是否不存在于列表中。


## 七、列表推导式

列表推导式是一种按照指定规则快速生成列表的方法。

基本语法：

    [要放入列表的值 for i in 序列]

例如生成1~20的平方：

    num_list = [i**2 for i in range(1, 21)]

结果：

    [1, 4, 9, 16, 25, ..., 400]

相当于传统写法：

    num_list = []

    for i in range(1, 21):
        num_list.append(i**2)


## 八、带条件的列表推导式

列表推导式还可以加入 `if` 条件。

基本语法：

    [要放入列表的值 for i in 序列 if 条件]

例如：

    num_list = [0, 2, 12, 32, 45, 77, 80, 92, 33, 57, 97, 98]

    new_list = [i**2 for i in num_list if i % 2 == 0]

这里的执行过程可以理解为：

    遍历num_list
        ↓
    判断当前元素是否为偶数
        ↓
    是偶数 → 计算平方
        ↓
    将平方结果加入新列表

最终得到：

    [0, 4, 144, 1024, 6400, 8464, 9604]


## 九、列表推导式与普通for循环的对比

普通写法：

    new_list = []

    for i in num_list:
        if i % 2 == 0:
            new_list.append(i**2)

列表推导式：

    new_list = [i**2 for i in num_list if i % 2 == 0]

列表推导式可以将多行简单的循环和判断逻辑压缩成一行。


## 十、今日重点

### 列表统计

    min() → 最小值
    max() → 最大值
    sum() → 总和
    len() → 元素数量

### 列表操作

    +       → 合并列表
    *       → 解包列表
    sort()  → 排序
    append() → 添加元素

### 列表判断

    in      → 判断元素是否存在
    not in  → 判断元素是否不存在

### 列表推导式

    [值 for i in 序列]

带条件：

    [值 for i in 序列 if 条件]


## 今日总结

今天继续学习了列表的实际应用。

通过用户输入练习了列表的数据存储和统计，学习了列表合并、解包、排序和去重。

重点学习了列表推导式，掌握了使用列表推导式快速生成列表，以及通过 `if` 条件筛选数据后生成新列表。