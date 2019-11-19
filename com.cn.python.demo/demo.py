import requests
from lxml import etree

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/66.0.3359.139 Safari/537.36',
}
url = "https://item.jd.com/10580735451.html"

response = requests.get(url, timeout=30, headers=head)
response.encoding = 'gbk'
# 页面源码
html = response.text
content = etree.HTML(html)
print(content.xpath('./text()'))