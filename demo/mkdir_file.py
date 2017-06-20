# coding:utf-8
import os
import time
import random
import fileinput

PATH = lambda p: os.path.abspath(p)
path = PATH(os.getcwd() + "/data")
timestamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# f = open(timestamp+'.txt', 'w')
# for i in range(0,10):
#     f.write(str(random.randint(0,9)))
if os.path.exists(timestamp + '.txt'):
    for line in fileinput.input(timestamp + '.txt', inplace=1):
        line = line.replace('is_first_login:False', 'is_first_login:Fals')
        print line
    # f = open(timestamp + '.txt')
    # line = f.readline()
    # lines = f.readlines()
    # print lines
    # f.close()
    # lines[1].replace('False', 'True')
    # print lines[1]

    # d = {}
    # while line:
    #     print line
    #     data = line.split(':')
    #     line.replace('False', 'True')
    #     print data[1]
    #     line = f.readline()
    # f.close()
else:
    f = open(timestamp + 'txt', 'w')
