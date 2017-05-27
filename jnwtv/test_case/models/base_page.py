# coding:utf-8


class Page(object):
    def __init__(self, appium_driver):
        self.driver = appium_driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_element_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def find_element_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def find_element_by_class_name(self, *loc):
        return self.driver.find_element_by_class_name(*loc)

    def find_element_by_link_text(self, *loc):
        return self.driver.find_element_by_link_text(*loc)

    def find_element_by_partial_link_text(self, *loc):
        return self.driver.find_element_by_partial_link_text(*loc)

    def find_elements_by_id(self, *loc):
        return self.driver.find_elements_by_id(*loc)

    def find_elements_by_name(self, *loc):
        return self.driver.find_elements_by_name(*loc)

    def find_elements_by_class_name(self, *loc):
        return self.driver.find_elements_by_class_name(*loc)

    def find_elements_by_link_text(self, *loc):
        return self.driver.find_elements_by_link_text(*loc)

    def find_elements_by_partial_link_text(self, *loc):
        return self.driver.find_elements_by_partial_link_text(*loc)


