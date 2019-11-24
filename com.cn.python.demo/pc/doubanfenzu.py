# -*- coding: utf-8 -*-
import json
import re
import time

import pymysql
from lxml import etree
import requests


class DatabaseAccess():
    # 初始化属性
    def __init__(self):
        self.__db_host = "60.205.168.159"
        self.__db_port = 3306
        self.__db_user = "root"
        self.__db_password = "123456"
        self.__db_database = "pc"

    # 链接数据库
    def isConnectionOpen(self):
        self.__db = pymysql.connect(
            host=self.__db_host,
            port=self.__db_port,
            user=self.__db_user,
            password=self.__db_password,
            database=self.__db_database,
            charset='utf8'
        )

    # 插入数据
    def linesinsert(self, grouping_name, grouping_personnel):
        try:
            # 连接数据库
            self.isConnectionOpen()
            # 创建游标
            global cursor
            cursor = self.__db.cursor()
            # sql命令
            sql = "insert into db_grouping(grouping_name,grouping_personnel) value(%s,%s)"
            # 执行sql命令
            cursor.execute(sql, (grouping_name, grouping_personnel))
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 提交
            self.__db.commit()
            # 关闭数据库连接
            self.__db.close()


def dob_fenzu(url, head):
    db = DatabaseAccess()
    response = requests.get(url, timeout=30, headers=head)
    context = response.content.decode("utf-8")
    html = json.loads(context)
    print(html['more'])
    if html['more']:
        for i in html['items']:
            zf_names = re.findall(r'alt="([\d\D]*?)">', i, re.S)
            arr_nuber = re.findall(r'<div class="info">([\d\D]*?)<', i, re.S)
            print(zf_names[0], re.findall(r'\d+', arr_nuber[0])[0])
            db.linesinsert(zf_names[0], re.findall(r'\d+', arr_nuber[0])[0])


if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 Safari/537.36',
        'Referer': 'https://www.douban.com/search?cat=1019&q=%E5%B0%8F%E7%BB%84',
        'Host': 'www.douban.com'
    }
    arr = ['%E6%9E%81%E7%AE%80', '%E6%96%AD%E8%88%8D%E7%A6%BB', '%E6%95%B4%E7%90%86', '%E7%AE%80%E6%9C%B4',
           '%E4%B8%8D%E6%8C%81%E6%9C%89']
    for name in arr:
        for i in range(1, 6):
            pag = (i - 1) * 20
            url = "https://www.douban.com/j/search?q={}&start={}&cat=1019".format(name, i)
            dob_fenzu(url, head)
            time.sleep(20)
