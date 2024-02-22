import env, psycopg2, psycopg2.extras

def connect():
    db_name = env.DB_NAME
    db_user = env.DB_USER
    db_host = env.DB_HOST
    db_port = env.DB_PORT
    db_pass = env.DB_PASS

    print("Attempting to connect to database...")
    conn = psycopg2.connect(user=db_user, database=db_name, host=db_host, password=db_pass, port=db_port)
    print("Connection established!")

    return conn

def execute_query(conn, query):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    return cursor.fetchall()
