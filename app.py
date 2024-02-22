import assets.responses as responses, assets.tsdb as tsdb
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/bin/<int:bin_id>", methods=["GET"])
def get_bin(bin_id:int):
    conn = tsdb.connect()
    query = f"SELECT * from ts_bins WHERE bin_id = '{bin_id}'"
    bins = [dict(row) for row in tsdb.execute_query(conn, query)]
    response = responses.get_bin_response(bins, bin_id)
    return jsonify(response)
