# -*- coding: utf-8 -*-
import pymysql
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
    response = requests.get(urls, timeout=30, headers=headers)
    if bm == 'GBK':
        response.encoding = 'GBK'
    else:
        response.encoding = 'utf-8'
    # 页面源码
    html = response.text
    print(html)
    return html


if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }
    i = 1
    for i in range(1, 12, 2):
        url = "https://search.jd.com/Search?keyword=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB%E4%B9%A6&enc=utf-8" \
              "&psort=4&page=" + str(i)
        get_html(url, head, '1')
        i = 1 + i
