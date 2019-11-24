import collections

import jieba
import numpy as np
import pymysql
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt  # 图像展示库


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

    def selectData(self, table, ztname):
        # 连接数据库
        self.isConnectionOpen()
        # 创建游标
        global cursor
        cursor = self.__db.cursor()
        # sql命令
        sql = "select {} from {}".format(ztname, table)
        # 执行sql命令
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data


def fcRead():
    db = DatabaseAccess()

    list = []
    tablelist = ['zhihu,anwer_name']
    for table in tablelist:
        tables = table.split(",")[0]
        name = table.split(",")[1]
        data = db.selectData(tables, name)
        for datum in data:
            list.append(datum[0])
    print(len(list))
    stopwords = [line.strip() for line in
                 open("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\百度停用词表.txt", encoding="utf-8").readlines()]
    jieba.load_userdict("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\fenci.txt")
    words = jieba.lcut(str(list))
    lists = []
    for word in words:
        # 不在停用词表中
        if word not in stopwords:
            # 不统计字数为一的词
            if len(word) == 1:
                continue
            else:
                lists.append(word)
    return collections.Counter(lists)


def pictureCreate():
    word_counts = fcRead()
    mask = np.array(Image.open('D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\timg.jpg'))  # 定义词频背景
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
        mask=mask,  # 设置背景图
        max_words=600,  # 最多显示词数
        max_font_size=100,  # 字体最大值
    )

    wc.generate_from_frequencies(word_counts)  # 从字典生成词云
    image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
    wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐标轴
    # wordcloud.to_file("D:\\biancheng\\python\\python-pc\\douban.png")
    # plt.show()  # 显示图像
    plt.savefig("D:\\biancheng\\python\\python-pc\\zhihu.jpg", dpi=600)


if __name__ == '__main__':
    pictureCreate()
