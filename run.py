

from mysql import connector
import pandas as pd
import datetime
from datetime import date

now = datetime.datetime.now()
current_date = (now.strftime("%Y/%m/%d"))

mydb = connector.connect(
    host='localhost',
    user='root',
    password = '12345',
   
    )

#mycursor = mydb.cursor()
curA = mydb.cursor(buffered=True)
curB = mydb.cursor(buffered=True)
query = ('SELECT warranty_expiry_date FROM qubeslocal.asset_secondary where warranty_expiry_date between %s and %s; ')
start = date(2022, 1, 1)
end = date(2023, 12, 31)
curA.execute(query, (start, end))

for (warranty_expiry_date) in curA:
    print('your warranty expires on %s'%warranty_expiry_date)









'''
for i in mycursor:
    df = []
    df.append(i)
    s = pd.DataFrame(df)
    s.drop([0,1,2,3,4,7,8,9,10,5],axis = 1, inplace=True)
    print(s)
    #k = s.iloc[:,6:7]
    #print(s.iloc[:,6:7])
    #if s.iloc[:,6:7] >= current_date:
        
      # print('upcoming')
    '''