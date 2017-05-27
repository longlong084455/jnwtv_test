# coding:utf-8
import os
import time
PATH = lambda p: os.path.abspath(p)
index = 1


def screenshot():
    path = PATH(os.getcwd() + "/result/image")
    timestamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    global index
    img_name = timestamp + '_' + str(index) + '.png'
    index += 1
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(PATH(os.getcwd() + "/result/image")):
        os.makedirs(path)
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + img_name))
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    print img_name
