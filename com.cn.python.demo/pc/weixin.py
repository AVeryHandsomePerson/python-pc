import random
import re
import time

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
    def linesinsert(self, gz_name, gz_number):
        try:
            # 连接数据库
            self.isConnectionOpen()
            # 创建游标
            global cursor
            cursor = self.__db.cursor()
            # sql命令
            sql = "insert into wx(gz_name,gz_number) value(%s,%s)"
            # 执行sql命令
            cursor.execute(sql, (gz_name, gz_number))
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 提交
            self.__db.commit()
            # 关闭数据库连接
            self.__db.close()


def getWXhtml(url, head):
    response = requests.get(url, timeout=30, headers=head)
    response.encoding = 'utf-8'
    html = response.text
    context = etree.HTML(html)
    db = DatabaseAccess()
    # sogou_vr_11002301_box_0
    urls = context.xpath('//*[@id="pagebar_container"]/div/text()')
    for i in range(10):
        a = context.xpath('//*[@id="sogou_vr_11002301_box_{}"]/div/div[2]/p[1]/a/text()'.format(i))
        em = context.xpath('//*[@id="sogou_vr_11002301_box_{}"]/div/div[2]/p[1]/a/em/text()'.format(i))
        number = re.findall(r'\d+', urls[0], re.S)
        fz_name = '{}{}'.format(''.join(a), ''.join(em))
        db.linesinsert(fz_name, number)
    # // *[ @ id = "sogou_vr_11002301_box_1"] / div / div[2] / p[1] / a / em[1]
    # print(html)


# //*[@id="sogou_vr_11002301_box_1"]/div/div[2]/p[1]/a/em[1]

if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 Safari/537.36',
        'Host': 'weixin.sogou.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3 '
    }
    for proxy in range(1, 11):

        url = "https://weixin.sogou.com/weixin?query=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB&_sug_type_=&sut=1506&lkt=1" \
              "%2C1574428792230%2C1574428792230&s_from=input&_sug_=n&sst0=1574428792333&page={}&ie=utf8&w=0 ".format(proxy)
        print(url)
        getWXhtml(url, head)
        time.sleep(20)
