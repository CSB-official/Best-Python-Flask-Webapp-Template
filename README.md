# python-flask-webapp-template
The absolute best Python Flask starter template for web apps, website, APIs, PWAs etc. WITHOUT HITTING CIRCULAR IMPORTS.

Steps to run locally:
- pip install all requirements
- python3 app.py

Core Libraries:
- Flask (Web Framework)
- Flask-login (Easily handle users authentication)
- Flask-SQLAlchemy (pythonic db query wrapper)
- Flask-cdn (critical for quick load times)
- Flask-cors (allows cdn to work properly / enables CORS support)

Useful reusable lines of code:
- Dynamic binding example for serving static files properly: 
- <link href="{{ url_for('static', filename='img/favicon.ico') }}" rel="shortcut icon">

Protected (will not error on data that does not exist) way of getting data out of POST requests: 
- request.form.get('create_new_account', "")

Set session cookie for user instance:
- session['store_in_session'] = store_this_var

Get session cookie for user instance:
- retrieve_this_var = session['store_in_session']