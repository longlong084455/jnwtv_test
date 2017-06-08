# coding:utf-8
import time
from touch_actions import SwipeAction
from wait_element import *
from screenshot import screenshot


# 0 指用户登录状态 1 游客状态
def logout(self):
    if not wait_element_visible_by_id(self.driver, 'confirm', '不在登陆界面'):
        image_btn = self.driver.find_element_by_id('toolbar'). \
            find_element_by_class_name('android.widget.ImageButton')
        image_btn.click()
        if not wait_element_visible_by_id(self.driver, 'again', '不是游客模式'):
            SwipeAction(self.driver).swipe_up(1000)
            self.driver.find_element_by_id('layout_exit').click()
            self.driver.find_element_by_id('btn2').click()
        else:
            self.driver.find_element_by_id('again').click()
            image_btn.click()
            self.driver.find_element_by_id('login').click()


def is_casually(self):
    if wait_element_visible_by_id(self.driver, 'title', '不在游客模式状态'):
        return True
    return False


def find_toast(driver, msg):
    message = '//*[@text=\'{}\']'.format(msg)
    try:
        ele = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_all_elements_located(By.LINK_TEXT, msg))
    except:
        screenshot()


def sum_list(list1, list2):
    # 按顺序排列商品列表
    all = []
    for i in range(len(list1)):
        j = 0
        if i + j <= len(list2) - 1:
            for j in range(len(list2)):
                all.append(list1[i])
                all.append(list2[i + j])
                break
        else:
            all.append(list1[i])
    return all