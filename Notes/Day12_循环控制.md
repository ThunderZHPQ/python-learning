# 循环控制与综合练习

## 一、break

`break` 用于立即结束当前循环。

只能在循环中使用。

例如：

    while True:
        num = int(input("请输入数字："))

        if num == 10:
            print("猜对了")
            break

当满足条件时执行 `break`，循环立即结束。

常用于：

- 登录成功后结束循环
- 游戏结束后退出循环
- 找到目标后结束循环


## 二、continue

`continue` 用于跳过本次循环剩余的代码，直接进入下一次循环。

例如：

    while True:
        username = input("请输入账号：")

        if username == "":
            print("账号不能为空")
            continue

        print("账号输入正确")

当输入为空时：

    continue

会跳过本次循环后面的代码，重新开始下一次循环。

区别：

    break     → 结束整个循环
    continue  → 跳过本次循环，进入下一次循环


## 三、使用while实现登录功能

需求：

- 用户名和密码正确才能登录成功
- 登录失败后继续输入
- 用户名或密码不能为空
- 登录成功后结束程序

示例：

    while True:
        username = input("请输入账号：")
        password = input("请输入密码：")

        if username == "" or password == "":
            print("账号或密码不能为空")
            continue

        if username == "admin" and password == "666888":
            print("登录成功，进入B站首页~")
            break
        elif username == "zhangsan" and password == "123456":
            print("登录成功，进入B站首页~")
            break
        elif username == "taoge" and password == "888666":
            print("登录成功，进入B站首页~")
            break
        else:
            print("用户名或密码错误，请重新输入！")

程序执行逻辑：

    while True
        ↓
    输入用户名和密码
        ↓
    判断是否为空
        ↓
    为空 → continue，重新输入
        ↓
    判断用户名和密码是否正确
        ↓
    正确 → break，结束循环
        ↓
    错误 → 提示错误，重新输入


## 四、random模块

Python可以通过 `random` 模块生成随机数。

首先导入：

    import random

使用：

    random.randint(1, 100)

表示生成一个 `1~100` 之间的随机整数。

例如：

    import random

    random_num = random.randint(1, 100)

每次运行程序时，`random_num` 都可能得到不同的数字。


## 五、猜数字小游戏

游戏逻辑：

- 系统随机生成一个1~100之间的数字
- 用户输入自己猜的数字
- 如果猜小了，提示“数字小了”
- 如果猜大了，提示“数字大了”
- 猜对后结束游戏

代码：

    import random

    random_num = random.randint(1, 100)

    while True:
        num = int(input("请输入猜的数字"))

        if random_num > num:
            print("您输入的数字小了")

        elif random_num < num:
            print("您输入的数字大了")

        else:
            print("恭喜您猜对了")
            break


## 六、今日重点

### break

    break

立即结束整个循环。

### continue

    continue

跳过本次循环，进入下一次循环。

### random.randint()

    random.randint(1, 100)

生成1~100之间的随机整数。


## 七、break和continue的区别

    break
    ↓
    直接结束整个循环

    continue
    ↓
    跳过本次循环
    ↓
    进入下一次循环


## 今日总结

今天学习了 `break` 和 `continue` 两个循环控制语句，并结合 `while`、`if`、`input()` 完成了反复登录功能。

同时学习了 `random` 模块和 `random.randint()`，通过猜数字小游戏练习了随机数、条件判断、循环以及 `break` 的综合使用。