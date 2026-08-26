# #(元组)tuple一旦定义完成,里面的所有元素都无法修改
# # #tuple可存储不同类型的元素,和list唯一的区别是内部元素不可变

# t1 = (1,2,3,4,5,6,7,8,9,10)

#tuple的常用方法有2个,count()和index(),作用和list方法一样

# print(t1)
# print(type(t1))

# print(t1[-1])
# print(t1[:5:2])

# print(t1.count(5))
# print(t1.index(9))

# # #如果要定义单元素的tuple,需要在单元素后加上","
# # t2 = (100,)
# # print(type(t2))

# #组包：将多个值合并到容器(list,tuple)中
# t1 = 1,2,3,4
# print(t1)
# print(type(t1))

# #基础解包：将容器中的值解开成单独的元素,并分别赋值给各个变量,赋值的数量要匹配
# a,b,c,d = t1
# print(f"{a},{b},{c},{d}")

# #拓展解包
# x,*y,z = t1 #x接受第一个,*y接受中间所有元素,z接受最后一个元素。*y接受的元素会生成list
# print(f"{x},{y},{z}")

# 现有两个变量,分别为：a=10,b=20,现需要将这两个变量值交换,然后输出到控制台。
# a,b = 10,20
# a,b = b,a #相当于t = a,b b,a = t
# print(f"{a} {b}")
# 现有三个变量,分别为：a=100,b=200,c=300,现需要将这三个变量值进行交换,将a,b,c的值分别赋值给c,a,b,并将其输出到控制台。
# a,b,c = 100,200,300
# print(f"{a} {b} {c}")
# c,a,b = a,b,c
# print(f"{a} {b} {c}")


# 根据如下提供的学生成绩单,完成如下需求：


# students =(
# ("S001","王林",85,92,78),
# ("S002","李慕婉",92,88,95),
# ("S003","十三",78,85, 82),
# ("S004","曾牛",88, 79, 91),
# ("S005","周轶",95,96, 89),
# ("S006","王卓",76, 82,77),
# ("S007","红蝶",89,91,94),
# ("S008","徐立国",75, 69,82),
# ("S009","许木",86,89, 98),
# ("S010","遁天",66,59,72)
# )

# 1。计算每个学生的总分、各科平均分,然后一并输出出来。
# 方式1：经典写法
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avg = total/3
#     print(f"学号：{s[0]}\t姓名：{s[1]}\t总分：{total}\t平均分：{avg:.1f}")

#方式2：通过元组解包进行赋值
# for id,name,chinese,math,english in students:
#     total = chinese + math + english
#     avg = total/3
#     print(f"学号：{id}\t姓名：{name}\t语文：{chinese}\t数学：{math}\t英语：{english}\t总分：{total}\t平均分：{avg:.1f}")

# 2.统计各科成绩的最低分、最高分、平均分,并输出。
# chinese_score = [s[2] for s in students]
# print(sorted(chinese_score))
# math_score = [s[3] for s in students]
# print(sorted(math_score))
# english_score = [s[4] for s in students]
# print(sorted(english_score))

# print(f"语文最高分为{max(chinese_score)},最低分为{min(chinese_score)}")
# print(f"数学最高分为{max(math_score)},最低分为{min(math_score)}")
# print(f"英语最高分为{max(english_score)},最低分为{min(english_score)}")

# print(f"语文平均分为{sum(chinese_score)/len(chinese_score)}")
# print(f"数学平均分为{sum(math_score)/len(math_score)}")
# print(f"英语平均分为{sum(english_score)/len(english_score)}")

# 3.查找成绩优秀(平均分大于90)的学生,并输出

# 方式1：经典写法
# print("优秀学生名单如下")
# print()
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avg = total/3
#     if avg > 90:
#         print(f"学号：{s[0]}\t姓名：{s[1]}\t总分：{total}\t平均分：{avg:.1f}")

#方式2：通过元组解包进行赋值
# print("优秀学生名单如下")
# for id,name,chinese,math,english in students:
#     total = chinese + math + english
#     avg = total/3
#     if avg > 90:
#          print(f"学号：{id}\t姓名：{name}\t总分：{total}\t平均分：{avg:.1f}")