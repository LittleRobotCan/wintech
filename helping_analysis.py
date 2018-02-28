import pandas as pd
from nltk.stem import PorterStemmer
ps= PorterStemmer()
from nltk.tokenize import word_tokenize
import re

df = pd.read_csv('private_data/helping_keywords.csv', header = None)
df.columns = ['keywords','location']
df = df.dropna()

# find unigrams
keywords = df['keywords'].tolist()
keywords = [word_tokenize(k.lower()) for k in keywords]
keywords_sets = [set(sublist) for sublist in keywords]
keywords = [item for sublist in keywords_sets for item in sublist]
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
output_df.to_csv('private_data/intech_helping/keywords_ranked_stemmed.csv')


# ngrams
keywords = df['keywords'].tolist()
keywords = [re.split(' ', k.lower()) for k in keywords]
keywords_stemmed = list()
for item in keywords:
  item_stemmed = [ps.stem(w) for w in item]
  keywords_stemmed.append(item_stemmed)
def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

bigrams = [find_ngrams(item, 2) for item in keywords_stemmed if len(item)>1]
trigrams = [find_ngrams(item, 3) for item in keywords_stemmed if len(item)>2]

bigrams = [item for sublist in bigrams for item in sublist]
trigrams = [item for sublist in trigrams for item in sublist]

ngrams = bigrams+trigrams
ngrams = [' '.join(list(n)) for n in ngrams]

ngrams_count = [(n, ngrams.count(n)) for n in set(ngrams)]
output = pd.DataFrame(ngrams_count, columns=['ngrams','counts'])
output.to_csv('private_data/intech_helping/ngrams_ranked_stemmed.csv')