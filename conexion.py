
from services.data_service import DataService

data_service = DataService()

# Verificar conexión
try:
    print("Conexión a MongoDB exitosa:", data_service.db.list_collection_names())
except Exception as e:
    print("Error en la conexión:", str(e))
