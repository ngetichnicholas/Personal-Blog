from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField, SubmitField,ValidationError
from wtforms.validators import Required,Email
from flask_login import current_user
from ..models import User

class UpdateProfile(FlaskForm):
  username = StringField('Enter Your Username', validators=[Required()])
  email = StringField('Email Address', validators=[Required(),Email()])
  bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
  profile_pic_path = FileField('profile picture', validators=[FileAllowed(['jpg','png'])])
  submit = SubmitField('Update')

class CreateBlog(FlaskForm):
  title = StringField('Title',validators=[Required()])
  description = TextAreaField('Blog Description',validators=[Required()])
  content = TextAreaField('Blog Content',validators=[Required()])
  submit = SubmitField('Post')