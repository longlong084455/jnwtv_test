# coding:utf-8
from xml.dom import minidom
from appium import webdriver


class AppiumDriver:
    def __init__(self):
        pass

    def start_appium(self, port, index=0):
        driver = webdriver.Remote('http://127.0.0.1:' + port + '/wd/hub', self.get_data(index))
        return driver

    @staticmethod
    def get_data(index):
        desired_caps = {'unicodeKeyboard': True, 'resetKeyboard': True}
        dom = minidom.parse('E:\\appium_work\\workplace\\jnwtv_1.0\\jnwtv\\data\\data.xml')
        root = dom.documentElement
        brands = root.getElementsByTagName('brand')
        packages = root.getElementsByTagName('package')
        for brand in brands:
            if brand.getAttribute("name") == 'oppo R9':
                desired_caps['deviceName'] = brand.getElementsByTagName('deviceName')[0].firstChild.data
                desired_caps['platformName'] = brand.getElementsByTagName('platformName')[0].firstChild.data
                desired_caps['platformVersion'] = brand.getElementsByTagName('platformVersion')[0].firstChild.data
        for package in packages:
            if package.getAttribute('name') == 'jnwtv':
                desired_caps['appPackage'] = package.getElementsByTagName('appPackage')[0].firstChild.data
                desired_caps['appActivity'] = package.getElementsByTagName('appActivity')[0].firstChild.data
                desired_caps['appWaitActivity'] = package.getElementsByTagName('appWaitActivity')[index].firstChild.data
        return desired_caps

