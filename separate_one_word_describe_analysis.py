import pandas as pd
import string, re

"""
word to describe their experience vs what they thought??? can't find in ideabook???
"""

df = pd.read_csv('private_data/sentiment_one_word_describe.csv')
df = df[['word','sentiment']]

"""
INTECH
"""
df_intech = pd.read_csv('private_data/intech_data.csv')
df_intech.columns = list(string.ascii_uppercase)[:len(df_intech.columns)]+['unnamed']

words = [str(i).lower() for i in df_intech['R'] if str(i) not in ['nan', ''] and len(str(i))<50]

words = [re.split(',| |\\|',w) for w in words]
words = [item for sublist in words for item in sublist]
words_count = [[w, words.count(w)] for w in set(words)]

sentiment_dict = {}
for index, row in df.iterrows():
    sentiment_dict[row['word']] = row['sentiment']

for row in words_count:
    if row[0] in sentiment_dict:
        row.append(sentiment_dict[row[0]])
    else:
        row.append('')
output = pd.DataFrame(words_count)
output.to_csv('private_data/intech_stakeholder_sentiments/intech.csv')


"""
STAKEHOLDER
"""
df_intech = pd.read_csv('private_data/stakeholder_data.csv')
df_intech.columns = list(string.ascii_uppercase)[:len(df_intech.columns)]+['unnamed']

words = [str(i).lower() for i in df_intech['R'] if str(i) not in ['nan', ''] and len(str(i))<50]

words = [re.split(',| |\\|',w) for w in words]
words = [item for sublist in words for item in sublist]
words_count = [[w, words.count(w)] for w in set(words)]

sentiment_dict = {}
for index, row in df.iterrows():
    sentiment_dict[row['word']] = row['sentiment']

for row in words_count:
    if row[0] in sentiment_dict:
        row.append(sentiment_dict[row[0]])
    else:
        row.append('')
output = pd.DataFrame(words_count)
output.to_csv('private_data/intech_stakeholder_sentiments/stakeholder.csv')