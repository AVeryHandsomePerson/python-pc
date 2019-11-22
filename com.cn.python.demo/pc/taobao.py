from lxml import etree
import re

import pymysql
import requests
import time
from lxml import etree

head = {
    'Host': 'login.taobao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
    'Referer': 'https://login.taobao.com/member/login.jhtml',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive'
}

url = "https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB%E4%B9%A6&suggest=0_4&_input_charset=utf-8&wq=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB&suggest_query=%E6%9E%81%E7%AE%80%E7%94%9F%E6%B4%BB&source=suggest"

"""
验证用户名密码，并获取st码申请URL
:return: 验证成功返回st码申请地址
"""
# verify_password_headers = {
#     'Connection': 'keep-alive',
#     'Cache-Control': 'max-age=0',
#     'Origin': 'https://login.taobao.com',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Referer': 'https://login.taobao.com/member/login.jhtml?from=taobaoindex&f=top&style=&sub=true&redirect_url=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm',
# }
# 登录toabao.com提交的数据，如果登录失败，可以从浏览器复制你的form data
verify_password_data = {
    'TPL_username': "",
    'ncoToken': 'cdf05a89ad5104403ebb12ebc9b7626af277b066',
    'slideCodeShow': 'false',
    'useMobile': 'false',
    'lang': 'zh_CN',
    'loginsite': 0,
    'newlogin': 0,
    'TPL_redirect_url': 'https://s.taobao.com/search?q=%E9%80%9F%E5%BA%A6%E9%80%9F%E5%BA%A6&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306',
    'from': 'tb',
    'fc': 'default',
    'style': 'default',
    'keyLogin': 'false',
    'qrLogin': 'true',
    'newMini': 'false',
    'newMini2': 'false',
    'loginType': '3',
    'gvfdcname': '10',
    'gvfdcre': '68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D61323330722E312E3735343839343433372E372E33353836363032633279704A767526663D746F70266F75743D7472756526726564697265637455524C3D6874747073253341253246253246732E74616F62616F2E636F6D25324673656172636825334671253344253235453925323538302532353946253235453525323542412532354136253235453925323538302532353946253235453525323542412532354136253236696D6766696C65253344253236636F6D6D656E64253344616C6C2532367373696425334473352D652532367365617263685F747970652533446974656D253236736F75726365496425334474622E696E64657825323673706D253344613231626F2E323031372E3230313835362D74616F62616F2D6974656D2E31253236696525334475746638253236696E69746961746976655F69642533447462696E6465787A5F3230313730333036',
    'TPL_password_2': "",
    'loginASR': '1',
    'loginASRSuc': '1',
    'oslanguage': 'zh-CN',
    'sr': '1440*900',
    'osVer': 'macos|10.145',
    'naviVer': 'chrome|76.038091',
    'osACN': 'Mozilla',
    'osAV': '5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'osPF': 'MacIntel',
    'appkey': '00000000',
    'mobileLoginLink': 'https://login.taobao.com/member/login.jhtml?redirectURL=https://s.taobao.com/search?q=%E9%80%9F%E5%BA%A6%E9%80%9F%E5%BA%A6&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&useMobile=true',
    'showAssistantLink': '',
    'um_token': 'T898C0FDF1A3CEE5389D682340C5F299FFE590F51543C8E3DDA8341C869',
    'ua': ""
}
response = requests.get(url, timeout=20, headers=head)
response.encoding = 'GBK'
html = response.text
print(html)
# content = etree.HTML(html)
# content_book = content.xpath('//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')
