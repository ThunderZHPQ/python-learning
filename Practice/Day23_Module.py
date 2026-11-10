# Python模块（module)：一个.py文件就是一个模块，模块是Python程序的基本组织单位。在模块中可以定义变量、函数、类，以及可执行的代码。
# 提高代码复用性,降低开发门槛,避免命名冲突

# 在使用模块中提供的功能之前，必须得先导入，再使用。

#导入模块 -->调用方式 模块命.功能名/别名.功能名
# import random

# import random as rd

# for i in range(100):
#     print(rd.randint(1,100))

# 导入模块中的特定功能 from...import... -->调用方式：功能名/别名
# from random import randint
# from random import *  导入所有功能
# for i in range(100):
#     print(randint(1,100))

# 每一个python文件都可以作为一个模块，模块的名字就是文件的名字（建议使用python标识符定义，规范命名）
# import moduleTest as mt

# print(mt.PI)

# mt.log_separator2()

# from moduleTest import *

# log_separator2()

# 包：本质就是一个文件夹，该文件夹中可以包含若干python模块（·py文件），文件夹下还包含了一个__init__·py。
# 作用：模块文件较多时，用来管理多个模块。（包的本质也是一个模块）

# import utils.my_fun

# utils.my_fun.log_separator2()

#注意：如果需要通过"*"导入所有模块，则必须在相关文件下加入"__all__=[]"
from utils import my_fun

my_fun.log_separator3()