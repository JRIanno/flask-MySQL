from curses import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, render_template, redirect, request
#need to plug in both classes below
from flask_app.models.users import Users

app = Flask(__name__)
