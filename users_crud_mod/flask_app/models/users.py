from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_cr').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users ( first_name, last_name, email, created_at, updated_at) Values ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );'

        return connectToMySQL('users_cr').query_db(query, data)

    @classmethod
    def user_num(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'

        results = connectToMySQL('users_cr').query_db(query, data)

        return cls(results[0])


    @classmethod
    def update_users(cls, data):
        query = 'UPDATE users Set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;'

        connectToMySQL('users_cr').query_db(query, data)

        return True

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL('users_cr').query_db(query, data)