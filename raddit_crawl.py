# -*- coding: utf-8 -*-
import praw
from datetime import datetime

import re

def clean_text(text):
    # �ٹٲ� ����
    text = text.replace('\n', ' ').strip()
    # ����, ����, �Ϲ����� �������� ����� (�ܴ̿� ����)
    text = re.sub(r"[^a-zA-Z0-9.,!?\'\"()\-:; ]", "", text)
    return text

# Reddit infor  
reddit = praw.Reddit(
    client_id="_8SGtgdhCTt0LmiZAAupnA",
    client_secret="TA1TOqLehetiygfNMboyp-ZxN4nMWQ",
    user_agent="zzz okjimin",
    username="TurbulentDream6933",       
    password="Ok75792000"
)

#Hot post in "CryptoMarkets"
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
searchSize = 50
subreddit = reddit.subreddit("CryptoMarkets")
f = open("raddit_hot_comments_" + now + ".txt" , 'w', encoding = 'utf-8')

f.write("Record Start Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
for i,post in enumerate(subreddit.hot(limit = searchSize), start = 1):
    f.write(f"\n\nPost {i}:\n")
    f.write(f"Title: {clean_text(post.title)}\n")
    #f.write(f"URL: {post.url}\n")
    f.write("Comments:\n")

    post.comments.replace_more(limit=0)
    for comment in post.comments[:5]:
        cleaned_comment = clean_text(comment.body)
        #cleaned_comment = comment.body.replace('\n', ' ').strip()
        f.write(f"- {cleaned_comment}\n")

f.write("\nRecord End Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
f.close()

