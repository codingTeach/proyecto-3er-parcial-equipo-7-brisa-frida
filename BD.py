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

    def create_ciudad(self, nombre, departamento):
        with self.driver.session() as session:
            session.run("MATCH (d:Departamento {nombre: $departamento}) "
                        "CREATE (:Ciudad {nombre: $nombre})-[:PERTENECE_A]->(d)",
                        nombre=nombre, departamento=departamento)

    def create_profesor(self, nombre, apellido, direccion, telefono, email, registro, departamento):
        with self.driver.session() as session:
            session.run("MATCH (d:Departamento {nombre: $departamento}) "
                        "CREATE (:Profesor {nombre: $nombre, apellido: $apellido, direccion: $direccion, "
                        "telefono: $telefono, email: $email, registro: $registro})-[:PERTENECE_A]->(d)",
                        nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, 
                        email=email, registro=registro, departamento=departamento)

    def create_sede(self, nombre, departamento, ciudad):
        with self.driver.session() as session:
            session.run("MATCH (d:Departamento {nombre: $departamento}), (c:Ciudad {nombre: $ciudad}) "
                        "CREATE (:Sede {nombre: $nombre})-[:PERTENECE_A]->(d)-[:UBICADO_EN]->(c)",
                        nombre=nombre, departamento=departamento, ciudad=ciudad)

    def create_carrera(self, nombre, duracion, costo, titulacion, sede):
        with self.driver.session() as session:
            session.run("MATCH (s:Sede {nombre: $sede}) "
                        "CREATE (:Carrera {nombre: $nombre, duracion: $duracion, costo: $costo, titulacion: $titulacion})-[:OFRECIDA_EN]->(s)",
                        nombre=nombre, duracion=duracion, costo=costo, titulacion=titulacion, sede=sede)
