import sqlite3

# Create the queries that we will use in the functions

CREATE_PW_TABLE = "CREATE TABLE IF NOT EXISTS passwords (app TEXT, user TEXT, password TEXT);"

INSERT_DATA = "INSERT INTO passwords (app, user, password) VALUES (?, ?, ?);"

GET_ALL_DATA = "SELECT * FROM passwords;"
GET_BY_APP = "SELECT * FROM passwords WHERE app = ?;"
GET_BY_USER = "SELECT * FROM passwords WHERE user = ?;"
DELETE_ROW = "DELETE FROM passwords WHERE app = ?"
UPDATE_COLUMN = "UPDATE passwords SET app = ?, user = ?, password = ? WHERE app = ?"

# Create the functions

#Create and connect the table database
def connect():
    return sqlite3.connect("passwords.db")

def create_database(connection):
    with connection:
        connection.execute(CREATE_PW_TABLE)

# Function to add new data in the database
def add_data(connection, app, user, password):
    with connection:
        connection.execute(INSERT_DATA, (app, user, password))

# Get all the data from the database
def get_all_data(connection):
    with connection:
        return connection.execute(GET_ALL_DATA).fetchall()

# Get data by the app or website name
def get_by_app(connection, app):
    with connection:
        return connection.execute(GET_BY_APP, (app)).fetchall()

# Get data by the user name
def get_by_user(connection, user):
    with connection:
        return connection.execute(GET_BY_USER, (user)).fetchall()

# Delete row 
def delete_info(connection, app):
    with connection:
        return connection.execute(DELETE_ROW, (app,))  

# Update app name, user or/and password
def modify_column(connection, app, user, password, appp):
    with connection:
        return connection.execute(UPDATE_COLUMN, (app, user, password, appp))
                    
