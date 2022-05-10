import pandas as pd

files = ['ps_titles_1947-2018.csv', 'ps_titles_2019-2021.csv']

master = pd.concat([pd.read_csv(f) for f in files])

master.to_csv('master_ps_titles.csv', index=False, encoding='utf-8-sig')
data = pd.read_csv('master_ps_titles.csv')

#print(data)