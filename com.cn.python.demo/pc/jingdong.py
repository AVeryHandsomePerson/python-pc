# -*- coding: utf-8 -*-
import re

import pymysql
import requests
import time
from lxml import etree

proxies = {
    'http': '59.57.148.45:9999',
    'http': '117.28.97.91:9999',
    'http': '117.28.96.19:9999',
    'http': '183.154.52.124:9999',
    'http': '171.35.147.28:9999',
    'http': '120.83.111.93:9999',
    'http': '117.26.45.118:9999',
    'http': '114.239.42.236:9999',
    'http': '117.69.201.238:9999',
    'http': '117.95.192.196:9999',
    'http': '122.5.107.132:9999',
    'http': '114.239.29.184:9999',
    'http': '113.121.95.110:9999',
    'http': '117.28.97.179:9999',
    'http': '117.69.201.66:9999',
    'http': '49.89.103.197:9999',
    'http': '61.145.48.91:9999',
    'http': '106.111.53.157:9999',
    'http': '59.57.38.81:9999',
    'http': '59.57.149.35:9999',
    'http': '121.226.214.84:9999',
    'http': '106.122.169.71:9999',
    'http': '49.70.85.158:9999',
    'http': '183.154.51.102:9999',
    'http': '180.122.148.181:9999',
    'http': '120.83.105.180:9999',
    'http': '222.190.163.154:9999',
    'http': '49.89.84.79:9999',
    'http': '171.35.148.198:9999',
    'http': '117.28.96.50:9999',
    'http': '114.239.251.140:808',
    'http': '114.239.42.42:9999',
    'http': '106.122.169.145:9999',
    'http': '61.145.48.248:9999',
    'http': '117.28.96.198:9999',
    'http': '115.211.226.244:9999',
    'http': '115.210.71.9:9999',
    'http': '36.25.41.130:9999',
    'http': '113.120.39.107:9999',
    'http': '114.239.146.156:808',
    'http': '117.95.214.140:9999',
    'http': '114.239.254.244:9999',
    'http': '120.83.107.206:9999',
    'http': '27.152.90.142:9999',
    'http': '49.89.87.196:9999',
    'http': '49.70.85.11:9999',
    'http': '117.30.112.167:9999',
    'http': '59.57.149.121:9999',
    'http': '121.233.206.79:9999',
    'http': '182.35.82.29:9999',
    'http': '182.34.36.62:9999',
    'http': '60.13.42.246:9999',
    'http': '223.242.225.199:9999',
    'http': '27.152.2.179:9999',
    'http': '117.95.199.105:9999',
    'http': '106.122.169.11:9999',
    'http': '183.166.71.121:9999',
    'http': '117.28.96.14:9999',
    'http': '171.35.220.247:9999',
    'http': '114.239.147.32:808',
    'http': '27.152.91.228:9999',
    'http': '27.152.8.232:9999',
    'http': '113.124.93.251:9999',
    'http': '49.70.17.11:9999',
    'http': '182.35.86.60:9999',
    'http': '113.120.38.51:9999',
    'http': '114.239.255.113:9999',
    'http': '59.57.149.62:9999',
    'http': '183.166.70.254:9999',
    'http': '36.25.40.206:9999',
    'http': '61.145.8.192:9999',
    'http': '114.239.150.89:808',
    'http': '117.95.200.71:9999',
    'http': '59.57.149.194:9999',
    'http': '59.57.38.225:9999',
    'http': '117.28.97.189:9999',
    'http': '27.152.90.6:9999',
    'http': '117.69.201.247:9999',
    'http': '182.34.37.171:9999',
    'http': '27.152.91.216:9999',
    'http': '61.145.8.24:9999',
    'http': '123.54.44.116:9999',
    'http': '117.26.44.44:9999',
    'http': '183.166.110.59:9999',
    'http': '115.195.94.131:8118',
    'http': '113.124.85.179:61234',
    'http': '119.122.212.2:9000',
    'http': '49.89.103.119:9999',
    'http': '117.57.91.241:9999',
    'http': '183.166.163.154:9999',
    'http': '183.146.156.29:9999',
    'http': '27.43.189.38:9999',
    'http': '117.28.97.119:9999',
    'http': '114.239.172.186:9999',
    'http': '59.57.149.169:9999',
    'http': '27.152.90.93:9999',
    'http': '182.35.85.160:9999',
    'http': '59.57.148.60:9999',
    'http': '182.35.82.124:9999',
    'http': '59.57.149.24:9999',
    'http': '117.57.90.41:9999',
    'http': '125.78.176.89:9999',
    'http': '27.152.90.242:9999',
    'http': '114.239.255.143:9999',
    'http': '113.121.23.210:9999',
    'http': '180.175.16.50:9797',
    'http': '113.120.35.50:9999',
    'http': '117.28.97.61:9999',
    'http': '27.43.191.21:9999',
    'http': '114.239.173.144:9999',
    'http': '144.123.71.88:9999',
    'http': '117.28.97.194:9999',
    'http': '114.239.148.166:9999',
    'http': '171.35.222.112:9999',
    'http': '114.239.173.12:9999',
    'http': '117.30.113.35:9999',
    'http': '59.57.148.45:9999',
    'http': '117.28.97.91:9999',
    'http': '117.28.96.19:9999',
    'http': '183.154.52.124:9999',
    'http': '171.35.147.28:9999',
    'http': '120.83.111.93:9999',
    'http': '117.26.45.118:9999',
    'http': '114.239.42.236:9999',
    'http': '117.69.201.238:9999',
    'http': '117.95.192.196:9999',
    'http': '122.5.107.132:9999',
    'http': '114.239.29.184:9999',
    'http': '113.121.95.110:9999',
    'http': '117.28.97.179:9999',
    'http': '117.69.201.66:9999',
    'http': '49.89.103.197:9999',
    'http': '61.145.48.91:9999',
    'http': '106.111.53.157:9999',
    'http': '59.57.38.81:9999',
    'http': '59.57.149.35:9999',
    'http': '121.226.214.84:9999',
    'http': '106.122.169.71:9999',
    'http': '49.70.85.158:9999',
    'http': '183.154.51.102:9999',
    'http': '180.122.148.181:9999',
    'http': '120.83.105.180:9999',
    'http': '222.190.163.154:9999',
    'http': '49.89.84.79:9999',
    'http': '171.35.148.198:9999',
    'http': '117.28.96.50:9999',
    'http': '114.239.251.140:808',
    'http': '114.239.42.42:9999',
    'http': '106.122.169.145:9999',
    'http': '61.145.48.248:9999',
    'http': '117.28.96.198:9999',
    'http': '115.211.226.244:9999',
    'http': '115.210.71.9:9999',
    'http': '36.25.41.130:9999',
    'http': '113.120.39.107:9999',
    'http': '114.239.146.156:808',
    'http': '117.95.214.140:9999',
    'http': '114.239.254.244:9999',
    'http': '120.83.107.206:9999',
    'http': '27.152.90.142:9999',
    'http': '49.89.87.196:9999',
    'http': '49.70.85.11:9999',
    'http': '117.30.112.167:9999',
    'http': '59.57.149.121:9999',
    'http': '121.233.206.79:9999',
    'http': '182.35.82.29:9999',
    'http': '182.34.36.62:9999',
    'http': '60.13.42.246:9999',
    'http': '223.242.225.199:9999',
    'http': '27.152.2.179:9999',
    'http': '117.95.199.105:9999',
    'http': '106.122.169.11:9999',
    'http': '183.166.71.121:9999',
    'http': '117.28.96.14:9999',
    'http': '171.35.220.247:9999',
    'http': '114.239.147.32:808',
    'http': '27.152.91.228:9999',
    'http': '27.152.8.232:9999',
    'http': '113.124.93.251:9999',
    'http': '49.70.17.11:9999',
    'http': '182.35.86.60:9999',
    'http': '113.120.38.51:9999',
    'http': '114.239.255.113:9999',
    'http': '59.57.149.62:9999',
    'http': '183.166.70.254:9999',
    'http': '36.25.40.206:9999',
    'http': '61.145.8.192:9999',
    'http': '114.239.150.89:808',
    'http': '117.95.200.71:9999',
    'http': '59.57.149.194:9999',
    'http': '59.57.38.225:9999',
    'http': '117.28.97.189:9999',
    'http': '27.152.90.6:9999',
    'http': '117.69.201.247:9999',
    'http': '182.34.37.171:9999',
    'http': '27.152.91.216:9999',
    'http': '61.145.8.24:9999',
    'http': '123.54.44.116:9999',
    'http': '117.26.44.44:9999',
    'http': '183.166.110.59:9999',
    'http': '1.198.73.188:9999',
    'http': '60.13.42.62:9999',
    'http': '123.163.96.179:9999',
    'http': '49.86.180.144:9999',
    'http': '27.152.90.149:9999',
    'http': '114.239.145.206:39716',
    'http': '117.57.90.41:9999',
    'http': '125.78.176.89:9999',
    'http': '27.152.90.242:9999'
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
    response = requests.get(urls, timeout=100,  headers=headers)
    if bm == 'GBK':
        response.encoding = 'GBK'
    else:
        response.encoding = 'utf-8'
    # 页面源码
    html = response.text
    return html


def read_son_book(urls, headers, db, dt):
    response = requests.get(urls, timeout=100, headers=headers)
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
    db.linesinsert(book_name, book_writer, urls, product_count, dt)


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
        time.sleep(2)
    time.sleep(10)
    print('----------运行中')


if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3 '
    }
    # i = 1
    # for i in range(1, 20, 2):
    #     print(i)
    url = "https://search.jd.com/Search?keyword=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB%E4%B9%A6&enc=utf-8" \
          "&psort=4&page=5"
    read_jd_book(url, head)
    # i = 1 + i
