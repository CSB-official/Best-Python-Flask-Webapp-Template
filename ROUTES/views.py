# Base app imports
from app import app

# Flask Imports
from flask import Flask, redirect, session, request, render_template


# WEBSITE ROUTES 
#############################################################################


# ADD ERROR HANDLERS HERE, EXAMPLE 404 WITH REDIRECT TO COMING SOON PAGE BELOW
'''
@app.errorhandler(404)
def handle_404(e):
        return redirect(url_for('soon'))
'''


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('/index.html')
