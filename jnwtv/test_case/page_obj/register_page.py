# coding:utf-8
import time
from ..models.base_page import Page
from selenium.webdriver.common.by import By
from ..utils.wait_element import *


class ResgisterPage(Page):
    """
        self.phone_edit = self.driver.find_element_by_id('phone_edit')
        self.password_edit = self.driver.find_element_by_id('password_edit')
        self.verification_code_edit = self.driver.find_element_by_id('verification_code_edit')
        self.get_verifition_but = self.driver.find_element_by_id('get_verifition_but')
        self.register_but = self.driver.find_element_by_id('register_but')
    """
    '''界面元素'''
    register_loc = 'register'  # ID
    phone_edit_loc = 'phone_edit'
    password_edit_loc = 'password_edit'
    verification_edit_loc = 'verification_code_edit'
    get_verification_loc = 'get_verifition_but'
    register_btn_loc = 'register_but'

    def register(self):
        self.find_element_by_id(self.register_loc).click()

    def input_phone(self, phone):
        self.find_element_by_id(self.phone_edit_loc).send_keys(phone)

    def input_password(self, password):
        self.find_element_by_id(self.password_edit_loc).send_keys(password)

    def input_verification(self, code):
        self.find_element_by_id(self.verification_edit_loc).send_keys(code)

    def verification_btn(self):
        self.find_element_by_id(self.get_verification_loc).click()

    def register_btn(self):
        self.find_element_by_id(self.register_btn_loc).click()

    def user_register(self, phone, password, code):
        self.register()
        self.input_phone(phone)
        self.input_password(password)
        self.verification_btn()
        # 判断是否出现弹出框，出现的话说明输入的用户名和密码不符合格式，此时不可以获得验证码
        # 没有出现说明输入的用户名和密码满足格式，可以获得验证码
        if not wait_element_visible_by_id(self.driver, 'btn_confirm', '验证码可以获得'):
            self.input_verification(code)
            self.register_btn()

    '''提示语'''
    message_loc = 'message'
    confirm_loc = 'btn_confirm'

    def get_message(self):
        return self.find_element_by_id(self.message_loc).get_attribute('text')

    def confirm(self):
        self.find_element_by_id(self.confirm_loc).click()

    '''注册成功后的验证字段'''
    title_loc = 'title'

    def get_title(self):
        return self.find_element_by_id(self.title_loc).get_attribute('text')
