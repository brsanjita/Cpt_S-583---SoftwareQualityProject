########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import Reserve, User
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import db


auth = Blueprint('auth', __name__) # create a Blueprint object that we name 'auth'

@auth.route('/login', methods=['GET', 'POST']) # define login page path
def login(): # define login page fucntion
    if request.method=='GET': # if the request is a GET we return the login page
        return render_template('login.html')
    else: # if the request is POST the we check if the user exist and with te right password
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user:
            flash('Please sign up before!')
            return redirect(url_for('auth.signup'))
        elif not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))

@auth.route('/signup', methods=['GET', 'POST'])# we define the sign up path
def signup(): # define the sign up function
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('signup.html')
    else: # if the request is POST, then we check if the email doesn't already exist and then we save data
        email = request.form.get('email')
        name = request.form.get('name')
        phone = request.form.get('phone')
        driving_license_number = request.form.get('driving_license_number')
        D_O_B = request.form.get('D_O_B')
        license_plate_number = request.form.get('license_plate_number')
        card_number = request.form.get('card_number')
        card_expiry = request.form.get('card_expiry')
        cvv = request.form.get('cvv')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, name=name, phone=phone, driving_license_number=driving_license_number, D_O_B=D_O_B, license_plate_number=license_plate_number, card_number=card_number, card_expiry=card_expiry, cvv=cvv, password=generate_password_hash(password, method='sha256')) #
        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

@auth.route('/logout') # define logout path
@login_required
def logout(): #define the logout function
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/reserve', methods=['GET', 'POST'])# we define the reserve path
def reserve(): # define the reserve function
    if request.method=='GET': # If the request is GET we return the reserve page and forms
        return render_template('reserve.html')
    else: # if the request is POST, then we check if the email doesn't already exist and then we save data
        name = request.form.get('name')
        parking_spot_number = request.form.get('parking_spot_number')
        Parking_start_datetime = request.form.get('Parking_start_datetime')
        Parking_end_datetime = request.form.get('Parking_end_datetime')
        
        new_reserve = Reserve(name=name, parking_spot_number=parking_spot_number, Parking_start_datetime=Parking_start_datetime, Parking_end_datetime=Parking_end_datetime)
        # add the new reservation to the database
        db.session.add(new_reserve)
        db.session.commit()
        return redirect(url_for('main.reservations'))