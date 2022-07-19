#Sentiment Analysis

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

#from textblob import TextBlob
#from textblob.sentiments import NaiveBayesAnalyzer

nlp = spacy.load('en_core_web_trf')
nlp.add_pipe("spacytextblob")   #not sure if this can be outside the function



def Sentiment(text):

    doc = nlp(text)
    sentiment_value = str(doc._.blob.polarity)

    #blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    #sentiment_value = blob.sentiment

    return sentiment_value

def Key_Figure(text):
    doc = nlp(text)

    #print("\n" + text)

    key_figure_value = ""
    key_label_value = ""

    for ent in doc.ents:
        Key_Figure = None
        Key_Label = None

        #print("Key Figure: " + ent.text + "\nType of Key Figure: " +  ent.label_)

        Key_Figure = ent.text
        Key_Label = ent.label_
        

        #Key figure decision tree
        #The first key figure is typically the primary subject of a sentence 
        #Additionally there is a heirarchy of figure types, heirarchy overrides position in sentence
        #The heirarchy of most important figure type in a sentance is 
        # PERSON > ORGANISATION >NATIONALITY/RELIGIOUS/POLITICAL GROUP > COUNTRY/CITY/STATE
        
        #example string : writing for Name-Opinion Magazine, "bob is rubbish" says BobSucksINC CEO Jim

        #example output decision tree
        #Name-Opinion Magazine is first named entity, so is initial primary candidate
        #Next named entity is "bob", as this is defined as a person, it outranks the magazine as an organisation and hence becomes primary candidate
        #bobSucksINC being an organisation is below "bob" in the heirarchy so is ignored, Jim is on the same level, but comes after bob, so is also ignored.
        
        #example output: bob 

        if key_label_value != "PERSON":   #If a person has not already been found
            if Key_Label == "PERSON":   #if the key figure is a person
                key_label_value = "PERSON"
                key_figure_value = Key_Figure

            if key_label_value != "ORG": #If a organisation has not already been found
                if Key_Label == "ORG":   #if the key figure is a organisation
                    key_label_value = "ORG"
                    key_figure_value = Key_Figure

                if key_label_value != "NORP": #If a group has not already been found
                    if Key_Label == "NORP":   #if the key figure is a group
                        key_label_value = "NORP"
                        key_figure_value = Key_Figure

                    if key_label_value != "GPE": #If a place has not already been found
                        if Key_Label == "GPE":   #if the key figure is a place
                            key_label_value = "GPE"
                            key_figure_value = Key_Figure

                        if key_label_value != "GPE" and key_label_value != "NORP" and key_label_value != "ORG" and key_label_value != "PERSON": #if no appropriote type of figure was found 
                            key_figure_value = "FigureNotFound" 

        else:
            pass 

    if len(doc.ents) == 0:
        key_figure_value = "FigureNotFound"  #This is a catch in case there's no key figure at all
    
    return key_figure_value
    