from flask import render_template, redirect,url_for,abort,request,flash
from . import main
from app.requests import get_quote
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Subscriber
from ..import db, photos
import secrets
import os
from PIL import Image
from .forms import UpdateProfile,CreateBlog
from ..email import mail_message



#Views
@main.route('/')
def index():
    quote = get_quote()
    page = request.args.get('page',1, type = int )
    blogs = Blog.query.order_by(Blog.time.desc()).paginate(page = page, per_page = 3)
    return render_template('index.html', blogs=blogs,quote = quote)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join('app/static/photos', picture_filename)
    
    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename

@main.route('/profile',methods = ['POST','GET'])
@login_required
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture_file = save_picture(form.profile_picture.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Succesfully updated your profile')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static',filename = 'photos/'+ current_user.profile_pic_path) 
    return render_template('profile/profile.html', profile_pic_path=profile_pic_path, form = form)