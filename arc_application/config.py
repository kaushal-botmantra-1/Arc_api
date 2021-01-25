import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    class config contains configurable parameters of the project
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'Botmantra@123@cfo_bridge')
    VERSION = "1.0.0"


class DevelopmentConfig(Config):
    """
    Development config contains configurable parameters for development environment.
    It inherits the base config class
    """
    ENVIRONMENT = "Development"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 8000


class ProductionConfig(Config):
    """
    Production config contains configurable parameters for Production environment.
    It inherits the base config class
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ""
    PORT = 8000


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
