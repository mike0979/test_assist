import pymysql

class Dao():
    def __init__(self):
        self.conn = pymysql.connect(host='172.16.10.41', port=3306, user='root', passwd='G_pids_2017', db='gz_pids', charset='utf8')
        self.cur = self.conn.cursor()
    def get_users(self, num):
        sql = 'SELECT account,password FROM tbl_user LIMIT ' + str(num)
        self.cur.execute(sql)
        return self.cur