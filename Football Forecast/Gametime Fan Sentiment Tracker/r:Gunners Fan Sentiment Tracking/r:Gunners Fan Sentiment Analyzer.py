import praw

reddit = praw.Reddit(
    client_id = "i2cta5pwoTbutnWT0m9Z8g",
    client_secret = "cVMc4BUuT1gy4-Ot5olgTFcVT2m47g",
    user_agent = "Football Forecast by Football_Forecast",
)

#NECESSARY INFO
Pre_Match_Thread_ID = ""
Match_Thread_ID = ""
Post_Match_Thread_ID = ""
Kickoff_TimeStamp = 0
Stoppage_Time_1 = 0
Second_Kickoff_Timestamp = 0
Stoppage_Time_2 = 0

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

post = reddit.submission(id=Match_Thread_ID)
post.comments.replace_more(limit=None)
for comment in post.comments.list():
    if comment.created_utc <= Kickoff_TimeStamp + 1*300:
        Phase_5.append(comment.body)
    elif comment.created_utc <= Kickoff_TimeStamp + 2*300:
        Phase_10.append(comment.body)
    elif comment.created_utc <= Kickoff_TimeStamp + 3*300:
        Phase_15.append(comment.body)
    elif comment.created_utc <= Kickoff_TimeStamp + 4*300:
        Phase_20.append(comment.body)
    elif comment.created_utc <= Kickoff_TimeStamp + 5*300:
        Phase_25.append(comment.body)
    elif comment.created_utc <= Kickoff_TimeStamp + 6*300:
        Phase_30.append(comment.body)
    elif comment.created_utc <= Kickoff_TimeStamp + 7*300:
        Phase_35.append(comment.body)
    elif comment.created_utc <= Kickoff_TimeStamp + 8*300:
        Phase_40.append(comment.body)
    elif comment.created_utc <= Kickoff_TimeStamp + 9*300:
        Phase_45.append(comment.body)
    elif comment.created_utc <= Kickoff_TimeStamp + 9*300 + Stoppage_Time_1:
        Phase_Stoppage_1.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 0*300:
        Phase_Halftime.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 1*300:
        Phase_50.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 2*300:
        Phase_55.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 3*300:
        Phase_60.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 4*300:
        Phase_65.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 5*300:
        Phase_70.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 6*300:
        Phase_75.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 7*300:
        Phase_80.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 8*300:
        Phase_85.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 9*300:
        Phase_90.append(comment.body)
    elif comment.created_utc <= Second_Kickoff_Timestamp + 9*300 + Stoppage_Time_2:
        Phase_Stoppage_2.append(comment.body)
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
    "airpod" : 1.1,
    "albert" : 0.8,
    "stuivenberg" : 0.8,
    "goat" : 2.1,
    "goated" : 2.1,
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
    "bossard" : 2.0,
    "estandards" : 2.3,
    "proper" : 1.4,
    "sleep" : 2.0,
    "masterclass": 2.1,
    "immensive" : 2.0,
    "clutch" : 2.1,
    "monster" : 2.0,
    "unit" : 2.3,
    "shithouse" : 1.7,
    "shithouser" : 1.7,
    "sleepy" : 2.0,
    "rocket" : 2.0,
    "mvp" : 2.5,
    "Hathaway" : 2.4,
    "boss" : 2.0,
    "underrated" : 2.1,
    "willy" : 2.4,
    "bow" : 2.1,
    "cold" : 2.0,
    "maldini" : 2.2,
    "california" : 2.2,
    "californication" : 2.2,
    "sensational" : 2.2,
    "supersub" : 2.2,
    "aura" : 2.2,
    "calafiorication" : 2.3,
    "californication" : 2.3
}
Sentiment_Analyzer.lexicon.update(New_Positive_Words)
New_Negative_Words = {
    "washed" : -2.2,
    "cooked" : -2.2,
    "ref" : -2.1,
    "refs" : -2.1,
    "referees" : -2.1,
    "refereeing" : -2.1,
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
    "officiating" : -1.3,
    "wtf" : -2.1,
    "shite" : -2.1,
    "shit" : -2.1,
    "boo" : -2.0,
    "booing" : -2.0,
    "brainless" : -1.5,
    "foul" : -2.1,
    "cucks" : -2.2,
    "thundercunt" : -2.3,
    "dogshit" : -2.1,
    "disasterclass" : -2.0
}
Sentiment_Analyzer.lexicon.update(New_Negative_Words)

Caps_Lock_Weight = 0.50
Z_W_Weight = 0.75

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_5) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_5) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_5) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_10) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_10) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_10) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_15) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_15) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_15) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_20) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_20) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_20) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_25) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_25) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_25) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_30) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_30) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_30) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_35) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_35) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_35) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_40) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_40) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_40) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_45) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_45) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_45) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_Stoppage_1) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_Stoppage_1) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_Stoppage_1) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_Halftime) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_Halftime) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_Halftime) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_50) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_50) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_50) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_55) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_55) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_55) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_60) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_60) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_60) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_65) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_65) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_65) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_70) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_70) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_70) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_75) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_75) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_75) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_80) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_80) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_80) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_85) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_85) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_85) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_90) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_90) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_90) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Phase_Stoppage_2) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Phase_Stoppage_2) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Phase_Stoppage_2) - Z_W_Weight*Zero_Words)
print ("Compound: ", Average_Compound_Score)






#pre-match thread
Pre_Match_Comments = []
post = reddit.submission(id=Pre_Match_Thread_ID)
post.comments.replace_more(limit=None)
for comment in post.comments.list():
    Pre_Match_Comments.append (comment.body)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
for i in range (len(Pre_Match_Comments)):
    tokens = word_tokenize (Pre_Match_Comments[i])
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Pre_Match_Comments) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Pre_Match_Comments) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Pre_Match_Comments) - Z_W_Weight*Zero_Words)
print ("\n", "Pre-Match Compound: ", Average_Compound_Score)





#post-match thread
Post_Match_Comments = []
post = reddit.submission(id=Post_Match_Thread_ID)
post.comments.replace_more(limit=None)
for comment in post.comments.list():
    Post_Match_Comments.append (comment.body)

Average_Pos_Score = 0
Average_Neg_Score = 0
Average_Compound_Score = 0
Zero_Words = 0
for i in range (len(Post_Match_Comments)):
    tokens = word_tokenize (Post_Match_Comments[i])
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
    elif Sentiment_Analyzer.polarity_scores(Processed_Word)["compound"] == 0:
        Zero_Words += 1
Average_Pos_Score = Average_Pos_Score / (len(Post_Match_Comments) - Z_W_Weight*Zero_Words)
Average_Neg_Score = Average_Neg_Score / (len(Post_Match_Comments) - Z_W_Weight*Zero_Words)
Average_Compound_Score = Average_Compound_Score / (len(Post_Match_Comments) - Z_W_Weight*Zero_Words)
print ("\n", "Post-Match Compound: ", Average_Compound_Score)