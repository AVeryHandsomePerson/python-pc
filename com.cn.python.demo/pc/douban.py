# -*- coding: utf-8 -*-
import re

import time

import jieba as jieba
import requests
import collections

f1 = open('test1.txt', 'w+', encoding='utf-8')

headers = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

for f in range(0, 300, 25):
    url = "https://www.douban.com/group/minimalists/discussion?start=%s" % (f)
    # url = "http://www.jingcaiyuedu.com/novel/6L0go3.html"
    # 模拟浏览器发送http请求
    response = requests.get(url, timeout=30, headers=headers)
    response.encoding = 'utf-8'
    # 页面源码
    html = response.text
    # print(html)
    dl = re.findall(r'td class="title">([\d\D]*?)</td>', html, re.S)
    # print(dl[1])
    # chapter_info_list = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"',dl[1],re.S)

    # //提取名称
    for i in range(0, dl.__len__()):
        chapter_info_list = re.findall(r'<a href="([\d\D]*?)" title="', dl[i], re.S)
        chapter_info_lists = re.findall(r'title="([\d\D]*?)" class="', dl[i], re.S)
        # seg_list_exact = jieba.cut(chapter_info_lists[0], cut_all=False)
        # list.append(chapter_info_lists)
        # for word in seg_list_exact:
        #     print(word)
        f1.write(chapter_info_list[0] + "\t" +chapter_info_lists[0])
        f1.write('\n')
        # print(re.findall(r'\t|\n|\.|-|:|;|\)|\(|\?|"', chapter_info_lists[0], re.S))
        # print(chapter_info_list[0] + "\t" + chapter_info_lists[0])
    # print(chapter_info_list[0] + "\t" + chapter_info_lists[0])
    time.sleep(10)
    # url = chapter_info_list[0]
    # response = requests.get(url, timeout=30, headers=headers)
    # response.encoding = 'utf-8'
    # # 页面源码
    # html = response.text
    # nerong = re.findall(r'<class="topic-richtext"([\d\D]*?)" title="', html, re.S)
    # print(html)
