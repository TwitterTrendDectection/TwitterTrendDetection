# from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from nltk import bigrams,trigrams
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
# from nltk.stem.lancaster import LancasterStemmer
from nltk import pos_tag
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

    if len(no_see_before) > 0:
        tag_list = pos_tag(no_see_before)
        for item in tag_list:
            tag = item[1].lower()
            lemmetized = item[0]
            if 'v' in tag:
                lemmetized = wnl.lemmatize(item[0],pos = 'v')

            elif 'n' in tag:
                lemmetized = wnl.lemmatize(item[0],pos = 'n')

            elif 'a' in tag:
                lemmetized = wnl.lemmatize(item[0],pos = 'a')

            res.append(lemmetized)
            visited[item[0]] = lemmetized
    return res


def remove_stop_words(word_list):
    from nltk.corpus import stopwords
    import string
    #remove english and also punctuation
    punctuation = [char for char in string.punctuation]
    stop = stopwords.words('english') + punctuation + ['rt', 'via']
    word_list = [term for term in word_list if term not in stop]
    return word_list

def remove_words_contain_numbers(word_list):
    import re
    res = [s for s in word_list if not re.search(r'\d',s)]
    return res

def remove_punctuation(raw_text):
    import string
    #remove punctuation
    for c in string.punctuation:
        raw_text = raw_text.replace(c,"")
    return raw_text

if __name__ == "__main__":
  # print "h"
  # for i in range(1,100000):
  #   from nltk import pos_tag
  # word_list = ["I","am","a","nice","guy"]
  # grab n-grams
  # words = ['the','cats','sat','on','mines','lies','going','got','cooler']
  # article = "There is also a corpus of instant messaging chat sessions, " \
  #           "originally collected by the Naval Postgraduate School for research " \
  #           "on automatic detection of Internet predators. The corpus contains " \
  #           "over 10,000 posts, anonymized by replacing usernames with generic names of " \
  #           "the form 'UserNNN', and manually edited to remove any other identifying information. " \
  #                             "The corpus is organized into 15 files, where each file contains several " \
  #                             "hundred posts collected on a given date, for an age-specific chatroom " \
  #                             "(teens, 20s, 30s, 40s, plus a generic adults chatroom). The filename " \
  #                             "contains the date, chatroom, and number of posts; e.g., 10-19-20s_706posts.xml " \
  #                             "contains 706 posts gathered from the 20s chat room on 10/19/2006."
  # list = tokenize(article)
  # lis = ["words","gave","following","was","cool","fuck","posts","feet","leave"]
  # st = WordNetLemmatizer()
  # list = lemmetize(lis, st)
  # print list
  # list = remove_stop_words(list)
  #
  #
  # print list

  # import string
  # print string.punctuation
  # print list("12312314")

  # words = remove_stop_words(words)
  # words = stemmize(words)
  # print words
  # three_gram = ngrams_wrapper(words,1)
  # print three_gram
# import nltk
    wnl = wnl = WordNetLemmatizer()
    word_list = lemmetize(['marketing','confusing','downloading'], wnl, {})
    print word_list