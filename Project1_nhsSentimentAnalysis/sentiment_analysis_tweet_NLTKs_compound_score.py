#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Import NLTKs SentimentIntensityAnalyzer
from nltk.sentiment import SentimentIntensityAnalyzer

# Create an instance of nltk.sentiment.SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# In[27]:


# Deactive URLs in the tweets to avoid accidental clicks
tweet_df['Tweet'] = [t.replace("://", "//") for t in tweet_df['Tweet']]

# Check a tweet to confirm deactivation of URL
tweet_df['Tweet'][0]


# In[62]:


# Calculate the compound sentiment score of each tweet and append the results in a list
polarity = [round(sia.polarity_scores(tweet)['compound'], 2) for tweet in tweet_df['Tweet']]

# Add a new column to tweet_df contianing each tweets compount sentiment score
tweet_df['Sentiment_Score'] = polarity

# Print the first 5 rows
tweet_df[['Tweet', 'Sentiment_Score']].head()


# In[76]:


# Create a For loop to count and classify the compound sentiment scores into positive, negative and unclassified 
sentiment_classification = []

for compound_score in tweet_df['Sentiment_Score']:
    total_tweet_count += 1
    if compound_score > 0:
        sentiment_classification.append('Positive')
    if compound_score < 0:
        sentiment_classification.append('Negative')
    if not (compound_score > 0 or compound_score < 0):
        sentiment_classification.append('Unclassified')

# Add a new column to tweet_df contianing each tweets sentiment classification
tweet_df['Sentiment_Classification'] = sentiment_classification

# Print the first 5 rows
tweet_df[['Tweet', 'Sentiment_Score', 'Sentiment_Classification']].head()


# In[94]:


# Save the changes to tweet_df in a CVS file
tweet_df.to_csv('tweet_NHSService.csv', index=False, header=True)

