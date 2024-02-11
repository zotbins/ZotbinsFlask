import psycopg2, psycopg2.extras, responses, tsdb
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/bin/<int:bin_id>", methods=["GET"])
def get_bin(bin_id:int):
    global conn
    query = f"SELECT * from ts_bins WHERE bin_id = '{bin_id}'"
    bins = [dict(row) for row in tsdb.execute_query(conn, query)]
    response = responses.get_bin_response(bins, bin_id)
    return jsonify(response)

if __name__ == "__main__":
    conn = tsdb.connect()
    app.run(port=5000)
