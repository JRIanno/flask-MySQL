from flask import Flask, render_template, redirect, request
from friend import Users
app = Flask(__name__)


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
        #'created_at': request.form['created_at'],
    }

    Users.save(data)
    return redirect('/read')

if __name__ == "__main__":
    app.run(debug=True)