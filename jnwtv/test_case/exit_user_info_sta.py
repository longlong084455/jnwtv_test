# coding:utf-8
import unittest
from models.myunit import MyTest, AppiumDriver
from page_obj.user_info_page import EditUserInfoPage, UserToolsPage
from utils.screenshot import screenshot, screen_verific, get_toast_log
from utils.cancle_dialog import CancleDialog
from utils.common_method import find_toast

class EditUserInfoTest(MyTest):
    """用户个人信息编辑"""
    def setUp(self):
        self.driver = AppiumDriver().start_appium('4723', 1)
        self.cancle_dialog = CancleDialog(self.driver)
        self.cancle_dialog.cancle_update()
        self.eui = EditUserInfoPage(self.driver)
        self.eui.login_user_info_btn()
        self.eui.login_edit_btn()

    def test_edit1(self):
        """昵称编辑"""
        self.old_name = self.eui.get_name()
        self.eui.name_btn()
        self.eui.set_name(u'龙龙')
        self.eui.name_ok_btn()
        try:
            self.eui.back_user_info_btn()
            self.eui.login_edit_btn()
            self.new_name = self.eui.get_name()
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


class UserToolsTest(MyTest):
    """用户关注 粉丝 剧点 赏金 测试"""
    def setUp(self):
        self.driver = AppiumDriver().start_appium('4723', 1)
        self.cancle_dialog = CancleDialog(self.driver)
        self.cancle_dialog.cancle_update()
        self.cancle_dialog.cancle_daily_share()
        self.cancle_dialog.cancle_vote()
        self.tools = UserToolsPage(self.driver)
        self.tools.login_user_info_btn()
        self.attentions_num = int(self.tools.get_amount(0)) # 关注数
        self.fans_num = int(self.tools.get_amount(1)) # 粉丝数
        self.jpoint_num = int(self.tools.get_amount(2)) # 剧点数
        self.coupon_num = int(self.tools.get_amount(3)) # 代金券
        self.reward_num = int(self.tools.get_amount(4)) # 赏金数

    def test_tool1(self):
        """关注列表内搜索测试"""
        try:
            if self.attentions_num == 0:
                self.skipTest('该用户没有关注别人')
            self.tools.tv_amount_btn(0) # 进入关注列表
            self.tools.set_search() # 搜索框输入内容
            num = self.tools.get_attentions_list() # 获取搜索之后列表
            self.assertEqual('1', str(len(num)), '搜索失败')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool2(self):
        """取消关注测试"""
        try:
            if self.attentions_num == 0:
                self.skipTest('该用户没有关注别人')
            self.tools.tv_amount_btn(0) # 进入关注列表
            self.tools.login_attention_info() # 进入第一个位置的用户的详情
            self.tools.cancle_attention_btn() # 取消对该用户的关注
            self.tools.back_attention_btn() # 返回关注列表界面
            self.tools.back_btn() # 返回个人中心页面
            new_amount = self.tools.get_amount(0) # 获取现在的关注数
            # 判断取消关注之前的数值和现在的数字的差值是否为1
            self.assertEqual(str(int(self.attentions_num) - int(new_amount)), '1', '取消关注失败')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool3(self):
        """粉丝页面测试"""
        try:
            if self.fans_num == 0:
                self.skipTest('该用户没有粉丝')
            self.tools.tv_amount_btn(1)
            fans_list = self.tools.get_all_fans()
            self.assertTrue(int(self.fans_num) - int(len(fans_list)) >= 0, '粉丝页面错误')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool4(self):
        """测试关注用户是否可以添加到关注"""
        try:
            if self.fans_num == 0:
                self.skipTest('条件不满足，没办法测试')
            self.tools.tv_amount_btn(1)
            self.tools.login_fans_detail()
            self.tools.cancle_attention_btn()
            self.tools.back_attention_btn()
            self.tools.back_btn()
            new_attentions_num = int(self.tools.get_amount(0))
            self.assertTrue(new_attentions_num - self.attentions_num == 1, '关注用户失败')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool5(self):
        """测试剧点和代金券内外是否一致"""
        try:
            self.tools.tv_amount_btn(2)
            inner_jpoint = int(self.tools.get_point_num())
            inner_coupon = int(self.tools.get_coupon_num())
            self.assertTrue(self.coupon_num + self.jpoint_num == inner_coupon + inner_jpoint, '内外剧点不一致')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool6(self):
        """充值商品个数测试"""
        try:
            self.tools.tv_amount_btn(2)
            self.tools.recharge_btn()
            products = self.tools.get_product_num()
            self.assertTrue(products == 7, '商品数量不对')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool7(self):
        """充值方式个数测试"""
        try:
            self.tools.tv_amount_btn(2)
            self.tools.recharge_btn()
            self.tools.product_btn()
            pay_ways_num = len(self.tools.get_pay_ways()) - 2
            self.assertTrue(pay_ways_num == 3, '支付方式的个数不对')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool8(self):
        """cdkey兑换代金券测试"""
        try:
            self.tools.tv_amount_btn(2)
            self.tools.exchange_btn()
            self.tools.set_cdkey('GJGVFDKWVJKXHDQV')
            self.tools.submit_btn()
            self.tools.check_jpoint_btn()
            new_coupon_num = int(self.tools.get_coupon_num())
            self.assertTrue(new_coupon_num - self.coupon_num == 5, '兑换代金券失败')
        except AssertionError, msg:
            screenshot()
            print msg

    @unittest.skip('10.4数据没办法测试')
    def test_tool9(self):
        """代金券任务测试"""
        try:
            self.tools.tv_amount_btn(2)
            self.tools.task_btn()
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool10(self):
        """赏金兑换商品数量的测试"""
        try:
            self.tools.tv_amount_btn(4) # 进入赏金页面
            self.tools.coupon_exchange_btn() # 进入赏金兑换代金券页面
            exchange_products_num = len(self.tools.get_exchange_products_list()) # 获得所有兑换商品的数量
            self.assertTrue(exchange_products_num == 3, '赏金兑换商品数量不对')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool11(self):
        """赏金兑换代金券测试"""
        try:
            self.tools.tv_amount_btn(4) # 进入赏金
            self.tools.coupon_exchange_btn() # 进入兑换
            if self.reward_num == 0:
                self.skipTest('赏金为0.跳过此次测试')
            self.tools.exchange_product_btn() # 选择商品
            self.tools.coupon_exchange_btn() # 点击兑换
            self.tools.back_btn() # 返回赏金
            self.tools.back_btn() # 返回个人中心
            new_reward_num = int(self.tools.get_amount(4)) # 获取新的赏金数
            new_coupon_num = int(self.tools.get_amount(3)) # 获取新的代金券数
            self.assertTrue(self.reward_num - new_reward_num  == 100, '赏金兑换失败')
            self.assertTrue(new_coupon_num - self.coupon_num  == 25, '赏金兑换失败')
        except AssertionError, msg:
            screenshot()
            print msg

    def test_tool12(self):
        """赏金提现测试"""
        try:
            self.tools.tv_amount_btn(4)
            if self.tools.withdraw_is_exist():
                self.tools.withdraw_btn()
                verification_text = self.tools.get_withdraw_commit_text()
                self.assertEqual(verification_text, u'提交并保存', '进入提现界面失败')
            else:
                self.skipTest('该用户不是剧组成员，不具备提现功能')
        except AssertionError, msg:
            screenshot()
            print msg
