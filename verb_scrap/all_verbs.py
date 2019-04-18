import sqlite3
from sqlite3 import Error
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from urllib.request import Request, urlopen
import unicodedata
import re 

def get_soup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)'
                                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                             ' Chrome/35.0.1916.47 Safari/537.36'})
    web_byte = urlopen(req).read()
    soup = BeautifulSoup(web_byte, 'html.parser')
    return soup
url = "http://www.conjugacao.com.br/verbos-populares/"
html_object = get_soup(url)

main_url="https://www.conjugacao.com.br/verbos-populares/"
def make_all_links(main_url):
    links_list = []
    links_list.append(main_url)
    r_list = list(range(2,51))
    for n in r_list:
        link = main_url + str(n) + '/'
        links_list.append(link)
    return links_list

all_pages = make_all_links(main_url)

def get_all_pages(page_list): # is defined as all_pages when the function is called bellow
    all_verbs = []
    for page in page_list: 
        page_soup = get_soup(page)
        lista_verbos = page_soup.find(class_='wrapper').findAll('li')
        for tag in lista_verbos:
            clean_tag = tag.find('a')
            link = "https://www.conjugacao.com.br" + clean_tag["href"]
            verb = clean_tag.text
            pair = (verb, link)
            all_verbs.append(pair)
    print(all_verbs)
    return all_verbs

lista_big = get_all_pages(all_pages) #links all pages # all_pages replaces page_list
print(lista_big)

def get_all_conj(url_tuple):
    conjugacoes=[]
    vlink = url_tuple[1]
    infinitive = url_tuple[0]
    html_object = get_soup(vlink)
    verbo_conj = html_object.findAll(class_="f")
    for i in verbo_conj:
        conj = i.text  
        conjugacoes.append(conj)
    gerundio = conjugacoes[0]
    participio = conjugacoes[1]
    presente_i_1 = conjugacoes[2]
    presente_i_2 = conjugacoes[3]
    presente_i_3 = conjugacoes[4]
    presente_i_4 = conjugacoes[5]
    presente_i_5 = conjugacoes[6]
    presente_i_6 = conjugacoes[7]
    imperfeito_i_1 = conjugacoes[8]
    imperfeito_i_2 = conjugacoes[9]
    imperfeito_i_3 = conjugacoes[10]
    imperfeito_i_4 = conjugacoes[11]
    imperfeito_i_5 = conjugacoes[12]
    imperfeito_i_6 = conjugacoes[13]
    perfeito_i_1 = conjugacoes[14]
    perfeito_i_2 = conjugacoes[15]
    perfeito_i_3 = conjugacoes[16]
    perfeito_i_4 = conjugacoes[17]
    perfeito_i_5 = conjugacoes[18]
    perfeito_i_6 = conjugacoes[19]
    mais_que_perf_i_1 = conjugacoes[20]
    mais_que_perf_i_2 = conjugacoes[21]
    mais_que_perf_i_3 = conjugacoes[23]
    mais_que_perf_i_4 = conjugacoes[24]
    mais_que_perf_i_5 = conjugacoes[25]
    mais_que_perf_i_6 = conjugacoes[26]
    fut_pres_i_1 = conjugacoes[27]
    fut_pres_i_2 = conjugacoes[28]
    fut_pres_i_3 = conjugacoes[29]
    fut_pres_i_4 = conjugacoes[30]
    fut_pres_i_5 = conjugacoes[31]
    fut_pres_i_6 = conjugacoes[32]
    fut_pret_i_1 = conjugacoes[33]
    fut_pret_i_2 = conjugacoes[34]
    fut_pret_i_3 = conjugacoes[35]
    fut_pret_i_4 = conjugacoes[36]
    fut_pret_i_5 = conjugacoes[37]
    fut_pret_i_6 = conjugacoes[38]
    presente_s_1 = conjugacoes[39]
    presente_s_2 = conjugacoes[40]
    presente_s_3 = conjugacoes[41]
    presente_s_4 = conjugacoes[42]
    presente_s_5 = conjugacoes[43]
    presente_s_6 = conjugacoes[44]
    pret_imperf_s_1 = conjugacoes[45]
    pret_imperf_s_2 = conjugacoes[46]
    pret_imperf_s_3 = conjugacoes[47]
    pret_imperf_s_4 = conjugacoes[48]
    pret_imperf_s_5 = conjugacoes[49]
    pret_imperf_s_6 = conjugacoes[50]
    futuro_s_1 = conjugacoes[51]
    futuro_s_2 = conjugacoes[52]
    #futuro_s_3 = conjugacoes[53]
    futuro_s_4 = conjugacoes[54]
    futuro_s_5 = conjugacoes[55]
    futuro_s_6 = conjugacoes[56]

    return infinitive, gerundio, participio, 
    presente_i_1, presente_i_2, presente_i_3, presente_i_4, presente_i_5, presente_i_6, 
    imperfeito_i_1, imperfeito_i_2, imperfeito_i_3, imperfeito_i_4, imperfeito_i_5, imperfeito_i_6, 
    perfeito_i_1, perfeito_i_2, perfeito_i_3, perfeito_i_4, perfeito_i_5, perfeito_i_6, 
    mais_que_perf_i_1, mais_que_perf_i_2, mais_que_perf_i_3, mais_que_perf_i_4, mais_que_perf_i_5, mais_que_perf_i_6, 
    fut_pres_i_1, fut_pres_i_2, fut_pres_i_3, fut_pres_i_4, fut_pres_i_5,fut_pres_i_6, 
    fut_pret_i_1, fut_pret_i_2, fut_pret_i_3, fut_pret_i_4, fut_pret_i_5, fut_pret_i_6, 
    presente_s_1, presente_s_2, presente_s_3, presente_s_4, presente_s_5, presente_s_6,
    pret_imperf_s_1, pret_imperf_s_2, pret_imperf_s_3, pret_imperf_s_4, pret_imperf_s_5, pret_imperf_s_6, 
    futuro_s_1, futuro_s_2, futuro_s_4, futuro_s_5, futuro_s_6
    #futuro_s_3,

def all_verbs_conj():
    for v in lista_big:
        get_all_conj(v)

all_verbs_conj()


##############################################################################
 
# def create_connection(db_file):
#     """ create a database connection to a SQLite database """
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
#         return conn
#     except Error as e:
#         print(e)
#     #finally:
#      #   conn.close()



# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     :return:
#     """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)



# def create_verb_in_table(conn, verb):
#     """
#     Create a new verb
#     :param conn:
#     :param verb:
#     :return:
#     """
 
#     sql = ''' INSERT INTO verbs(infinitive,gerundio, participio, 
#     presente_i_1, presente_i_2, presente_i_3, presente_i_4, presente_i_5, presente_i_6, 
#     imperfeito_i_1, imperfeito_i_2, imperfeito_i_3, imperfeito_i_4, imperfeito_i_5, imperfeito_i_6, 
#     perfeito_i_1, perfeito_i_2, perfeito_i_3, perfeito_i_4, perfeito_i_5, perfeito_i_6, 
#     mais_que_perf_i_1, mais_que_perf_i_2, mais_que_perf_i_3, mais_que_perf_i_4, mais_que_perf_i_5, mais_que_perf_i_6, 
#     fut_pres_i_1, fut_pres_i_2, fut_pres_i_3, fut_pres_i_4, fut_pres_i_5,fut_pres_i_6, 
#     fut_pret_i_1, fut_pret_i_2, fut_pret_i_3, fut_pret_i_4, fut_pret_i_5, fut_pret_i_6, 
#     presente_s_1, presente_s_2, presente_s_3, presente_s_4, presente_s_5, presente_s_6,
#     pret_imperf_s_1, pret_imperf_s_2, pret_imperf_s_3, pret_imperf_s_4, pret_imperf_s_5, pret_imperf_s_6, 
#     futuro_s_1, futuro_s_2, futuro_s_3, futuro_s_4, futuro_s_5, futuro_s_6)
                                    
#               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
#     cur = conn.cursor()
#     cur.execute(sql, verb)
#     return cur.lastrowid

# def create_db():
#     database = "verbs_test.db"
    
#     sql_create_verbs_table = """ CREATE TABLE IF NOT EXISTS verbs (
#                                         infinitive text PRIMARY KEY,
#                                         gerundio text, participio text, 
#                                         presente_i_1 text, presente_i_2 text, presente_i_3 text, 
#                                         presente_i_4 text, presente_i_5 text, 
#                                         presente_i_6 text, imperfeito_i_1 text, 
#                                         imperfeito_i_2 text, imperfeito_i_3 text, 
#                                         imperfeito_i_4 text, imperfeito_i_5 text, imperfeito_i_6 text, 
#                                         perfeito_i_1 text, perfeito_i_2 text, perfeito_i_3 text,
#                                         perfeito_i_4 text, perfeito_i_5 text, perfeito_i_6 text, 
#                                         mais_que_perf_i_1 text, mais_que_perf_i_2 text, 
#                                         mais_que_perf_i_3 text, mais_que_perf_i_4 text, 
#                                         mais_que_perf_i_5 text, mais_que_perf_i_6 text, 
#                                         fut_pres_i_1 text, fut_pres_i_2 text, fut_pres_i_3 text, 
#                                         fut_pres_i_4 text, fut_pres_i_5 text,fut_pres_i_6 text, 
#                                         fut_pret_i_1 text, fut_pret_i_2 text, fut_pret_i_3 text, 
#                                         fut_pret_i_4 text, fut_pret_i_5 text, fut_pret_i_6 text, 
#                                         presente_s_1 text, presente_s_2 text, presente_s_3 text, 
#                                         presente_s_4 text, presente_s_5 text, presente_s_6 text,
#                                         pret_imperf_s_1 text, pret_imperf_s_2 text, pret_imperf_s_3 text, 
#                                         pret_imperf_s_4 text, pret_imperf_s_5 text, pret_imperf_s_6 text, 
#                                         futuro_s_1 text, futuro_s_2 text, futuro_s_3 text, 
#                                         futuro_s_4 text, futuro_s_5 text, futuro_s_6 text
                                        
#                                     ); """
 
#     # create a database connection
#     conn = create_connection(database)
#     print(conn)
#     if conn is not None:
#         # create verbs table
#         create_table(conn, sql_create_verbs_table)
       
#     else:
#         print("Error! cannot create the database connection.")


# #create_db()

# def add_verbs():
#     database = "verbs_test.db"
 
#     # create a database connection
#     conn = create_connection(database)
#     with conn:
#         # verbs
#         for verb in lista_big:
#             create_verb_in_table(conn, verb)

# create_db()
# add_verbs()




