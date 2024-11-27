from flask import Flask, jsonify, request
from services.data_service import get_all_data, get_data_by_category
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET'])
def get_data():
    data = get_all_data()
    return jsonify(data)

@app.route('/data/<category>', methods=['GET'])
def get_data_category(category):
    data = get_data_by_category(category)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
