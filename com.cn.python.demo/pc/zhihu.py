# -*- coding: utf-8 -*-
import json

import requests
# from lxml import etree
from pymysql.constants.FIELD_TYPE import JSON


def get_html(url, head):
    r = requests.get(url, headers=head)
    return r.content.decode('utf-8')


def start_end_pag(start):
    pag = (int(start) -1) *20
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/74.0.3729.169 Safari/537.36'
       }
    url = "https://www.zhihu.com/api/v4/search_v3?t=general&q=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB&correction=1" \
          "&offset={}&limit=20&lc_idx=24&show_all_topics=0&search_hash_id=32329e4d11b0e30572e37b7f670a10a3" \
          "&vertical_info=0%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C1 ".format(pag)
    html = get_html(url, head)
    context = json.loads(html)
    print(context)


if __name__ == '__main__':
    page = input('请输入要爬取的页数:')
    start_end_pag(page)



