# coding:utf-8
import smtplib
import time
import os
import unittest
from email.header import Header
from email.mime.text import MIMEText



import HTMLTestRunner
from jnwtv.test_case.login_sta import LoginTest
from jnwtv.test_case.register_sta import RegisterTest
from jnwtv.test_case.exit_user_info_sta import EditUserInfoTest
from jnwtv.test_case.exit_user_info_sta import UserToolsTest



report_dir = 'E:\\appium_work\\workplace\\jnwtv_1.0\\jnwtv\\report'

# 发送邮件
def send_email(target_email, new_file):
    f = open(new_file, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('剧能玩自动化测试报告', 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com', port=25)
    smtp.login('longlong.li@jnwtv.com', 'Li13781421950')
    smtp.sendmail('longlong.li@jnwtv.com', target_email, msg.as_string())
    smtp.quit()
    print 'email has send out !!!'

# 获得最新的测试报告
def new_report(self):
    lists = os.listdir(self.report_dir)
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + '\\' + fn))
    file_new = os.path.join(self.report_dir, lists[-1])
    print file_new
    return file_new

def run_suite():
    # 声明一个测试套件
    suite = unittest.TestSuite()

    # 添加测试用例到测试套件
    # tests = [RegisterTest('test_register1'), RegisterTest('test_register2'), RegisterTest('test_register3'),
    #          LoginTest("test_login1"), LoginTest('test_login2'), LoginTest('test_login3'),
    #          LoginTest('test_sina_login'), LoginTest('test_qq_login'), LoginTest('test_login4'),
    #          EditUserInfoTest('test_edit1'), EditUserInfoTest('test_edit2'), EditUserInfoTest('test_edit3'),
    #          EditUserInfoTest('test_edit4'), EditUserInfoTest('test_edit5'),
    #          UserToolsTest('test_tool1'), UserToolsTest('test_tool2'), UserToolsTest('test_tool3'),
    #          UserToolsTest('test_tool4'), UserToolsTest('test_tool5'), UserToolsTest('test_tool6'),
    #          UserToolsTest('test_tool7'), UserToolsTest('test_tool8'), UserToolsTest('test_tool9'),
    #          UserToolsTest('test_tool10'), UserToolsTest('test_tool11'), UserToolsTest('test_tool12'), ]
    # tests = [LoginTest('test_sina_login'), LoginTest('test_qq_login'), LoginTest('test_login4'), ]
    # tests = [LoginTest('test_qq_login'), LoginTest('test_login4'), ]
    tests = [LoginTest('test_qq_login'), ]
    suite.addTests(tests)
    print suite.countTestCases()

    # 创建一个新的测试结果文件
    filename = 'jnwtv/report/' + time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())) + "jnwtvLog.html"
    fp = file(filename, 'wb')
    # 声明测试运行的对象
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                            title=u'剧能玩测试报告',
                                            description=u'用例测试情况')
    # 运行测试，并且将结果生成为HTML
    runner.run(suite)

    # 关闭文件输出
    fp.close()


if __name__ == '__main__':
    # 执行测试
    run_suite()

    # 发送测试结果
    # new_report = TestRunner().new_report()
    # TestRunner.send_email('948815501@qq.com', new_report)
