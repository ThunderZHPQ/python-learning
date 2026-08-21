#set（集合）是一种无序的,不可重复的,可修改的数据容器
#set集合会自动去重,无法存储重复的数据

# s1 = {"A","B","C","D","A"}
# #定义空集合
# s2 = set()
# print(s1)
# print(type(s1))

#set常用方法：
#add() 添加元素
#remove() 移除元素,注意,元素不存在会报错
#pop() 随机删除元素并返回
#clear() 清空集合
#different() 求两个集合的差集（包含第一个集合的元素但不包含第二个集合的元素）
#union() 求两个集合的并集
#intersection() 求两个集合的并集

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s2 = {1,2,3,4,5,13,14,15,16}

# s1.add(11)
# print(s1)

# s1.remove(11)
# print(s1)

# s1.pop()
# print(s1)

# # s1.clear()
# # print(s1)

# print(s1.difference(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))


#案例练习

# 根据提供的班级学生的选课情况，完成如下需求：

#选修足球学生名单
football_set ={"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
# 选修篮球学生名单
basketball_set={"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
#选修法语学生名单
french_set ={"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
# 选修艺术学生名单
art_set ={"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

# 1，找出同时选修了法语和艺术的学生
# print(f"同时选修法语和艺术的学生为:{french_set.intersection(art_set)}") #方法1
print(f"同时选修法语和艺术的学生为:{french_set&art_set}") #方法2 使用"&"

# 2，找出同时选修了所有四门课程的学生
print(f"同时选修所有学科的的学生为:{french_set&art_set&basketball_set&football_set}")

# 3.找出选修了足球，但是没有选修篮球的学生
print(f"选修了足球，但没选修篮球的学生为：{football_set-basketball_set}")#使用"-"求差集

# 方式三：集合推导式--->快速构建集合，语法：{要往集合中添加的数据forsinset1if条件】
fb_set3 ={s for s in football_set if s not in basketball_set}
print(f"选修了足球，但没选修篮球的学生为：{fb_set3}")

# 4.统计每一个学生选修的课程数量

#提取出学生名单
studentds = football_set|basketball_set|french_set|art_set  #使用"|"来求并集
# print(studentds)

#解包出集合中所有的元素
all_list = [*football_set,*basketball_set,*french_set,*art_set]
# print(all_list)

for s in studentds:
    print(f"{s}选修了{all_list.count(s)}们课程",end="\n")