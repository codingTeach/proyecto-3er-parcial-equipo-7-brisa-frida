from neo4j import GraphDatabase
from neo_config import uri, user, password 

class DatabaseManager:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_departamento(self, nombre):
        with self.driver.session() as session:
            session.run("CREATE (:Departamento {nombre: $nombre})", nombre=nombre)

    def create_ciudad(self, nombre, departamento_nombre):
        with self.driver.session() as session:
            session.run(
                "MATCH (d:Departamento {nombre: $departamento_nombre}) "
                "CREATE (c:Ciudad {nombre: $nombre})-[:PERTENECE_A]->(d)",
                nombre=nombre,
                departamento_nombre=departamento_nombre
            )

    def create_profesor(self, nombre, apellido, direccion, telefono, email, registro, carreras):
        with self.driver.session() as session:
            session.run(
                "CREATE (:Profesor {nombre: $nombre, apellido: $apellido, direccion: $direccion, "
                "telefono: $telefono, email: $email, registro: $registro})",
                nombre=nombre,
                apellido=apellido,
                direccion=direccion,
                telefono=telefono,
                email=email,
                registro=registro
            )

    def create_sede(self, nombre, departamento, ciudad_nombre):
        with self.driver.session() as session:
            session.run(
                "MATCH (c:Ciudad {nombre: $ciudad_nombre}) "
                "CREATE (s:Sede {nombre: $nombre, departamento: $departamento})-[:ESTA_EN]->(c)",
                nombre=nombre,
                departamento=departamento,
                ciudad_nombre=ciudad_nombre
            )

    def create_carrera(self, descripcion, duracion, cuota, titulo, sede_nombre):
        with self.driver.session() as session:
            session.run(
                "MATCH (s:Sede {nombre: $sede_nombre}) "
                "CREATE (c:Carrera {descripcion: $descripcion, duracion: $duracion, "
                "cuota: $cuota, titulo: $titulo})-[:IMPARTIDA_EN]->(s)",
                descripcion=descripcion,
                duracion=duracion,
                cuota=cuota,
                titulo=titulo,
                sede_nombre=sede_nombre
            )


db_manager = DatabaseManager(uri, user, password)

db_manager.close()
