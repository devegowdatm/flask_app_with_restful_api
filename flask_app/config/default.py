import os

APP_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_FOLDER = os.path.abspath(os.path.join(APP_ROOT_DIR, "static"))

MEDIA_FOLDER = os.path.join(STATIC_FOLDER, "media")

DEBUG = True

PROJECT_ENV = 'development'

SECRET_KEY = 'P\xef\xfa\x85\xc3\x88\xd6\xb0$\xf59\xbc\x88q|\xaf\x0c\x89K\x07\xdd\xdf\xd5\x8a'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dev:dev@123@127.0.0.1:5432/dev_db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
