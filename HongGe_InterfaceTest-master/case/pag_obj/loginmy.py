# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2019-5-31
@author: 北京-宏哥
Project:学习和使用封装与调用--流程类接口关联
'''
# 3.导入模块
import requests
# from common.logger import Log
# 禁用安全请求警告
import urllib3

urllib3.disable_warnings()
import warnings

warnings.simplefilter("ignore", ResourceWarning)


class Jenkins1():
    # log = Log()

    def __init__(self, s):
        # s = requests.session()  # 全局参数
        self.s = s

    def login(self):
        '''登录接口'''
        url = "http://10.39.37.55:10300/api/system/page"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
        }  # get方法其它加个ser-Agent就可以了
        d = {
            "accessType":"null",
            "authType":"null",
            "pageNum":1,
            "pageSize":10,
            "systemTag":"null",
            "memo":"null",
            "id":"null",
            "isDeleted":"false"
            }

        s = requests.session()
        r = s.post(url, headers=headers, data=d)
        return r




if __name__ == "__main__":
    s = requests.session()
    Jenkins(s).login()
