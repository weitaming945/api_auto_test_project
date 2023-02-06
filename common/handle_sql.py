# -*- coding:utf-8 -*-
# @Time:2021/8/9 15:27
# @Author:lucky
# @Email:
# @File:handle_sql.py
import pymysql
from common.handle_config import conf
from common.handle_log import log

class HandleDB:


    def __init__(self,section):
        host = conf.get(section, "host")
        port = conf.get(section, "port")
        username = conf.get(section, "username")
        password = conf.get(section, "password")
        #打开数据库连接
        self.con = pymysql.connect(host=host,
                              port=eval(port),
                              user=username,
                              password=password,
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor #添加此属性时，自动转换成字典，多条数据时，返回列表，嵌套字典
                              )

    def find_all(self,sql):
        "查询查询到的所有数据"

        #con.cursor()，使用cursor()方法创建一个游标对象为cur
        with self.con.cursor() as cur:
            #使用execute()方法执行sql查询
            cur.execute(sql)

        res = cur.fetchall()
        cur.close()
        return res

    def find_one(self,sql):
        "查询一条数据"
        with self.con.cursor() as cur:
            cur.execute(sql)

        #cur.fetchone()方法获取单条数据
        res = cur.fetchone()
        #关闭不使用的游标对象
        cur.close()
        return res

    def find_count(self,sql):
        "sql执行后，返回的数据条数"
        with self.con.cursor() as cur:
            res = cur.execute(sql)
        cur.close()
        return res

    def delete_data(self,sql):
        """
        连接数据库，删除指定的数据，用于清除测试数据
        """
        try:
            with self.con.cursor() as cur:
                cur.execute(sql)
                #提交修改
                self.con.commit()
        except Exception as e :
            #发生错误时回滚
            self.con.rollback()
            log.info("数据库连接成功，数据删除失败")
            log.error(e)
        else:
            log.info("数据库连接成功，数据删除成功")






# 销毁对象
    def __del__(self):
        #关闭数据库连接
        self.con.close()

db = HandleDB("section")

if __name__ == '__main__':


    # db = HandleDB("section")
    # sql = 'SELECT id FROM cr_sanjiu.user_info where mobile = "00000000000"'
    sql = 'delete FROM cr_sanjiu.user_info where mobile = "00000000000"'
    db.delete_data(sql)
