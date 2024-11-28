from flask import Flask, jsonify, request
from flask_cors import CORS
from services.data_service import DataService  # Importa la clase DataService

app = Flask(__name__)
CORS(app)

# Instancia de la clase DataService
data_service = DataService()

@app.route('/data', methods=['GET'])
def get_data():
    page = int(request.args.get('page', 1))  # Obtiene la página de los parámetros GET
    per_page = int(request.args.get('per_page', 10))  # Número de elementos por página
    data = data_service.get_all_data(page=page, per_page=per_page)  # Llama al método de la instancia
    return jsonify(json.loads(data))

@app.route('/data/<category>', methods=['GET'])
def get_data_category(category):
    page = int(request.args.get('page', 1))  # Obtiene la página de los parámetros GET
    per_page = int(request.args.get('per_page', 10))  # Número de elementos por página
    data = data_service.get_data_by_category(category, page=page, per_page=per_page)  # Llama al método de la instancia
    return jsonify(json.loads(data))

@app.route('/visualization/<viz_type>', methods=['GET'])
def get_visualization_data(viz_type):
    data = data_service.get_visualization_data(viz_type)  # Llama al método de la instancia
    return jsonify(json.loads(data))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
