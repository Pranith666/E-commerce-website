from flask import Blueprint, render_template,request,flash
from . import db 
import random
from flask import Flask, redirect, url_for
from flask_login import login_user,logout_user,fresh_login_required
from flask_login import current_user
from .models import User


auth =Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phno = request.form.get('phno')
        password = request.form.get('password')

        user = User.query.filter_by(phno=phno).first()
        if user:
            if user.password==password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

    

@auth.route('/logout')
@fresh_login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        phno = request.form.get('phno')
        firstname = request.form.get('FirstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print(phno, firstname, password1, password2)

        user=User.query.filter_by(phno=phno).first()
        if user:
            flash('Phone number already exists',category='error')
        elif len(phno) < 4:
            flash('Phone number length must be greater than 4', category='error')
        elif len(password1) < 4:
            flash('Password must be greater than 4', category='error')
        elif password1 != password2:
            flash('Passwords dont match', category='error')
        else:
            new_user = User(phno=phno, firstname=firstname, password=password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html')



@auth.route('/laptopbuy')
def laptopbuy():
    return render_template('laptopbuy.html')

@auth.route('/phonebuy')
def phonebuy():
    return render_template('phonebuy.html')

@auth.route('/tabletbuy')
def tabletbuy():
    return render_template('tabletbuy.html')

@auth.route('/gamebuy')
def gamebuy():
    return render_template('gamebuy.html')

@auth.route('/watchesbuy')
def watchesbuy():
    return render_template('watchesbuy.html')

