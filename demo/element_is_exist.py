# coding:utf-8
import time
from jnwtv.test_case.models.myunit import MyTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from jnwtv.test_case.utils.cancle_dialog import CancleDialog


class Utils:
    def __init__(self, driver):
        self.driver = driver
    # 获取屏幕的宽高

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 上下滑动，x轴不变   左右滑动，y轴不变
    def swipe_up(self, t):
        location = self.get_size()
        x1 = int(location[0] * 0.5)  # x轴坐标
        y1 = int(location[1] * 0.99)  # 滑动前y轴坐标
        y2 = int(location[1] * 0.01)  # 滑动后y轴坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 0 指用户登录状态 1 游客状态
    def logout(self, state):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.widget.ImageButton')), '找不到元素')
        image_btn = self.driver.find_element_by_class_name('android.widget.ImageButton')
        image_btn.click()
        if state == 0:
            time.sleep(3)
            self.swipe_up(1000)
            time.sleep(3)
            # 退出登录  btn2 确定  btn1 取消
            self.driver.find_element_by_id('layout_exit').click()
            self.driver.find_element_by_id('btn2').click()
        elif state == 1:
            self.driver.find_element_by_id('again').click()
            time.sleep(1)
            image_btn.click()
            time.sleep(1)
            self.driver.find_element_by_id('login').click()
            time.sleep(1)


class Demo(MyTest):
    def test_demo(self):
        Utils(self.driver).logout(0)
        CancleDialog(self.driver).cancle_update()
        self.confirm = self.driver.find_element_by_id('confirm')
        self.confirm.click()
        time.sleep(10)

    def wait_element_visible(self, ):
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(
                (By.ID, 'btn_update_now')), '没有版本更新')
            return True
        except Exception, msg:
            print msg
            return False


