import json, env, psycopg2, psycopg2.extras
from flask import Flask, request, jsonify

app = Flask(__name__)

def tsdb_connect():
    db_name = env.DB_NAME
    db_user = env.DB_USER
    db_host = env.DB_HOST
    db_port = env.DB_PORT
    db_pass = env.DB_PASS

    print("Attempting to connect to database...")
    conn = psycopg2.connect(user=db_user, database=db_name, host=db_host, password=db_pass, port=db_port)
    print("Connection established!")

    return conn

@app.route("/bin/<int:bin_id>", methods=["GET"])
def get_bin(bin_id:int):
    global conn
    query = f"SELECT * from ts_bins WHERE bin_id = '{bin_id}'"
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    bins = [dict(row) for row in cursor.fetchall()]
    response = get_bin_response(bins, bin_id)
    return jsonify(response)

def get_bin_response(bins, bin_id):
    if len(bins) == 0:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'detail': f'Bin not found: {bin_id}'
            }),
            'headers': {
                "Content-Type": "application/json"
            }
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(bins, default=str),
            'headers': {
                "Content-Type": "application/json"
            }
        }

if __name__ == "__main__":
    conn = tsdb_connect()
    app.run(port=5000)
