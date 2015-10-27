# *****__author__ = 'Yan'*****
import re
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

# use this line to execute the main function
if __name__ == "__main__":
    list_tweet = []
    tweet1 = "Increased defense and domestic spending. https://t.co/Rnopp8mT1D"
    tweet2 = "Top 5 most addictive iOS games. http://t.co/rWGeXW9cdT"
    tweet3 = "Who is Guan Wang? Interesting question. www.t.co/Bpg6kq6lW5"
    list_tweet.append(tweet1)
    list_tweet.append(tweet2)
    list_tweet.append(tweet3)
    extract_link(list_tweet)
