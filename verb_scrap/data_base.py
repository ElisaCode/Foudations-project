import sqlite3
from sqlite3 import Error
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from urllib.request import Request, urlopen
import unicodedata
import re 



#scrapping functions

def get_soup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)'
                                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                             ' Chrome/35.0.1916.47 Safari/537.36'})
    web_byte = urlopen(req).read()
    soup = BeautifulSoup(web_byte, 'html.parser')
    return soup


def make_all_links(main_url):
    links_list = []
    links_list.append(main_url)
    r_list = list(range(2,51))
    for n in r_list:
        link = main_url + str(n) + '/'
        links_list.append(link)
    print(links_list)
    return links_list


def get_all_verbs(page_list):
    all_verbs = []
    for page in page_list:
        page_soup = get_soup(page)
        lista_verbos = page_soup.find(class_='wrapper').findAll('li')
        for tag in lista_verbos:
            clean_tag = tag.find('a')
            link = "https://www.conjugacao.com.br" + clean_tag["href"]
            verb = clean_tag.text
            print(verb)
            pair = (verb, link)
            all_verbs.append(pair)
    print(all_verbs)
    return all_verbs



main_url="https://www.conjugacao.com.br/verbos-populares/"
all_pages = make_all_links(main_url)
lista_big = get_all_verbs(all_pages)



 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    #finally:
        #conn.close()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_verb(conn, verb):
    """
    Create a new verb
    :param conn:
    :param verb:
    :return:
    """
 
    sql = ''' INSERT INTO verbs(infinitive,link,presente,preterito)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, verb)
    return cur.lastrowid


def create_db():
    database = "verbos_db.db"
    
    sql_create_verbs_table = """ CREATE TABLE IF NOT EXISTS verbs (
                                        infinitive text PRIMARY KEY,
                                        link text NOT NULL,
                                        presente text,
                                        preterito text
                                    ); """
 
    # create a database connection
    conn = create_connection(database)
    print(conn)
    if conn is not None:
        # create verbs table
        create_table(conn, sql_create_verbs_table)
       
    else:
        print("Error! cannot create the database connection.")


#create_db()


def add_verbs():
    database = "verbos_db.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        # verbs
        for verb in lista_big:
            create_verb(conn, verb)



add_verbs()