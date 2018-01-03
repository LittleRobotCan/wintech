import pandas as pd
import re

# load in the data
data = pd.read_csv('data/response_data.csv')

# collect the response into a list
responses = data['Q2'].tolist()

# for each response, break by punctuation
response_split = [re.split(',|;|\.|!', response) for response in responses]
response_list = [item for sublist in response_split for item in sublist]

# split each response into a bag of words
word_list = [re.split(' ', response) for response in response_list]

# clean up spaces and unwanted words
word_list_clean = []
for _list in word_list:
    _list_clean = [l.lower() for l in _list if l not in ['','of', 'in', 'and', 'the', 'also', 'is', 'a', 'I', 'are']]
    word_list_clean.append(_list_clean)

# generate n-grams
def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

print find_ngrams(['there', 'fewer', 'opportunities'], 1)
print find_ngrams(['there', 'fewer', 'opportunities'], 2)
print find_ngrams(['there', 'fewer', 'opportunities'], 3)

# generate n-grams and tabulate
n_gram_list = []
for list_clean in word_list_clean:
    n_gram_list.extend(find_ngrams(list_clean, 1))
    n_gram_list.extend(find_ngrams(list_clean, 2))
    n_gram_list.extend(find_ngrams(list_clean, 3))

n_gram_list = [' '.join(l) for l in n_gram_list]

n_gram_counts = []
for n_gram in set(n_gram_list):
    count = n_gram_list.count(n_gram)
    n_gram_counts.append([n_gram, count])

n_gram_count_df = pd.DataFrame(n_gram_counts, columns = ['ngram', 'counts'])

n_gram_count_df = n_gram_count_df.sort_values(by=['counts'], ascending=False)

n_gram_count_df.to_csv('data/n_grams.csv')

# from there the data can be gone through by hand, but is more often put through topic modeling
# topic modeling groups the responses into similar categories ...
# Each category calculated using the n-grams they have in common
# ex: lack of community support, tech field stereotypes, male at the work place, etc.