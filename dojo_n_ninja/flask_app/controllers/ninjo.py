from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import dojos
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninjas

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos= dojos.Dojos.get_all())

@app.route('/ninjas/1/add', methods=['POST'])
def add_ninjas():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninjas.add_ninjas(data)
    return redirect('/dojos')

