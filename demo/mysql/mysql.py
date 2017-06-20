# coding:utf-8
import MySQLdb

HOST = '192.168.1.110'
USERNAME = 'jnwtest'
PASSWORD = 'jnwtest2015'
DATABASE = 'jnwtv2_0_1'


def get_instance():
    """初始化数据库"""
    database = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE, cursorclass=MySQLdb.cursors.DictCursor, )
    cursor = database.cursor()
    return database, cursor

def select(sql):
    try:
        (database, cursor) = get_instance()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception, e:
        print e






if __name__ == '__main__':
    sql = """
               SELECT ui.account, ui.user_nick, ui.mobile
               FROM u_user_info ui
               WHERE ui.account like '177%'
               """
    data = select(sql)
    print data
    user_list = []
    for item in data:
        user_info = {}
        print item
        user_info.setdefault('account', item['account'])
        user_info.setdefault('user_nick', item['user_nick'])
        user_info.setdefault('mobile', item['mobile'])
        user_list.append(user_info)
        break
    print user_list
