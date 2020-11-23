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
    'app':'D:\\com.tal.kaoyan_3.6.0_109.apk',
    'appPackge':'com.tal.kaoyan',
    'noReset': True,
    'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)