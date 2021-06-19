from flask import render_template, redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog
from ..import db, photos

#Views
@main.route('/', methods = ["GET", "POST"])
def index():
  '''
  Function to render home page with its data
  '''
  return render_template('index.html')