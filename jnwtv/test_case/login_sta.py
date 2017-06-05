# coding:utf-8
from models.myunit import MyTest
from page_obj.login_page import LoginPage, ThirdLogin
from utils.screenshot import screenshot
from utils.cancle_dialog import CancleDialog
from utils.common_method import logout
from jnwtv.test_case.models.driver import AppiumDriver


class LoginTest(MyTest):
    """登录测试"""
    def setUp(self):
        # super(LoginTest, self).setUp()
        self.driver = AppiumDriver().start_appium('4723', 0)
        # 如果有系统更新的话，直接取消更新
        self.cancle_dialog = CancleDialog(self.driver)
        self.cancle_dialog.cancle_update()
        # 用户名密码登陆的实例
        self.lp = LoginPage(self.driver)
        # 三方登陆的实例
        self.tp = ThirdLogin(self.driver)

    def user_login_verify(self, phone='', password=''):
        self.lp.user_login(phone, password)

    def test_login1(self):
        """用户名、密码为空"""
        self.user_login_verify()
        try:
            self.assertEqual(self.lp.get_message(), u'请输入正确的手机号码', '手机号输入格式错误的提示不正确')
        except AssertionError, msg:
            screenshot()
            print msg
        finally:
            self.lp.btn_confirm()
            self.lp.logout()

    def test_login2(self):
        """用户名正确、密码为空"""
        self.user_login_verify(phone='17737150711')
        try:
            self.assertEqual(self.lp.get_message(), u'密码不能少于6位！！！', '密码格式不正确的时候的提示不正确')
        except AssertionError, msg:
            screenshot()
            print msg
        finally:
            self.lp.btn_confirm()
            self.lp.logout()

    def test_login3(self):
        """用户名为空、密码正确"""
        self.user_login_verify(password='123456')
        try:
            self.assertEqual(self.lp.get_message(), u'请输入正确的手机号码', '手机号输入格式错误的提示不正确')
        except AssertionError, msg:
            screenshot()
            print msg
        finally:
            self.lp.btn_confirm()
            self.lp.logout()

    def test_login4(self):
        """用户名正确、密码正确"""
        self.user_login_verify(phone='15601732620', password='123456')
        try:
            self.cancle_dialog.cancle_daily_share()
            self.cancle_dialog.cancle_vote()
            self.assertEqual(self.lp.get_title(), u'最新', '登录失败')
        except AssertionError, msg:
            screenshot()
            print msg
        finally:
            print '退出'
            logout(self, 0)

    def test_sina_login(self):
        """微博登陆"""
        self.tp.sina_login()
        try:
            self.cancle_dialog.cancle_daily_share()
            self.cancle_dialog.cancle_vote()
            self.assertEqual(self.lp.get_title(), u'剧能玩', '登录失败')
        except AssertionError, msg:
            screenshot()
            print msg
        finally:
            logout(self, 0)

    def test_qq_login(self):
        """QQ登陆"""
        self.tp.qq_login()
        try:
            self.cancle_dialog.cancle_daily_share()
            self.cancle_dialog.cancle_vote()
            self.assertEqual(self.lp.get_title(), u'剧能玩', '登录失败')
        except AssertionError, msg:
            screenshot()
            print msg
        finally:
            logout(self, 0)

    # def test_casual_login(self):
    #     """游客登陆"""
    #     print self.driver.get_settings()
    #     # 判断当前页面是否在游客模式下
    #     if is_casually(self):
    #         logout(1)
    #     self.tp.casual_login()
    #     try:
    #         CancleDialog(self.driver).cancle_daily_share()
    #         self.assertEqual(self.lp.get_title(), u'剧能玩', '登陆失败')
    #     except AssertionError, msg:
    #         screenshot()
    #         print msg
    #     finally:
    #         logout(self, 1)

