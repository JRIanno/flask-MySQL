from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('login').query_db(query, data)


    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;" 
        results = connectToMySQL('login').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


    @classmethod
    def get_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('login').query_db(query, data)
        return cls(results[0])


    @staticmethod
    def validate_user(users):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;" 
        results = connectToMySQL('login').query_db(query, users)
        if not EMAIL_REGEX.match(users['email']):
            flash('invalid email address or password!')
            is_valid = False
        if len(results) >= 1:
            flash('email address is already taken')
            is_valid = False
        if len(users['first_name']) < 2:
            flash('First name must be at least 2 characters!')
            is_valid = False
        if len(users['last_name']) < 2:
            flash('Last name must be at least 2 characters!')
            is_valid = False
        if len(users['password']) < 8:
            flash('Password must be at least 8 characters!')
            is_valid = False
        if (users['password']) != (users['confirm_password']):
            flash('Password must match!')
            is_valid = False
        return is_valid    