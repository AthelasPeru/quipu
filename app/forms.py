from flask_wtf import Form
from flask_wtf.html5 import IntegerField, EmailField, TelField, DateField
from wtforms import TextField, TextAreaField
from wtforms.validators import Required, Length

class AddStudentForm(Form):
	code = TextField("Student Code", validators=[Required()])
	name = TextField("Student Name", validators=[Required()])
	lastname = TextField("Student Name", validators=[Required()])

class AddGroupForm(Form):
	code = TextField("Group Code", validators=[Required()])
	