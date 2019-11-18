# -*- coding: utf-8 -*-
import collections

import jieba

# print(jieba.lcut('中国是一个伟大的国家'))
txt = open("D:\\biancheng\\python\\pc\\com.cn.python.demo\\pc\\test1.txt", encoding="utf-8").read()
stopwords = [line.strip() for line in open("D:\\biancheng\\python\\pc\\com.cn.python.demo\\百度停用词表.txt", encoding="utf-8").readlines()]
jieba.add_word('双11')
jieba.add_word('双十一')
jieba.add_word('买了')
# jieba.load_userdict(stopwords)
words = jieba.lcut(txt)
counts = {}
lists = []
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
word_counts_top10 = word_counts.most_common(20)
# print(word_counts_top10)
for f in range(0,50,25):
    print(f)