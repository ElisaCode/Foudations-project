import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_verb_conjugation(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM verbs WHERE infinitive='infinitivo'")
  
 
def main():
    database = "verbs.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("2. Query all conj")
        select_verb_conjugation(conn)


# def get_conjugation(infinitive):
#     return """CREATE [TEMP] VIEW [IF NOT EXISTS] conjugation(*)
# AS 
#    SELECT * FROM verbs WHERE infinitive='infinitivo';
# """