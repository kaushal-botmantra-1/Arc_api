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
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + str(os.environ.get("DB_USER")) + ":" + str(os.environ.get("DB_PASSWORD")) + "@" + str(
        os.environ.get("DB_URL")) + ":" + str(os.environ.get("DB_PORT")) + "/" + str(os.environ.get("DB_NAME"))
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 5000
    HOST = "127.0.0.1"
    AGEING_REPORTS = os.path.join(
        os.getcwd(), 'arc_application', 'static', 'ageing_report')


class ProductionConfig(Config):
    """
    Production config contains configurable parameters for Production environment.
    It inherits the base config class
    """
    DEBUG = False
    ENVIRONMENT = "Production"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + str(os.environ.get("DB_USER")) + ":" + str(os.environ.get("DB_PASSWORD")) + "@" + str(
        os.environ.get("DB_URL")) + ":" + str(os.environ.get("DB_PORT")) + "/" + str(os.environ.get("DB_NAME"))
    PORT = 8000
    HOST = "0.0.0.0"


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
