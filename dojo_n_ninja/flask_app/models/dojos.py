from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import Ninjas


class Dojos:
    def __init__(self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojinja').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name) VALUES ( %(name)s);'

        return connectToMySQL('dojinja').query_db(query, data)

    @classmethod
    def one_dojo(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojinja').query_db(query, data)
        print(results)
        dojos = cls(results[0])
        for db_row in results:
            ninja = {
                'id': db_row['ninjas.id'],
                'first_name': db_row['first_name'],
                'last_name': db_row['last_name'],
                'age': db_row['age'],
            }
            dojos.ninjas.append(Ninjas(ninja))
        return dojos
    
