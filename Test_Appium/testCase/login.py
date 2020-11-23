# !/usr/bin/env python
# -*- coding: UTF-8 –*-
__author__ = 'Mr.Li'
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    'platformName':'Android',#android的apk还是IOS的
    'deviceName':'127.0.0.1:62001',#手机设备名称，通过adb devices查看
    # 'automationName':"uiautomator2",
    'platforVersion':'5.1.1',
    'noReset': True,
    'app':'d:\\ygyg.cn.ygd_V1.2.1.apk',
    'appPackage':'ygyg.cn.ygd',#apk的包名
    'appActivity':'ygyg.cn.ygd.modular.login.activity.LoginActivity',#apk的launcherActivity
    # 'unicodeKeyboard':'True',#unicodeKeyboard是使用unicode编码方式发送字符串
    # 'resetKeyboard':'True',#resetKeyboard是将键盘隐藏起来
}

# desired_caps = {
#     'platformName':'Android',
#     'deviceName':'127.0.0.1:62001',
#     'platforVersion':'5.1.1',
#     'app':'D:\\com.mymoney_12.55.0.0_12055000.apk',
#     'appPackge':'com.mymoney',
#     'noReset': True,
#     'appActivity':'com.mymoney.biz.splash.SplashScreenActivity',
# }
deivces = 'http://127.0.0.1:4723/wd/hub'

driver = webdriver.Remote(deivces,desired_caps)

time.sleep(3)

driver.find_element_by_id('ygyg.cn.ygd:id/et_login_username').send_keys('ww001')

driver.find_element_by_id('ygyg.cn.ygd:id/et_login_password').send_keys('admin11')
driver.find_element_by_class_name('android.widget.LinearLayout').click()


toast_loc = ("xpath", ".//*[contains(@text,'用户名或者密码错误！')]")
elm =  WebDriverWait(driver, 5).until(EC.presence_of_element_located(toast_loc))


print(elm.text)
time.sleep(3)
driver.quit()