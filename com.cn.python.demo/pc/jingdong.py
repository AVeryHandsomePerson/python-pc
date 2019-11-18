# -*- coding: utf-8 -*-
import re
import requests
from urllib import request
from bs4 import BeautifulSoup
from lxml import etree


def read_jdbook(url, head):
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
            content_book[i-1] = result
        except Exception as e:
            continue
    # for i in content_book:
        http = "https:"+content_book[0]
        read_sonBook(http,head)

    # for i in range(len(content)):
    #     print(content_book[i].tag)
    #     print(content_book[i].attrib)
    #     print(content_book[i].text)

def read_sonBook(url, head):
    response = requests.get(url, timeout=30, headers=head)
    response.encoding = 'utf-8'
    # 页面源码
    html = response.text
    content = etree.HTML(html)
    # content_book = content.xpath('//div[@class="w"]/div[@id="product-intro"]/div['
    #                              '@class="m-item-inner"]/div[@id="itemInfo"]/div[@id="choose"]/div['
    #                              '@id="choose-attrs"]/div[@id="choose-attr-1"]/div[@class="dd"]/div[@class="item  '
    #                              'selected"]/a/i')
    content_book = content.xpath('//div[@class="w"]/div[@id="product-intro"]/div[@id="preview"]/div['
                                 '@id=id="spec-n1"]/img/@alt')
    print(content_book)
    # content = etree.HTML(html)

if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }
    url = "https://search.jd.com/Search?keyword=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB%E4%B9%A6&enc=utf-8"
    read_jdbook(url, head)