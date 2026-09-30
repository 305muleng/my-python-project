# 导入pytest测试框架和要测试的函数
import pytest
from calculator import add, multiply

# 测试加法函数
def test_add():
    # 断言：预期结果和实际结果相等则测试通过
    assert add(2, 3) == 5       # 正数相加
    assert add(-1, 1) == 0      # 正负相加
    assert add(0, 0) == 0       # 零相加

# 测试乘法函数
def test_multiply():
    assert multiply(3, 4) == 12 # 正数相乘
    assert multiply(2, 0) == 0  # 乘零
    assert multiply(-2, 5) == -10 # 正负相乘
