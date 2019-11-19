# -*- coding: utf-8 -*-

import pandas as pd
import pymysql as pymysql
from pandas import DataFrame, Series

dbconn = pymysql.connect(host='60.205.168.159', database='pc', user='root', password='ljh')
# sql = 'select * from demo'
# a = pd.read_sql(sql, dbconn)
data = {'水果':Series(['苹果','梨','草莓']),
       '数量':Series([3,2,5]),
       '价格':Series([10,9,8])}
df = DataFrame(data)
print(df)
#写入数据，table_name为表名，‘replace’表示如果同名表存在就替换掉
df.to_sql(name="demo", con=dbconn, if_exists='replace', index=False)
# b = a.head()
# print(b)
# 关闭连接
dbconn.close()
