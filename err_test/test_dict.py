
from typing import Any



print("\n========单元测试==========\n")
# 单元测试
# 如果你听说过“测试驱动开发”（TDD：Test-Driven Development），单元测试就不陌生。
# 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

# 单元测试通过后有什么意义呢？
# 如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对abs()函数原有的行为造成影响，
# 如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。
# 这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。
# 在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        
        except KeyError :
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value




