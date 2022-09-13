from flask_app import app
from flask import render_template,redirect,request,flash
from flask_app.models.dojos import Dojos

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    dojos = Dojos.get_all()
    print(dojos)
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def save():
    data = {
        'name': request.form['name']
    }
    Dojos.save(data)
    return redirect('/dojos')


@app.route('/dojo/<int:id>')
def dojo_num(id):
    data = {
        'id': id
    }
    return render_template('dojo_one.html', dojo=Dojos.one_dojo(data))