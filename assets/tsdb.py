import os, psycopg2, psycopg2.extras

def connect():
    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']
    db_host = os.environ['DB_HOST']
    db_port = os.environ['DB_PORT']
    db_pass = os.environ['DB_PASS']

    conn = psycopg2.connect(user=db_user, database=db_name, host=db_host, password=db_pass, port=db_port)

    return conn

def execute_query(conn, query):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    return cursor.fetchall()