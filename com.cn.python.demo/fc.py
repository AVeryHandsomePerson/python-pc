# -*- coding: utf-8 -*-
import collections

import jieba

# print(jieba.lcut('中国是一个伟大的国家'))
# txt = open("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\test11.txt", encoding="utf-8").read()
txt = open("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\test1.txt", encoding="utf-8").read()
# stopwords = [line.strip() for line in open("E:\\PycharmProjects\\python-pc\\com.cn.python.demo\\百度停用词表.txt", encoding="utf-8").readlines()]
stopwords =[line.strip() for line in open("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\百度停用词表.txt", encoding="utf-8").readlines()]
# jieba.add_word('双11')
jieba.add_word('克制买')
jieba.add_word('买的冲动')
# jieba.load_userdict(stopwords)
jieba.load_userdict("D:\\biancheng\\python\\python-pc\\com.cn.python.demo\\fenci.txt")
words = jieba.lcut(txt)
counts = {}
lists = []
print("|".join(words))
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
    print(str(i[0]))
