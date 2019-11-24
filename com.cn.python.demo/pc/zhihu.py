# -*- coding: utf-8 -*-
import json
import time

import pymysql
import requests
# from lxml import etree
from pymysql.constants.FIELD_TYPE import JSON


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
    def linesinsert(self, grouping_name, grouping_number):
        try:
            # 连接数据库
            self.isConnectionOpen()
            # 创建游标
            global cursor
            cursor = self.__db.cursor()
            # sql命令
            sql = "insert into zhihu(anwer_name,anwer_number) value(%s,%s)"
            # 执行sql命令
            cursor.execute(sql, (grouping_name, grouping_number))
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 提交
            self.__db.commit()
            # 关闭数据库连接
            self.__db.close()


def get_html(url, head):
    r = requests.get(url, headers=head)
    return r.content.decode('utf-8')


def start_end_pag(start):
    db = DatabaseAccess()
    pag = (int(start) - 1) * 20
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/74.0.3729.169 Safari/537.36'
    }
    url = "https://www.zhihu.com/api/v4/search_v3?t=general&q=%E6%96%AD%E8%88%8D%E7%A6%BB&correction=1" \
          "&offset={}&limit=20&lc_idx=24&show_all_topics=0&search_hash_id=32329e4d11b0e30572e37b7f670a10a3" \
          "&vertical_info=0%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C1 ".format(pag)
    html = get_html(url, head)
    context = json.loads(html)
    for i in context['data']:
        anwer_type = i['type']
        if anwer_type == 'search_result':
            anwer_name = i['highlight']['title'].replace("<em>", "").replace("</em>", "")
            anwer_number = i['object']['voteup_count']
            print(anwer_name, anwer_number)
            db.linesinsert(anwer_name, anwer_number)


if __name__ == '__main__':
    for i in range(1, 11):
        start_end_pag(i)
        time.sleep(20)
