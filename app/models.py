from flask_sqlalchemy.model import Model
from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash

