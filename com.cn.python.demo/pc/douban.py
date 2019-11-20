# -*- coding: utf-8 -*-
import collections
import re

import time

import jieba as jieba
import requests


def read_db():
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }
    list = []
    for f in range(0, 300, 25):
        url = "https://www.douban.com/group/minimalists/discussion?start=%s" % (f)
        # url = "http://www.jingcaiyuedu.com/novel/6L0go3.html"
        # 模拟浏览器发送http请求
        response = requests.get(url, timeout=30, headers=head)
        response.encoding = 'utf-8'
        # 页面源码
        html = response.text
        dl = re.findall(r'td class="title">([\d\D]*?)</td>', html, re.S)
        for i in range(0, dl.__len__()):
            # chapter_info_list = re.findall(r'<a href="([\d\D]*?)" title="', dl[i], re.S)
            chapter_info_lists = re.findall(r'title="([\d\D]*?)" class="', dl[i], re.S)
            # f1.write(chapter_info_list[0] + "\t" +chapter_info_lists[0])
            list.append(chapter_info_lists[0])
            # f1.write('\n')
        time.sleep(2)
    return list


def analyze():
    print(1)

if __name__ == '__main__':
    words = jieba.lcut(str(read_db()))
    stopwords = [line.strip() for line in
                 open("E:\\PycharmProjects\\python-pc\\com.cn.python.demo\\百度停用词表.txt", encoding="utf-8").readlines()]
    counts = {}
    lists = []
    jieba.load_userdict("E:\\PycharmProjects\\python-pc\\com.cn.python.demo\\abc.txt")
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
    word_counts_top10 = word_counts.most_common(20)
    print(word_counts_top10)
