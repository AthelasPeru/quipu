from extensions import db

from sqlalchemy import (
	Column,
	Integer,
	String,
	Text,
	ForeignKey,
	Table, 
	DateTime
)

from sqlalchemy.orm import backref, relationship

class User(db.Model):
	"""
	Usuario de nuestra aplicacion.

	"""

	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	stp_id = Column(String(255, convert_unicode=True), unique=True)
	username = Column(String(25, convert_unicode=True), unique=True)
	name = Column(String(25, convert_unicode=True))
	lastname = Column(String(25, convert_unicode=True))
	
	#One to many
	groups = relationship("Group", order_by="Group.id", backref="tutor")
	students = relationship("Student", order_by="Student.lastname", backref="tutor")

	# Many to many (Not yet implemented correctly)
	sessions = relationship("Session", order_by="Session.date", backref="tutor")
	group_sessions = relationship("GroupSession", order_by="GroupSession.date", backref="tutor")

	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return "<this is user {}>".format(self.username)



class Student(db.Model):
	"""
	Alumno relacionado a un Usuario
	"""
	__tablename__ = "students"

	id = Column(Integer, primary_key=True)
	code = Column(String(255, convert_unicode=True), unique=True)
	name = Column(String(255, convert_unicode=True))
	lastname = Column(String(255, convert_unicode=True))
	user_id = Column(Integer, ForeignKey("users.id"))
	group_id = Column(Integer, ForeignKey("groups.id"))
	sessions = relationship("Session", order_by="Session.date", backref="student")
	age = Column(Integer)

	def __init__(self, code, name, lastname, tutor):
		self.code = code
		self.name = name
		self.lastname = lastname
		self.tutor = tutor


	def __repr__(self):
		return "<this is {0} {1}, and his student-code is {2}>".format(self.name, self.lastname, self.code)

class Group(db.Model):
	"""
	Grupo de Alumnos relacionado a un Usuario
	"""
	__tablename__ = "groups"

	id = Column(Integer, primary_key=True)
	code = Column(String(255, convert_unicode=True), unique=True)
	students = relationship("Student", order_by="Student.lastname", backref="group")
	sessions = relationship("GroupSession", order_by="GroupSession.date", backref="group")
	user_id = Column(Integer, ForeignKey("users.id"))

	def __init__(self, code, tutor, students=[]): 
		self.code = code
		self.students = students
		self.tutor = tutor

	def __repr__(self):
		return "<this is the group with code of = {}>".format(self.code)



# Not yet correctly implemented
class Session(db.Model):
	"""
	Sesiones relacionadas a un User y a un Student
	"""
	
	__tablename__ = "sessions"

	id = Column(Integer, primary_key=True)
	date = Column(String(255, convert_unicode=True))
	user_id = Column(Integer, ForeignKey("users.id"))
	student_id = Column(Integer, ForeignKey("students.id"))


	def __init__(self, date, tutor, student):
		self.date = date
		self.tutor = tutor
		self.student = student

	def __repr__(self):
		return "<this is session {}>".format(self.id)

# Not yet correctly implemented
class GroupSession(db.Model):
	"""
	Sesiones relacionadas a un User y a un Group
	"""
	
	__tablename__ = "group_sessions"

	id = Column(Integer, primary_key=True)
	date = Column(String(255, convert_unicode=True))
	user_id = Column(Integer, ForeignKey("users.id"))
	group_id = Column(Integer, ForeignKey("groups.id"))

	def __init__(self, date, tutor, group):
		self.date = date
		self.tutor = tutor
		self.group = group

	def __repr__(self):
		return "<this is session {}>".format(self.id)



