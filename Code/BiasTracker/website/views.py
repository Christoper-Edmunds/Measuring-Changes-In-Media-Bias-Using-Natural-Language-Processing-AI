from flask import Blueprint, render_template, request
from .models import biasdatabase
from . import db
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():

    sentiment_axis1 = []
    date_axis1 = []
    KeyFigure1 = ""

    
    if request.method == 'POST':
        KeyFigure1 = request.form.get('KeyFigure1')
        KeyFigure1 = KeyFigure1.lower()
        print(KeyFigure1)

        table_data = biasdatabase.query.filter_by(KeyFigure=KeyFigure1).all()

        for row in table_data:
            print ("Key Figure:", row.KeyFigure, "Sentiment: ",row.Sentiment, "Address:",row.Date)
            sentiment_axis1.append(row.Sentiment)

            date_axis1_preproces = row.Date

            date_axis1.append(date_axis1_preproces)

        print(date_axis1)

        duplicate_sentiment_removed = []
        duplicate_date_removed = []
        while len(date_axis1) > 0:
            duplicates = []
            duplicates_average = 0
            duplicates_count = 0
            iterator = 0

            for i in date_axis1:
                if date_axis1[0] == i:
                    duplicates.append(iterator)

                iterator += 1

            duplicates_count = len(duplicates)
            duplicate_date_removed.append(date_axis1[0])

            for index in reversed(duplicates):
                
                duplicates_average = duplicates_average + sentiment_axis1[index]


                del date_axis1[index]
                del sentiment_axis1[index]

                
            duplicate_sentiment_removed.append(duplicates_average / duplicates_count)
        
        date_axis1 = duplicate_date_removed
        sentiment_axis1 = duplicate_sentiment_removed
                







    return render_template("home.html", verticalrow1=sentiment_axis1,  horizontalrow1=date_axis1,  name1=KeyFigure1)

