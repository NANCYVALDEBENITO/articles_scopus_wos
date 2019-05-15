 
#!/usr/bin/env python
# -*- coding: utf-8 -*
import pandas as pd
import csv
import os
import numpy as np
import string

df1 = pd.read_csv('/home/nvaldebenito/Documentos/02_reporte_2018/cr2_articles.xlsx',sep=',')
df2 = pd.read_csv('scopus.csv',sep=',')

print df1
print df2

# df=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10])
# print df

# user        =df['user']
# email       =df['email']
# lastlogin   =df['lastLogin']




# dftest = pd.DataFrame({'user':np.array(user),'email':np.array(email)})

# dftest=dftest.drop_duplicates(['user'],keep='last')



# print dftest

# #dfend=pd.DataFrame({'lastLogin':np.array(lastlogin),'email':np.array(email),'user':np.array(user)})
# dftest.to_csv('users_list.csv',encoding='utf-8',sep = ',')
