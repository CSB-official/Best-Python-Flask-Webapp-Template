from flask import Blueprint, render_template, request, redirect, session

from flask_login import login_user, logout_user


# Combine login and create user route
@auth_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    from models import db, User

    try:
        logout_user()
    except:
        print("New user logging in")

    message = ''

    if request.method == 'POST':

        # If creating account
        if request.form.get('create_new_account', "") == "Submit":
            if request.form.get('new_password', "") == request.form.get('confirm_new_password', ""):
                try:
                    new_user = User(
                        email=request.form.get('email', ""),
                        password=request.form.get('confirm_new_password', ""),
                        first_name=request.form.get('firstname', ""),
                        last_name=request.form.get('lastname', ""),
                        phone=request.form.get('phonenumber', ""),
                    )
                    db.session.add(new_user)
                    db.session.commit()
                    message = 'Account successfully created!'
                except:
                    message = 'Warning: This account already exists.'
            else:
                message = "Warning: The input passwords do not match, please try again."

        # If logging in
        if request.form.get('login_user', "") == "Submit":
            if request.form.get('password', "") != "":

                user = User.query.filter_by(
                    email=request.form.get('email', "")).first()
                
                if user:
                    if user.password == request.form.get('password', ""):
                        login_user(user)
                        db.session.close()
                        return redirect('/next_page_route')

                    else:
                        message = "Incorrect password, please try again."
                else:
                    message = "Email does not exist in our system, please try again."

    db.session.close()
    return render_template('/login.html', message=message)
