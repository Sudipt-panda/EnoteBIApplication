from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import mysql.connector



mydateparser = lambda x: pd.datetime.strptime(x, "%m/%d/%y")
#df = pd.read_csv("C:/Users/Sudipt Panda/Downloads/Data Analyst assignment_enote/BI_assignment_transaction.csv", names=['id_transaction', 'id_account','transaction_type','transaction_date','transaction_amount'], parse_dates=['transaction_date'], date_parser=mydateparser)
df_trans = pd.read_csv("C:/Users/Sudipt Panda/Downloads/Data Analyst assignment_enote/BI_assignment_transaction.csv")
df_pers = pd.read_csv("C:/Users/Sudipt Panda/Downloads/Data Analyst assignment_enote/BI_assignment_person.csv")
df_acc = pd.read_csv("C:/Users/Sudipt Panda/Downloads/Data Analyst assignment_enote/BI_assignment_account.csv")



df_trans['transaction_date'] = pd.to_datetime(df_trans['transaction_date'],format = '%m/%d/%y', 
                                                   errors = 'coerce')
df_pers['birth_date'] = pd.to_datetime(df_pers['birth_date'],format = '%m/%d/%y', 
                                                   errors = 'coerce')

df_pers = df_pers.replace(to_replace='None', value=np.nan).dropna(how='all')

#df_pers[['id_person', 'zip','phone_number']] = df_pers[['id_person', 'zip','phone_number']].apply(pd.to_numeric) 
convert_dict = {'id_person': int, 
               } 
  
df_pers = df_pers.astype(convert_dict) 
print(df_acc.dtypes) 
tableName1 = 'bi_assignment_transaction'
tableName2 = 'bi_assignment_person'
tableName3 = 'bi_assignment_account'
sqlEngine = create_engine('mysql+pymysql://root:Pass@1234@localhost/EnoteCode')
dbConnection    = sqlEngine.connect()

df_pers.to_sql(tableName2, con = dbConnection,if_exists = 'append',chunksize = 1000, index = False )
df_acc.to_sql(tableName3, con = dbConnection,if_exists = 'append',chunksize = 1000, index = False )
df_trans.to_sql(tableName1, con = dbConnection,if_exists = 'append',chunksize = 1000, index = False )

        

dbConnection.close()