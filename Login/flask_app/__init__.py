from curses import flash
from flask import Flask


app = Flask(__name__)
app.secret_key = 'qwerty'
