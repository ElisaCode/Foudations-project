from flask import Flask
from flask import render_template, redirect, url_for, request
import sqlite3
from sqlite3 import Error
from flask import current_app, g
from flask.cli import with_appcontext




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
  cur.execute("SELECT * FROM  verbs WHERE infinitivo=?", (infinitive,))
  result = cur.fetchall()
  return result  





# page routes and app object 


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  print(request.method)
  print(request.__dict__)
    #infinitive = request.form.get('infinitive') # [] makes the field mandatory, otherwise we can use ()
  if request.method == 'POST':
    print(request.form)
    #print(request.form['infinitive'])
    verb_query = request.form['infinitive']
    result_query = query_verb_conj(verb_query)[0] #por enquanto ela s'o retorna falar
    print(result_query)
    return render_template('verb_result.html', verbs=result_query)

        #return 
        #return render_template('verbs_list.html') 
        #'<h1> The verb is : {}</h1>'.format('infinitive')
    
  return render_template('index.html')

@app.route('/project_description')
def project_description():
  return render_template('project_description.html')

@app.route('/verbs_list')
def list_verbs():
  return render_template('verbs_list.html')


app.run(debug = True, host='127.0.0.1', port=5000)