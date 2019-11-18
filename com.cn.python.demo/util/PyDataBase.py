# -*- coding: utf-8 -*-

import pandas as pd
import pymysql as pymysql

dbconn = pymysql.connect(host='60.205.168.159', database='pc', user='root', password='ljh')
sql = 'select * from demo'
a = pd.read_sql(sql, dbconn)
b = a.head()
print()
