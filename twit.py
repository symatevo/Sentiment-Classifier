punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
results = []
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, '')
    return word

def get_pos(sentences):
    sentences = sentences.lower()
    count = 0
    words = sentences.split()
    for word in words:
        word = strip_punctuation(word)
        if word in positive_words:
            count = count + 1
    return count

def get_neg(sentences):
    sentences = sentences.lower()
    count = 0
    words = sentences.split()
    for word in words:
        word = strip_punctuation(word)
        if word in negative_words:
            count = count + 1
    return count

def get_retwet(sentence):
    lst = sentence.split(',')
    return int(lst[-2])

def get_replies(sentence):
    lst = sentence.split(',')
    return int(lst[-1][:-1])

with open("project_twitter_data.csv") as data_f:
    lines = data_f.readlines()
    lst = ""
    for lin in lines[1:]:
        retweet = get_retwet(lin)
        replies = get_replies(lin)
        pos_score = get_pos(lin)
        neg_score = get_neg(lin)
        net_score = pos_score - neg_score
        lst = "{}, {}, {}, {}, {}".format(str(retweet), str(replies) ,str(pos_score), str(neg_score), str(net_score))
        results.append(lst)


with open("resulting_data.csv", "w") as file:
    header = {}
    names = ['Number of Retweets, ', 'Number of Replies, ', 'Positive Score, ', 'Negative Score, ', 'Net Score']
    for item in names:
        file.write(item)
    file.write('\n')
    for item in results:
        file.write(item)
        file.write('\n')
