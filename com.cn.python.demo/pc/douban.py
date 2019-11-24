# -*- coding: utf-8 -*-
import collections
import re

import time

import jieba as jieba
import pymysql
import requests
from lxml import etree


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
    def linesinsert(self, word_tmp, number, dt):
        try:
            # 连接数据库
            self.isConnectionOpen()
            # 创建游标
            global cursor
            cursor = self.__db.cursor()
            # sql命令
            sql = "insert into db(word_tmp,number_t,dt) value(%s,%s,%s)"
            # 执行sql命令
            cursor.execute(sql, (word_tmp, number, dt))
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 提交
            self.__db.commit()
            # 关闭数据库连接
            self.__db.close()


def read_db():
    ben = DatabaseAccess()
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }
    dt = time.strftime("%Y-%m-%d", time.localtime())
    #豆瓣小组话题
    for f in range(0, 600, 25):
        url = "https://www.douban.com/group/minimalists/discussion?start=%s" % (f)
        # 模拟浏览器发送http请求
        response = requests.get(url, timeout=30, headers=head)
        response.encoding = 'utf-8'
        # 页面源码
        html = response.text
        jx = etree.HTML(html)
        for i in range(2, 26):
            chapter_info_lists = jx.xpath(
                'string(//*[@id="content"]/div/div[1]/div[2]/table/tr[{}]/td[1])'.format(i)).replace(" ", "").replace(
                "\n", "")
            chapter_number = jx.xpath('string(//*[@id="content"]/div/div[1]/div[2]/table/tr[{}]/td[3])'.format(i))

            print(chapter_info_lists, chapter_number)
            ben.linesinsert(chapter_info_lists, chapter_number, dt)
        time.sleep(20)


if __name__ == '__main__':
    read_db()

