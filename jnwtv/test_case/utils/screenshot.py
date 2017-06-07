# coding:utf-8
import os
import time
from pyocr import pyocr
from PIL import Image
tools = pyocr.get_available_tools()[:]
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
def screen_verific(name):
    path = PATH(os.getcwd() + "/result/verification_image")
    img_name = 'verification_' + name + '.png'
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(PATH(os.getcwd() + "/result/verification_image")):
        os.makedirs(path)
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + img_name))
    os.popen("adb shell rm /data/local/tmp/tmp.png")

def get_toast_log(name, msg):
    path = PATH(os.getcwd() + "/result/verification_image")
    img_name = 'verification_' + name + '.png'
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(PATH(os.getcwd() + "/result/verification_image")):
        os.makedirs(path)
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + img_name))
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    file_path = 'E:\\appium_work\\workplace\\jnwtv_1.0\\jnwtv\\test_case\\result\\verification_image\\' \
                'verification_' + name + '.png'
    tools[0].image_to_string(Image.open(file_path), )
