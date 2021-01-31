class Config(object):
	"""Base config, uses staging database server."""
	DEBUG = False
	TESTING = False
	DB_SERVER = "192.168.0.1"
	SECRET_KEY = "your_secret_key_here"

	@property
	def DATABASE_URI(self):       # Note: all caps
		return "mysql://user@{}/foo".format(self.DB_SERVER)


class ProductionConfig(Config):
	"""Uses production database server."""
	DB_SERVER = "192.168.19.32"


class DevelopmentConfig(Config):
	DB_SERVER = "localhost"
	DEBUG = True


class TestingConfig(Config):
	DB_SERVER = "localhost"
	DEBUG = True
	DATABASE_URI = "sqlite:///:memory:"
