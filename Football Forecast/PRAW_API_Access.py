import praw

reddit = praw.Reddit(
    client_id = "xxx",
    client_secret = "xxx",
    user_agent = "Football Forecast by Football_Forecast",
)

#subreddit = reddit.subreddit ("Gunners")
#hot_posts = subreddit.hot(limit=20)
#for post in hot_posts:
#    print ("Title - ", post.title)
#    print ("Author - ", post.author)
#    print ("\n")

Arsenal_subreddit = reddit.subreddit("Gunners")
for i in range (2):
    posts = Arsenal_subreddit.new(limit=None)

    for post in posts:
        print (post.title)
        print ("\n")

