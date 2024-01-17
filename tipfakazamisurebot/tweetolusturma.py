import random
import re

class RastgeleTweetSec:
    def __init__(self):
        pass

    def rastgele_tweet_sec(self):

        with open("hashtaglar.txt", "r") as file:
            hashtags = file.readlines()

        with open("tweetler.txt", "r") as file:
            tweets = file.readlines()

        with open("mentionlar.txt", "r") as file:
            mentions = file.readlines()

        selected_tweet = random.choice(tweets).strip()
        selected_mentions = random.sample(mentions, k=3)
        selected_hashtags = random.sample(hashtags, k=3)

        new_tweet = selected_tweet
        for mention in selected_mentions:
            new_tweet += f" @{mention.strip()}"
        for hashtag in selected_hashtags:
            new_tweet += f" #{hashtag.strip()}"
        
        if len(new_tweet) > 280:
            new_tweet = re.sub(r"(\s@\w+)\s*(?!.*\s@\w+)$", "", new_tweet)
        if len(new_tweet) > 280:
            new_tweet = re.sub(r"(\s#\w+)\s*(?!.*\s#\w+)$", "", new_tweet)
        if len(new_tweet) > 280:
            new_tweet = re.sub(r"(\s@\w+)\s*(?!.*\s@\w+)$", "", new_tweet)
        if len(new_tweet) > 280:
            new_tweet = re.sub(r"(\s#\w+)\s*(?!.*\s#\w+)$", "", new_tweet)
        if len(new_tweet) > 280:
            new_tweet = re.sub(r"(\s@\w+)\s*(?!.*\s@\w+)$", "", new_tweet)

        return new_tweet
