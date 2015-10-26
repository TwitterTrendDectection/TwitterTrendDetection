
import langid
import pandas as pd



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
def example():
    df = pd.read_csv("table1000.csv")
    df['tweet_text'] = df['tweet_text'].apply(lambda content:filter_question_mark(content))
    df['lang'] = df['tweet_text'].apply(lambda content: language_identify(content))
    # df['count'] = df['lang'].apply(lambda content: 1)
    # print df['lang'].apply(lambda content: count_en(content))
    # print df.groupby(['lang','count']).sum()
    print df['lang'].value_counts()
if __name__ == "__main__":
    example()