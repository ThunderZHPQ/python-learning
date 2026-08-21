import pytest


def test_day06_input_withdrawal_updates_balance(script_runner):
    result = script_runner.run("Day06_input.py", inputs=["123456", "2500"])

    assert result["total"] == 10000
    assert result.lines == [
        "密码正确：123456",
        "剩余余额: 7500",
    ]


def test_day06_input_rejects_non_numeric_amount(script_runner):
    with pytest.raises(ValueError):
        script_runner.run("Day06_input.py", inputs=["123456", "abc"])


@pytest.mark.parametrize(
    ("entered", "outside_range"),
    [("5", True), ("10", False), ("15", False), ("20", False), ("42", True)],
)
def test_day07_operator_range_check(script_runner, entered, outside_range):
    result = script_runner.run("Day07_operator.py", inputs=[entered])

    assert result.lines == [f"该整数是否不在10-20之间: {outside_range}"]


@pytest.mark.parametrize(
    ("year", "is_leap"),
    [
        ("2024", True),
        ("2023", False),
        ("1900", False),
        ("2000", True),
        ("2100", False),
    ],
)
def test_day08_leap_year(script_runner, year, is_leap):
    result = script_runner.run("Day08_ifelse.py", inputs=[year])

    expected = f"{year}是闰年" if is_leap else f"{year}不是闰年"
    assert result.lines == [expected]


@pytest.mark.parametrize(
    ("oper", "expected"),
    [
        ("+", "6.0 + 3.0 = 9.0"),
        ("-", "6.0 - 3.0 = 3.0"),
        ("*", "6.0 * 3.0 = 18.0"),
        ("/", "6.0 / 3.0 = 2.0"),
    ],
)
def test_day09_calculator_supported_operators(script_runner, oper, expected):
    result = script_runner.run("day09_elif_match.py", inputs=["6", oper, "3"])

    assert result.lines == [expected]


def test_day09_calculator_rejects_unknown_operator(script_runner):
    result = script_runner.run("day09_elif_match.py", inputs=["6", "%", "3"])

    assert result.lines == ["操作不支持"]


def test_day09_calculator_rejects_division_by_zero(script_runner):
    result = script_runner.run("day09_elif_match.py", inputs=["6", "/", "0"])

    assert result.lines == ["操作不支持"]
