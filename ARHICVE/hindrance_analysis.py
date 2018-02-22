import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from gensim import corpora, models

df = pd.read_csv('private_data/hindrance_keywords.csv', )

keywords = df['keywords'].tolist()
documents = [k.lower() for k in keywords]

texts = [[word for word in document.lower().split()]
         for document in documents]

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
kmeans = KMeans(n_clusters=10, random_state=0).fit(X)

label_doc_list = []
for i in range(len(documents)):
    doc = documents[i]
    label = kmeans.labels_[i]
    label_doc = [label,doc]
    label_doc_list.append(label_doc)


output_df = pd.DataFrame(label_doc_list)

output_df.to_csv('data/clustered_hindrance.csv')