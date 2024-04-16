import unittest
from test_dict import Dict

# 编写单元测试
class TestDict(unittest.TestCase):

    # 编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
    def setUp(self) -> None:
        print(self._testMethodName, "setUp...")
    
    def tearDown(self) -> None:
        print(self._testMethodName, "tearDown...")

    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, Dict))
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 运行单元测试:
# 一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。

# 方式1
# 命令：python mydict_test.py
# 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()

# 方式2
# 命令行通过参数-m unittest直接运行单元测试
# 命令：python -m unittest 08test_dict_test