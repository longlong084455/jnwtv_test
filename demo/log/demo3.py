# coding:utf-8
import logging
from unittest import TestCase


# 设置log文件的路径
log_file = './demo.log'
# 设置日志水平
log_level = logging.DEBUG

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
#
logger = logging.getLogger('')
hander = logging.FileHandler(log_file)
# 设置日志的输出格式
formatter = logging.Formatter("[%(lineno)d][%(module)s]"
                              "[%(levelname)s][%(funcName)s][%(asctime)s][%(message)s]")

hander.setFormatter(formatter)
logger.addHandler(hander)
logger.setLevel(log_level)

class ClassA(TestCase):
    def __init__(self):
        pass
    def func(self, name=0):
        try:
            print '%s是一个好人'
            self.assertTrue(name == '111')
        except Exception, e:
            logging.error(e)


ClassA().func('000')


# def func(name, ):
#     print name + '： 你好'
#
# if __name__ == '__main':
#     func('龙龙')

