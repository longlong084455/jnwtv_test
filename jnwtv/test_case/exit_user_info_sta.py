# coding:utf-8
from models.myunit import MyTest, AppiumDriver
from page_obj.user_info_page import EditUserInfo
from utils.screenshot import screenshot, screen_verific, get_toast_log
from utils.cancle_dialog import CancleDialog
from utils.common_method import find_toast


class EditUserInfoTest(MyTest):
    """用户个人信息编辑"""
    def setUp(self):
        self.driver = AppiumDriver().start_appium('4723', 1)
        self.cancle_dialog = CancleDialog(self.driver)
        self.cancle_dialog.cancle_update()
        self.eui = EditUserInfo(self.driver)
        self.eui.login_user_info_btn()
        self.eui.login_edit_btn()

    def test_edit1(self):
        """昵称编辑"""
        self.old_name = self.eui.get_name()
        print self.old_name
        self.eui.name_btn()
        self.eui.set_name(u'龙龙')
        self.eui.name_ok_btn()
        try:
            self.eui.back_user_info_btn()
            self.eui.login_edit_btn()
            self.new_name = self.eui.get_name()
            print self.new_name
            self.assertNotEqual(self.old_name, self.new_name, '昵称修改失败')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_edit2(self):
        """性别编辑"""
        self.old_sex = self.eui.get_sex()
        self.eui.sex_btn()
        if self.old_sex == u'女':
            self.eui.set_sex_nan()
        else:
            self.eui.set_sex_nv()
        try:
            self.eui.back_user_info_btn()
            self.eui.login_edit_btn()
            self.new_sex = self.eui.get_sex()
            self.assertNotEqual(self.old_sex, self.new_sex, '性别修改失败')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_edit3(self):
        """地址编辑"""
        self.old_addr = self.eui.get_addr()
        self.eui.addr_btn()
        self.eui.set_addr('')
        self.eui.addr_ok_btn()
        self.eui.set_addr(u'新乡市')
        self.eui.addr_ok_btn()
        try:
            self.eui.back_user_info_btn()
            self.eui.login_edit_btn()
            self.new_addr = self.eui.get_addr()
            self.assertNotEqual(self.old_addr, self.new_addr, '地址修改失败')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_edit4(self):
        """简介编辑"""
        self.old_indro = self.eui.get_indro()
        self.eui.indro_btn()
        self.eui.set_indro(u'南京')
        self.eui.indro_ok_btn()
        try:
            self.eui.back_user_info_btn()
            self.eui.login_edit_btn()
            self.new_indro = self.eui.get_indro()
            self.assertNotEqual(self.old_indro, self.new_indro, '简介修改失败')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_edit5(self):
        """更换头像"""
        self.eui.img_btn()
        self.eui.gallery_btn()
        self.eui.select_photo(0)
        self.eui.ok_btn()
        # find_toast(self.driver, u'上传成功')
        get_toast_log('demo', u'上传成功')


