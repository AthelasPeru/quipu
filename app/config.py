class Config(object):
	SECRET_KEY = "mydickismysuperkeybitch"


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

