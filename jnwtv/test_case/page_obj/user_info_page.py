# coding:utf-8
from jnwtv.test_case.models.base_page import Page
from selenium.webdriver.common.by import By

class EditUserInfo(Page):
    '''界面元素'''
    # nick_name_loc = (By.ID, 'tv_nick_name') # 昵称
    # user_desc_loc = (By.ID, 'tv_desc') # 简介
    #
    # def get_nick_name(self):
    #     return self.find_element(*self.nick_name_loc).get_attribute('text')
    #
    # def get_user_desc(self):
    #     return self.find_element(*self.user_desc_loc).get_attribute('text')
    login_user_info_loc = (By.CLASS_NAME, 'android.widget.ImageButton')  # 进入个人中心的按钮
    login_edit_info_loc = (By.ID, 'layout_personal')  # 进入编辑个人中心的按钮

    # 进入个人中心
    def login_user_info_btn(self):
        self.find_element(*self.login_user_info_loc).click()

    # 进入个人信息编辑
    def login_edit_btn(self):
        self.find_element(*self.login_edit_info_loc).click()

    back_user_info_loc = (By.CLASS_NAME, 'android.widget.ImageButton') # 返回个人中心
    def back_user_info_btn(self):
        self.find_element(*self.back_user_info_loc).click()

    # 名字
    name_r_loc = (By.ID, 'personal_name_r')
    name_c_loc = (By.ID, 'personal_name_c')
    name_edit_loc = (By.ID, 'name_dailog_edit')
    name_edit_cancle_loc = (By.ID, 'dialog_cancel')
    name_edit_ok_loc = (By.ID, 'dialog_ok')
    def name_btn(self):
        self.find_element(*self.name_r_loc).click()

    def get_name(self):
        return self.find_element(*self.name_c_loc).get_attribute('text')

    def set_name(self, name):
        self.find_element(*self.name_edit_loc).send_keys(name)

    def name_ok_btn(self):
        self.find_element(*self.name_edit_ok_loc).click()

    # 性别
    sex_r_loc = (By.ID, 'personal_sex_r')
    sex_c_loc = (By.ID, 'personal_sex_c')
    sex_nan_loc = (By.ID, 'sex1')
    sex_nv_loc = (By.ID, 'sex2')
    def sex_btn(self):
        self.find_element(*self.sex_r_loc).click()

    def get_sex(self):
        return self.find_element(*self.sex_c_loc).get_attribute('text')

    def set_sex_nan(self):
        self.find_element(*self.sex_nan_loc).click()

    def set_sex_nv(self):
        self.find_element(*self.sex_nv_loc).click()


    # 简介
    indro_r_loc = (By.ID, 'personal_introduction_r')
    indro_c_loc = (By.ID, 'jj_text')
    indro_edit_loc = (By.ID, 'jj_name_dailog_edit')
    indro_edit_cancle_loc = (By.ID, 'jj_dialog_cancel')
    indro_edit_ok_loc = (By.ID, 'jj_dialog_ok')
    def indro_btn(self):
        self.find_element(*self.indro_r_loc).click()

    def get_indro(self):
        return self.find_element(*self.indro_c_loc).get_attribute('text')

    def set_indro(self, indro):
        self.find_element(*self.indro_edit_loc).send_keys(indro)

    def indro_ok_btn(self):
        self.find_element(*self.indro_edit_ok_loc).click()

    # 地址
    addr_r_loc = (By.ID, 'personal_area_r')
    addr_c_loc = (By.ID, 'personal_area_c')
    addr_edit_loc = (By.ID, 'jj_name_dailog_edit')
    addr_edit_cancle_loc = (By.ID, 'jj_dialog_cancel')
    addr_edit_ok_loc = (By.ID, 'jj_dialog_ok')

    def addr_btn(self):
        self.find_element(*self.addr_r_loc).click()

    def get_addr(self):
        return self.find_element(*self.addr_c_loc).get_attribute('text')

    def set_addr(self, addr):
        self.find_element(*self.addr_edit_loc).send_keys(addr)

    def addr_ok_btn(self):
        self.find_element(*self.addr_edit_ok_loc).click()








