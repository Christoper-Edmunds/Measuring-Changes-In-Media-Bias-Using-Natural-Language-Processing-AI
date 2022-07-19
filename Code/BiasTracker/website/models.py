from sqlalchemy import func
from . import db
import datetime

class biasdatabase(db.Model):
    id = db.Column('Id', db.Integer, primary_key=True)
    KeyFigure = db.Column('KeyFigure', db.String(150), unique=False)
    Sentiment = db.Column('Sentiment', db.Float)
    Date = db.Column('Date', db.String(200))
    Article_URL = db.Column('URL', db.String(2000))