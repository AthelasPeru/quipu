from flask import render_template, Blueprint, redirect, url_for

main = Blueprint("main", __name__)

from extensions import db
from models import User, Session, Student, Group, GroupSession

@main.route("/")
def index():
	users = db.session.query(User).all()
	sessions = db.session.query(Session).all()
	students = db.session.query(Student).all()
	groups = db.session.query(Group).all()
	groupSessions = db.session.query(GroupSession).all()
	return render_template(
		"index.html",
		users=users,
		sessions=sessions,
		students=students,
		groups=groups,
		groupSessions=groupSessions,
	)

@main.route("/addUser/<string:name>")
def addUser(name):
	user = User(name)
	db.session.add(user)
	db.session.commit()
	return redirect(url_for("main.index"))


@main.route("/addStudent/<string:studentCode>/<string:name>/<string:lastname>/<string:username>")
def addStudent(studentCode, name, lastname, username):
	#Parseamos la base de datos para encontrar el usuario (tutor) de este alumno:
	tutor = db.session.query(User).filter_by(username=username).first()

	#Creamos al nuevo alumno, con el id del usuario (tutor)
	if tutor: 
		new_student = Student(studentCode, name, lastname, tutor=tutor)
		db.session.add(new_student)
		db.session.commit()

	#Redirect al home, hayamos creado al alumno o no
	return redirect(url_for("main.index"))


@main.route("/addToGroup/<string:groupCode>/<string:studentCode>/<string:username>")
def addToGroup(groupCode, studentCode, username):
	#Parseamos la base de datos para encontrar el usuario (tutor) de este alumno:
	tutor = db.session.query(User).filter_by(username=username).first()
	student = db.session.query(Student).filter_by(code=studentCode).first()
	group = db.session.query(Group).filter_by(code=groupCode).first()

	if tutor and student: 
		if group:
			#We add the group id to the student info
			student.group = group  #Aqui estoy llamando al backref definido en Group
			#We add the student info to the group
			group.students.append(student)
			db.session.add_all([group, student])
		else:
			new_group = Group(groupCode, tutor=tutor)
			new_group.students.append(student)
			db.session.add(new_group)
		db.session.commit()

	#Redirect al home, hayamos creado al alumno o no
	return redirect(url_for("main.index"))



@main.route("/addSession/<string:date>/<string:studentCode>/<string:username>")
def addSession(date, studentCode, username):
	#Parseamos la base de datos para encontrar el usuario por su username unico
	user = db.session.query(User).filter_by(username=username).first()
	student = db.session.query(Student).filter_by(code=studentCode).first()

	#Creamos la nueva sesion con el id de ese usuario
	if user:
		new_session = Session(date, user, student)
		db.session.add(new_session)
		db.session.commit()
	
	#Redirect al home, hayamos creado la sesion o no.
	return redirect(url_for("main.index"))



@main.route("/addGroupSession/<string:date>/<string:groupCode>/<string:username>")
def addGroupSession(date, groupCode, username):
	#Parseamos la base de datos para encontrar el usuario por su username unico
	user = db.session.query(User).filter_by(username=username).first()
	group = db.session.query(Group).filter_by(code=groupCode).first()
	
	#Creamos la nueva sesion con el id de ese usuario
	if user and group:
		new_session = GroupSession(date, user, group)
		db.session.add(new_session)
		db.session.commit()
	
	#Redirect al home, hayamos creado la sesion o no.
	return redirect(url_for("main.index"))


