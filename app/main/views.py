from flask import render_template, redirect,url_for,abort,request
from . import main
from app.requests import get_quote
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Subscriber
from ..import db, photos

#Views
@main.route('/')
def index():
    quote = get_quote()
    page = request.args.get('page',1, type = int )
    blogs = Blog.query.order_by(Blog.time.desc()).paginate(page = page, per_page = 3)
    return render_template('index.html', blogs=blogs,quote = quote)
