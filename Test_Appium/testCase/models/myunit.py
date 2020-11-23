# !/usr/bin/env python
# -*- coding: UTF-8 –*-
__author__ = 'Mr.Li'

import time
import unittest

from models.driver import browser
from testCase.page_obj.a1_0_loginPage import Login
import warnings


class MyTest(unittest.TestCase,Login):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)


    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
    def tearDown(self):
        print(self.driver.current_url)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    t = MyTest()
    t().test_ceshi()