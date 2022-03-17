from flask import Blueprint, render_template, request, redirect, session
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

client_dashboard_blueprint = Blueprint('client_dashboard_blueprint', __name__, template_folder='templates')


@client_dashboard_blueprint.route("/account_home", methods=['GET', 'POST'])
@login_required
def account_home():
    return render_template('/account_home.html', current_user=current_user)


@client_dashboard_blueprint.route("/account_settings", methods=['GET', 'POST'])
@login_required
def account_settings():
    from models import db, User

    message = ''

    if request.method == 'POST':
        
        # If creating account
        if request.form.get('save_changes', "") == "Submit":
            current_user.email = request.form.get('email', "")
            current_user.first_name = request.form.get('firstname', "")
            current_user.last_name = request.form.get('lastname', "")
            current_user.phone = request.form.get('phonenumber', "")
            
            if request.form.get('new_password', "") == request.form.get('confirm_new_password', ""):
                current_user.password = request.form.get('confirm_new_password', "")

            message='Account updated'
            db.session.commit()

    return render_template('/account_settings.html', message = message)


@client_dashboard_blueprint.route("/logout", methods=['GET', 'POST'])
def logout():
    try:
        logout_user()
    except:
        print("No user to log out")

    return redirect('/')