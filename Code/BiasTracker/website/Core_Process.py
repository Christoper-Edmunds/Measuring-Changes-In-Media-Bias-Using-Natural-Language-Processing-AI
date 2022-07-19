import Web_Crawler
import NLP_Processor
import numpy as np
import sqlite3
from sqlite3 import Error
from datetime import date
import schedule
import time

#This function takes the full sentance by sentance analysis of the text, and crunches it down into average sentiment values of each unique key-figure. 
def Analysis_Calculator(analysis_values, current_article):
    numpy_analysis_values = np.array(analysis_values) # converts the values array to a numpy values array


    
    final_values = []

    while len(numpy_analysis_values) > 0: #keeps going while there are still unprocessed duplicates 
        sentiment_average = 0.0
        
        numpy_duplicate_index = []
        numpy_duplicate_index = np.where(numpy_analysis_values == (numpy_analysis_values[0][0])) #finds the index of all duplicates of the first name (column 1 row 1) 
        numpy_duplicate_index = np.array(numpy_duplicate_index)[0]

        if len(numpy_duplicate_index) > 1:
            for index in numpy_duplicate_index:
                sentiment_average = sentiment_average + float((numpy_analysis_values[index][1])) # adds together the values
        else:
            sentiment_average = float(numpy_analysis_values[0][1])

            

        today = date.today()
        sentiment_average = sentiment_average / len(numpy_duplicate_index) #averages out the values

        row_holder = [numpy_analysis_values[0][0].lower(), round(sentiment_average, 2), today.strftime("%d/%m/%Y") ,current_article]


        final_values.append(row_holder) #this is where final row of end data is produced 
        numpy_analysis_values = np.delete(numpy_analysis_values, numpy_duplicate_index, axis=0) #deltes (array, row, column (as column is axis(0), it deletes the whole row))

    iterator = 0
    article_weight = 0.0
    for finished_row in final_values:

        if finished_row[0] == "figurenotfound":
            article_weight = final_values[iterator][1]
            final_values.pop(iterator)
        else:
            pass

        iterator += 1

    iterator_two = 0
    for finished_row in final_values:
        final_values[iterator_two][1] = final_values[iterator_two][1] + ((article_weight / 100) * 10) #weights all results by a percentage value of the sentences without key figures 
        iterator_two += 1
    return final_values

#This function establishes the connection to the sqlite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        #print(sqlite3.version)
    except Error as e:
        print(e)
    #finally:
        #if conn:
            #conn.close()
    return conn

#This function adds a row into the sqlite database 
def create_row(conn, final_values):
    sql = ''' INSERT INTO BiasDatabase(KeyFigure,Sentiment,Date,URL)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, final_values)
    conn.commit()
    return cur.lastrowid

#This function selects out the various parent URL's under which bbc articles are published 
def ParentUrlSelector(URLSelection):
    Current_Parent_URL = ""
    if URLSelection == 0:
        Current_Parent_URL = "https://www.bbc.co.uk/news/uk"
    elif URLSelection == 1: 
        Current_Parent_URL = "https://www.bbc.co.uk/news/world"
    elif URLSelection == 2: 
        Current_Parent_URL = "https://www.bbc.co.uk/news/business"
    elif URLSelection == 3: 
        Current_Parent_URL = "https://www.bbc.co.uk/news/politics" 
    elif URLSelection == 4: 
        Current_Parent_URL = "https://www.bbc.co.uk/news/technology"
    elif URLSelection == 5: 
        Current_Parent_URL = "https://www.bbc.co.uk/news/science_and_environment"
    elif URLSelection == 6: 
        Current_Parent_URL = "https://www.bbc.co.uk/news/health"
    elif URLSelection == 7: 
        Current_Parent_URL = "https://www.bbc.co.uk/news/education"
    elif URLSelection == 8: 
        Current_Parent_URL = "https://www.bbc.co.uk/news/entertainment_and_arts"
    
    return Current_Parent_URL


def MainBody():
    print("\n"+"Checking for new articles now! :D")
    print(time.ctime())
    for x in range (9):
        Unprocessed_Articles = Web_Crawler.PageUrls(ParentUrlSelector(x))

        print("Parent URL: " + ParentUrlSelector(x) + "\n")
        print(Unprocessed_Articles)
        print("\n")

        for i in Unprocessed_Articles:
            text_to_process = Web_Crawler.PageContents(i)
            current_article = i
            analysis_values = []

            print(current_article)
            for sentence_to_process in text_to_process:
                analysis_values.append([NLP_Processor.Key_Figure(sentence_to_process), NLP_Processor.Sentiment(sentence_to_process)])
            
            #print(analysis_values)

            final_values = Analysis_Calculator(analysis_values, current_article)

            print(final_values)

            conn = create_connection(r"website\SentimentDatabase.db")

            for finished_row in final_values:
                create_row(conn, finished_row)
            
            print(i + "\n")


MainBody()

schedule.every(30).minutes.do(MainBody)

while True:
    schedule.run_pending()
    time.sleep(1)