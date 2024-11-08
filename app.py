from flask import Flask, request, jsonify
from db import data_store

app = Flask(__name__)


# Route for GET request
@app.route('/', methods=['GET'])
def get_data():
    return jsonify(data_store), 200


# Route for POST request
@app.route('/', methods=['POST'])
def post_data():
    if request.is_json:
        data = request.get_json()
        data_store.append(data)  # Save data to the data_store
        return jsonify({"message": "Data added successfullyyyy!", "data": data}), 201
    return jsonify({"error": "Request must be JSON"}), 400


if __name__ == '__main__':
    app.run(debug=True)
