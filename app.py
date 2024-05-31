import assets.responses as responses, assets.tsdb as tsdb
from flask import Flask, jsonify, make_response, request
from datetime import datetime
import time
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

FORMAT_DATA = "%Y-%m-%d %H:%M:%S%z"
@app.route("/bin/<int:bin_id>", methods=["GET"])
def get_bin(bin_id:int):
    
    conn = tsdb.connect()
    query = f"SELECT * from ts_bins_info NATURAL JOIN ts_sensor_data WHERE bin_id = {bin_id};"
    bins = [dict(row) for row in tsdb.execute_query(conn, query)]
    response = responses.get_bin_response(bins, bin_id)
    conn.close() 


    return jsonify(response)

@app.route("/get_location/<int:bin_id>", methods=["GET"])
def get_location(bin_id:int):
    conn = tsdb.connect()
    query = f"SELECT latitude, longitude from ts_bins_info WHERE bin_id = {bin_id};"
    bins = [dict(row) for row in tsdb.execute_query(conn, query)]
    response = responses.get_bin_response(bins, bin_id)
    conn.close()



    return jsonify(response)

@app.route("/get_bins", methods=["GET"])
def get_bins():
    conn = tsdb.connect()
    query = f"SELECT * from ts_bins_info;"
    bins = [dict(row) for row in tsdb.execute_query(conn, query)]
    response = responses.get_bins_response(bins)
    conn.close()


    

    return jsonify(response)

@app.route("/get_usage/<int:bin_id>", methods=["GET"])
def get_usage(bin_id:int):
    start = request.args.get('start')
    end = request.args.get('end')
    valid_date = True
    conn = tsdb.connect()
    query = f"SELECT usage, timestamp FROM ts_sensor_data WHERE bin_id = {bin_id}"
    if start != None:
        start_timestamp = datetime.strptime(start, FORMAT_DATA)
        query += f" AND timestamp >= '{start_timestamp}'"
    if end != None:
        end_timestamp = datetime.strptime(end, FORMAT_DATA)
        query += f" AND timestamp < '{end_timestamp}'"
    query+=';'
    if (start!=None and end !=None) and start_timestamp > end_timestamp:
        valid_date = False
    bins = [dict(row) for row in tsdb.execute_query(conn, query)]
    response = responses.get_usage_response(bins, bin_id, valid_date)
    if len(response )== 0:
        single_query = f"SELECT * from ts_bins_info NATURAL JOIN ts_sensor_data WHERE bin_id = {bin_id};"
        single_bin = [dict(row) for row in tsdb.execute_query(conn, single_query)]
        response = responses.get_bin_response(single_bin, bin_id)
        
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

