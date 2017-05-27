# coding:utf-8
from wait_element import *


class CancleDialog:
    def __init__(self, driver):
        self.driver = driver

    def cancle_daily_share(self):
        if wait_element_visible_by_id(self.driver, 'rl_sharedialog', '今天不是第一次登录'):
            cancle_share = self.driver.find_element_by_id('iv_dis')
            cancle_share.click()

    def cancle_update(self):
        if wait_element_visible_by_id(self.driver, 'btn_update_now', '没有版本更新'):
            btn_update_later = self.driver.find_element_by_id('btn_update_later')
            btn_update_later.click()
