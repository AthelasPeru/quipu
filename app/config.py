import private
import os

class Config(object):
	SECRET_KEY = os.environ.get("SECRET_KEY", private.SECRET_KEY)
	STORMPATH_API_KEY_FILE = os.environ.get("STORMPATH_API_KEY_FILE", private.STORMPATH_API_KEY_FILE)
	STORMPATH_APPLICATION = "Quipu"


class DevelConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"


class ProdConfig(Config):
	pass


config = {
	"default": DevelConfig,
	"devel": DevelConfig,
	"production": ProdConfig
}

