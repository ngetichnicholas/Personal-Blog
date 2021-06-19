from flask import render_template, redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog
from ..import db, photos
from ..requests import get_quote

#Views
@main.route('/', methods = ["GET", "POST"])
def index():
    quote = get_quote()


    return render_template("index.html",quote = quote)