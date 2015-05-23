# coding=UTF-8

from flask import Flask

from config import config

from extensions import toolbar, db, foundation, stormpath


def create_app(config_mode):
	
	app = Flask(__name__)
	
	#utilizamos el config desde el objeto llamado por el key config_model en el diccionario config importado arriba
	app.config.from_object(config[config_mode])

	# Permite arrancar el toolbar varias veces
	toolbar.init_app(app)

	#Permite arrancar foundation varias veces
	foundation.init_app(app)

	#Inicializamos stormpath para esta instancia de la aplicación
	stormpath.init_app(app)

	#Importamos las vistas
	from views import main

	#El blueprint no existe en la aplicacion hasta que lo registramos
	app.register_blueprint(main)

	#Arrancamos la base de datos
	db.init_app(app)

	db.create_all(app=app)



	

	return app


