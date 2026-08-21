def test_day01_hello_prints_three_lines(script_runner):
    result = script_runner.run("Day01_hello.py")

    assert result.lines == [
        "Hello, World!",
        "This is a Python script.",
        "It demonstrates basic print functionality.",
    ]


def test_day02_print_poem_has_border(script_runner):
    result = script_runner.run("Day02_print.py")

    assert len(result.lines) == 7
    assert result.lines[0] == result.lines[-1] == "###################"
    assert "静夜思" in result.lines[1]
    assert all(line.startswith("###") for line in result.lines)


def test_day03_variable_arithmetic(script_runner):
    result = script_runner.run("Day03_variable.py")

    assert result["base"] == 20.7
    assert result["incr"] == 50
    assert result.lines == [
        "计算数据的值为： 70.7",
        "进一步计算数据的值为： 120.7",
    ]


def test_day04_identifier_swaps_values(script_runner):
    result = script_runner.run("Day04_identifier.py")

    assert result.lines == [
        "交换前：a=10,b=20",
        "交换后：a=20,b=10",
    ]
    assert (result["a"], result["b"]) == (20, 10)


def test_day05_string_formatting_styles_agree(script_runner):
    result = script_runner.run("Day05_string.py")

    assert result.lines == ["a = 123, b = hello"] * 4
    assert result["s1"] == "Hello"
    assert result["s2"] == "Python"
    assert result["s3"].startswith("\n尊敬的客户：")
    assert result["s3"].endswith("祝好~\n")
