from textblob import TextBlob
import nltk
import streamlit as st
from textblob.sentiments import NaiveBayesAnalyzer
import sqlite3
import tweepy
import numpy


consumer_key = '5qQHILVWzVhnyQ1th0zh60PyH'
consumer_secret = 'JkS3UfaWIDVIgGbYH5wz9K21dKa6wIhC9qeahUB0qVGNTO31wU'
access_token = '1371668314183892998-raTq0eYTo1xn26R6nOv6kxJu7heprU'
access_token_secret = '4JPBQVi0j01G2uKpJ79cN3XEAsEceTzPjVldER7dUwW0i'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


st.title(""" ## Genie: The Machine Learning Powered Sentiment Analysis Generator """)
st.header(""" - an Automated Sentiment Analysis Solution """)

# Database Functionality (Initialization)
#conn = sqlite3.connect('C:\\Users\\Octopus\\CS4\\Sentiment-Analysis-Project\\userEntries.db')
#cur = conn.cursor()
#sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS entries (id integer PRIMARY KEY, entry TEXT NOT NULL, sentiment TEXT); """

#if conn is not None:
 #   conn.execute(sql_create_projects_table)
  #  print("table should be created")
#else:
 #   print("Error! cannot create the database connection.")


## Basic Functionality -- Inputs Text Generates Output
st.subheader(""" Basic Text Sentiment Functionality - text from any Social Media Platform """)
opinionInput = st.text_input('Type in some text')
if (st.button('Generate Sentiment!') and opinionInput != ""):
    opinion = TextBlob(opinionInput, analyzer=NaiveBayesAnalyzer())
    st.write(opinion.sentiment)
    #Write insert statement here
    test = opinion.replace(" ", "") + " " + opinion.sentiment[0]
    strippedOpinion = str(opinion).replace(" ", "")
    resultingSentiment = str(opinion.sentiment[0])
    #qry = "INSERT INTO entries(entry,sentiment) VALUES( '"+strippedOpinion+ "' , '"+resultingSentiment+"');"
    #conn.execute(qry)
    #conn.commit()
else:
     st.write('Provide an Input!')




st.subheader(""" Twitter Sentiment Functionality - queries text from Twitter Social Media Platform """)
twitterOpinionInput = st.text_input('Enter text')
if (st.button('Generate Sentiment') and opinionInput != ""):
    stro = ""
    for tweets in api.search(q=twitterOpinionInput, lang="en"):
        stro += tweets.text + " "
    print(stro)
    opinion = TextBlob(stro, analyzer=NaiveBayesAnalyzer())
    st.write(opinion.sentiment)
    #Write insert statement here
    test = opinion.replace(" ", "") + " " + opinion.sentiment[0]
    strippedOpinion = str(opinion).replace(" ", "")
    resultingSentiment = str(opinion.sentiment[0])
    #qry = "INSERT INTO entries(entry,sentiment) VALUES( '"+strippedOpinion+ "' , '"+resultingSentiment+"');"
    #conn.execute(qry)
    #conn.commit()
else:
     st.write('Provide an Input!')
# Test
#opinion = TextBlob("I hate Arsenal!", analyzer=NaiveBayesAnalyzer())
#print(opinion.sentiment)
#opinion = TextBlob("I hate Arsenal!")
#print(opinion.sentiment)
# End of Test
