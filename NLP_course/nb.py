from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np

data = pd.read_csv('data/spambase/spambase.data').as_matrix()
np.random.shuffle(data)  # inplace random shuffle

X = data[:,:48]
Y = data[:,-1]

Xtrain = X[:-100,]
Ytrain = Y[:-100,]
Xtest = X[-100:,]
Ytest = Y[-100:,]

model = MultinomialNB()
model.fit(Xtrain, Ytrain)

print("Classfication rate for NB:{}".format(model.score(Xtest, Ytest)))

from sklearn.ensemble import AdaBoostClassifier

model = AdaBoostClassifier()
model.fit(Xtrain, Ytrain)
print("classification rate for AdaBoost:{}".format(model.score(Xtest, Ytest)))

"""
Always try something simple first to establish a baseline
Also, 1% gain in accuracy is not worth the 100hr increase in training time
"""