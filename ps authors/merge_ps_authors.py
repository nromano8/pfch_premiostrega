import pandas as pd

files = ['ps_authors_1947-2018.csv', 'ps_authors_2019-2021.csv']

master = pd.concat([pd.read_csv(f) for f in files])

master.to_csv('master_ps_authors.csv', index=False, encoding='utf-8-sig')
data = pd.read_csv('master_ps_authors.csv')

#print(data)