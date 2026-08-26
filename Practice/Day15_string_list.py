from learn_utils import reverse_text

# # # 介绍：字符串是字符的容器，一个字符串中可以存放任意数量的字符。如："Python" 'Python' ""Python""
# # # 特点：不可变性（无法修改）、有序性、可迭代性。
# # # 字符串中的每一个字符元素都有其对应的下标（索引），通过元素对应的索引，就可以获取到对应的元素。

# # s = "hello_world"
# # print(s[4])
# # print(s[-6])

# # print(s[0:5])#切片
# # print(s[6::])
# # print(s[-1:-6:-1])#步长取负数，可以翻转字符串

# 字符串操作常用方法：
# find() 在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1 s.find('Python')
# count() 统计子串在字符串中出现的次数 s.count('H')
# upper() 将字符串中的所有字母转换为大写 s.upper()
# lower() 将字符串中的所有字母转换为小写 s.lower()
# split() 将字符串按指定分隔符分割成列表 s.split(' ')
# strip() 去除字符串两端的空白字符或指定字符 s.strip() / s.strip('*')
# replace() 将字符串中的指定子串替换为新的子串 s.replace('H','C')
# startswith() /endwith() 检查字符串是否以指定子串开头，返回布尔值 s.startwith('P')/s.endwith('P')

# s = "     Hello-Python-Hello-World         "
# print(s.find('l'))

# print(s.count('l'))

# print(s.upper())

# print(s.lower())

# print(s.split('-'))

# print(s.strip())

# print(s.replace('-','_'))

# print(s.startswith("     Hello"))

# print(s.endswith("Python"))

#邮箱案例，用户输入一个邮箱，要求有一个@和至少一个'.'，如果包含则返回正常，否则返回"邮箱格式错误"

# mail =input("请输入邮箱")
#方式1
# if mail.count("@") == 1 and mail.count(".") >= 1:
#     print(f"{mail}为合法邮箱")
# else:
#     print(f"{mail}为非法邮箱")

#方式2
# if mail.count("@") == 1 and "." in mail:
#     print(f"{mail}为合法邮箱")
# else:
#     print(f"{mail}为非法邮箱")

#练习1：判断输入的字符串是否是回文
# s1 = input("请输入语句:")
# s2 = reverse_text(s1)

# if s1 == s2:
#     print("该段语句为回文")
# else:
#     print("该段语句不是回文")

#练习2：用户输入任意字符串，将其全部反转后转为大写，最后遍历输出
str_list1 = input("请输入任意字符串：")

str_list2 = reverse_text(str_list1)

str_list3 = [str_list2,str_list2.upper()]


print(str_list3)

for i in str_list3:
    print(i)