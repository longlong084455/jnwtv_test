# coding:utf-8
import logging
import time

# 设置log文件的路径
timestamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
log_file = 'E:\\appium_work\\workplace\\jnwtv_1.0\\logger\\' + timestamp + 'jnwtv_test_info.log'
# 设置日志水平
log_level = logging.INFO

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
#
Logger = logging.getLogger('')
hander = logging.FileHandler(log_file)
# 设置日志的输出格式
formatter = logging.Formatter(">%(levelname)s:[%(lineno)d][%(asctime)s]"
                              "[%(module)s][%(funcName)s] %(message)s")

hander.setFormatter(formatter)
Logger.addHandler(hander)
Logger.setLevel(log_level)