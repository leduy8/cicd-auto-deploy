import logging
import os

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


def get_env():
    env = BaseConfig.ENVIRONMENT

    if env.lower() in ["development", "dev"]:
        return DevelopmentConfig
    elif env in ["production", "prod", "staging", "stag"]:
        return ProductionConfig
    elif env in ["testing", "test"]:
        return TestingConfig


class BaseConfig:
    LOGGING_LEVEL = logging.INFO
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ENVIRONMENT = os.environ.get("ENVIRONMENT")

    # ? For sqlite
    # 'sqlite:///' + os.path.join(basedir, '{db_name}.db')
    # ? For MySQL
    # "mysql+pymysql://root:123456@127.0.0.1/{db_name}"
    # ? For PostgreSQL
    # 'postgresql+psycopg2://postgres:123456@localhost/{db_name}'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_DEV")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestingConfig(DevelopmentConfig):
    TESTING = True

    # ? For sqlite
    # 'sqlite:///' + os.path.join(basedir, '{db_name}_test.db')
    # ? For MySQL
    # "mysql+pymysql://root:123456@127.0.0.1/{db_name}_test"
    # ? For PostgreSQL
    # 'postgresql+psycopg2://postgres:123456@localhost/{db_name}_test'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_TEST")


config = get_env()
