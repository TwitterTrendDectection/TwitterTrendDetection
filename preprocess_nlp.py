# from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from nltk import bigrams,trigrams
from collections import defaultdict

from nltk.stem.lancaster import LancasterStemmer
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


def tokenize(raw_text):
  tokens = word_tokenize(raw_text)
  return tokens

def stemmize(word_list):
    st = LancasterStemmer()
    for i in range(len(word_list)):
        word_list[i] = st.stem(word_list[i])
    return word_list

def remove_stop_words(word_list):
    from nltk.corpus import stopwords
    import string
    #remove english and also punctuation
    # punctuation = [string.punctuation]
    punctuation = [char for char in string.punctuation]
    stop = stopwords.words('english') + punctuation + ['rt', 'via']
    word_list = [term for term in word_list if term not in stop]
    return word_list


if __name__ == "__main__":
  # word_list = ["I","am","a","nice","guy"]
  # grab n-grams
  # words = ['the','cats','sat','on','mines','lies','going','got','cooler']
  article = "There is also a corpus of instant messaging chat sessions, " \
            "originally collected by the Naval Postgraduate School for research " \
            "on automatic detection of Internet predators. The corpus contains " \
            "over 10,000 posts, anonymized by replacing usernames with generic names of " \
            "the form 'UserNNN', and manually edited to remove any other identifying information. " \
                              "The corpus is organized into 15 files, where each file contains several " \
                              "hundred posts collected on a given date, for an age-specific chatroom " \
                              "(teens, 20s, 30s, 40s, plus a generic adults chatroom). The filename " \
                              "contains the date, chatroom, and number of posts; e.g., 10-19-20s_706posts.xml " \
                              "contains 706 posts gathered from the 20s chat room on 10/19/2006."
  list = tokenize(article)
  list = stemmize(list)
  list = remove_stop_words(list)


  print list
  # import string
  # print string.punctuation
  # print list("12312314")

  # words = remove_stop_words(words)
  # words = stemmize(words)
  # print words
  # three_gram = ngrams_wrapper(words,1)
  # print three_gram
# import nltk

