# Data Analytics Portfolio
This is a repository of data analytic projections I have completed from personal interests to develop and showcase my skills following completition of the IBM Data Analytics Professional Certificate program on Coursera.
> [View certificate](https://www.coursera.org/account/accomplishments/specialization/certificate/3A3L55KNPPW7)

___

### Project 1: Sentiment analysis of NHS service tweets between 2017 and 2022
Platforms and skills demonstrated:
- Python 3 via Jupyter Notebook
- SQL via PostgreSQL's pgAdmin 4
- IBM Watson Studio for visualisation

<details><summary>STEP 1 - Data Scraping</summary>
<p>

#### Snscrape was used to scrape twitter for tweets on "NHS Service"
  The results of which are appended to a list, converted to a pandas dataframe. The data was cleaned by removing dubplicate tweets before being saved as a csv file.
  This process is repeated for each year between 2017 and 2022.
  > [Veiw code](https://github.com/ritchieaseke/Data-Analytics-Portfolio/blob/b43b0c6e2dcb1b85f2a371c471bd138aee83968d/Project1_nhsSentimentAnalysis/sentiment_analysis_twitter_data_scrapping.py)

</p>
</details>

<details><summary>STEP 2 - The Natural Language Toolkit</summary>
<p>

#### The Natural Language Toolkits (NLTKs) pre-trained sentiment analyzer was used to calculate the compound sentiment score (CSS) of all the tweets.
  The results of which are appended appended to the original dataframe in a new column. Each CSS is then classified as negative, positive or neutral in another column. The new dataframe is then saved as a CSV file
  > [Veiw code](https://github.com/ritchieaseke/Data-Analytics-Portfolio/blob/b43b0c6e2dcb1b85f2a371c471bd138aee83968d/Project1_nhsSentimentAnalysis/sentiment_analysis_twitter_data_scrapping.py)

</p>
</details>
