from learn_utils import check_login, read_int

#if 条件判断的基础类型
# score = 695
# if score >= 680:#注意，在if语句中，冒号是必须的，表示条件判断的开始，缩进表示条件成立时执行的代码块。
#     print("恭喜你，考上了清华大学")
# else:
#     print("很遗憾，你没有考上清华大学")

#缩进代表条件成立时执行的代码块，缩进的空格数可以是任意的，但必须保持一致，通常使用4个空格作为一个缩进层级。
# input_score = read_int("请输入你的高考分数: ")
# if input_score >= 680:
#     print("恭喜你，考上了清华大学")
# else:
#     print("很遗憾，你没有考上清华大学")

#模拟账号密码登录，要求用户输入账号和密码，如果账号和密码都正确，则提示登录成功，否则提示登录失败。
# accounts = {"2678324880": "123456"}
# input_account = input("请输入账号: ")
# input_password = input("请输入密码: ")
# if check_login(input_account, input_password, accounts):
#     print("登录成功")
# else:
#     print("登录失败")

#根据输入的年份判断是否为闰年，闰年的条件是：能被4整除但不能被100整除，或者能被400整除。
year = read_int("请输入年份: ")
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")