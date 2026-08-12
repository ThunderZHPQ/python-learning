"""
#while基础语法 输出10遍：while基础语法
i = 0
while i < 10:
    print("whlie循环语法")
    i += 1
else:
    print("循环结束")


#用while循环计算1~100之间的所有偶数和
total = 0
num = 1
while num <= 100:

    if num % 2 == 0:

        total += num
    num += 1

print(f"1~100之间的偶数和为{total}")


#定义要遍历的字符串
msg = input("请输入需要遍历的字符串")

for i in msg:

    print(f"遍历元素{i}")
else: 
    print("遍历结束")

# #for循环与while循环的场景
# While循环
# 用于在某个条件满足时一直循环，循环的次数通常是未知的，只知道循环开始结束的条件。关注的是循环的条件
# for循环：
# 用于对一个已知的数据集进行遍历或已知次数的循环。关注的是遍历每一个元素


#range语句，生成指定规则的数列
#range(end),获取到0到end的数列,不含end本身
# range(5),生成0,1,2,3,4
# #range(start,end)，获取从start到end的数列，不含end
# range(1,5),生成1,2,3,4
# #range(start,end,step)获取一个从start开始，到end结束的数字序列，step为步长（不含end本身）
# range(0,10,2),生成0,2,4,6,8

#用for循环计算1-100之间所有奇数的累加和
total = 0
for i in range(1,100,2):
    total += i
print(f"1-100之间的奇数和为{total}")
"""

#计算100-500之间所有3的倍数的和
total = 0
for i in range(100,501):
    if i % 3 == 0:
        total += i
print(f"100-500之间所有3的倍数的和是{total}")