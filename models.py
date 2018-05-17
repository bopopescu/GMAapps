from pkgapp import db
import datetime
class User(db.Model):
	__tablename__ = 'User'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

class QuestionBank(db.Model):
	__tablename__ = 'QuestionBank'
	id = db.Column(db.Integer, primary_key=True)
	Publisher=db.Column(db.String(4), index=True)
	Book = db.Column(db.String(4), index=True)
	Year = db.Column(db.String(4), index=True)
	Section = db.Column(db.String(4), index=True)
	q_no= db.Column(db.Integer,nullable=False)
	q_text = db.Column(db.Text(20000),nullable=False)
	A = db.Column(db.Text(6000), nullable=False)
	B = db.Column(db.Text(6000), nullable=False)
	C = db.Column(db.Text(6000), nullable=False)
	D = db.Column(db.Text(6000), nullable=False)
	E = db.Column(db.Text(6000), nullable=False)
	Correct_ans = db.Column(db.String(2),nullable=False)

	def __repr__(self):
		return '<Question : {}>'.format(self.q_text)

class Results(db.Model):
	__tablename__ = 'Results'
	row_id = db.Column(db.Integer, primary_key=True)
	user_id=db.Column(db.Integer, db.ForeignKey('User.id'))
	q_id=db.Column(db.Integer, db.ForeignKey('QuestionBank.id'))
	ans_selected=db.Column(db.Text(4000),nullable=False)
	attempCount = db.Column(db.Integer)
	#time_taken = db.Column(db.String(6),nullable=False)
	#timestamp = db.Column(db.DateTime,default=datetime.datetime.utcnow)

	def __repr__(self):
		return '<Question : {}>'.format(self.row_id)