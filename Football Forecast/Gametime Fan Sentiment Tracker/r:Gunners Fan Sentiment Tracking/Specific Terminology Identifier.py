import praw
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
Sentiment_Analyzer = SentimentIntensityAnalyzer()

reddit = praw.Reddit(
    client_id = "i2cta5pwoTbutnWT0m9Z8g",
    client_secret = "cVMc4BUuT1gy4-Ot5olgTFcVT2m47g",
    user_agent = "Football Forecast by Football_Forecast",
)

import sys
sys.stdout = open('Specific-Terminology-Identifier.txt', 'w')

#NECESSARY INFO
Match_Thread_ID = "1f5kqf7"

Unprocessed_Comments = 0
Total_Comments = 0

post = reddit.submission(id=Match_Thread_ID)
post.comments.replace_more(limit=None)
for comment in post.comments.list():
    Total_Comments += 1
    tokens = word_tokenize (comment.body)
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Compound_Score = Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Compound_Score == 0:
        Unprocessed_Comments +=1
        print (comment.body, " --> ", Compound_Score)

print ("\n", Unprocessed_Comments, "/", Total_Comments)
    
sys.stdout.close()