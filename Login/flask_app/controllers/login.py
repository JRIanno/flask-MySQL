from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.backlog import Users
from flask_bcrypt import Bcrypt
from password_strength import PasswordPolicy
from password_strength import PasswordStats
bcrypt = Bcrypt(app)

policy = PasswordPolicy.from_names(
    length = 8,
    uppercase = 1,
    numbers = 1,
    strength=0.44
    )


@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        password = request.form.get('password')
        stats = PasswordStats(password)
        checkpolicy = policy.test(password)
        if stats.strength() < 0.44:
            print(stats.strength())
            flash('Password does not meet the minimum requirements/weak password')
            return redirect('/') 
    if not Users.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    user_id = Users.save(data)
    session['user_id'] = user_id
    return redirect('/welcome')

@app.route('/login', methods=['POST'])
def login():
    data = { 'email': request.form['email']}
    user_in_db = Users.get_by_email(data)
    if not user_in_db:
        flash('Wrong email or password!')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash('Wrong email or password!')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id'],
    }
    return render_template('welcome.html', users=Users.get_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')