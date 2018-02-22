import pandas as pd
import string, re

"""
word to describe their experience vs what they thought??? can't find in ideabook???
"""

df = pd.read_csv('private_data/wordlcoud.csv')

df['color'] = [i.lower() for i in df['Colour'].tolist()]
df = df[df['color'].isin(['blue','yellow'])]
df['word'] = [i.lower() for i in df['Word'].tolist()]

word_count = {w:df['word'].tolist().count(w) for w in set(df['word'])}
import operator
word_count_sorted = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)

print word_count_sorted[:10]

#challenging
locations = list(set(df['location']))
for i in range(10):
    word =word_count_sorted[i][0]
    print word
    df2 = df[df['word']==word]
    output = []
    for location in locations:
        pos_count = len(df2[(df2['location']==location)&(df2['Colour']=='yellow')])
        neg_count = len(df2[(df2['location']==location)&(df2['Colour']=='blue')])
        output.append([location, pos_count,neg_count])
    df_output = pd.DataFrame(output, columns=['location', 'pos','neg'])
    df_output.to_csv('private_data/wordcloud_results/'+word+'.csv')

