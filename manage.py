from flask.ext.script import Manager
from app import create_app

from app.extensions import db

from app.models import User, Session, Student, Group

app = create_app("default")

manager = Manager(app)


@manager.shell
def make_shell_context():
	return dict(
		app = app,
		db=db,
		User=User,
		Session=Session,
		Student=Student,
		Group=Group
	)


if __name__ == '__main__':
	manager.run()