import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('data/spam.csv', encoding='ISO-8859-1')

df = df.drop(["Unnamed: 2","Unnamed: 3","Unnamed: 4"], axis=1)

df.columns = ['labels', 'data']

# create a binary labels
df['b_labels'] = df['labels'].map({'ham':0,'spam':1})
Y = df['b_labels'].as_matrix()

#count_vectorizer = CountVectorizer(decode_error="ignore")
tfidf_vectorizer = TfidfVectorizer(decode_error="ignore")
#X = count_vectorizer.fit_transform(df['data'])
X = tfidf_vectorizer.fit_transform(df['data'])

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.33)

model = MultinomialNB()
model.fit(Xtrain, Ytrain)
print("train score:{}".format(model.score(Xtrain, Ytrain)))
print("test score:{}".format(model.score(Xtest, Ytest)))