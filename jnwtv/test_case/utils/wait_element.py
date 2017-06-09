# coding:utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def wait_element_visible_by_id(driver, loc, msg=None):
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.ID, loc)), msg)
        return True
    except Exception, msg:
        return False


def wait_element_visible_by_name(driver, loc, msg=None):
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.NAME, loc)), msg)
        return True
    except Exception, msg:
        return False


def wait_element_visible_by_class_name(driver, loc, msg=None):
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.CLASS_NAME, loc)), msg)
        return True
    except Exception, msg:
        return False


