from flask import Flask, request, jsonify
from BD import DatabaseManager
from neo_config import uri, user, password

app = Flask(__name__)
db_manager = DatabaseManager(uri, user, password)

@app.route('/profesores', methods=['GET'])
def get_profesores():
    profesores = db_manager.get_profesores()  # Implementar esta función en BD.py
    return jsonify(profesores)

@app.route('/profesores', methods=['POST'])
def create_profesor():
    data = request.json
    db_manager.create_profesor(**data)  # Implementar esta función en BD.py
    return jsonify({"message": "Profesor creado exitosamente"})

if __name__ == "__main__":
    app.run(debug=True)
