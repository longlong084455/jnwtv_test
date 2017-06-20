# coding:utf-8
'''
使用方法：1.在主程序中先实例化DB Mysql数据库操作类。
      2.使用方法:db=database()  db.fetch_all("sql")
'''
import MySQLdb
import MySQLdb.cursors

HOST = '192.168.1.110'
USERNAME = 'jnwtest'
PASSWORD = 'jnwtest2015'
DATABASE = 'jnwtv2_0_1'


# 数据库操作类
class Database:
    def __init__(self, dbname=None, dbhost=None):
        # 这里的None相当于其它语言的NULL
        if dbname is None:
            self._dbname = DATABASE
        else:
            self._dbname = dbname
        if dbhost is None:
            self._dbhost = HOST
        else:
            self._dbhost = dbhost

        self._dbuser = USERNAME
        self._dbpassword = PASSWORD
        self._conn = self.connectMySQL()

        if (self._conn):
            self._cursor = self._conn.cursor()

    # 数据库连接
    def connectMySQL(self):
        conn = False
        try:
            conn = MySQLdb.connect(host=self._dbhost,
                                   user=self._dbuser,
                                   passwd=self._dbpassword,
                                   db=self._dbname,
                                   cursorclass=MySQLdb.cursors.DictCursor,
                                   )
        except Exception, data:
            conn = False
            print data, '11111111111'
        return conn

    # 获取查询结果集
    def fetch_all(self, sql):
        res = ''
        if (self._conn):
            try:
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception, data:
                res = False
                print data, '22222222222'
        return res

    def update(self, sql):
        flag = False
        if (self._conn):
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                flag = True
            except Exception, data:
                flag = False
                self._logger.warn("update database exception, %s" % data)

        return flag

    # 关闭数据库连接
    def close(self):
        if (self._conn):
            try:
                if (type(self._cursor) == 'object'):
                    self._cursor.close()
                if (type(self._conn) == 'object'):
                    self._conn.close()
            except Exception, data:
                print data, type(self._cursor), type(self._conn)


if __name__ == '__main__':
    sql = """
               SELECT ui.account, ui.user_nick, ui.mobile
               FROM u_user_info ui
               WHERE ui.account like '177%'
               """
    database = Database()
    data = database.fetch_all(sql)
    try:
        user_list = []
        for item in data:
            user_info = {}
            user_info.setdefault('account', item['account'])
            user_info.setdefault('user_nick', item['user_nick'])
            user_info.setdefault('mobile', item['mobile'])
            user_list.append(user_info)
            break
        print user_list
    except Exception, e:
        print e
    finally:
        database.close()

