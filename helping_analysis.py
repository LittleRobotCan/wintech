import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from gensim import corpora, models
import re, string

df = pd.read_csv('private_data/helping_keywords.csv', header = None)
df.columns = ['keywords','location']
df = df.dropna()

keywords = df['keywords'].tolist()
keywords = [re.split(' ', k.lower()) for k in keywords]
keywords = [item for sublist in keywords for item in sublist]
keywords = [k for k in keywords if len(k)>2 and k not in ['for','and','the']]

keyword_counts = [(k, keywords.count(k)) for k in set(keywords)]
sorted(keyword_counts, key=lambda x: x[1])

output = pd.DataFrame(keyword_counts, columns=['keywords','counts'])
output.to_csv('private_data/intech_helping/keywords_ranked.csv')

# ngrams
keywords = df['keywords'].tolist()
keywords = [re.split(' ', k.lower()) for k in keywords]
def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

bigrams = [find_ngrams(item, 2) for item in keywords if len(item)>1]
trigrams = [find_ngrams(item, 3) for item in keywords if len(item)>2]

bigrams = [item for sublist in bigrams for item in sublist]
trigrams = [item for sublist in trigrams for item in sublist]

ngrams = bigrams+trigrams
ngrams = [' '.join(list(n)) for n in ngrams]

ngrams_count = [(n, ngrams.count(n)) for n in set(ngrams)]
output = pd.DataFrame(ngrams_count, columns=['ngrams','counts'])
output.to_csv('private_data/intech_helping/ngrams_ranked.csv')