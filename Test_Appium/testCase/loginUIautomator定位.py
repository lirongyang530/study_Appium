# !/usr/bin/env python
# -*- coding: UTF-8 –*-
__author__ = 'Mr.Li'
from appium import webdriver
import time

desired_caps = {
    'platformName':'Android',#android的apk还是IOS的
    'platfromVersion':'4.4.2',#Android系统的版本号
    'deviceName':'127.0.0.1:62001',#手机设备名称，通过adb devices查看
    # 'appPackage':'com.taobao.taobao',#apk的包名
    # 'appActivity':'com.taobao.taobao.ContainerActivity',#apk的launcherActivity
    # 'nuicodeKeyboard':'True',
    # 'resetKerboard':'True',
}
deivces = 'http://127.0.0.1:4723/wd/hub'

driver = webdriver.Remote(deivces,desired_caps)

time.sleep(5)

# driver.find_element_by_id('ygyg.cn.ygd:id/et_login_username').send_keys('xiaoming')

driver.find_element_by_android_uiautomator('new UiSelector().resourceId("ygyg.cn.ygd:id/et_login_username")').send_keys('xiaoming')


#1、android uiautomator text定位
# ele = driver.find_element_by_android_uiautomator('new UiSelector().text("请输入淘宝账户")')
# ele.send_keys("123")

#2 、uiautomator text模糊定位
# ele = driver.find_element_by_android_uiautomator('new UiSelector().textContains("请输入淘")')
# ele.send_keys("123")

#3、 textMatches 正则匹配查找
ele = driver.find_element_by_android_uiautomator('new UiSelector().textMatches("^请输入淘.*")')
ele.send_keys("123")

#4、uiautomator resourceID定位
ele = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.taobao.taobao:id/aliuser_login_account_et")')
ele.send_keys('234')

#5、resourceIDMatches 定位
ele = driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".+aliuser_login_account_et")')
ele.send_keys('234')

#6、iautomator className定位
ele = driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.EditText")')
ele.send_keys('234')

#7、 uiautomator classNameMatches定位
ele = driver.find_element_by_android_uiautomator('new UiSelector().classNameMatches (".*EditText")')
ele.send_keys('234')