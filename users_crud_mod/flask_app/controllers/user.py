from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users import Users


@app.route('/')
def index():
    return redirect('/read')


@app.route('/read')
def read():
    users = Users.get_all()
    print(users)
    return render_template('read_all.html', users=users)


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    Users.save(data)
    return redirect('/read')


@app.route('/user/<int:user_id>')
def user_one(user_id):
    data = {
        'id': user_id
    }
    user = Users.user_num(data)
    print(user)
    return render_template('user_one.html', user = user)


@app.route('/user/<int:user_id>/edit')
def r_user_edit(user_id):
    data = {
        'id': user_id
    }
    user = Users.user_num(data)
    print(user)
    return render_template('user_edit.html', user = user)


@app.route('/user/update_user', methods = ['POST'])
def user_edit():
    data = {
        'id': request.form.get('user_id'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email')
    }

    Users.update_users(data)
    return redirect(f'/user/{data["id"]}')


@app.route('/user/<int:user_id>/delete')
def user_delete(user_id):
    data = {
        'id': user_id
    }
    Users.delete(data)
    return redirect('/read')