from flask import Flask
from flask import render_template, redirect, url_for, request
import sqlite3
from sqlite3 import Error
from flask import current_app, g






def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect('verbs.db')
        return conn
    except Error as e:
        print(e)
 
    return None

 
def query_verb_conj(infinitive):
  conn = create_connection()
  cur = conn.cursor()
  cur.execute("SELECT * FROM  verbs WHERE infinitive=?", (infinitive,))
  result = cur.fetchall()
  for v_conj in result:
    print (v_conj)

  return v_conj 





# page routes and app object 


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  print(request.method)
  print(request.__dict__)
  if request.method == 'POST':
    print(request.form)
    #print(request.form['infinitive'])
    verb_query = request.form['infinitive']
    result_query = query_verb_conj(verb_query) 
    print(result_query)
    return render_template('verb_result.html', verbs=result_query)
    
  return render_template('index.html')

@app.route('/project_description')
def project_description():
  return render_template('project_description.html')

@app.route('/verbs_list')
def list_verbs():
  return render_template('verbs_list.html')


app.run(debug = True, host='127.0.0.1', port=5000)