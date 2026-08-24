# Python中的字典（dict）,里面存储的是键值对（key:value）类型的数据,可以根据键（key)找到对应的值（value）。
# 键值对（key:value）存储、键（key）不能重复、可修改value值。如果重复,后面的值会覆盖前面的值
# 字典是没有索引下标的,不能根据索引获取值,只可以根据key获取value

# # dict1 = {"zhang":670,"wang":684,"li":703}
# dict1 = {"zhang":670,"wang":684,"li":703,"zhang":750}
# print(dict1)
# print(dict1["wang"])#获取值

# dict1["wang"] = 688#修改值
# print(dict1["wang"])

# dict2 = {}#空字典
# dict3 = dict()#空字典

# # 注意:字典(dict)中的value可以是任何类型的数据,而key不能为可变类型（如:不能为列表list、集合set、字典dict)。


# 字典常用方法
# 添加 字典名称[key]=value 往指定字典中添加key-value键值对 dict1["涛哥"]=688
# 字典名称.pop(key) 删除字典中指定的key,并返回该key对应的value score =dictl.pop（"涛哥"）
# del字典名称[key] 删除字典中指定的键值对 del dict1["涛哥"]
# 字典名称[key]=value 修改字典中指定的key对应的值 dict1["小智"] =658
# 字典名称[key] 根据key获取value dict1["涛哥"]
# 字典名称.get(key) 根据key获取value dictl.get("涛哥")
# 字典名称.keys() 获取所有的key dict1.keys()
# 字典名称.values() 获取所有的value dict1.values()
# 字典名称.items（) 获取所有的key-value键值对 dictl.items()

# dict1={"小智":675,"李思":608,"李琪":478,"小黑":545,"温韬":429}

# #key不存在时执行添加操作
# dict1["小张"] = 687
# print(dict1)

# #key存在时执行修改操作
# dict1["小张"] = 666
# print(dict1)

# # 根据键值获取value
# print(dict1["小张"])
# print(dict1.get("小张"))

# # 获取所有key
# print(dict1.keys())

# # 获取所有value
# print(dict1.values())

# # 获取所有key-value键值对
# print(dict1.items())

# # 删除（有返回值）
# score = dict1.pop("小张")
# print(dict1)
# print(score)

# # 删除（无返回值）
# del dict1["小智"]
# print(dict1)

#遍历
# for k,v in dict1.items():
#     print(f"{k},{v}")

# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1，添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2，修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xX×，商品价格：×X×，商品数量：x×x"。
# 5.退出购物车、

# shopping = {"香蕉":[10,1.98]}
# function_list = {1:"添加购物车",2:"修改购物车",3:"删除购物车",4:"删除购物车",5:"退出购物车"}
# while(True):
    
#     function_choose = input("请选择您想要的功能:")
#     match function_choose:
#         case"1":
#             name = input("请输入需要添加的商品名称：")
#             if name in shopping:
#                 print("该商品已存在")
#             else:
#                 quantity = input("请输入商品的数量：")
#                 cost = input("请输入商品的价格：")
#                 shopping[name] = [quantity,cost]
#                 print("商品添加成功")
#         case"2":
#             name = input("请输入需要修改的商品名称：")
#             if name in shopping:
#                 quantity = input("请输入商品的数量：")
#                 cost = input("请输入商品的价格：")
#                 shopping[name] = [quantity,cost]
#                 print("商品修改成功")
#             else:
#                 print("库存中没有该商品")
#         case"3":
#             name = input("请输入需要删除的商品名称：")
#             if name in shopping:
#                 del shopping[name]
#                 print("商品已删除")
#                 print(shopping)
#             else:
#                 print("库存中没有该商品")
#         case"4":
#             print("显示商品明细")
#             for name,[quantity,cost] in shopping.items():
#                 print(f"商品名称：{name},商品数量：{quantity},商品价格：{cost}")
#         case"5":
#             print("已退出购物车")
#             break
#         case _:
#             print("请选择正确的功能")

#方式2
print("test")
shopping = {"香蕉":{"price":1.98,"num":10}}
function_list = {1:"添加购物车",2:"修改购物车",3:"删除购物车",4:"删除购物车",5:"退出购物车"}
while(True):
    
    function_choose = input("请选择您想要的功能:")
    match function_choose:
        case"1":
            name = input("请输入需要添加的商品名称：")
            if name in shopping:
                print("该商品已存在")
                continue
            quantity = input("请输入商品的数量：")
            cost = input("请输入商品的价格：")
            shopping[name] = {"price":cost,"num":quantity}
            print("商品添加成功")

        case"2":
            name = input("请输入需要修改的商品名称：")
            if name in shopping:
                quantity = input("请输入商品的数量：")
                cost = input("请输入商品的价格：")
                shopping[name] = {"price":cost,"num":quantity}
                print("商品修改成功")
            else:
                print("库存中没有该商品")
        case"3":
            name = input("请输入需要删除的商品名称：")
            if name in shopping:
                del shopping[name]
                print("商品已删除")
                print(shopping)
            else:
                print("库存中没有该商品")
        case"4":
            print("显示商品明细")
            for name in shopping.keys():
                shopping_info = shopping[name]
                print(f"商品名称：{name},商品数量：{shopping_info['num']},商品价格：{shopping_info['price']}")
        case"5":
            print("已退出购物车")
            break
        case _:
            print("请选择正确的功能")
        

        
        





