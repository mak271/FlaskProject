# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, url_for
from app import app, db
from app.forms import EmployerForm
from app.models import Employer
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "Home", employers = Employer.query.all())

@app.route('/deleteAll')
def deleteAll():
    employers = Employer.query.all()
    for em in employers:
        db.session.delete(em)
    db.session.commit()
    return redirect(url_for('index'))   

@app.route('/add_employer', methods = ['GET', 'POST'])
def add_employer():
    form = EmployerForm()
    if form.validate_on_submit():
        flash('Name: {}, Surname: = {}, Age: {}, Date: {}'.format(
            form.name.data, form.surname.data, form.age.data, form.date_employment.data
        ))
        employer = Employer(
            name = form.name.data, 
            surname = form.surname.data, 
            age = form.age.data, 
            date_employment = form.date_employment.data
        )
        db.session.add(employer)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add_employer.html', title = "Add emloyer", form = form)
