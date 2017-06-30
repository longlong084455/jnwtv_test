# coding:utf-8
import json
from mysql.database import Database

class UserInfo:
    def __init__(self, account='17737150711'):
        if account == None:
            self._account = '17737150711'
        else:
            self._account = account
        self._data = self.load_data(self._account)[0]
        self.pwd = self._data['pwd'] # 密码 md5加密
        self.user_nick = self._data['user_nick'] # 用户昵称 显示乱码
        self.mobile = self._data['mobile'] # 用户手机号
        self.user_desc = self._data['user_desc'] # 用户个人简介
        self.head_img_url = self._data['head_img_url'] # 用户头像地址
        self.j_point = self._data['j_point'] # 用户剧点数
        self.coupon = self._data['coupon'] #　用户代金券数
        self.reward_mount = self._data['reward_mount'] # 用户赏金数
        self.used_reward_amt = self._data['used_reward_amt'] # 用户消耗赏金数
        self.attention_nums = self._data['attention_nums'] # 用户关注数量
        self.follower_nums = self._data['follower_nums'] #
        self.favouite_nums = self._data['favouite_nums']
        self.user_type = self._data['user_type'] # 用户类型0:正常用户 1:禁言 2:禁止登陆 3:VIP组
        self.sex = self._data['sex'] # 性别 0女1男2未知
        self.address = self._data['address'] # 地址
        self.id_no = self._data['id_no'] # 身份证号
        self.way = self._data['way'] # (方式)0:剧能玩用户 1:第三方登陆 2:游客
        self.user_token = self._data['user_token'] # 用户登录token
        self.user_role = self._data['user_role'] # 用户角色：1普通用户；2演职人员
        self.user_sub_role = self._data['user_sub_role'] #　演职人员类别区分：1:普通演员;2:可配音演员
        self.invite_code = self._data['invite_code'] # 用户邀请码
        self.is_invited = self._data['is_invited'] # 用户是否已经接受过邀请Y:是；N：否
        self.is_navy = self._data['is_navy'] # 是否是水军用户Y:是；N:否；
        self.is_gag = self._data['is_gag'] # 是否禁言用户：Y：是;N:否
        self.is_vip = self._data['is_vip'] #　是否是vip用户：Y:是;N:否;
        self.is_manager = self._data['is_manager'] #　是否是管理者（目前权限：水区/剧圈帖子删除；评论删除）Y:是；N:否
        self.total_invite_num = self._data['total_invite_num'] # 总邀请人数
        self.remain_invite_num = self._data['remain_invite_num'] # 剩余可用的的邀请人数
    def load_data(self, account):
        # data = Database().fetch_all('select '
        #                             'ui.account, ui.user_token, ui.user_role, ui.user_sub_role, '
        #                             'ui.is_vip, ui.is_manager '
        #                             'from u_user_info ui '
        #                             'where ui.account = \'%s\'' % (self._account))
        conn = Database()
        data = conn.fetch_all('select '
                                    '* '
                                    'from u_user_info ui '
                                    'where ui.account = \'%s\'' % (account))
        conn.close()
        return data


    def is_first_login(self):
        pass

if __name__ == '__main__':
    user_info = UserInfo()
    print user_info.head_img_url