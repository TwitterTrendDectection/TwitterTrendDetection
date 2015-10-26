# from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from nltk import bigrams,trigrams
from collections import defaultdict
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

def ngrams(words, n, padding=False):
    "Compute n-grams with optional padding"
    pad = [] if not padding else [None]*(n-1)
    grams = pad + words + pad
    return (tuple(grams[i:i+n]) for i in range(0, len(grams) - (n - 1)))

def ngrams_count(tuple_list):
  counts = defaultdict(int)
  for ng in tuple_list:
      counts[ng] += 1
  return counts

def ngrams_wrapper(words, n, padding = False):
  tuple_list = ngrams(words, n, padding=False)
  counts = ngrams_count(tuple_list)
  res = []
  for key in counts:
    res.append([k for k in key] + [counts[key]])
  return res

def remove_stop_words(word_list):
  filtered_word_list = word_list[:] #make a copy of the word_list
  for word in word_list: # iterate over word_list
    if word in stopwords:
      filtered_word_list.remove(word) # remove word from filtered_word_list if it is a stopword
  return filtered_word_list

def tokenize(raw_text):
  tokens = word_tokenize(raw_text)
  return tokens

if __name__ == "__main__":
  # word_list = ["I","am","a","nice","guy"]
  # grab n-grams
  words = ['the','cat','sat','on','the','dog','on','the','cat']
  words = remove_stop_words(words)
  three_gram = ngrams_wrapper(words,1)
  print three_gram


