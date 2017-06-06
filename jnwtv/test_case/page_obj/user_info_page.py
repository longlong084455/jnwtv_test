# coding:utf-8
from jnwtv.test_case.models.base_page import Page
from selenium.webdriver.common.by import By

class EditUserInfoPage(Page):
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

    # 头像更换
    img_r_loc = (By.ID, 'personal_img_r')
    camera_loc = (By.ID, 'camera') # 相机
    gallery_loc = (By.ID, 'gallery') # 相册

    def img_btn(self):
        self.find_element(*self.img_r_loc).click()

    def camera_btn(self):
        self.find_element(*self.camera_loc).click()

    def gallery_btn(self):
        self.find_element(*self.gallery_loc).click()

    # 图片列表
    photos_loc = (By.ID, 'wrap_layout')
    back_btn_loc = (By.ID, 'btn_back') # 取消更换
    def back_btn(self):
        self.find_element(*self.back_btn_loc).click()

    def get_photos(self):
        return self.find_elements_by_id('wrap_layout')

    # 选择要修改的头像， 默认为第二张
    def select_photo(self, index=0):
        # 如果相册为空的话，返回原来的界面，选择去相机
        if len(self.get_photos()) == 0:
            return
        self.get_photos()[index].click()

    # 确认图片的页面
    cancel_loc = (By.ID, 'cancel')
    ok_loc = (By.ID, 'ok')
    def cancel_btn(self):
        self.find_element(*self.cancel_loc).click()

    def ok_btn(self):
        self.find_element(*self.ok_loc).click()


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

class UserToolsPage(Page):
    login_user_info_loc = (By.CLASS_NAME, 'android.widget.ImageButton')  # 进入个人中心的按钮
    # 进入个人中心
    def login_user_info_btn(self):
        self.find_element(*self.login_user_info_loc).click()


    # 用户的小功能
    tv_amount_loc = (By.ID, 'tv_amount')
    def get_tv_amounts(self):
        return self.find_elements_by_id('tv_amount')

    # 0 关注  1 粉丝  2 剧点 3 代金券 4 赏金
    def tv_amount_btn(self, index):
        """0 关注  1 粉丝  2 剧点 3 代金券 4 赏金"""
        self.get_tv_amounts()[index].click()

    def get_amount(self, index):
        """0 关注  1 粉丝  2 剧点 3 代金券 4 赏金"""
        return self.get_tv_amounts()[index].get_attribute('text')

    # 搜索输入框
    filter_edit_loc = (By.ID, 'filter_edit')
    def set_search(self, index=0):
        self.find_element(*self.filter_edit_loc).send_keys(self.get_atten_name()[index].get_attribute('text'))

    # 返回按钮
    back_loc = (By.CLASS_NAME, 'android.widget.ImageButton')
    def back_btn(self):
        self.find_element(*self.back_loc).click()

    # 关注列表
    item_layout_loc = (By.ID, 'item_layout')
    focuson_item_name_loc = (By.ID, 'focuson_item_name')
    def get_attentions_list(self):
        return self.find_elements(*self.item_layout_loc)

    def get_atten_name(self):
        return self.find_elements(*self.focuson_item_name_loc)

    # 进入关注的用户的详情
    def login_attention_info(self, index=0):
        self.get_attentions_list()[index].click()

    # 取消关注按钮
    btn_attention_loc = (By.ID, 'btn_attention')
    def cancle_attention_btn(self):
        self.find_element(*self.btn_attention_loc).click()

    # 返回关注列表的返回键
    iv_go_back_loc = (By.ID, 'iv_go_back')
    def back_attention_btn(self):
        self.find_element(*self.iv_go_back_loc).click()


    # 粉丝
    ll_item_fans_loc = (By.ID, 'll_item_fans')
    def get_all_fans(self):
        return self.find_elements(*self.ll_item_fans_loc)

    def login_fans_detail(self):
        self.get_all_fans()[0].click()


    # 剧点和代金券
    jpoint_num_loc = (By.ID, 'jpoint_num')
    coupon_num_loc = (By.ID, 'coupon_num')
    def get_point_num(self):
        return self.find_element(*self.jpoint_num_loc).get_attribute('text') # 获取内部的剧点

    def get_coupon_num(self):
        return self.find_element(*self.coupon_num_loc).get_attribute('text') # 获取内部的代金券

    # 充值按钮
    recharge_btn_loc = (By.ID, 'btn_charge')
    def recharge_btn(self):
        self.find_element(*self.recharge_btn_loc).click()

    # 兑换按钮
    exchange_btn_loc = (By.ID, 'top_up')
    def exchange_btn(self):
        self.find_element(*self.exchange_btn_loc).click()

    # 代金券任务按钮
    task_btn_loc = (By.ID, 'btn_jpoint_task')
    def task_btn(self):
        self.find_element(*self.task_btn_loc).click()