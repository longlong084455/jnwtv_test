# coding:utf-8
from models.myunit import MyTest
from page_obj.register_page import ResgisterPage
from utils.screenshot import screenshot
from utils.cancle_dialog import CancleDialog


class RegisterTest(MyTest):
    """注册测试"""
    def register_verify(self, phone='', password='', code=''):
        ResgisterPage(self.driver).user_register(phone, password, code)

    def test_register1(self):
        """没有输入正确的手机号格式"""
        self.register_verify(phone='123456789')
        re = ResgisterPage(self.driver)
        try:
            self.assertEqual(re.get_message(), u'亲，请输入正确的手机号 !!!', '手机号格式不正确的提示错误')
        except AssertionError, msg:
            screenshot()
            print msg
        finally:
            re.confirm()

    def test_register2(self):
        """正确的手机号格式、密码格式不正确"""
        self.register_verify(phone='12345678909', password='123')
        re = ResgisterPage(self.driver)
        try:
            self.assertEqual(re.get_message(), u'亲！！密码不能小于6位！！！', '密码格式不正确的提示错误')
        except AssertionError, msg:
            screenshot()
            print msg
        finally:
            re.confirm()

    def test_register3(self):
        """正确的手机号格式、密码格式正确、验证码为空"""
        self.register_verify(phone='12345678909', password='123456')
        re = ResgisterPage(self.driver)
        try:
            self.assertEqual(re.get_message(), u'验证码不能为空', '验证码为空的提示错误')
        except AssertionError, msg:
            screenshot()
            print msg
        finally:
            re.confirm()

    # def test_register4(self):
    #     """正确的手机号、正确的密码格式、正确的验证码"""
    #     self.register_verify(phone='17737150711', password='123456123', code='9874')
    #     re = ResgisterPage(self.driver)
    #     try:
    #         CancleDialog(self.driver).cancle_daily_share()
    #         self.assertEqual(re.get_title(), u'剧能玩', '登录失败')
    #     except AssertionError, msg:
    #         screenshot()
    #         print msg




