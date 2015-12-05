# coding=utf-8
# from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from nltk import bigrams,trigrams
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
# from nltk.stem.lancaster import LancasterStemmer
from nltk import pos_tag
from nltk.stem.snowball import SnowballStemmer
def lowercase(word_list):
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
    return word_list



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


def tokenize(raw_text):
  tokens = word_tokenize(raw_text)
  return tokens

# def lemmetize(word_list, st):
#
#
#     for i in range(len(word_list)):
#         word_list[i] = st.lemmatize(word_list[i])
#     return word_list

def lemmetize(word_list, wnl, visited):


    res = []
    no_see_before = []
    for item in word_list:
        if item in visited:
            # print item
            res.append(visited[item])
        else:
            no_see_before.append(item)

    # if len(no_see_before) > 0:
    #     tag_list = pos_tag(no_see_before)
    #     for item in tag_list:
    #         tag = item[1].lower()
    #         lemmetized = item[0]
    #         if 'v' in tag:
    #             lemmetized = wnl.lemmatize(item[0],pos = 'v')
    #
    #         elif 'n' in tag:
    #             lemmetized = wnl.lemmatize(item[0],pos = 'n')
    #
    #         elif 'a' in tag:
    #             lemmetized = wnl.lemmatize(item[0],pos = 'a')
    #
    #         res.append(lemmetized)
    #         visited[item[0]] = lemmetized
    return res


def remove_stop_words(word_list):
    from nltk.corpus import stopwords
    import string
    #remove english and also punctuation
    punctuation = [char for char in string.punctuation]
    stop = stopwords.words('english') + punctuation + ['rt', 'via']
    word_list = [term for term in word_list if term not in stop and term.find('http') == -1]
    return word_list

def remove_words_contain_numbers(word_list):
    import re
    res = [s for s in word_list if not re.search(r'\d',s)]
    return res

def remove_punctuation(raw_text):
    import string
    #remove punctuation
    punctuation = string.punctuation + u'‘’“”…。，';
    for c in punctuation:
        raw_text = raw_text.replace(c,"")
    return raw_text

def stemmize(tokens):
    res = []
    for token in tokens:
        res.append(SnowballStemmer("english").stem(token))
    return res


if __name__ == "__main__":

    wnl = wnl = WordNetLemmatizer()
    word_list = lemmetize(['marketing','confusing','downloading'], wnl, {})
    print word_list