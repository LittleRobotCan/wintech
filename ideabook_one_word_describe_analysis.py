import pandas as pd
import string, re



"""
INTECH RESPONSES
"""
df = pd.read_csv('private_data/intech_data.csv')
df.columns = list(string.ascii_uppercase)[:len(df.columns)]+['unnamed']

df['word'] = [re.sub(' ', '', w.lower()) if str(w)!='nan' else '' for w in df['R']]
df_small = df[df['word'].isin(['challenge','challenging','challenges'])]['S'].tolist()

# family work life challenge and childcare
indexes = []
for index, row in df.iterrows():
    doc = str(row['U']).lower()
    if re.search('family|child|balance|flexibility|flexible', doc) is not None:
        indexes.append(row['A'])

df_small = df[df['A'].isin(indexes)]
df_small.to_csv('private_data/intech_hindrance/family.csv')


df['region'] = [re.split('_',i)[0] if str(i)!='nan' else '' for i in df['A']]
len(df[df['region']=='BAR']) #9
len(df[df['region']=='EDM']) #9
len(df[df['region']=='KEL']) #9
len(df[df['region']=='KIN']) #9
len(df[df['region']=='OTT']) #9
len(df[df['region']=='PG']) #9
len(df[df['region']=='REG']) #9
len(df[df['region']=='TOR']) #9
len(df[df['region']=='VAN']) #9
len(df[df['region']=='WIN']) #9


