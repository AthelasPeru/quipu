from flask.ext.stormpath import(
	login_required,
	StormpathError,
	login_user,
	logout_user,
	user as _user
)

from flask import(
	render_template, 
	Blueprint, 
	redirect, 
	url_for,
	flash
)

main = Blueprint("main", __name__)

from extensions import db
from models import User, Session, Student, Group, GroupSession
from forms import AddStudentForm


@main.route("/", methods=["GET", "POST"])
@login_required
def index():

	#Intentamos revisar si el usuario existe en la base de datos.
	try:
		#Buscamos un user cuyo stp_id sea igual que el link del usuario de stormpath que se ha logeado.
		user = db.session.query(User).filter_by(stp_id=_user.href).first()
	except:
		raise ValueError("Problemas con la base de datos")
	
	#Si no encontramos un usuario.
	if not user:
		
		#Sacamos el username de su email (Esto hay que cambiarlo o permitirle al ususario cambiarlo)
		username = _user.email.split("@")[0]
		
		#Creamos un nuevo usario con username y stp_id
		user = User(username=username, stp_id=_user.href, name=_user.given_name, lastname=_user.surname, email=_user.email)
		
		#Lo agregamos a la sesion
		db.session.add(user)

		#Comiteamos la sesion
		db.session.commit()

	#Ahora importamos nuestro formulario para agregar Students
	form = AddStudentForm()

	#Si valida el formulario
	if form.validate_on_submit():
		#Agregamos los datos necesarios
		code = form.code.data
		name = form.name.data
		lastname = form.lastname.data
		#Y los usamos para crear un nuevo Student en nuestr BD
		student = Student(code=code, name=name, lastname=lastname, tutor=user)

		#Luego, metemos ese student en el User ya creado
		user.students.append(student)

		#Luego, metemos las dos vainasen la BD efectivamente.
		db.session.add_all([user, student])
		db.session.commit()

		flash("Your student was added succesfully", "success")

	#Finalmente, el index debe renderizar el template Index.html y mandarle el user y el form.
	return render_template(
		"index.html",
		user=user,
		form=form
	)

