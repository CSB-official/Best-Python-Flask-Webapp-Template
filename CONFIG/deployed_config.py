# IMPORT OS, USED TO FIND DB PATH
import os
from os.path import join, dirname, realpath

# DB-CONFIG
# HEROKU POSTGRES URI
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# MISC CONFIG
DEBUG = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "mybigsecretkey"
BUILD_VERSION = "v1.0.0" + " | Production"

# FLASK-CDN SETUP
CDN_DOMAIN = '3hhf99des03d.cloudfront.net'
CDN_TIMESTAMP = False

# FILE UPLOAD CONFIG
UPLOADS_PATH = "/tmp/"