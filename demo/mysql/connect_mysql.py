# coding:utf-8
import MySQLdb

"""
        host: 192.168.1.110
    username: jnwtest
    password: jnwtest2015
    database: jnwtv2_0_1

"""
HOST = '192.168.1.110'
USERNAME = 'jnwtest'
PASSWORD = 'jnwtest2015'
DATABASE = 'jnwtv2_0_1'


class ConnectSQL:
    # 静态实例变量
    __database = None
    __cursor = None

    def __init__(self, host, user, pwd, db):
        self.__database = MySQLdb.connect(host, user, pwd, db)
        self.__cursor = self.__database.cursor()

    def release(self):
        self.__database.close()

    def select(self, select_sql):
        self.__cursor.execute(select_sql)
        result = self.__cursor.fetchall()
        return result

    def commit(self, commit_sql):
        try:
            self.__cursor.execute(commit_sql)
            self.__database.commit()
        except :
            self.__database.rollback()


if __name__ == '__main__':
    conn = ConnectSQL(HOST, USERNAME, PASSWORD, DATABASE)
    sql = """
            SELECT ui.account, ui.user_nick, ui.mobile 
            FROM u_user_info ui 
            WHERE ui.account like '177%'
            """
    data = conn.select(select_sql=sql)
    conn.release()
    user_list = []
    for item in data:
        user_info = {}
        user_info.setdefault('account', item[0])
        user_info.setdefault('user_nick', item[1])
        user_info.setdefault('mobile', item[2])
        user_list.append(user_info)
        break
    print user_list


