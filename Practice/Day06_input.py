from learn_utils import read_int

#input中的字符串会被当作提示信息显示在控制台上，等待用户输入。用户输入的内容会被存储在变量s中，并且可以通过print函数输出。
#input函数的返回值是一个字符串类型，如果需要将输入的内容转换为其他类型，需要使用相应的类型转换函数。
# name = input("请输入一个姓名: ")
# age = input("请输入一个年龄: ")
# print(f"您的姓名是: {name}, 年龄是: {age}")

#模拟银行卡取款

#假设初始余额为10000元
total = 10000

#输入密码
password = input("请输入银行卡密码: ")
print(f"密码正确：{password}")

# #输入取款金额
# withdrawal_amount = float(input("请输入取款金额: "))
# print(f"取款金额: {withdrawal_amount}")

# #计算余额
# # total -= withdrawal_amount
# # print(f"剩余余额: {total}")
# print(f"剩余余额: {total - withdrawal_amount}")

#假设withdrwal_amount为str类型
withdrawal_amount = read_int("请输入取款金额: ")
print(f"剩余余额: {total - withdrawal_amount}")