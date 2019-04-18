import sqlite3
from sqlite3 import Error
from all_verbs import lista_big
from all_verbs import all_verbs_conj



##############################################################################
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    #finally:
     #   conn.close()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    conn = sqlite3.connect()
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "tester.db"
 
    sql_create_verbs_table = """ CREATE TABLE IF NOT EXISTS verbs (
                            infinitive text PRIMARY KEY,
                            gerundio text, participio text, 
                            presente_i_1 text, presente_i_2 text, presente_i_3 text,                                       
                            presente_i_4 text, presente_i_5 text, presente_i_6 text, 
                            imperfeito_i_1 text, imperfeito_i_2 text, imperfeito_i_3 text, 
                            imperfeito_i_4 text, imperfeito_i_5 text, imperfeito_i_6 text,                                         
                            perfeito_i_1 text, perfeito_i_2 text, perfeito_i_3 text,
                            perfeito_i_4 text, perfeito_i_5 text, perfeito_i_6 text, 
                            mais_que_perf_i_1 text, mais_que_perf_i_2 text, 
                            mais_que_perf_i_3 text, mais_que_perf_i_4 text, 
                            mais_que_perf_i_5 text, mais_que_perf_i_6 text, 
                            fut_pres_i_1 text, fut_pres_i_2 text, fut_pres_i_3 text, 
                            fut_pres_i_4 text, fut_pres_i_5 text,fut_pres_i_6 text, 
                            fut_pret_i_1 text, fut_pret_i_2 text, fut_pret_i_3 text, 
                            fut_pret_i_4 text, fut_pret_i_5 text, fut_pret_i_6 text, 
                            presente_s_1 text, presente_s_2 text, presente_s_3 text, 
                            presente_s_4 text, presente_s_5 text, presente_s_6 text,
                            pret_imperf_s_1 text, pret_imperf_s_2 text, pret_imperf_s_3 text, 
                            pret_imperf_s_4 text, pret_imperf_s_5 text, pret_imperf_s_6 text, 
                            futuro_s_1 text, futuro_s_2 text, futuro_s_3 text, 
                            futuro_s_4 text, futuro_s_5 text, futuro_s_6 text
                            ); """
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_verbs_table)
    else:
        print("Error! cannot create the database connection.")

def create_verb_in_table(conn, verb):
    """
    Create a new verb
    :param conn:
    :param verb:
    :return:
    """
 
    sql = ''' INSERT INTO verbs(infinitive,gerundio, participio, 
    presente_i_1, presente_i_2, presente_i_3, presente_i_4, presente_i_5, presente_i_6, 
    imperfeito_i_1, imperfeito_i_2, imperfeito_i_3, imperfeito_i_4, imperfeito_i_5, imperfeito_i_6, 
    perfeito_i_1, perfeito_i_2, perfeito_i_3, perfeito_i_4, perfeito_i_5, perfeito_i_6, 
    mais_que_perf_i_1, mais_que_perf_i_2, mais_que_perf_i_3, mais_que_perf_i_4, mais_que_perf_i_5, mais_que_perf_i_6, 
    fut_pres_i_1, fut_pres_i_2, fut_pres_i_3, fut_pres_i_4, fut_pres_i_5,fut_pres_i_6, 
    fut_pret_i_1, fut_pret_i_2, fut_pret_i_3, fut_pret_i_4, fut_pret_i_5, fut_pret_i_6, 
    presente_s_1, presente_s_2, presente_s_3, presente_s_4, presente_s_5, presente_s_6,
    pret_imperf_s_1, pret_imperf_s_2, pret_imperf_s_3, pret_imperf_s_4, pret_imperf_s_5, pret_imperf_s_6, 
    futuro_s_1, futuro_s_2, futuro_s_3, futuro_s_4, futuro_s_5, futuro_s_6)
                                    
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, verb)
    return cur.lastrowid

def add_verbs():
    database = "tester.db"
 
    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()

    sql = (
            """
            ''' INSERT INTO verbs(infinitive,gerundio, participio, 
    presente_i_1, presente_i_2, presente_i_3, presente_i_4, presente_i_5, presente_i_6, 
    imperfeito_i_1, imperfeito_i_2, imperfeito_i_3, imperfeito_i_4, imperfeito_i_5, imperfeito_i_6, 
    perfeito_i_1, perfeito_i_2, perfeito_i_3, perfeito_i_4, perfeito_i_5, perfeito_i_6, 
    mais_que_perf_i_1, mais_que_perf_i_2, mais_que_perf_i_3, mais_que_perf_i_4, mais_que_perf_i_5, mais_que_perf_i_6, 
    fut_pres_i_1, fut_pres_i_2, fut_pres_i_3, fut_pres_i_4, fut_pres_i_5,fut_pres_i_6, 
    fut_pret_i_1, fut_pret_i_2, fut_pret_i_3, fut_pret_i_4, fut_pret_i_5, fut_pret_i_6, 
    presente_s_1, presente_s_2, presente_s_3, presente_s_4, presente_s_5, presente_s_6,
    pret_imperf_s_1, pret_imperf_s_2, pret_imperf_s_3, pret_imperf_s_4, pret_imperf_s_5, pret_imperf_s_6, 
    futuro_s_1, futuro_s_2, futuro_s_3, futuro_s_4, futuro_s_5, futuro_s_6)
                                    
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
            """
    )

    values = (all_verbs_conj[0], all_verbs_conj[1], )
    cur.execute(sql, values)
    cur.commit()

main()
add_verbs()








#    """CREATE TABLE IF NOT EXISTS verbs (
#  infinitive text PRIMARY KEY,
#  gerundio text, participio text, 
# presente_i_1 text, presente_i_2 text, presente_i_3 text,                                       
# presente_i_4 text, presente_i_5 text, presente_i_6 text, 
# imperfeito_i_1 text, imperfeito_i_2 text, imperfeito_i_3 text, 
# imperfeito_i_4 text, imperfeito_i_5 text, imperfeito_i_6 text,                                         
# perfeito_i_1 text, perfeito_i_2 text, perfeito_i_3 text,
# perfeito_i_4 text, perfeito_i_5 text, perfeito_i_6 text, 
# mais_que_perf_i_1 text, mais_que_perf_i_2 text, 
# mais_que_perf_i_3 text, mais_que_perf_i_4 text, 
# mais_que_perf_i_5 text, mais_que_perf_i_6 text, 
# fut_pres_i_1 text, fut_pres_i_2 text, fut_pres_i_3 text, 
# fut_pres_i_4 text, fut_pres_i_5 text,fut_pres_i_6 text, 
# fut_pret_i_1 text, fut_pret_i_2 text, fut_pret_i_3 text, 
# fut_pret_i_4 text, fut_pret_i_5 text, fut_pret_i_6 text, 
# presente_s_1 text, presente_s_2 text, presente_s_3 text, 
# presente_s_4 text, presente_s_5 text, presente_s_6 text,
# pret_imperf_s_1 text, pret_imperf_s_2 text, pret_imperf_s_3 text, 
# pret_imperf_s_4 text, pret_imperf_s_5 text, pret_imperf_s_6 text, 
# futuro_s_1 text, futuro_s_2 text, futuro_s_3 text, 
# futuro_s_4 text, futuro_s_5 text, futuro_s_6 text
# ); """

# cur.execute("SELECT * FROM  verbs WHERE infinitivo=?", (infinitive,))
# result = cur.fetchall()

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



# def columns_table(conn, verb):
#     database = "verbs_tester.db"
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



# def add_verbs():
#     database = "verbs_test.db"
 
#     # create a database connection
#     conn = create_connection(database)
#     with conn:
#         # verbs
#         for verb in lista_big:
#             columns_table(conn, verb)

# create_db()
# add_verbs()
