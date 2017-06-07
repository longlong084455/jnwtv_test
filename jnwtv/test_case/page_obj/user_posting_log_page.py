# coding:utf-8
from selenium.webdriver.common.by import By
from user_info_base_page import UserInfoBasePage
from jnwtv.test_case.utils.wait_element import *

class UserPostingLogPage(UserInfoBasePage):
    """用户发帖记录页面元素和方法"""
    login_posting_loc = (By.ID, 'layout_log_record')
    def login_posting_btn(self):
        # 进入发帖记录
        self.find_element(*self.login_posting_loc).click()

    user_icon_loc = (By.ID, 'main_portrait')
    def click_user_icon(self):
        self.find_elements(*self.user_icon_loc)[0].click()

    # 等级
    def lever_is_exist(self):
        return wait_element_visible_by_id(self.driver, 'main_level', '没有显示等级')

    def time_is_exist(self):
        return wait_element_visible_by_id(self.driver, 'main_time', '没有显示时间')

    # 评论数量 int
    comment_loc = (By.ID, 'main_comment')
    def get_comment_num(self):
        return int(self.find_elements(*self.comment_loc)[0].get_attribute('text'))

    # 点赞按钮
    praise_loc = (By.ID, 'iv_praise')
    def click_priase(self):
        self.find_elements(*self.praise_loc)[0].click()
    # 点赞数量
    praise_num_loc = (By.ID, 'main_praise')
    def get_praise_num(self):
        return int(self.find_elements(*self.praise_num_loc)[0].get_attribute('text'))
