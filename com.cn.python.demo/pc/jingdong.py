# -*- coding: utf-8 -*-
import re

import pymysql
import requests
import time
from lxml import etree

proxies = {
'http': '58.218.92.81:8314',
'http': '58.218.92.173:5257',
'http': '58.218.92.173:2023',
'http': '58.218.92.172:8842',
'http': '58.218.92.172:7091',
'http': '58.218.92.171:8124',
'http': '58.218.92.170:3671',
'http': '58.218.92.81:8895',
'http': '58.218.92.81:6774',
'http': '58.218.92.171:2105',
'http': '58.218.92.171:6379',
'http': '58.218.92.171:3828',
'http': '58.218.92.81:2815',
'http': '58.218.92.174:4580',
'http': '58.218.92.173:9966',
'http': '58.218.92.173:8415',
'http': '58.218.92.170:6208',
'http': '58.218.92.172:3539',
'http': '58.218.92.170:7980',
'http': '58.218.92.172:4487',
'http': '58.218.92.167:9754',
'http': '58.218.92.86:9958',
'http': '58.218.92.167:9660',
'http': '58.218.92.86:9547',
'http': '58.218.92.167:9660',
'http': '58.218.92.86:9547',
'http': '58.218.92.167:9754',
'http': '58.218.92.86:9958'
}
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
    def linesinsert(self, book_name, witer_name, url, product_count, dt):
        try:
            # 连接数据库
            self.isConnectionOpen()
            # 创建游标
            global cursor
            cursor = self.__db.cursor()
            # sql命令
            sql = "insert into jd(book_name,witer_name,url,product_count,dt) value(%s,%s,%s,%s,%s)"
            # 执行sql命令
            cursor.execute(sql, (book_name, witer_name, url, product_count, dt))
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 提交
            self.__db.commit()
            # 关闭数据库连接
            self.__db.close()


def get_html(urls, headers, bm):
    response = requests.get(urls, timeout=100, proxies=proxies, headers=headers)
    if bm == 'GBK':
        response.encoding = 'GBK'
    else:
        response.encoding = 'utf-8'
    # 页面源码
    html = response.text
    return html


def read_son_book(urls, headers, db, dt):
    response = requests.get(urls, timeout=100,headers=headers)
    response.encoding = 'gbk'
    # 页面源码
    html = response.text
    content = etree.HTML(html)
    book_name = re.findall(r'《([\d\D]*?)》', content.xpath('string(//head/title)'), re.S)[0]
    product_id = re.findall(r'item.jd.com/(\d*).html', urls)[0]
    url = "https://sclub.jd.com/comment/productCommentSummaries.action?referenceIds=%s" % product_id
    json = get_html(url, headers, 'GBK')
    product_count = re.findall(r'"CommentCountStr":"([\d\D]*?)",', json, re.S)[0]
    try:
        book_writer = re.findall(r'\(([\d\D]*?)\)', content.xpath('string(//head/title)'), re.S)[0]
    except Exception as e:
        book_writer = content.xpath('string(//div[@class="p-author"]/a)')
    print(book_name)
    # db.linesinsert(book_name, book_writer, urls, product_count, dt)


def read_jd_book(url, head):
    # 模拟浏览器发送http请求
    content = etree.HTML(get_html(url, head, 'utf-8'))
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
        time.sleep(5)
    time.sleep(10)
    print('----------运行中')


if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }
    i = 1
    for i in range(1, 20, 2):
        print(i)
        url = "https://search.jd.com/Search?keyword=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB%E4%B9%A6&enc=utf-8" \
              "&psort=4&page=" + str(i)
        read_jd_book(url, head)
        i = 1 + i
