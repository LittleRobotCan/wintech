import pandas as pd
import string
from nltk.stem import PorterStemmer
ps= PorterStemmer()
from nltk.tokenize import word_tokenize

"""
word to describe their experience vs what they thought??? can't find in ideabook???
"""

#df = pd.read_csv('private_data/sentiment_one_word_describe.csv')
#df = df[['word','sentiment']]

"""
INTECH
"""
df_intech = pd.read_csv('private_data/intech_data.csv')
df_intech.columns = list(string.ascii_uppercase)[:len(df_intech.columns)]

words = [str(i).lower() for i in df_intech['R'] if str(i) not in ['nan', ''] and len(str(i))<50]

keywords = [word_tokenize(k.lower()) for k in words]
keywords = [item for sublist in keywords for item in sublist]
keywords = [k for k in keywords if len(k)>2 and k not in ['for','and','the','in','of','to','up']]

# stem the keywords
keywords_stem = [(ps.stem(w),w) for w in keywords]

# collect and count the stems
stems = [i[0] for i in keywords_stem]
stem_counts = [(s, stems.count(s)) for s in set(stems)]
stem_counts_sorted = sorted(stem_counts, key=lambda x: x[1], reverse=True)

# create a stem to keyword dictionary
stem_keyword_dict = dict()
for item in keywords_stem:
  stem, keyword = item
  if stem in stem_keyword_dict:
    stem_keyword_dict[stem].add(keyword)
  else:
    stem_keyword_dict[stem] = set([keyword])

output = list()
for item in stem_counts_sorted:
  stem, c = item
  keywords = ', '.join(stem_keyword_dict[stem])
  output.append([stem, c, keywords])

output_df = pd.DataFrame(output, columns=['stem', 'counts', 'keywords'])
output_df.to_csv('private_data/one_word_intech_stakeholder/intech_stemmed.csv')


"""
STAKEHOLDER
"""
df_intech = pd.read_csv('private_data/stakeholder_data.csv')
df_intech.columns = list(string.ascii_uppercase)[:len(df_intech.columns)]+['unnamed']

words = [str(i).lower() for i in df_intech['R'] if str(i) not in ['nan', ''] and len(str(i))<50]

keywords = [word_tokenize(k.lower()) for k in words]
keywords = [item for sublist in keywords for item in sublist]
keywords = [k for k in keywords if len(k)>2 and k not in ['for','and','the','in','of','to','up']]

# stem the keywords
keywords_stem = [(ps.stem(w),w) for w in keywords]

# collect and count the stems
stems = [i[0] for i in keywords_stem]
stem_counts = [(s, stems.count(s)) for s in set(stems)]
stem_counts_sorted = sorted(stem_counts, key=lambda x: x[1], reverse=True)

# create a stem to keyword dictionary
stem_keyword_dict = dict()
for item in keywords_stem:
  stem, keyword = item
  if stem in stem_keyword_dict:
    stem_keyword_dict[stem].add(keyword)
  else:
    stem_keyword_dict[stem] = set([keyword])

output = list()
for item in stem_counts_sorted:
  stem, c = item
  keywords = ', '.join(stem_keyword_dict[stem])
  output.append([stem, c, keywords])

output_df = pd.DataFrame(output, columns=['stem', 'counts', 'keywords'])
output_df.to_csv('private_data/one_word_intech_stakeholder/stakeholder_stemmed.csv')