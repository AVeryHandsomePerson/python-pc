# -*- coding: utf-8 -*-
import re
import time

import requests
from lxml import etree


def read_jd_book(url, head):
    # 模拟浏览器发送http请求
    response = requests.get(url, timeout=30, headers=head)
    response.encoding = 'utf-8'
    # 页面源码
    html = response.text
    content = etree.HTML(html)
    content_book = content.xpath('//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')
    for i in range(1, 31):
        try:
            result = re.split(r":", content_book[i - 1])[1]
            content_book[i - 1] = result
        except Exception as e:
            continue
    list = []
    for i in content_book:
        http = "https:" + i
        list.append(read_son_book(http, head))
        time.sleep(2)
        print('----------%s' % '运行中')
    return list


def read_son_book(urls, headers):
    response = requests.get(urls, timeout=30, headers=headers)
    response.encoding = 'gbk'
    # 页面源码
    html = response.text
    content = etree.HTML(html)
    # book_name = re.findall(r'《([\d\D]*?)》', content.xpath('//head/title/text()')[0], re.S)[0]
    # book_writer = re.findall(r'\(([\d\D]*?)\)', content.xpath('//head/title/text()')[0], re.S)[0]
    print(content.xpath('//head/title/text()')[0])
    return ''


if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }
    url = "https://search.jd.com/Search?keyword=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB%E4%B9%A6&enc=utf-8&psort=4&page=3"
    ben = read_jd_book(url, head)

    print(len(ben))
