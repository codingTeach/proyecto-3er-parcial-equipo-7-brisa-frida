from BD import DatabaseManager
from neo_config import uri, user, password

# Conexión a Neo4j
db_manager = DatabaseManager(uri, user, password)

departamentos = [
    "Departamento de Ciencias", "Departamento de Ingeniería", "Departamento de Matemáticas",
    "Departamento de Física", "Departamento de Química", "Departamento de Biología",
    "Departamento de Filosofía", "Departamento de Historia", "Departamento de Geografía",
    "Departamento de Psicología"
]

ciudades = [
    ("Ciudad de México", "Departamento de Ciencias"),
    ("Guadalajara", "Departamento de Ingeniería"),
    ("Monterrey", "Departamento de Matemáticas"),
    ("Puebla", "Departamento de Física"),
    ("Cancún", "Departamento de Química"),
    ("Mérida", "Departamento de Biología"),
    ("Tijuana", "Departamento de Filosofía"),
    ("León", "Departamento de Historia"),
    ("Querétaro", "Departamento de Geografía"),
    ("San Luis Potosí", "Departamento de Psicología")
]

profesores = [
    ("Juan", "Pérez", "Calle 123", "123456789", "juan.perez@example.com", "REG001", "Ciencias"),
    ("María", "González", "Avenida 456", "987654321", "maria.gonzalez@example.com", "REG002", "Ingeniería"),
    ("Luis", "Martínez", "Calle 789", "123123123", "luis.martinez@example.com", "REG003", "Matemáticas"),
    ("Ana", "Rodríguez", "Calle 101", "321321321", "ana.rodriguez@example.com", "REG004", "Física"),
    ("Carlos", "Hernández", "Calle 202", "456456456", "carlos.hernandez@example.com", "REG005", "Química"),
    ("María", "López", "Calle 303", "654654654", "maria.lopez@example.com", "REG006", "Biología"),
    ("Pedro", "García", "Calle 404", "789789789", "pedro.garcia@example.com", "REG007", "Filosofía"),
    ("Laura", "Martín", "Calle 505", "321654987", "laura.martin@example.com", "REG008", "Historia"),
    ("Javier", "Fernández", "Calle 606", "654123789", "javier.fernandez@example.com", "REG009", "Geografía"),
    ("Sofía", "Pérez", "Calle 707", "123789456", "sofia.perez@example.com", "REG010", "Psicología"),
]

sedes = [
    ("Sede Norte", "Departamento de Ciencias", "Ciudad de México"),
    ("Sede Sur", "Departamento de Ingeniería", "Guadalajara"),
    ("Sede Este", "Departamento de Matemáticas", "Monterrey"),
    ("Sede Oeste", "Departamento de Física", "Puebla"),
    ("Sede Central", "Departamento de Química", "Cancún"),
    ("Sede Norte Centro", "Departamento de Biología", "Mérida"),
    ("Sede Sur Centro", "Departamento de Filosofía", "Tijuana"),
    ("Sede Este Centro", "Departamento de Historia", "León"),
    ("Sede Oeste Centro", "Departamento de Geografía", "Querétaro"),
    ("Sede Centro", "Departamento de Psicología", "San Luis Potosí"),
]

carreras = [
    ("Ingeniería de Software", "5 años", 2000.00, "Ingeniero en Software", "Sede Norte"),
    ("Ingeniería Civil", "5 años", 1800.00, "Ingeniero Civil", "Sede Sur"),
    ("Licenciatura en Matemáticas", "4 años", 1500.00, "Licenciado en Matemáticas", "Sede Este"),
    ("Licenciatura en Física", "4 años", 1600.00, "Licenciado en Física", "Sede Oeste"),
    ("Licenciatura en Química", "4 años", 1700.00, "Licenciado en Química", "Sede Central"),
    ("Licenciatura en Biología", "4 años", 1600.00, "Licenciado en Biología", "Sede Norte Centro"),
    ("Licenciatura en Filosofía", "4 años", 1400.00, "Licenciado en Filosofía", "Sede Sur Centro"),
    ("Licenciatura en Historia", "4 años", 1300.00, "Licenciado en Historia", "Sede Este Centro"),
    ("Licenciatura en Geografía", "4 años", 1500.00, "Licenciado en Geografía", "Sede Oeste Centro"),
    ("Licenciatura en Psicología", "4 años", 1600.00, "Licenciado en Psicología", "Sede Centro"),
]

for depto in departamentos:
    db_manager.create_departamento(depto)

for ciudad, depto in ciudades:
    db_manager.create_ciudad(ciudad, depto)

for prof in profesores:
    db_manager.create_profesor(*prof)

for sede in sedes:
    db_manager.create_sede(*sede)

for carrera in carreras:
    db_manager.create_carrera(*carrera)

db_manager.close()
