# -*- coding:utf-8 -*-
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2019-5-30
@author: 杜宏
Project:项目结构设计
'''
# 3.导入模块
import unittest
import requests
import warnings,sys
sys.path.append(".pag_obj")
from loginmy import Jenkins1
from common.logger import Log


class Test(unittest.TestCase):
    log = Log()
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        s = requests.session()
        self.jenkins = Jenkins1(s)

    def test_01_login(self):
        '''登录接口测试用例'''
        self.log.info("--------------start-------------")
        t = self.jenkins.login()
        self.log.info("状态码：%s" % t.status_code)
        self.log.info("--------------end-------------")


if __name__ == "__main__":
    unittest.main()
