# coding:utf-8
from appium.webdriver.common.mobileby import By
from jnwtv.test_case.models.base_page import Page


class LoginPage(Page):
    # 界面元素
    login_loc = (By.ID, 'confirm')
    phone_loc = (By.ID, 'phone_edit')
    password_loc = (By.ID, 'password_edit')
    submit_loc = (By.ID, 'register_but')
    logout_loc = (By.ID, 'login_bottom_back')
    reset_password_loc = (By.ID, 'login_bottom_forget')

    def login(self):
        self.find_element(*self.login_loc).click()

    def login_phone(self, phone):
        self.find_element(*self.phone_loc).send_keys(phone)

    def login_password(self, pwd):
        self.find_element(*self.password_loc).send_keys(pwd)

    def submit(self):
        self.find_element(*self.submit_loc).click()

    def logout(self):
        self.find_element(*self.logout_loc).click()

    def reset_password(self):
        self.find_element(*self.reset_password_loc).click()

    def user_login(self, phone, password):
        self.login()
        self.login_phone(phone)
        self.login_password(password)
        self.submit()

    btn_confirm_loc = (By.ID, 'btn_confirm')
    message_loc = (By.ID, 'message')

    def btn_confirm(self):
        self.find_element(*self.btn_confirm_loc).click()

    def get_message(self):
        return self.find_element(*self.message_loc).get_attribute('text')

    title_loc = (By.ID, 'title')

    def get_title(self):
        return self.find_element(*self.title_loc).get_attribute('text')


class ThirdLogin(Page):
    """
    第三方登陆
    """
    '''界面元素'''
    wechat_login_loc = (By.ID, 'wechat_login')
    sina_login_loc = (By.ID, 'sina_login')
    qq_login_loc = (By.ID, 'qq_login')

    casual_login_loc = (By.ID, 'casually')

    """
    QQ 微博 授权确定元素
    """
    confirm_loc = (By.CLASS_NAME, 'android.widget.Button')

    def wechat_login(self):
        self.find_element(*self.wechat_login_loc).click()

    def sina_login(self):
        self.find_element(*self.sina_login_loc).click()
        self.find_element(*self.confirm_loc).click()

    def qq_login(self):
        self.find_element(*self.qq_login_loc).click()
        self.find_element(*self.confirm_loc).click()

    def casual_login(self):
        self.find_element(*self.casual_login_loc).click()
