import assets.responses as responses, assets.tsdb as tsdb
from flask import Flask, jsonify, make_response
# Test Comment for Push
app = Flask(__name__)

@app.route("/bin/<int:bin_id>", methods=["GET"])
def get_bin(bin_id:int):
    conn = tsdb.connect()
    query = f"SELECT * from ts_bins_info NATURAL JOIN ts_sensor_data WHERE bin_id = {bin_id};"
    bins = [dict(row) for row in tsdb.execute_query(conn, query)]
    response = responses.get_bin_response(bins, bin_id)
    conn.close() 
    return jsonify(response)

@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
