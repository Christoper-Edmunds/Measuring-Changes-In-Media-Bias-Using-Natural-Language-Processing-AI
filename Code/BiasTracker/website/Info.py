from flask import Blueprint, render_template

Info = Blueprint('Info', __name__)

@Info.route('/Info')
def Information():
    return render_template("Info.html")