# -*- coding: utf-8 -*-
import unittest

"""
    单元测试，即模块测试
    单元指一个函数，模块，类等
    库unittest的基本组成
    类unittest.TestCase提供了许多测试方法
"""

class TestMethods(unittest.TestCase):

    # 判断两个值是否相等
    def test_equal(self):
        a = 1
        b = 1
        self.assertEqual(a, b)
        print('test equal done')

    # 判断值为True或False
    def test_bool(self):
        self.assertTrue(1)
        self.assertFalse(0)
        print('test bool done')

    # 方法名不以test开头就不执行
    def run_test(self):
        print('method without test not run')


