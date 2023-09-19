# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:46:11 2022

@author: LTP-5
"""

from mysql import connector
import datetime
db = connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345')

cursor = db.cursor()

query = ('SELECT purchase_order_no, warranty_start_date, warranty_expiry_date,  FROM qubeslocal.asset_secondary where warranty_expiry_date between %s and %s;   ')

warranty_start_date = datetime.date(2022,1,1)
warranty_end_date = datetime.date(2023,12,31)

cursor.execute(query,(warranty_start_date, warranty_end_date))

for(purchase_order_no, warranty_start_date, warranty_expiry_date) in cursor:
    print('upcoming')

