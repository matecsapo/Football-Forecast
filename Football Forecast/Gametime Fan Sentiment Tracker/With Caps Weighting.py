import praw

reddit = praw.Reddit(
    client_id = "i2cta5pwoTbutnWT0m9Z8g",
    client_secret = "cVMc4BUuT1gy4-Ot5olgTFcVT2m47g",
    user_agent = "Football Forecast by Football_Forecast",
)

Phase_5 = []
Phase_10 = []
Phase_15 = []
Phase_20 = []
Phase_25 = []
Phase_30 = []
Phase_35 = []
Phase_40 = []
Phase_45 = []
Phase_Stoppage_1 = []
Phase_Halftime = []
Phase_50 = []
Phase_55 = []
Phase_60 = []
Phase_65 = []
Phase_70 = []
Phase_75 = []
Phase_80 = []
Phase_85 = []
Phase_90 = []
Phase_Stoppage_2 = []


post = reddit.submission(id="1euhuir")
post.comments.replace_more(limit=None)
Num_Comments = 0
for comment in post.comments.list():
    if comment.created_utc <= 1723903500:
        Phase_5.append(comment.body)
    elif comment.created_utc <= 1723903800:
        Phase_10.append(comment.body)
    elif comment.created_utc <= 1723904100:
        Phase_15.append(comment.body)
    elif comment.created_utc <= 1723904400:
        Phase_20.append(comment.body)
    elif comment.created_utc <= 1723904700:
        Phase_25.append(comment.body)
    elif comment.created_utc <= 1723905000:
        Phase_30.append(comment.body)
    elif comment.created_utc <= 1723905300:
        Phase_35.append(comment.body)
    elif comment.created_utc <= 1723905600:
        Phase_40.append(comment.body)
    elif comment.created_utc <= 1723905900:
        Phase_45.append(comment.body)
    elif comment.created_utc <= 1723905960:
        Phase_Stoppage_1.append(comment.body)
    elif comment.created_utc <= 1723906920:
        Phase_Halftime.append(comment.body)
    elif comment.created_utc <= 1723907220:
        Phase_50.append(comment.body)
    elif comment.created_utc <= 1723907520:
        Phase_55.append(comment.body)
    elif comment.created_utc <= 1723907820:
        Phase_60.append(comment.body)
    elif comment.created_utc <= 1723908120:
        Phase_65.append(comment.body)
    elif comment.created_utc <= 1723908420:
        Phase_70.append(comment.body)
    elif comment.created_utc <= 1723908720:
        Phase_75.append(comment.body)
    elif comment.created_utc <= 1723909020:
        Phase_80.append(comment.body)
    elif comment.created_utc <= 1723909320:
        Phase_85.append(comment.body)
    elif comment.created_utc <= 1723909620:
        Phase_90.append(comment.body)
    elif comment.created_utc <= 1723909920:
        Phase_Stoppage_2.append(comment.body)
    Num_Comments += 1
#all comments from match-thread are now stored the game phases

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
Sentiment_Analyzer = SentimentIntensityAnalyzer()
New_Positive_Words = {
    "massive" : 2.0,
    "airpods" : 1.1,
    "albert" : 0.8,
    "stuivenberg" : 0.8,
    "goat" : 2.1,
    "coyg" : 2.7,
    "vamos" : 2.6,
    "hattrick" : 1.0,
    "boyz" : 1.2,
    "foggin" : 2.1,
    "gais" : 2.0,
    "motm" : 1.5,
    "gargantuan" : 2.0,
    "jover" : 0.8,
    "coyfg" : 2.7,
    "lfg" : 2.4,
    "Zidane" : 0.9,
    "spicy" : 1.8,
    "star" : 2.5,
    "starboy" : 2.6,
    "starman" : 2.6,
    "starboi" : 2.6,
    "banger" : 2.2,
    "chilli" : 2.3,
    "silky" : 2.0,
    "royce" : 2.5,
    "king" : 2.7,
    "waka" : 2.7,
    "d'or" : 1.5,
    "tsamina" : 2.7,
    "mina" : 2.7,
    "giroud" : 1.2,
    "mbappe" : 1.2,
    "warra" : 1.2,
    "golden" : 1.5,
    "fantasy" : 1.5,
    "purple" : 1.5,
    "glove" : 1.5,
    "augustvertz" : 2.5,
    "cooking" : 2.2,
    "magic" : 2.1,
    "racoon" : 2.0,
    "raccoon" : 2.0,
    "poty" : 2.3,
    "henry" : 1.5,
    "saucy" : 1.9,
    "magical" : 1.8,
    "class" : 2.0,
    "world" : 2.0,
    "tross" : 2.0,
    "estandards" : 2.3,
    "proper" : 1.4
}
Sentiment_Analyzer.lexicon.update(New_Positive_Words)
New_Negative_Words = {
    "washed" : -2.2,
    "cooked" : -2.2,
    "ref" : -2.1,
    "commentators" : -1.5,
    "clown" : -2.1,
    "city" : -1.9,
    "115" : -1.9,
    "manchester" : -1.4,
    "var" : -2.1,
    "ass" : -2.1,
    "red" : -1.7,
    "pgmol" : -2.4,
    "subs" : -1.3,
    "officiating" : -1.3
}
Sentiment_Analyzer.lexicon.update(New_Negative_Words)

Caps_Lock_Weight = 0.60

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_5)):
    tokens = word_tokenize (Phase_5[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_5)
Average_Neg_Score = Average_Neg_Score / len(Phase_5)
Average_Compound_Score = Average_Compound_Score / len(Phase_5)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_10)):
    tokens = word_tokenize (Phase_10[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_10)
Average_Neg_Score = Average_Neg_Score / len(Phase_10)
Average_Compound_Score = Average_Compound_Score / len(Phase_10)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_15)):
    tokens = word_tokenize (Phase_15[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_15)
Average_Neg_Score = Average_Neg_Score / len(Phase_15)
Average_Compound_Score = Average_Compound_Score / len(Phase_15)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_20)):
    tokens = word_tokenize (Phase_20[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_20)
Average_Neg_Score = Average_Neg_Score / len(Phase_20)
Average_Compound_Score = Average_Compound_Score / len(Phase_20)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_25)):
    tokens = word_tokenize (Phase_25[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_25)
Average_Neg_Score = Average_Neg_Score / len(Phase_25)
Average_Compound_Score = Average_Compound_Score / len(Phase_25)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_30)):
    tokens = word_tokenize (Phase_30[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_30)
Average_Neg_Score = Average_Neg_Score / len(Phase_30)
Average_Compound_Score = Average_Compound_Score / len(Phase_30)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_35)):
    tokens = word_tokenize (Phase_35[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_35)
Average_Neg_Score = Average_Neg_Score / len(Phase_35)
Average_Compound_Score = Average_Compound_Score / len(Phase_35)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_40)):
    tokens = word_tokenize (Phase_40[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_40)
Average_Neg_Score = Average_Neg_Score / len(Phase_40)
Average_Compound_Score = Average_Compound_Score / len(Phase_40)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_45)):
    tokens = word_tokenize (Phase_45[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_45)
Average_Neg_Score = Average_Neg_Score / len(Phase_45)
Average_Compound_Score = Average_Compound_Score / len(Phase_45)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_Stoppage_1)):
    tokens = word_tokenize (Phase_Stoppage_1[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_Stoppage_1)
Average_Neg_Score = Average_Neg_Score / len(Phase_Stoppage_1)
Average_Compound_Score = Average_Compound_Score / len(Phase_Stoppage_1)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_Halftime)):
    tokens = word_tokenize (Phase_Halftime[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_Halftime)
Average_Neg_Score = Average_Neg_Score / len(Phase_Halftime)
Average_Compound_Score = Average_Compound_Score / len(Phase_Halftime)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_50)):
    tokens = word_tokenize (Phase_50[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_50)
Average_Neg_Score = Average_Neg_Score / len(Phase_50)
Average_Compound_Score = Average_Compound_Score / len(Phase_50)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_55)):
    tokens = word_tokenize (Phase_55[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_55)
Average_Neg_Score = Average_Neg_Score / len(Phase_55)
Average_Compound_Score = Average_Compound_Score / len(Phase_55)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_60)):
    tokens = word_tokenize (Phase_60[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_60)
Average_Neg_Score = Average_Neg_Score / len(Phase_60)
Average_Compound_Score = Average_Compound_Score / len(Phase_60)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_65)):
    tokens = word_tokenize (Phase_65[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_65)
Average_Neg_Score = Average_Neg_Score / len(Phase_65)
Average_Compound_Score = Average_Compound_Score / len(Phase_65)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_70)):
    tokens = word_tokenize (Phase_70[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_70)
Average_Neg_Score = Average_Neg_Score / len(Phase_70)
Average_Compound_Score = Average_Compound_Score / len(Phase_70)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_75)):
    tokens = word_tokenize (Phase_75[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_75)
Average_Neg_Score = Average_Neg_Score / len(Phase_75)
Average_Compound_Score = Average_Compound_Score / len(Phase_75)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_80)):
    tokens = word_tokenize (Phase_80[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_80)
Average_Neg_Score = Average_Neg_Score / len(Phase_80)
Average_Compound_Score = Average_Compound_Score / len(Phase_80)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_85)):
    tokens = word_tokenize (Phase_85[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_85)
Average_Neg_Score = Average_Neg_Score / len(Phase_85)
Average_Compound_Score = Average_Compound_Score / len(Phase_85)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_90)):
    tokens = word_tokenize (Phase_90[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_90)
Average_Neg_Score = Average_Neg_Score / len(Phase_90)
Average_Compound_Score = Average_Compound_Score / len(Phase_90)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
for i in range (len(Phase_Stoppage_2)):
    tokens = word_tokenize (Phase_Stoppage_2[i])
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    Processed_Word = ' '.join(lemmatized_tokens)
    Average_Pos_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["pos"]
    Average_Neg_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["neg"]
    Average_Compound_Score += Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"]
    if Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0 and Processed_Word.isupper():
        if Average_Compound_Score > 0:
            Average_Compound_Score += Caps_Lock_Weight
        elif Average_Compound_Score < 0:
            Average_Compound_Score -= Caps_Lock_Weight
Average_Pos_Score = Average_Pos_Score / len(Phase_Stoppage_2)
Average_Neg_Score = Average_Neg_Score / len(Phase_Stoppage_2)
Average_Compound_Score = Average_Compound_Score / len(Phase_Stoppage_2)
print ("Compound: ", Average_Compound_Score, "; Pos: ", Average_Pos_Score, "; Neg: ", Average_Neg_Score, "; Pos - Neg: ", Average_Pos_Score - Average_Neg_Score)


print ("\n", Num_Comments, "out of ", post.num_comments)
