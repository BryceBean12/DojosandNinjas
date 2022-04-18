

from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_rows(cls):

        query = "SELECT * FROM dojos;"

        results = connectToMySQL("dojos_ninjas_schema").query_db(query)

        all_rows = []
        for row in results:
            all_rows.append(Dojo(row))

        return all_rows

    @classmethod
    def insert_row(cls, data):

        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL("dojos_ninjas_schema").query_db(query, data)

        return results