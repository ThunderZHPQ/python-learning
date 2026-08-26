"""练习中重复出现的通用工具函数。

各个 Day 的练习里反复出现同样的写法（带提示的数字输入、列表的最大/最小/平均值统计、
列表去重、字符串反转、账号密码校验等），统一放在这里，练习文件通过
`from learn_utils import xxx` 使用。
"""


def read_int(prompt):
    """读取一个整数输入。"""
    return int(input(prompt))


def read_float(prompt):
    """读取一个浮点数输入。"""
    return float(input(prompt))


def read_int_list(count, prompt):
    """连续读取 count 个整数，返回列表。"""
    return [read_int(prompt) for _ in range(count)]


def average(values):
    """计算平均值。"""
    return sum(values) / len(values)


def describe_numbers(values):
    """返回 (最小值, 最大值, 平均值)。"""
    return min(values), max(values), average(values)


def dedupe(values):
    """去除重复元素，保留首次出现的顺序。"""
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result


def sum_multiples(start, end, factor):
    """计算 [start, end] 区间内所有 factor 的倍数之和。"""
    return sum(i for i in range(start, end + 1) if i % factor == 0)


def reverse_text(text):
    """反转字符串。"""
    return text[::-1]


def check_login(username, password, accounts):
    """校验账号密码，accounts 为 {用户名: 密码} 字典。"""
    return username in accounts and accounts[username] == password
