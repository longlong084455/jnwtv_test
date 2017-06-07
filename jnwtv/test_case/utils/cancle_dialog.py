# coding:utf-8
from wait_element import *


class CancleDialog:
    def __init__(self, driver):
        self.driver = driver

    def cancle_update(self):
        """取消更新提示弹框"""
        if wait_element_visible_by_id(self.driver, 'btn_update_now', '没有版本更新'):
            btn_update_later = self.driver.find_element_by_id('btn_update_later')
            btn_update_later.click()

    def cancle_daily_share(self):
        """取消日常分享弹框"""
        if wait_element_visible_by_id(self.driver, 'rl_sharedialog', '今天不是第一次登录'):
            cancle_share = self.driver.find_element_by_id('iv_dis')
            cancle_share.click()

    def cancle_vote(self):
        """取消活动选票弹框"""
        if wait_element_visible_by_id(self.driver, 'btn2', '没有送选票'):
            cancle_look = self.driver.find_element_by_id('btn2')
            cancle_look.click()
