# Base imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import sys
from flask_cdn import CDN
from flask_cors import CORS


# IMPORT ALL BLUEPRINT .PY FILES
# AUTH ROUTES
from ROUTES.auth_routes import auth_blueprint

# ADDITIONAL ROUTES
from ROUTES.additional_blueprint_routes import client_dashboard_blueprint

# INIT APP AND CORS SUPPORT FOR CDN
app = Flask(__name__)
CORS(app)

# INIT DB
db = SQLAlchemy(app)

# REGISTER ALL BLUEPRINTS AFTER IMPORTING ABOVE
# REGISTERING AUTH BLUEPRINTS
app.register_blueprint(auth_blueprint)
# REGISTERING ADDITIONAL BLUEPRINTS
app.register_blueprint(client_dashboard_blueprint)


####### VERIFY IF DEPLOYED OR NOT, THIS WILL SWITCH WHICH CONFIG FILE IS USED FOR LOCAL VS DEPLOYED #######
is_deployed = True

# Config switcher
if is_deployed:
    app.config.from_pyfile(os.path.abspath(os.getcwd()) + '/CONFIG/deployed_config.py')
    build_version = app.config['BUILD_VERSION']

else:
    app.config.from_pyfile(os.path.abspath(os.getcwd()) + '/CONFIG/development_config.py')
    build_version = app.config['BUILD_VERSION']
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
####### VERIFY IF DEPLOYED OR NOT #######


# Import all of views
from ROUTES.views import *

# Config Login Manager w/ a User Loader
login_manager = LoginManager()
login_manager.init_app(app)

# init CDN via flask_cdn with URL in CONFIG files
cdn = CDN()
cdn.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from models import db, User
    return User.query.get(int(user_id))


if __name__ == "__main__":
    # Optional Cache settings
    #app.jinja_env.cache = {}
    # Run app
    app.run(debug=app.config['DEBUG'])