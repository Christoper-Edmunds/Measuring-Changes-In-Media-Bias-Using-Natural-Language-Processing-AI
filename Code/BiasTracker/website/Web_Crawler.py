#Web crawler

from fileinput import filename
from bs4 import BeautifulSoup
import requests
import re
import csv
import os
#parent_url = "https://www.bbc.co.uk/news/uk" 





"""                                                       URL PARSER                                                          """
""" The purpose of this block of code is to scrape the URL's of all of the pages currently linked via the "latest update" tab """

#Parent URL's refer to the URLs of the pages in which "latest update" is contained for each specific catagory of news, this is where individual article urls are sourced
#Child URL's refer to the URLs of specific articles 

def PageUrls(parent_url):
    result = requests.get(parent_url)
    doc = BeautifulSoup(result.text, "html.parser")
    
    Processed_Articles = []
    Current_Articles = []
    Unprocessed_Articles = []
    file_Name = "website\BBC.csv"

    if os.stat(file_Name).st_size == 0:
        with open(file_Name, "w") as f:
            data = csv.writer(f)
            data.writerow(Processed_Articles)

    else:
        with open(file_Name ,'r')as f:
            data = csv.reader(f) 
            Processed_Articles = next(data)



    for link in doc.find_all("a",{"class":"qa-heading-link lx-stream-post__header-link", 'href': True}):

        #print("https://www.bbc.co.uk" + link.get('href'))
        website_holder = ("https://www.bbc.co.uk" + link.get('href'))

        Current_Articles.append(website_holder)

        if website_holder not in Processed_Articles:
            Processed_Articles.append(website_holder)
            Unprocessed_Articles.append(website_holder)

        

                
    if len(Processed_Articles) >= 400:
        Processed_Articles.pop(0)

    with open(file_Name, "w") as f:
        data = csv.writer(f)
        data.writerow(Processed_Articles)


    #Unprocessed_Articles.append(website_holder)  #THIS IS FOR TESTING, DELETE THIS #THIS IS FOR TESTING, DELETE THIS #THIS IS FOR TESTING, DELETE THIS #THIS IS FOR TESTING, DELETE THIS 
    return Unprocessed_Articles


"""                                                       Text Scraper                                                        """
""" The purpose of this block of code is go to the URL's of the latest news articles, and seperate out the main body of text  """
"""              It also does a degree of cleaning and prepreparing the text so it can be readily processed                   """


def PageContents (child_url):

    website = 0


    result = requests.get(child_url)
    doc = BeautifulSoup(result.text, "html.parser")

    for aside_removed in doc.find_all("aside"):
        aside_removed.decompose()
    

    website_content = ""
    for link in doc.find_all("p", class_="ssrcss-1q0x1qg-Paragraph eq5iqo00"):
    
        website_paragraph = link.get_text()
        website_content = website_content + " " + website_paragraph
        #body = doc.find(property="articleBody")

        

    website_content_cleaned = website_content.replace("This video can not be played", " ").replace("Â© 2022 BBC. The BBC is not responsible for the content of external sites. Read about our approach to external linking.", " ").replace("Send your story ideas to south.newsonline@bbc.co.uk.", " ")
    website_content_cleaned = website_content_cleaned.strip()
    #print(website_content_cleaned + "\n")

    website_content_split = website_content_cleaned.split('. ')
    
    counter = 0
    for i in website_content_split:
        website_content_split[counter].strip()
        counter +=1 

    #print(*website_content_split, sep='\n')
    website += 1 

    return website_content_split


#this is just a clean tidied away method for managing the filenames for the processed articles csv files 

def fileNameMaker(parent_url): 
    file_name = ""

    if parent_url == "https://www.bbc.co.uk/news/coronavirus":
        file_name = "COVID.csv"

    elif parent_url == "https://www.bbc.co.uk/news/uk":
        file_name = "UK.csv"

    elif parent_url == "https://www.bbc.co.uk/news/world":
        file_name = "WORLD.csv"

    elif parent_url == "https://www.bbc.co.uk/news/business":
        file_name = "BUSINESS.csv"

    elif parent_url == "https://www.bbc.co.uk/news/politics":
        file_name = "POLITICS.csv"

    elif parent_url == "https://www.bbc.co.uk/news/technology":
        file_name = "TECH.csv"

    elif parent_url == "https://www.bbc.co.uk/news/science_and_environment":
        file_name = "SCIENCE.csv"

    elif parent_url == "https://www.bbc.co.uk/news/health":
        file_name = "HEALTH.csv"

    elif parent_url == "https://www.bbc.co.uk/news/education":
        file_name = "EDUCATION.csv"

    elif parent_url == "https://www.bbc.co.uk/news/entertainment_and_arts":
        file_name = "ARTS.csv"

    return file_name

