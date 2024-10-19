import praw

reddit = praw.Reddit(
    client_id = "xxx",
    client_secret = "xxx",
    user_agent = "Football Forecast by Football_Forecast",
)

#Phase_5 = []
#Phase_10 = []
#Phase_15 = []
#Phase_20 = []
#Phase_25 = []
#Phase_30 = []
#Phase_35 = []
#Phase_40 = []
#Phase_45 = []
#Phase_Stoppage_1 = []
#Phase_Halftime = []
#Phase_50 = []
#Phase_55 = []
#Phase_60 = []
#Phase_65 = []
#Phase_70 = []
#Phase_75 = []
#Phase_80 = []
#Phase_85 = []
#Phase_90 = []
#Phase_Stoppage_2 = []

Comment_Phases = [""] * 21

post = reddit.submission(id="1euhuir")
post.comments.replace_more(limit=None)
Num_Comments = 0
for comment in post.comments.list():
    if comment.created_utc <= 1723903500:
        Comment_Phases[0] += (comment.body)
    elif comment.created_utc <= 1723903800:
        Comment_Phases[1] += (comment.body)
    elif comment.created_utc <= 1723904100:
        Comment_Phases[2] += (comment.body)
    elif comment.created_utc <= 1723904400:
        Comment_Phases[3] += (comment.body)
    elif comment.created_utc <= 1723904700:
        Comment_Phases[4] += (comment.body)
    elif comment.created_utc <= 1723905000:
        Comment_Phases[5] += (comment.body)
    elif comment.created_utc <= 1723905300:
        Comment_Phases[6] += (comment.body)
    elif comment.created_utc <= 1723905600:
        Comment_Phases[7] += (comment.body)
    elif comment.created_utc <= 1723905900:
        Comment_Phases[8] += (comment.body)
    elif comment.created_utc <= 1723905960:
        Comment_Phases[9] += (comment.body)
    elif comment.created_utc <= 1723906920:
        Comment_Phases[10] += (comment.body)
    elif comment.created_utc <= 1723907220:
        Comment_Phases[11] += (comment.body)
    elif comment.created_utc <= 1723907520:
        Comment_Phases[12] += (comment.body)
    elif comment.created_utc <= 1723907820:
        Comment_Phases[13] += (comment.body)
    elif comment.created_utc <= 1723908120:
        Comment_Phases[14] += (comment.body)
    elif comment.created_utc <= 1723908420:
        Comment_Phases[15] += (comment.body)
    elif comment.created_utc <= 1723908720:
        Comment_Phases[16] += (comment.body)
    elif comment.created_utc <= 1723909020:
        Comment_Phases[17] += (comment.body)
    elif comment.created_utc <= 1723909320:
        Comment_Phases[18] += (comment.body)
    elif comment.created_utc <= 1723909620:
        Comment_Phases[19] += (comment.body)
    elif comment.created_utc <= 1723909920:
        Comment_Phases[20] += (comment.body)
    Num_Comments += 1
#all comments from match-thread are now stored in Comment_Phases
#now we sentiment analyze them

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

for i in range (21):
    tokens = word_tokenize(Comment_Phases[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Comment_Phases[i] = ' '.join(lemmatized_tokens)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
Sentiment_Analyzer = SentimentIntensityAnalyzer()
for i in range (21):
    #print (Sentiment_Analyzer.polarity_scores(Comment_Phases[i]))
    print (Sentiment_Analyzer.polarity_scores(Comment_Phases[i])["pos"] - Sentiment_Analyzer.polarity_scores(Comment_Phases[i])["neg"], " --> ",
           Sentiment_Analyzer.polarity_scores(Comment_Phases[i]))

print ("\n", Num_Comments, "out of ", post.num_comments)
