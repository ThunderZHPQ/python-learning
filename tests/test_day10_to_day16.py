import random

import pytest


def test_day10_sums_multiples_of_three(script_runner):
    result = script_runner.run("Day10_while_for.py")

    expected = sum(i for i in range(100, 501) if i % 3 == 0)
    assert expected == 39900
    assert result["total"] == expected
    assert result.lines == [f"100-500之间所有3的倍数的和是{expected}"]


def test_day11_nested_loop_is_fully_commented_out(script_runner):
    result = script_runner.run("Day11_nested_loop.py")

    assert result.stdout == ""


@pytest.mark.parametrize(
    ("guesses", "expected"),
    [
        (["50"], ["恭喜您猜对了"]),
        (["10", "50"], ["您输入的数字小了", "恭喜您猜对了"]),
        (["90", "50"], ["您输入的数字大了", "恭喜您猜对了"]),
        (
            ["1", "99", "50"],
            ["您输入的数字小了", "您输入的数字大了", "恭喜您猜对了"],
        ),
    ],
)
def test_day12_guess_number_game(script_runner, monkeypatch, guesses, expected):
    monkeypatch.setattr(random, "randint", lambda low, high: 50)

    result = script_runner.run("Day12_nested_loop2", inputs=guesses)

    assert result["random_num"] == 50
    assert result.lines == expected


def test_day13_list_literal(script_runner):
    result = script_runner.run("Day13_list.py")

    assert result["s"] == [15, 687, 567, 35, 10, 368, 6]
    assert result.stdout == ""


def test_day14_squares_of_even_numbers(script_runner):
    result = script_runner.run("Day14_list_test.py")

    assert result["new_list"] == [0, 4, 144, 1024, 6400, 8464, 9604]
    assert result.lines == ["[0, 4, 144, 1024, 6400, 8464, 9604]"]


@pytest.mark.parametrize(
    ("entered", "reversed_text"),
    [
        ("abc", "cba"),
        ("Hello World", "dlroW olleH"),
        ("上海自来水", "水来自海上"),
        ("", ""),
    ],
)
def test_day15_reverses_and_uppercases(script_runner, entered, reversed_text):
    result = script_runner.run("Day15_string_list.py", inputs=[entered])

    assert result["str_list3"] == [reversed_text, reversed_text.upper()]
    assert result.lines[1:] == [reversed_text, reversed_text.upper()]


def test_day16_lists_only_students_averaging_above_90(script_runner):
    result = script_runner.run("Day16_tuple.py")

    assert result.lines[0] == "优秀学生名单如下"

    names = [line.split("\t")[1].removeprefix("姓名：") for line in result.lines[1:]]
    assert names == ["李慕婉", "周轶", "红蝶", "许木"]

    assert result.lines[1] == "学号：S002\t姓名：李慕婉\t总分：275\t平均分：91.7"
    for student in result["students"]:
        assert len(student) == 5
