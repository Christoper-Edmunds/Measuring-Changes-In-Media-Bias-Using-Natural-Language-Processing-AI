# Measuring-Changes-In-Media-Bias-Using-Natural-Language-Processing-AI
A dissertation project seeking to test the practicality of detecting changes in bias in a media organisation, by using NLP technologies and Machine Learning.

Specifically the tool processes every article posted to the BBC News website. Finds the main named entity in every sentence based on certain rules, assesses the sentiment of that sentence and attatches that sentiment to the named entity, weights all named entities sentiments based on the overall sentiment of the article, and enters this into a database with its date and article details. 

On the user end exists a web server where the user can view how the sentiment of a named entity has changed over time in a graph format. 

## Technologies Utilised

### Web Server 
- Flask
- Chart.js
- Bootstrap
- SQLite
- SQLAlchemy
- Python

### Web Crawler
- BeautifulSoup
- Requests

## Sentiment Analysis 
- Spacy 
-TextBlob
