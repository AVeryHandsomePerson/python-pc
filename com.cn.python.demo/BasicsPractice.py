# -*- coding: utf-8 -*-
import re
import requests
from lxml import etree

if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }
    # url = "https://item.jd.com/11584281.html"
    url = "https://www.douban.com/group/minimalists/discussion?start=25"
    urls = "https://sclub.jd.com/comment/productCommentSummaries.action?referenceIds=11584281"
    # https://sclub.jd.com/comment/productCommentSummaries.action?referenceIds=11584281&callback=jQuery4393158&_=1574165521492
    response = requests.get(url, timeout=30, headers=head)
    response.encoding = 'gbk'
    # 页面源码
    html = response.text
    content = etree.HTML(html)
    print(html)
    print(re.findall(r'"CommentCountStr":"([\d\D]*?)",', html, re.S))
