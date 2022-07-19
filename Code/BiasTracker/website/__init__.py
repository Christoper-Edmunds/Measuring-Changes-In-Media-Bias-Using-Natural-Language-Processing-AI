from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "SentimentDatabase.db"   

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chrisistesting'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .Info import Info

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(Info, url_prefix='/')
    
    from .models import biasdatabase

    return app  


