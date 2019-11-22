# -*- coding: utf-8 -*-
import requests
from lxml import etree

url = 'https://www.zhihu.com/topic/19938518'
kv = {'User-Agent': 'Mozilla/5.0'}  # 模拟登陆，
r = requests.get(url, headers=kv)  # 获取网页
# print(r.status_code)
#
# print(len(r.text))
print(r.text)

content = etree.HTML(r.text)
theme = content.xpath('//*[@id="TopicMain"]/div[6]/div/div/div/div/div/h2/div/a/text()')
# //*[@id="SearchMain"]/div/div/div/div/div[1]/div/div/div/div[1]/div/a
# //*[@id="TopicMain"]/div[3]/div/div/div/div[2]/div/h2/a
# //*[@id="TopicMain"]/div[3]/div/div/div/div[1]/div/h2/div/a
# //*[@id="TopicMain"]/div[3]/div/div/div/div[6]/div/h2/div/a
print(theme)
