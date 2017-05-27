# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SwipeAction:
    def auto_check_cartoon(self, times, start, end, duration):
        for s in range(times):
            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            x1 = int(x * 0.5)
            y1 = int(y * start)
            y2 = int(y * end)
            self.driver.swipe(x1, y1, x1, y2, duration)

    # 获取屏幕的宽高
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 上下滑动，x轴不变   左右滑动，y轴不变
    def swipe_up(self, t):
        location = self.get_size()
        x1 = int(location[0] * 0.5)  # x轴坐标
        y1 = int(location[1] * 0.99)  # 滑动前y轴坐标
        y2 = int(location[1] * 0.01)  # 滑动后y轴坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t):
        location = self.get_size()
        x1 = int(location[0] * 0.5)
        y1 = int(location[1] * 0.25)
        y2 = int(location[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_left(self, t):
        location = self.get_size()
        x1 = int(location[0] * 0.75)
        y1 = int(location[1] * 0.5)
        x2 = int(location[1] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, t):
        location = self.get_size()
        x1 = int(location[0] * 0.05)
        y1 = int(location[1] * 0.5)
        x2 = int(location[1] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    def __init__(self, driver):
        self.driver = driver
        print ''