


from datetime import datetime
from flask_login import UserMixin
from albumy.extensions import db


#用户
class User(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,index=True)
	email = db.Column(db.String(254),unique=True,index=True)
	password_hash = db.Column(db.String(128))
	name = db.Column(db.String(30))
	website = db.Column(db.String(255))
	bio = db.Column(db.String(120))
	location = db.Column(db.String(50))
	member_since = db.Column(db.Datetime,default=datetime.utcnow)
	#用户状态
	confirmed = db.Column(db.Boolean,default=False)