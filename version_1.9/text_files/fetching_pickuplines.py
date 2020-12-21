# install praw (python wrapper for reddit's api)
from dotenv import load_dotenv
from pathlib import Path
import os
from praw import Reddit
from pandas import DataFrame

env_path = Path('../.env')
load_dotenv(dotenv_path=env_path)

reddit = Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT')
)

def get_subreddit_data(sub, lim):
    posts = [] # list of subreddits
    SUBREDDIT = reddit.subreddit(sub) # name of subreddit'
    LIMIT = lim # limit of posts

    for post in SUBREDDIT.hot(limit=LIMIT):
        posts.append([post.id, post.subreddit, post.title, post.url, post.selftext])

    posts = DataFrame(posts, columns=['id', 'subreddit', 'title', 'url', 'body'])
    return posts

df = get_subreddit_data('pickuplines', 1000)
df['possible pick-up line'] = df[['title', 'body']].apply(lambda x: ' '.join(x), axis=1)

f = open('pickup_lines.txt', 'w+')

for line in df['possible pick-up line']:
    newline = f'{ line }\n'
    f.write(newline)

f.close()