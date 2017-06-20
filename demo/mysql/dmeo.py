# coding:utf-8

name = None


def demo():
    global name
    print name + '11'
    name = 'longlong'
    print name + '222'


if __name__ == '__main__':
    name = 'hj'
    demo()
