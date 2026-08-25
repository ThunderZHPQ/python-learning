# 函数是组织好的、可重复使用的、用来实现特定功能的代码片段。
# 函数一定是先定义,后调用

# # 定义函数 
# def out_line():
#     print("------------")

# # 调用函数
# out_line()

# 计算圆的面积
#形参与实参的数量要一致

# def circle_area(r):
#     area = 3.14 * r * r
#     return area

# c_area = circle_area(3)
# print(c_area)

# # 函数2：计算长方形的面积--长,宽
# def rectangle_area(l,w):
#     '''
#     根据长宽计算长方形的面积
#     :param l:长度
#     :param w:宽度
#     :return:长方形面积
#     '''
#     area = l * w
#     return area

# r_rectangle = rectangle_area(5,10)
# print(r_rectangle)

# #函数3：计算圆的面积,周长--半径---->如果返回值有多个,多个返回值之间逗号分隔。多个返回值会封装到元组之中
# def circle_area_len(r):
#     '''
#     根据圆的半径,计算圆的面积和周长
#     :param r:半径
#     :return：圆的面积,圆的周长
#     '''
#     return round(3.14 *r*r,1),round(2 *3.14 *r,1)

# a_area = circle_area_len(10)
# print(a_area)

# # 解包提取返回值
# area,lens = circle_area_len(10)
# print(area,lens)

# 嵌套调用指的是在一个函数中,又调用了另外一个函数。
# 函数调用遵循栈结构,最后被调用的函数最先返回LIFO（LastInFirstOut,后进先出）
# def function_a():
#     print("a ...before")
#     function_b()
#     print("a ... after")

# def function_b():
#     print("b.... before")
#     function_c()
#     print("b..after")

# def function_c():
#     print("c...")

# function_a()





# 定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积=底*高／2）。
# def triangle(l,d):
#     return round(l*d/2,1)

# area_triangle = triangle(3,6)
# print(area_triangle)

# 定义一个函数：计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）。
# def strings(s):
#     num = 0
#     for i in s:
#         if i in "aeiouAEIOU":
#             num+=1
#     return num

# vowel = strings(input("请输入字符串："))
# print(f"元音字母的数量为：{vowel}")

# 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数）,并返回。
def calc_score(score_list):
    '''
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
    :param score_list：分数列表
    :return：最高分,最低分,平均分
    '''
    max_s =max(score_list)
    min_s = min(score_list)
    avg_s =round(sum(score_list)/len(score_list),1)
    return max_s, min_s, avg_s

s_list =[589,609,605,643,677,455,477,489,503]
max_score, min_score,avg_score = calc_score(s_list)
print(max_score, min_score,avg_score)