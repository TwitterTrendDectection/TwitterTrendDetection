
import langid
import pandas as pd
import re

def language_identify(content):
    threshold = 0.5
    if content == "":
        return ''
    tuple = langid.classify(content)
    if tuple[0] == 'en' and float(tuple[1]) > threshold:
        return 'en'
    else:
        return tuple[0]
def count_letters(word):
    return len(word) - word.count(' ')
def filter_question_mark(content):
    threshold = 0.3
    count_question = content.count('?')
    count_all = count_letters(content)
    if count_question * 1.0 / count_all > threshold:
        return ""
    else:
        return content
def count_en(content):
    if content == "en":
        return 1

def extract_link(list_text):
    print "start extracting link.\n"
    link_group = []
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    for text in list_text:
        match = re.search(regex, text)
        if match:
            print "succeed.\n"
            print match.group() + "\n"
            link_group.append(match.group())
        else:
            print "failed.\n"
    return link_group


def example():
    df = pd.read_csv("table1000.csv")
    df['tweet_text'] = df['tweet_text'].apply(lambda content:filter_question_mark(content))
    df['lang'] = df['tweet_text'].apply(lambda content: language_identify(content))
    df['link'] = df['tweet_text'].apply(lambda content: extract_link(content))
    #TODO df['hashtag'] = df['tweet_text'].apply(lambda content: xxx(content)) #xxx return hashtags' list

    #TODO df['at_people'] = df['tweet_text'].apply(lambda content: xxx(content)) #xxx return at_people list
    print df['lang'].value_counts()
if __name__ == "__main__":
    example()