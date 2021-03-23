from textblob import TextBlob
import nltk
import streamlit as st
from textblob.sentiments import NaiveBayesAnalyzer
import sqlite3

st.write(""" 
## AJ Bamgbelu's Sentiment Analysis Generator

Insert your sample text in order to determine what your 
""")

# Database Functionality (Initialization)
conn = sqlite3.connect('C:\\Users\\Octopus\\CS4\\Sentiment-Analysis-Project\\userEntries.db')
cur = conn.cursor()
sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS entries (id integer PRIMARY KEY, entry TEXT NOT NULL, sentiment TEXT); """

if conn is not None:
    conn.execute(sql_create_projects_table)
    print("table should be created")
else:
    print("Error! cannot create the database connection.")


## Basic Functionality -- Inputs Text Generates Output
opinionInput = st.text_input('Enter some text')
if (st.button('Generate Sentiment') and opinionInput != ""):
    opinion = TextBlob(opinionInput, analyzer=NaiveBayesAnalyzer())
    st.write(opinion.sentiment)
    #Write insert statement here
    test = opinion.replace(" ", "") + " " + opinion.sentiment[0]
    strippedOpinion = str(opinion).replace(" ", "")
    resultingSentiment = str(opinion.sentiment[0])
    qry = "INSERT INTO entries(entry,sentiment) VALUES( '"+strippedOpinion+ "' , '"+resultingSentiment+"');"
    conn.execute(qry)
    conn.commit()
else:
     st.write('Provide an Input!')

# Test
#opinion = TextBlob("I hate Arsenal!", analyzer=NaiveBayesAnalyzer())
#print(opinion.sentiment)
#opinion = TextBlob("I hate Arsenal!")
#print(opinion.sentiment)
# End of Test
