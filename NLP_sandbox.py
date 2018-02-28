from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps= PorterStemmer()

words  = ['supported', 'supporting', 'supports']

for word in words:
    print ps.stem(word)


sentence = "Supportive ENVIRONMENT"
words = [w.lower() for w in word_tokenize(sentence)]
for word in words:
    print ps.stem(word)