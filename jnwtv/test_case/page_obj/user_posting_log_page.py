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

    """发帖记录列表的元素"""
    # 所有的帖字
    logs_loc = (By.ID, 'main_content')
    def get_all_log(self):
        return self.find_elements(*self.logs_loc)

    def click_log_detail(self, index=0):
        # 进入帖子详情 默认进入第一条
        self.get_all_log()[index].click()

    # 头像
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

    """帖子详情的元素"""
    detail_comment_num_loc = (By.ID, 'comment_num')
    def get_detail_comment_num(self):
        return int(self.find_element(*self.detail_comment_num_loc).get_attribute('text'))

    detail_priase_loc = (By.ID, 'btn_praise')
    def click_detail_priase(self):
        self.find_element(*self.detail_priase_loc).click()

    detail_priase_num_loc = (By.ID, 'praise_num')
    def get_detail_priase_num(self):
        return int(self.find_element(*self.detail_priase_num_loc).get_attribute('text'))


    """评论框元素和方法"""
    emoji_loc = (By.ID, 'btn_emoji')
    def click_emoji(self):
        self.find_element(*self.emoji_loc).click()

    edit_comment_loc = (By.ID, 'edit')
    def set_comment(self,message):
        self.find_element(*self.edit_comment_loc).send_keys(message).get()

    gift_loc = (By.ID, 'btn_gift')
    def click_gift(self):
        self.find_element(*self.gift_loc).click()

    send_loc = (By.ID, 'btn_send')
    def click_send(self):
        self.find_element(*self.send_loc).click()

    content_loc = (By.ID, 'content')
    def get_contents(self):
        return self.find_elements(*self.content_loc)

    def now_comment_is_exist(self, message):
        for item in self.get_contents():
            if item.get_attribute('text') == message:
                return True
        return False



