import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from gensim import corpora, models
import re, string

df = pd.read_csv('private_data/hindrance_keywords.csv', )

keywords = df['keywords'].tolist()
keywords = [re.split(' ', k.lower()) for k in keywords]
keywords = [item for sublist in keywords for item in sublist]
keywords = list(set(keywords))
keywords = [k for k in keywords if len(k)>2 and k not in ['for','and','the']]

df_analyze = pd.read_csv('private_data/stakeholder_data.csv')
df_analyze.columns = list(string.ascii_uppercase)[:len(df_analyze.columns)]+['unnamed']

hindrances = list(df_analyze['U'])
texts = []
raw_texts = []
for item in hindrances:
    try:
        item = item.lower()
        keep = [k for k in keywords if re.search('\\b'+k+'\\b',item) is not None]
        if len(keep)>1:
            #keep  = [i for i in item if len(i)>2 and i not in ['for','and','the']]
            texts.append(keep)
            raw_texts.append(item)
    except AttributeError:
        continue

from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

# create the tfidf non-sparse matrix
tfidf_full_matrix = []
for doc in corpus_tfidf:
    vector = [0]*len(dictionary.token2id)
    for d in doc:
        vector[d[0]] = d[1]
    tfidf_full_matrix.append(vector)

X = np.array(tfidf_full_matrix)
kmeans = KMeans(n_clusters=8, random_state=0).fit(X)

label_doc_list = []
for i in range(len(texts)):
    doc = ' '.join(texts[i])
    label = kmeans.labels_[i]
    label_doc = [label,doc]
    label_doc_list.append(label_doc)

output_df = pd.DataFrame(label_doc_list)

output_df.to_csv('private_data/intech_stakeholder_hindrance/stakeholder_clustered_hindrance.csv')