# -*- coding: utf-8 -*-
import json
import re

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
    response.encoding = 'utf-8'
    html = response.text
    content = etree.HTML(html)
    fz = content.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div[2]/div/h3/a/text()')
    for i in range(1, len(fz) - 1):
        fz_name = fz[i]
        number = re.findall(r'\d+', content.xpath(
            'string(//*[@id="content"]/div/div[1]/div[3]/div[2]/div[{}]/div[2]/div/div)'.format(i)))
        print('{}==={}'.format(fz_name, number[0]))
        db.linesinsert(fz_name, number[0])


def jt_fz():
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 Safari/537.36',
        'Referer': 'https://www.douban.com/search?cat=1019&q=%E5%B0%8F%E7%BB%84',
        'Host': 'www.douban.com'
    }
    urls = "https://www.douban.com/j/search?q=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB&start=20&cat=1019"
    db = DatabaseAccess()
    response = requests.get(urls, timeout=30, headers=head)
    response.encoding = 'utf-8'
    html = response.text.replace("'", "\"").replace("\\", "")
    zf_names = re.findall(r'alt="([\d\D]*?)">', html, re.S)
    arr_nuber = re.findall(r'<div class="info">([\d\D]*?)<', html, re.S)
    for i in range(0, len(zf_names)):
        # print(zf_names[i],re.findall(r'\d+',arr_nuber[i])[0])
        db.linesinsert(zf_names[i], re.findall(r'\d+', arr_nuber[i])[0])


if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 Safari/537.36',
        'Referer': 'https://www.douban.com/search?cat=1019&q=%E5%B0%8F%E7%BB%84',
        'Host': 'www.douban.com'
    }

    url = "https://www.douban.com/search?cat=1019&q=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB"
    dob_fenzu(url, head)
    jt_fz()
