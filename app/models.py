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
	sessions = relationship("Session", order_by="Session.id", backref="user")

	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return "<this is user {}>".format(self.username)



class Session(db.Model):
	"""
	Sesiones relacionadas a un Usuario
	"""
	
	__tablename__ = "sessions"

	id = Column(Integer, primary_key=True)
	date = Column(String(255, convert_unicode=True))
	user_id = Column(Integer, ForeignKey("users.id"))

	def __init__(self, date, user_id):
		self.date = date
		self.user_id = user_id

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

	def __init__(self, code, name, lastname):
		self.code = code
		self.name = name
		self.lastname = lastname


	def __repr__(self):
		return "<this is {1}{2}, and his student-code is {3}".format(self.name, self.lastname, self.code)

class Group(db.Model):
	"""
	Grupo de Alumnos relacionado a un Usuario
	"""
	__tablename__ = "groups"

	id = Column(Integer, primary_key=True)

	def __init__(sefl):
		pass

	def __repr__(self):
		return "<this is the group with id = {}>".format(self.id)


