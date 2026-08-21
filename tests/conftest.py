import builtins
import io
import pathlib
import runpy
from contextlib import redirect_stdout

import pytest

PRACTICE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Practice"


class ScriptRunner:
    """执行 Practice 目录下的脚本，替换 input() 并捕获标准输出。"""

    def __init__(self, monkeypatch):
        self._monkeypatch = monkeypatch

    def run(self, script_name, inputs=()):
        script_path = PRACTICE_DIR / script_name
        assert script_path.exists(), f"脚本不存在: {script_path}"

        pending = list(inputs)
        prompts = []

        def fake_input(prompt=""):
            prompts.append(prompt)
            if not pending:
                raise AssertionError(f"脚本请求的输入超出预设数量: {prompt!r}")
            return pending.pop(0)

        self._monkeypatch.setattr(builtins, "input", fake_input)

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            namespace = runpy.run_path(str(script_path), run_name="__main__")

        assert not pending, f"未被使用的输入: {pending}"
        return ScriptResult(buffer.getvalue(), namespace, prompts)


class ScriptResult:
    def __init__(self, stdout, namespace, prompts):
        self.stdout = stdout
        self.namespace = namespace
        self.prompts = prompts

    @property
    def lines(self):
        return self.stdout.splitlines()

    def __getitem__(self, name):
        return self.namespace[name]


@pytest.fixture
def script_runner(monkeypatch):
    return ScriptRunner(monkeypatch)
