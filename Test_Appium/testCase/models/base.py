# !/usr/bin/env python
# -*- coding: UTF-8 –*-
__author__ = 'Mr.Li'
from selenium.webdriver.common.action_chains import ActionChains

class Page(object):
    '''
    页面基础类，用于所有页面的继承
    '''
    url = '/'
    bbs_url = 'http://10.240.0.105/login'#bate环境

    def __init__(self,selenium_driver,base_url=bbs_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def on_page(self):
        return self.driver.current_url == (self.base_url)

    def _open(self):
        url = self.base_url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s' % url

    def open(self):
        self._open()

    def find_element(self,*loc):
        return self.driver.find_element(*loc)#单元素查询

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)#多元素查询

    def script(self,src):
        return self.driver.execute_script(src)#执行js脚本


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    p = Page(driver)
    p.open()


