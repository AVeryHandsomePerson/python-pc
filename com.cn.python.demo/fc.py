# -*- coding: utf-8 -*-
import collections
import wordcloud  # 词云展示库
import jieba
from PIL import Image  # 图像处理库
import matplotlib.pyplot as plt  # 图像展示库
import numpy as np # numpy数据处理库
# print(jieba.lcut('中国是一个伟大的国家'))
# txt = open("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\test11.txt", encoding="utf-8").read()

txt = open("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\test1.txt", encoding="utf-8").read()
# stopwords = [line.strip() for line in open("E:\\PycharmProjects\\python-pc\\com.cn.python.demo\\百度停用词表.txt", encoding="utf-8").readlines()]
stopwords = [line.strip() for line in
             open("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\百度停用词表.txt", encoding="utf-8").readlines()]
# jieba.add_word('双11')
jieba.add_word('克制买')
jieba.add_word('买的冲动')
# jieba.load_userdict(stopwords)
jieba.load_userdict("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\fenci.txt")
words = jieba.lcut(txt)
lists = []
# print("|".join(words))
for word in words:
    # 不在停用词表中
    if word not in stopwords:
        # 不统计字数为一的词
        if len(word) == 1:
            continue
        else:
            lists.append(word)
            # counts[word] = counts.get(word,0) + 1
# items = list(counts.items())
# items.sort(key=lambda x:x[1], reverse=True)
# for i in range(30):
#     word, count = items[i]
#     print ("{:<10}{:>7}".format(word, count))
word_counts = collections.Counter(lists)
word_counts_top10 = word_counts.most_common(len(word_counts))

for i in word_counts_top10:
    print(str(i[0]), i[1])

mask = np.array(Image.open('D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\timg.jpg'))  # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
    mask=mask,  # 设置背景图
    max_words=200,  # 最多显示词数
    max_font_size=100  # 字体最大值
)

wc.generate_from_frequencies(word_counts)  # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
plt.imshow(wc)  # 显示词云
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图像
