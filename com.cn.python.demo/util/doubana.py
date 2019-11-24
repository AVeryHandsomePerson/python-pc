import requests

head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
    }

# for f in range(0, 300, 25):
#     url = "https://www.douban.com/group/minimalists/discussion?start=%s" % (f)

# 模拟浏览器发送http请求
url = "https://www.douban.com/group/minimalists/discussion?start=25"
response = requests.get(url, timeout=30, headers=head)
response.encoding = 'gbk'
html = response.text
print(html)

# words = jieba.lcut(str(read_db()))

# stopwords = [line.strip() for line in
#              open("/root/file/百度停用词表.txt", encoding="utf-8").readlines()]
# counts = {}
# lists = []
# jieba.load_userdict("/root/file/fenci.txt")
# for word in words:
#     # 不在停用词表中
#     if word not in stopwords:
#         # 不统计字数为一的词
#         if len(word) == 1:
#             continue
#         else:
#             lists.append(word)
#             # counts[word] = counts.get(word,0) + 1
# word_counts = collections.Counter(lists)
# word_counts_top10 = word_counts.most_common(len(word_counts))
#
# ben = DatabaseAccess()
# print("开始写入")
# for i in word_counts_top10:
#     ben.linesinsert(i[0], i[1], dt)