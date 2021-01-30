import os

basedir = os.path.abspath(os.path.dirname(__file__))
os.environ["DB_USER"] = "doadmin"
os.environ["DB_PASSWORD"] = "vn1dzzs4o9r5jvhi"
os.environ["DB_URL"] = "dev-faas-do-user-7830134-0.a.db.ondigitalocean.com"
os.environ["DB_PORT"] = "25060"
os.environ["DB_NAME"] = "cfo_faas"


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
