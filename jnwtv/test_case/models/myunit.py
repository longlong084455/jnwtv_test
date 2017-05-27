# coding:utf-8
from selenium.webdriver.common.by import By
from unittest import TestCase
from driver import AppiumDriver


class MyTest(TestCase):
    def setUp(self):
        """
        args1: 端口号
        args2: 等待的appWaitActivity 默认是0：用于登陆，注册，游客模式的用例
                1：用于其它的所有用例
        :return:
        """
        self.driver = AppiumDriver().start_appium('4723', 0)

    def tearDown(self):
        self.driver.quit()


