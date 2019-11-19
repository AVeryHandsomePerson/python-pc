# -*- coding: utf-8 -*-
import re
import time

import pymysql
import requests
from lxml import etree
import time;


class DatabaseAccess():
    # 初始化属性
    def __init__(self):
        self.__db_host = "60.205.168.159"
        self.__db_port = 3306
        self.__db_user = "root"
        self.__db_password = "ljh"
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
    def linesinsert(self, book_name, witer_name, url, dt):
        try:
            # 连接数据库
            self.isConnectionOpen()
            # 创建游标
            global cursor
            cursor = self.__db.cursor()
            # sql命令
            sql = "insert into jd(book_name,witer_name,url,dt) value(%s,%s,%s,%s)"
            # 执行sql命令
            cursor.execute(sql, (book_name, witer_name, url, dt))
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 提交
            self.__db.commit()
            # 关闭数据库连接
            self.__db.close()


def get_html(urls, headers):
    response = requests.get(urls, timeout=30, headers=headers)
    response.encoding = 'utf-8'
    # 页面源码
    html = response.text
    return html


def read_jd_book(url, head):
    # 模拟浏览器发送http请求
    # response = requests.get(url, timeout=30, headers=head)
    # response.encoding = 'utf-8'
    # # 页面源码
    # html = response.text
    content = etree.HTML(get_html(url, head))
    content_book = content.xpath('//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')
    for i in range(1, 31):
        try:
            result = re.split(r":", content_book[i - 1])[1]
            content_book[i - 1] = result
        except Exception as e:
            continue
    db = DatabaseAccess()
    dt = time.strftime("%Y-%m-%d", time.localtime())
    for i in content_book:
        http = "https:" + i
        read_son_book(http, head, db, dt)
        time.sleep(2)
        print('----------%s' % '运行中')


def read_son_book(urls, headers, db, dt):
    response = requests.get(urls, timeout=30, headers=headers)
    response.encoding = 'gbk'
    # 页面源码
    html = response.text
    content = etree.HTML(html)
    book_name = re.findall(r'《([\d\D]*?)》', content.xpath('string(//head/title)'), re.S)[0]
    product_id = re.findall(r'item.jd.com/(\d*).html', urls)[0]
    url = "https://sclub.jd.com/comment/productCommentSummaries.action?referenceIds=%s" % product_id
    json = get_html(url, headers)
    product_count = re.findall(r'"CommentCountStr":"([\d\D]*?)",', json, re.S)[0]
    try:
        book_writer = re.findall(r'\(([\d\D]*?)\)', content.xpath('string(//head/title)'), re.S)[0]
    except Exception as e:
        book_writer = content.xpath('string(//div[@class="p-author"]/a)')

    print(book_name, book_writer, product_count)
    # db.linesinsert(book_name, book_writer, urls, dt)


if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }
    url = "https://search.jd.com/Search?keyword=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB%E4%B9%A6&enc=utf-8&psort=4&page=3"
    read_jd_book(url, head)
