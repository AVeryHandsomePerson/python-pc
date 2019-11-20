# -*- coding: utf-8 -*-
import collections
import re

import time

import jieba as jieba
import pymysql
import requests


def read_db():
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }
    list = []
    for f in range(0, 600, 25):
        url = "https://www.douban.com/group/minimalists/discussion?start=%s" % (f)
        # 模拟浏览器发送http请求
        response = requests.get(url, timeout=30, headers=head)
        response.encoding = 'utf-8'
        # 页面源码
        html = response.text
        dl = re.findall(r'td class="title">([\d\D]*?)</td>', html, re.S)
        for i in range(0, dl.__len__()):
            chapter_info_lists = re.findall(r'title="([\d\D]*?)" class="', dl[i], re.S)
            list.append(chapter_info_lists[0])
        time.sleep(10)
    return list


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


if __name__ == '__main__':
    words = jieba.lcut(str(read_db()))
    stopwords = [line.strip() for line in
                 open("/root/file/百度停用词表.txt", encoding="utf-8").readlines()]
    counts = {}
    lists = []
    jieba.load_userdict("/root/file/fenci.txt")
    for word in words:
        # 不在停用词表中
        if word not in stopwords:
            # 不统计字数为一的词
            if len(word) == 1:
                continue
            else:
                lists.append(word)
                # counts[word] = counts.get(word,0) + 1
    word_counts = collections.Counter(lists)
    word_counts_top10 = word_counts.most_common(len(word_counts))
    dt = time.strftime("%Y-%m-%d", time.localtime())
    ben = DatabaseAccess()
    print("开始写入")
    for i in word_counts_top10:
        ben.linesinsert(i[0], i[1], dt)
