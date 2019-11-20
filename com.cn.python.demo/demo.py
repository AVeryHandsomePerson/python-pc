
import requests
from lxml import etree

# proxies = {
#     'http': '58.218.92.81:8314',
#     'http': '58.218.92.173:5257',
#     'http': '58.218.92.173:2023',
#     'http': '58.218.92.172:8842',
#     'http': '58.218.92.172:7091',
#     'http': '58.218.92.171:8124',
#     'http': '58.218.92.170:3671',
#     'http': '58.218.92.81:8895',
#     'http': '58.218.92.81:6774',
#     'http': '58.218.92.171:2105',
#     'http': '58.218.92.171:6379',
#     'http': '58.218.92.171:3828',
#     'http': '58.218.92.81:2815',
#     'http': '58.218.92.174:4580',
#     'http': '58.218.92.173:9966',
#     'http': '58.218.92.173:8415',
#     'http': '58.218.92.170:6208',
#     'http': '58.218.92.172:3539',
#     'http': '58.218.92.170:7980',
#     'http': '58.218.92.172:4487',
#     'http': '58.218.92.167:9754',
#     'http': '58.218.92.86:9958',
#     'http': '58.218.92.167:9660',
#     'http': '58.218.92.86:9547',
#     'http': '58.218.92.167:9660',
#     'http': '58.218.92.86:9547',
#     'http': '58.218.92.167:9754',
#     'http': '58.218.92.86:9958'
# }
'''head 信息'''
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Connection': 'keep-alive'}
'''http://icanhazip.com会返回当前的IP地址'''
list = []
for i in range(0, 7):
    http = 'https://www.xicidaili.com/wt/{}'.format(i)
    print(http)
    html = requests.get('https://www.xicidaili.com/wt/1', headers=head)
    content = etree.HTML(html.text)
    for node in content.xpath('//table[@id="ip_list"]//tr'):
       ip = node.xpath('string(./td[2])') + ':' + node.xpath('string(./td[3])')
       if ip != ':':
        proxies = {
            'http': ip,
            'https': ip
        }
        try:
            html = requests.get('https://search.jd.com/Search?keyword=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB%E4%B9%A6&enc=utf-8', headers=head, proxies=proxies)
        except Exception as e:
            content
        if html.status_code == 200:
            print(ip)