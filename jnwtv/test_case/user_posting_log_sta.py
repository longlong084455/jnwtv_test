# coding:utf-8
from page_obj.user_posting_log_page import UserPostingLogPage
from models.myunit import MyTest
from models.driver import AppiumDriver
from utils.cancle_dialog import CancleDialog
from utils.screenshot import screenshot


class UserPostingLogTest(MyTest):
    def setUp(self):
        self.driver = AppiumDriver().start_appium('4723', 1)
        self.cancle_dialog = CancleDialog(self.driver)
        self.cancle_dialog.cancle_update()
        self.cancle_dialog.cancle_daily_share()
        self.cancle_dialog.cancle_vote()
        self.uplp = UserPostingLogPage(self.driver)
        self.uplp.login_user_info_btn() # 进入个人中心
        self.uplp.login_posting_btn() # 进入发帖记录

    def test_post1(self):
        try:
            self.uplp.login_posting_btn()
        except AssertionError, msg:
            screenshot()
            print msg
