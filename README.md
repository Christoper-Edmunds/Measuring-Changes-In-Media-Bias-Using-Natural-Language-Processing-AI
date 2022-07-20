# Measuring Changes In Media Bias Using Natural Language Processing AI
A dissertation project seeking to test the practicality of detecting changes in bias in a media organisation, by using NLP technologies and Machine Learning.

Specifically the tool processes every article posted to the BBC News website. Finds the main named entity in every sentence based on certain rules, assesses the sentiment of that sentence and attatches that sentiment to the named entity, weights all named entities sentiments based on the overall sentiment of the article, and enters this into a database with its date and article details. 

On the user end, a django web server is hosted where the user can view how the sentiment of a named entity has changed over time in a graph format. 

#### Project being tested with "BBC" as a string showing how positve or negative the BBC has been about itself over time, -1 is very negative and 1 is very positive
![Final Image of project being tested](https://raw.githubusercontent.com/Christoper-Edmunds/Measuring-Changes-In-Media-Bias-Using-Natural-Language-Processing-AI/main/Documentation/unknown.png)


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
- TextBlob

#### Component Based Engineering Structure 
![Component Map](https://raw.githubusercontent.com/Christoper-Edmunds/Measuring-Changes-In-Media-Bias-Using-Natural-Language-Processing-AI/main/Documentation/ComponentBasedSoftwareEngineering.png)


#### Whitebox design concept for a potential future version, potential future developments are well documented in the dissertation under the documentation folder
![whitebox design concept showing various additional features](https://raw.githubusercontent.com/Christoper-Edmunds/Measuring-Changes-In-Media-Bias-Using-Natural-Language-Processing-AI/main/Documentation/Whitebox%20Annotated.png)

