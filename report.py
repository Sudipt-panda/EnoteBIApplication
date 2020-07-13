from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import mysql.connector
from tabulate import tabulate



tableName = 'test'
sqlEngine = create_engine('mysql+pymysql://root:Pass@1234@localhost/EnoteCode')
dbConnection    = sqlEngine.connect()


with sqlEngine.connect() as connection:
    result = connection.execute('''
SELECT enotecode.bi_assignment_account.id_person,CONCAT(MONTH(enotecode.bi_assignment_transaction.transaction_date), '.', YEAR(enotecode.bi_assignment_transaction.transaction_date)) as 'month', SUM(enotecode.bi_assignment_transaction.transaction_amount) as 'sum of transactions'
FROM enotecode.bi_assignment_transaction, enotecode.bi_assignment_account
WHERE enotecode.bi_assignment_transaction.id_account = enotecode.bi_assignment_account.id_account
AND enotecode.bi_assignment_transaction.transaction_date >= CAST('2020-02-15' AS DATE) 
AND enotecode.bi_assignment_transaction.transaction_date <= CAST('2020-06-06' AS DATE)
AND enotecode.bi_assignment_account.id_person IN ('345','1234')
GROUP BY enotecode.bi_assignment_account.id_person,YEAR(enotecode.bi_assignment_transaction.transaction_date), MONTH(enotecode.bi_assignment_transaction.transaction_date)
ORDER BY enotecode.bi_assignment_account.id_person DESC,YEAR(enotecode.bi_assignment_transaction.transaction_date), MONTH(enotecode.bi_assignment_transaction.transaction_date)
''')
df1 = pd.DataFrame(data=result)
 
col = ['id_person','month','sum_of_transactions']
print(tabulate(df1, headers= col, tablefmt='psql'))
#print(df.to_markdown())

# for row in result:
#     print(row)