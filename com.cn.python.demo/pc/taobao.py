from lxml import etree
import re

import pymysql
import requests
import time
from lxml import etree

head = {
    'Host': 'login.taobao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.108 Safari/537.36',
    'Referer': 'https://www.taobao.com/'
}

url = "https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&search_type=item&imgfile=&q=%E6%9E%81%E7" \
      "%AE%80%E7%94%9F%E6%B4%BB%E4%B9%A6&_input_charset=utf-8 "

response = requests.get(url, timeout=20, headers=head)
response.content.decode('utf-8')
html = response.text
print(html)
# content = etree.HTML(html)
# content_book = content.xpath('//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')
