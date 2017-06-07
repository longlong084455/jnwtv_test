# coding:utf-8
from jnwtv.test_case.models.base_page import Page
from selenium.webdriver.common.by import By

class UserInfoBasePage(Page):
    """通用元素和方法"""
    login_user_info_loc = (By.CLASS_NAME, 'android.widget.ImageButton')  # 进入个人中心的按钮

    def login_user_info_btn(self):
        self.find_element(*self.login_user_info_loc).click()

    base_back_loc = (By.ID, 'android.widget.ImageButton')
    def base_back_btn(self):
        self.find_element(*self.base_back_loc).click()

    title_loc = (By.ID, 'title')
    def get_title(self):
        return self.find_element(*self.title_loc).get_attribute('text')