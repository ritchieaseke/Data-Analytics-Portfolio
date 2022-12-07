#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install  and import Snscrape to scrape tweets from twitter
get_ipython().system('pip install snscrape')
import snscrape.modules.twitter as sntwitter

# Import Pandas libary to convert the generated tweets list to dataframe
import pandas as pd


# In[2]:


# Create a list to append all the tweet data
tweet_container = []
tweet_count = 0

# Use .TwitterSearchScraper() to append the tweet data to the tweet_container list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('nhs service since:2021-01-01 until:2021-12-31').get_items()):
    if i > 2000000:
        break
    if tweet.lang == 'en': # Scrape tweets only written in English
        if str(tweet.place) != 'None':
            place = tweet.place.__dict__ 
            if place['countryCode'] == 'GB': # Scrape tweets only tweeted in the UK
                tweet_container.append([tweet.user.username,
                                     tweet.user.verified,
                                     tweet.user.created,
                                     tweet.user.followersCount,
                                     tweet.user.friendsCount,
                                     tweet.retweetCount,
                                     tweet.lang,
                                     tweet.date,
                                     tweet.likeCount,
                                     tweet.sourceLabel,
                                     tweet.id,
                                     tweet.content,
                                     tweet.hashtags,
                                     tweet.conversationId,
                                     tweet.inReplyToUser,
                                     tweet.coordinates.__dict__,
                                     tweet.place.__dict__])
                tweet_count += 1
                if tweet_count == 1500:
                    break

# Print the number of tweets successfully scrapped 
print(tweet_count, 'have been successfully scraped!')


# In[3]:


# Convert the list into a dataframe
tweet_df = pd.DataFrame(tweet_container, columns=["User",
                                                   "Verified",
                                                   "Date Created",
                                                   "Follows Count",
                                                   "Friends Count",
                                                   "Retweet_Count",
                                                   "Language",
                                                   "Date_Tweet",
                                                   "Number_of_Likes",
                                                   "Source_of_Tweet",
                                                   "Tweet_Id",
                                                   "Tweet",
                                                   "Hashtags",
                                                   "Conversation_Id",
                                                   "In_reply_To",
                                                   "Coordinates",
                                                   "Place"])

# Output the first 5 rows
tweet_df[['User', 'Tweet', 'Number_of_Likes', 'Date_Tweet', 'Place']].head()


# In[4]:


# Print a summary of the data frame
tweet_df.info()


# In[5]:


# Save the data frame as a cvs file
tweet_df.to_csv('tweet_NHSService2021_raw.csv', index=False, header=True)

