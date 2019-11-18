import re

from bs4 import BeautifulSoup
from soupsieve.util import string

soup = BeautifulSoup(open("D:\\biancheng\\python\\pc\\com.cn.python.demo\\aaa", 'rb'), 'lxml')
# ben = soup.find_all("div", class_="p-name")
ben = soup.find("ul",class_="gl-warp clearfix")
# str = ''.join(ben)
# print(type(ben))
# print(ben.em)
# soup = BeautifulSoup(str, 'lxml')
# ben = soup.find_all(attrs={"class": "skcolor_ljg"})
print(ben.find_all(attrs={"class": "skcolor_ljg"}))
# for i in ben:
#     # print(i)
#     if string(type(i)) == '<class \'bs4.element.Tag\'>':

        # for j in i.font:
            # print(j)


    # print(re.findall(r'class="gl-item"([\d\D]*?)</li>',i, re.S))
    # print(i.get("em"))
