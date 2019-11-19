# -*- coding: utf-8 -*-

import pandas as pd
import pymysql as pymysql

dbconn = pymysql.connect(host='', database='', user='', password='')
sql = 'select * from demo'
a = pd.read_sql(sql, dbconn)
b = a.head()
print()
