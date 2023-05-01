import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    SECRET_KEY = 'Io%OERc-W||$%@?|5K9X8`ZmV,u}_%n.h78v|=swJMPTlP=K:XiYX:1o,F|54'
    SECRET_KEY = os.getenv('SECRET_KEY') or SECRET_KEY

    RECAPTCHA_SITE_KEY = '6LcG5XUaAAAAABrZvxKadcW5S30MGVuBKwYuzjGc'
    RECAPTCHA_SECRET_KEY = '6LcG5XUaAAAAANTwDqaEIHpY6mJApz-7Y1iZ2mpJ'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    DEBUG = True

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = bool(os.getenv('MAIL_USE_TLS', False))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    db_user_name = os.getenv('DB_USER')
    db_user_pass = os.getenv('DB_PASS')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    if os.getenv('DB_TYPE') == "mysql":
        charset = 'utf8mb4'
        SQLALCHEMY_DATABASE_URI = f'mysql://{db_user_name}:{db_user_pass}@{db_host}:{db_port}/{db_name}?charset={charset}'

    elif os.getenv('DB_TYPE') == "postgresql":
        charset = 'utf8'
        SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user_name}:{db_user_pass}@{db_host}:{db_port}/{db_name}?client_encoding={charset}'

    elif os.getenv('DB_TYPE') == "sqlite":
        charset = 'utf8'
        SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_name}.db'


class ProductionConfig(BaseConfig):
    ENV = "production"
    DEBUG = False

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = bool(os.getenv('MAIL_USE_TLS', False))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    db_user_name = os.getenv('DB_USER')
    db_user_pass = os.getenv('DB_PASS')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    if os.getenv('DB_TYPE') == "mysql":
        charset = 'utf8mb4'
        SQLALCHEMY_DATABASE_URI = f'mysql://{db_user_name}:{db_user_pass}@{db_host}:{db_port}/{db_name}?charset={charset}'

    else:
        charset = 'utf8'
        SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user_name}:{db_user_pass}@{db_host}:{db_port}/{db_name}?client_encoding={charset}'
