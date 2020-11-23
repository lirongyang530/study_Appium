# !/usr/bin/env python
# -*- coding: UTF-8 –*-
__author__ = 'Mr.Li'

from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
    desired_caps = {
        'platformName': 'Android',  # android的apk还是IOS的
        'platfromVersion': '4.4.2',  # Android系统的版本号
        'deviceName': '127.0.0.1:62001',  # 手机设备名称，通过adb devices查看
        # 'appPackage':'com.taobao.taobao',#apk的包名
        # 'appActivity':'com.taobao.taobao.ContainerActivity',#apk的launcherActivity
        # 'unicodeKeyboard':'True',#unicodeKeyboard是使用unicode编码方式发送字符串
        # 'resetKerboard':'True',#resetKeyboard是将键盘隐藏起来
    }
    deivces = 'http://127.0.0.1:4723/wd/hub'

    driver = webdriver.Remote(deivces, desired_caps)
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.quit()