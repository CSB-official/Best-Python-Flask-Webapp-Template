# IMPORT OS, USED TO FIND DB PATH
import os
from os.path import join, dirname, realpath

# DB-CONFIG
# THIS IS TO BE USED FOR LOCAL SQLITE DB CONNECTION
file_path = os.path.abspath(os.getcwd())+"/local-db.db"
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+file_path
SQLALCHEMY_TRACK_MODIFICATIONS = False

# MISC CONFIG
DEBUG = True
SECRET_KEY = "mybigsecretkey"
BUILD_VERSION = "v1.0.0" + " | Development"

# FLASK-CDN SETUP
CDN_DOMAIN = '3hhf99des03d.cloudfront.net'
CDN_TIMESTAMP = False

# FILE UPLOAD CONFIG
UPLOADS_PATH = join(dirname(realpath(__file__)), 'tmp') + "/"
UPLOADS_PATH = UPLOADS_PATH.replace("/CONFIG", "")