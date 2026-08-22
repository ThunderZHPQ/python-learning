from learn_utils import dedupe, describe_numbers, read_int_list

# 将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值。

# num_list = read_int_list(10, "请输入数字")
# print(num_list)

# num_list.sort()#排序
# print(num_list)

# lowest, highest, avg = describe_numbers(num_list)
# print(f"最小值为{lowest}")
# print(f"最大值为{highest}")
# print(f"平均值为{avg}")
    
# 合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）。
# num_list1 = [19,23,54,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]


# 1，合并列表
#解包：将列表这一类容器解开成一个一个独立的元素
#组包：将多个值合并到一个容器
# num_list =[*num_list1,*num_list2]
# num_list.sort()
# print(num_list)

# num_list3 = num_list1 + num_list2 #列表合并
# num_list3.sort()
# print(num_list3)

# #去重复
# new_list = dedupe(num_list3) #保留首次出现的顺序，去除重复元素
# new_list.sort()
# print(new_list)

#生成1-20的平方列表。
#传统方式
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)

# print(num_list)

# 方式二：列表推导式--->就是按照一定的规则快速生成一个列表的方法-->语法格式1：[要插入的值 for i in 序列/列表]
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)

# 从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表。
num_list = [0,2,12,32,45,77,80,92,33,57,97,98]

#列表推导式--->就是按照一定的规则快速生成一个列表的方法-->语法格式2：[要插入的值 for i in 序列/列表 if 条件]
new_list = [i**2 for i in num_list if i%2 == 0]
print(new_list)