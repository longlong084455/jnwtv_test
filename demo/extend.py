# coding:utf-8
# from abc import abstractmethod, ABCMeta
from unittest import TestCase
"""加个注释"""

class Parent:
    def __init__(self):
        print '777777'

    def test_demo(self):
        print '22222222222222 '


class Child(Parent):
    def test_demo(self):
        Parent().test_demo()
        print '1111111111111'


if __name__ == "__main__":
    Child().test_demo()