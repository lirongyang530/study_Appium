# !/usr/bin/env python
# -*- coding: UTF-8 –*-
__author__ = 'Mr.Li'

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

desired_caps = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:62001',
    'platforVersion':'5.1.1',
    'app':'D:\\com.mymoney_12.55.0.0_12055000.apk',
    'appPackge':'com.mymoney',
    'noReset': True,
    'appActivity':'com.mymoney.biz.splash.SplashScreenActivity',
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)