from flask import render_template, Blueprint, redirect, url_for

main = Blueprint("main", __name__)

from extensions import db
from models import User, Session, Student, Group

@main.route("/")
def index():
	users = db.session.query(User).all()
	sessions = db.session.query(Session).all()
	return render_template(
		"index.html",
		users=users,
		sessions=sessions,
	)

@main.route("/addUser/<string:name>")
def addUser(name):
	user = User(name)
	db.session.add(user)
	db.session.commit()
	return redirect(url_for("main.index"))


@main.route("/addSession/<string:date>/<int:username>")
def addSession(date, username):
	#Parseamos la base de datos para encontrar el usuario por su username unico
	user = db.session.query(User).filter_by(username=username).first()
	
	#Creamos la nueva sesion con el id de ese usuario
	if user:
		new_session = Session(date, user.id)
		db.session.add(session)
		db.session.commit()
	
	#Redirect al home, hayamos creado la sesion o no.
	return redirect(url_for("main.index"))