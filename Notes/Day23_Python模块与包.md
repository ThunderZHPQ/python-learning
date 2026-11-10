# Day23 Python模块与包（Module & Package）

## 一、Python模块（Module）

模块（Module）是Python程序的基本组织单位。

简单理解：

**一个 `.py` 文件就可以作为一个模块。**

模块中可以定义：

- 变量
- 函数
- 类
- 可执行代码

例如，创建一个文件：

```text
moduleTest.py
```

在里面定义：

```python
PI = 3.1415926

NAME = "张"

def log_separator():
    print("- " * 30)
```

那么 `moduleTest.py` 就是一个模块。

### 模块的作用

1. 提高代码复用性：一个模块中的功能可以被其他文件导入使用。
2. 降低开发门槛：可以直接使用Python内置模块或第三方模块提供的功能。
3. 避免命名冲突：不同模块可以定义相同名称的变量和函数，通过模块名区分。

使用模块中的功能之前，需要先导入模块。

---

## 二、导入模块：import

### 1. 普通导入

基本格式：

```python
import 模块名
```

调用模块中的功能：

```python
模块名.功能名
```

例如：

```python
import random

num = random.randint(1, 100)

print(num)
```

这里：

```python
import random
```

表示导入Python内置的随机数模块。

```python
random.randint(1, 100)
```

表示调用random模块中的randint()函数，生成1到100之间的随机整数。

### 2. 给模块设置别名

如果模块名称比较长，可以使用 `as` 设置别名。

基本格式：

```python
import 模块名 as 别名
```

例如：

```python
import random as rd

num = rd.randint(1, 100)

print(num)
```

这里：

```python
random as rd
```

表示将random模块设置为别名rd。

后续可以直接通过：

```python
rd.randint(1, 100)
```

调用功能。

---

## 三、导入模块中的指定功能：from...import

如果只需要使用模块中的某个功能，可以直接导入指定功能。

基本格式：

```python
from 模块名 import 功能名
```

调用时不需要再写模块名。

例如：

```python
from random import randint

num = randint(1, 100)

print(num)
```

与普通导入的区别：

普通导入：

```python
import random

random.randint(1, 100)
```

指定功能导入：

```python
from random import randint

randint(1, 100)
```

### 1. 导入多个指定功能

```python
from random import randint, choice
```

这样可以同时导入randint和choice两个功能。

### 2. 给指定功能设置别名

```python
from random import randint as rd

num = rd(1, 100)
```

### 3. 导入模块中的所有功能

```python
from random import *
```

表示导入random模块中允许通过 `*` 导入的所有功能。

后续可以直接使用：

```python
randint(1, 100)
```

不需要写：

```python
random.randint(1, 100)
```

注意：

实际开发中不建议频繁使用 `from 模块名 import *`，因为可能导入大量名称，造成命名冲突，也不容易判断某个函数来自哪个模块。

---

## 四、自己创建的Python文件也可以作为模块

每一个Python文件都可以作为一个模块。

例如项目结构：

```text
Python-Learning/
│
├── main.py
│
└── moduleTest.py
```

在 `moduleTest.py` 中定义：

```python
PI = 3.1415926

NAME = "张"

def log_separator1():
    print("- " * 30)

def log_separator2():
    print("+ " * 30)
```

在 `main.py` 中导入：

```python
import moduleTest as mt

print(mt.PI)

print(mt.NAME)

mt.log_separator2()
```

也可以使用：

```python
from moduleTest import log_separator2

log_separator2()
```

这里的重点是：

**自己编写的.py文件，也可以被其他Python文件导入使用。**

---

## 五、Python包（Package）

当项目中的模块越来越多时，如果全部放在同一个文件夹下，就不方便管理。

这时可以使用包（Package）。

包的本质是一个用于组织和管理多个模块的文件夹。

例如：

```text
Python-Learning/
│
├── main.py
│
└── utils/
    │
    ├── __init__.py
    │
    ├── my_fun.py
    │
    └── my_var.py
```

其中：

```text
utils
```

是一个包。

```text
my_fun.py
my_var.py
```

是包中的两个模块。

传统的Python包通常包含：

```python
__init__.py
```

这个文件用于标识和初始化包。

补充：较新的Python也支持不包含 `__init__.py` 的命名空间包，但目前学习阶段可以先按照包含 `__init__.py` 的常规包结构理解。

### 包的作用

1. 管理多个模块。
2. 将相关功能组织在一起。
3. 让项目结构更加清晰。
4. 方便其他文件导入和使用。

---

## 六、导入包中的模块

假设项目结构：

```text
Python-Learning/
│
├── main.py
│
└── utils/
    │
    ├── __init__.py
    │
    └── my_fun.py
```

`my_fun.py` 中定义：

```python
def log_separator1():
    print("- " * 30)

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)
```

### 方式一：import完整模块路径

```python
import utils.my_fun

utils.my_fun.log_separator2()
```

调用时需要写完整的模块路径。

### 方式二：from...import导入模块

```python
from utils import my_fun

my_fun.log_separator3()
```

这种方式直接导入utils包中的my_fun模块。

调用时只需要写：

```python
my_fun.log_separator3()
```

### 方式三：直接导入模块中的函数

```python
from utils.my_fun import log_separator3

log_separator3()
```

这种方式直接导入指定函数，调用时不需要写模块名。

---

## 七、__all__特殊变量

`__all__` 是一个特殊变量，用来控制使用：

```python
from 模块名 import *
```

时，哪些功能会被导入。

例如：

在 `moduleTest.py` 中定义：

```python
__all__ = [
    "log_separator1",
    "log_separator2"
]

PI = 3.1415926

NAME = "张"

def log_separator1():
    print("- " * 30)

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)
```

在另一个文件中：

```python
from moduleTest import *

log_separator1()

log_separator2()
```

可以正常使用。

但是：

```python
log_separator3()
```

会报错，因为它没有被写入 `__all__`。

### __all__的作用

```python
__all__ = [
    "log_separator1",
    "log_separator2"
]
```

表示：

当其他文件使用：

```python
from moduleTest import *
```

时，只导入：

```text
log_separator1
log_separator2
```

### 注意

`__all__` 并不会删除或隐藏其他功能。

例如：

```python
from moduleTest import log_separator3

log_separator3()
```

即使 `log_separator3` 没有写入 `__all__`，只要它存在，仍然可以通过明确指定名称的方式导入。

因此：

**__all__主要控制星号导入（*），不限制普通的指定名称导入。**

---

## 八、包中的__all__

除了模块可以定义 `__all__`，包中的 `__init__.py` 也可以定义。

例如：

```text
utils/
│
├── __init__.py
│
├── my_fun.py
│
└── my_var.py
```

在 `__init__.py` 中：

```python
__version__ = "1.0.0"

__all__ = [
    "my_fun",
    "my_var"
]
```

这里的：

```python
__all__ = ["my_fun", "my_var"]
```

表示当其他文件使用：

```python
from utils import *
```

时，包允许导入的名称是：

```text
my_fun
my_var
```

注意区分：

模块中的 `__all__`：

```python
__all__ = ["log_separator1", "log_separator2"]
```

控制：

```python
from moduleTest import *
```

导入哪些功能。

包中的 `__all__`：

```python
__all__ = ["my_fun", "my_var"]
```

控制：

```python
from utils import *
```

导入哪些模块或包成员。

---

## 九、__init__.py的作用

`__init__.py` 是包的初始化文件。

除了标识和初始化包之外，还可以在里面：

1. 定义包级别的变量。
2. 导入包中的模块。
3. 暴露常用功能。
4. 定义 `__all__`。

例如：

```python
# utils/__init__.py

__version__ = "1.0.0"

from . import my_fun
from . import my_var

__all__ = [
    "my_fun",
    "my_var"
]
```

这里：

```python
from . import my_fun
```

表示从当前包中导入my_fun模块。

其中：

```text
.
```

代表当前包。

这样其他文件就可以使用：

```python
from utils import my_fun

my_fun.log_separator3()
```

---

## 十、常量的命名规范

常量是指在程序设计中约定不应该改变的变量。

Python没有真正强制不可修改的常量机制，通常使用全大写字母命名来表示常量。

例如：

```python
PI = 3.1415926

NAME = "张"

MAX_SIZE = 100
```

命名规范：

```text
普通变量：小写字母

函数名称：小写字母，多个单词使用下划线分隔

常量：全大写字母，多个单词使用下划线分隔
```

注意：

全大写只是约定俗成的命名规范，并不会阻止程序修改变量。

例如：

```python
PI = 3.1415926

PI = 3.14
```

Python仍然允许这样修改。

---

## 十一、__name__特殊变量

`__name__` 是Python内置的特殊变量，用于表示当前模块的名称。

它有两种常见情况：

### 1. 直接运行当前Python文件

如果直接运行：

```python
moduleTest.py
```

那么：

```python
__name__
```

的值为：

```python
"__main__"
```

### 2. 当前文件被其他模块导入

如果在另一个文件中：

```python
import moduleTest
```

那么在 `moduleTest.py` 内部：

```python
__name__
```

的值就是模块名：

```python
"moduleTest"
```

如果模块位于包中，通常会包含包路径，例如：

```python
"utils.my_fun"
```

---

## 十二、if __name__ == "__main__"

在Python开发中，经常看到：

```python
if __name__ == "__main__":
    ...
```

它的作用是：

**只有直接运行当前文件时，才执行这个条件中的代码；当文件被其他模块导入时，不执行这部分代码。**

例如：

```python
def log_separator1():
    print("- " * 30)

def log_separator2():
    print("+ " * 30)

if __name__ == "__main__":
    log_separator1()
```

如果直接运行当前文件：

```text
执行log_separator1()
```

如果其他文件导入：

```python
import moduleTest
```

则不会自动执行：

```python
log_separator1()
```

但是其他文件仍然可以主动调用：

```python
moduleTest.log_separator1()
```

### 为什么需要它？

假设一个模块既包含：

```text
可以被其他文件调用的函数
```

又包含：

```text
用于测试的代码
```

如果没有这个判断，其他文件导入模块时，测试代码也可能自动执行。

使用：

```python
if __name__ == "__main__":
```

就可以把测试代码和模块功能分开。

---

## 十三、模块、包与文件之间的关系

可以通过下面的结构理解：

```text
Python项目
    │
    ├── main.py
    │
    ├── moduleTest.py
    │
    └── utils（包）
          │
          ├── __init__.py
          │
          ├── my_fun.py（模块）
          │
          └── my_var.py（模块）
```

对应关系：

```text
.py文件
    ↓
模块（Module）

包含多个模块的文件夹
    ↓
包（Package）

多个模块和包
    ↓
组成完整的Python项目
```

---

## 十四、今日重点

### 导入整个模块

```python
import random

random.randint(1, 100)
```

### 给模块设置别名

```python
import random as rd

rd.randint(1, 100)
```

### 导入指定功能

```python
from random import randint

randint(1, 100)
```

### 导入所有功能

```python
from random import *
```

### 导入自己编写的模块

```python
import moduleTest as mt

mt.log_separator2()
```

### 导入包中的模块

```python
from utils import my_fun

my_fun.log_separator3()
```

### __all__

```python
__all__ = [
    "log_separator1",
    "log_separator2"
]
```

控制使用 `from 模块名 import *` 时导入的名称。

### __init__.py

包的初始化文件，可以定义包级别的变量、导入模块和设置 `__all__`。

### 常量命名

```python
PI = 3.1415926
```

全大写是一种命名规范，不是强制限制。

### __name__

```python
if __name__ == "__main__":
    print("直接运行当前文件时执行")
```

直接运行当前文件时，`__name__` 为 `"__main__"`；被导入时则为模块名。

---

## Day23总结

今天开始学习Python模块与包，主要掌握了：

- 理解了模块（Module）的概念，知道一个 `.py` 文件可以作为一个模块
- 了解了模块提高代码复用性、降低开发门槛和避免命名冲突的作用
- 学习了使用 `import` 导入模块
- 学习了使用 `as` 给模块或指定功能设置别名
- 学习了使用 `from...import...` 导入模块中的指定功能
- 了解了 `from...import *` 的使用方式
- 学习了将自己编写的Python文件作为模块导入
- 理解了包（Package）的概念，以及包对多个模块的管理作用
- 学习了使用 `__init__.py` 初始化包
- 学习了使用 `__all__` 控制星号导入的内容
- 区分了模块中的 `__all__` 和包中的 `__all__`
- 学习了常量的全大写命名规范
- 理解了 `__name__` 的作用及不同运行场景下的取值
- 学习了 `if __name__ == "__main__"`，将模块功能和测试代码区分开来

今天的学习重点是理解模块与包的组织方式，为后续把一个完整程序拆分成多个文件、实现功能复用打下基础。