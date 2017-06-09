# coding:utf-8
from page_obj.user_posting_log_page import UserPostingLogPage
from models.myunit import MyTest
from models.driver import AppiumDriver
from utils.cancle_dialog import CancleDialog
from utils.screenshot import screenshot
from utils.logger import Logger
from utils.touch_actions import SwipeAction
from time import sleep


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
        # 获得页面信息  评论数和点赞数
        self.comment_num = self.uplp.get_comment_num()
        self.priase_num = self.uplp.get_praise_num()

    def test_post1(self):
        """发帖记录页点赞测试"""
        try:
            if len(self.uplp.get_all_log()) == 0:
                Logger.info('跳过测试，该用户没有发过帖子')
                self.skipTest('该用户没有发过帖子')
            self.uplp.click_priase() # 点赞按钮
            new_priase_num = self.uplp.get_praise_num()
            self.assertTrue(abs(new_priase_num - self.priase_num) == 1, '点赞失败')
            Logger.info('点赞测试成功')
        except AssertionError, msg:
            screenshot()
            print msg
            Logger.error(msg)

    def test_post2(self):
        """帖子详情内点赞测试"""
        try:
            if len(self.uplp.get_all_log()) == 0:
                Logger.info('跳过测试，该用户没有发过帖子')
                self.skipTest('该用户没有发过帖子')
            self.uplp.click_log_detail()
            self.uplp.click_detail_priase()
            new_priase_num = self.uplp.get_detail_priase_num()
            self.assertTrue(abs(new_priase_num - self.priase_num) == 1, '帖子详情内点赞失败')
            Logger.info('帖子详情内点赞测试通过')
        except AssertionError, msg:
            screenshot()
            print msg
            Logger.error(msg)

    def test_post3(self):
        """帖子详情内评论测试"""
        try:
            if len(self.uplp.get_all_log()) == 0:
                Logger.info('跳过测试，该用户没有发过帖子')
                self.skipTest('该用户没有发过帖子')
            self.uplp.click_log_detail()
            self.uplp.set_comment(u'我是个测试数据6')
            self.uplp.click_send()
            SwipeAction(self.driver).pull_refresh(0.75, 0.25, 1000, u'再怎么找也没有啦')
            is_exist = self.uplp.now_comment_is_exist(u'我是个测试数据6')
            self.assertTrue(is_exist == True, '发表评论失败')
            Logger.info('帖子详情内评论测试通过')
        except AssertionError, msg:
            screenshot()
            print msg
            Logger.error(msg)