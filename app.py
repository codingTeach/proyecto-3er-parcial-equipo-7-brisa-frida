from flask import Flask, jsonify, request
from flask_cors import CORS
from services.data_service import DataService  # Importa la clase DataService

app = Flask(__name__)
CORS(app)

# Instancia de la clase DataService
data_service = DataService()

# Ruta principal, que devuelve un mensaje simple
@app.route('/')
def home():
    return "Bienvenido a la API de la Tienda de Discos"

@app.route('/data', methods=['GET'])
def get_data():
    data = data_service.get_all_data()  # Llama al método de la instancia
    return jsonify(data)

@app.route('/data/<category>', methods=['GET'])
def get_data_category(category):
    data = data_service.get_data_by_category(category)  # Llama al método de la instancia
    return jsonify(data)

@app.route('/insert_data', methods=['POST'])
def insert_data():
    data = [
        {"nombre": "Being Funny in a Foreign Language", "categoria": "CD", "precio": 19.99, "fecha_creacion": "2022-10-14", "stock": 120, "descripcion": "El último álbum de The 1975, explorando nuevos sonidos en la música pop experimental.", "artista": "The 1975", "codigo": "CD041", "formato": "CD", "anio_lanzamiento": 2022},
        {"nombre": "LNG/SHT 2024", "categoria": "Vinil", "precio": 24.99, "fecha_creacion": "2024-05-05", "stock": 80, "descripcion": "Un álbum innovador de LNG/SHT, fusionando electrónica con géneros urbanos.", "artista": "LNG/SHT", "codigo": "VR042", "formato": "Vinil", "anio_lanzamiento": 2024},
        {"nombre": "TINI", "categoria": "CD", "precio": 17.99, "fecha_creacion": "2021-03-12", "stock": 100, "descripcion": "El aclamado álbum de TINI, con influencias del pop latino y la música urbana.", "artista": "TINI", "codigo": "CD043", "formato": "CD", "anio_lanzamiento": 2021},
        {"nombre": "Mundo Estático", "categoria": "Vinil", "precio": 22.99, "fecha_creacion": "2020-11-25", "stock": 55, "descripcion": "Álbum de Little Jesus, con un enfoque fresco en el indie rock y sonidos experimentales.", "artista": "Little Jesus", "codigo": "VR044", "formato": "Vinil", "anio_lanzamiento": 2020},
        {"nombre": "El Rollo Continúa", "categoria": "CD", "precio": 21.99, "fecha_creacion": "2022-09-10", "stock": 75, "descripcion": "El último álbum de TINI, con un estilo renovado y colaboraciones destacadas.", "artista": "TINI", "codigo": "CD045", "formato": "CD", "anio_lanzamiento": 2022},
        {"nombre": "Sabor a Noche", "categoria": "Vinil", "precio": 27.99, "fecha_creacion": "2023-06-20", "stock": 90, "descripcion": "El esperado álbum de LNG/SHT, que fusiona géneros como reggaetón, trap y electrónica.", "artista": "LNG/SHT", "codigo": "VR046", "formato": "Vinil", "anio_lanzamiento": 2023}
    ]
    
    data_service.insert_data(data)
    return jsonify({"message": "Datos insertados correctamente"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
