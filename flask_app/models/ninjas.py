#  This is a template for how to do a basic query of the databse. This exampe shows how to pull and create data.

# Allows us to connect to our database and query it
from flask_app.config.mysqlconnection import connectToMySQL

# Create A Class of our DB table
class Ninja:
    # We pass in our data as a dict
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all_rows_from_dojo(cls, id):
        # MySQL query
        query = f"SELECT * FROM ninjas WHERE dojo_id = {id};"
        # Results returns a list of dictionaries
        results = connectToMySQL("dojos_ninjas_schema").query_db(query)

        # Takes our results and converts a list of dicts to a list of our User instances 
        all_rows = []
        for row in results:
            all_rows.append(Ninja(row))
        # Returns a list of instances
        return all_rows

    @classmethod
    def insert_row(cls, data):
        # MySQL Query
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        results = connectToMySQL("dojos_ninjas_schema").query_db(query, data)
        # return prints if successful
        return results