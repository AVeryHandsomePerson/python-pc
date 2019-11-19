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
    dl = re.findall(r'td class="title">([\d\D]*?)</td>', html, re.S)
    # //提取名称
    for i in range(0, dl.__len__()):
        chapter_info_list = re.findall(r'<a href="([\d\D]*?)" title="', dl[i], re.S)
        chapter_info_lists = re.findall(r'title="([\d\D]*?)" class="', dl[i], re.S)
        f1.write(chapter_info_list[0] + "\t" +chapter_info_lists[0])
        f1.write('\n')
    time.sleep(10)
def A():
    print(1)