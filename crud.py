from BD import DatabaseManager
from neo_config import uri, user, password

db_manager = DatabaseManager(uri, user, password)


class CRUDOperations:
    def __init__(self):
        self.db_manager = db_manager

    def create_example_data(self):
        # Creación
        self.create_profesor(
            "Mario", "Sánchez", "Calle Nueva 123", "111222333", "mario.sanchez@example.com", "REG011", "Filosofía"
        )

        # Creación y asociación de carrera con sede
        self.create_carrera(
            "Licenciatura en Letras", "4 años", 1400.00, "Licenciado en Letras", "Sede Sur Centro"  # Ciudad: Ciudad de México
        )

        # Creación de relación entre el nuevo profesor y la carrera recién creada
        self.create_relacion_profesor_carrera("REG011", "Licenciatura en Letras")

    def create_profesor(self, nombre, apellido, direccion, telefono, email, registro, carreras):
        self.db_manager.create_profesor(nombre, apellido, direccion, telefono, email, registro, carreras)
        print(f"Profesor {nombre} {apellido} creado exitosamente.")

    def create_carrera(self, nombre, duracion, costo, titulo, sede):
        self.db_manager.create_carrera(nombre, duracion, costo, titulo, sede)
        print(f"Carrera {nombre} creada exitosamente.")

    def create_relacion_profesor_carrera(self, registro, nombre_carrera):
        with self.db_manager.driver.session() as session:
            session.run(
                "MATCH (p:Profesor {registro: $registro}), (c:Carrera {nombre: $nombre_carrera}) "
                "MERGE (p)-[:IMPARTE]->(c)",
                registro=registro,
                nombre_carrera=nombre_carrera
            )
        print(f"Relación creada entre profesor con registro {registro} y la carrera {nombre_carrera}.")

    def update_profesor(self, registro, nombre=None, apellido=None, direccion=None, telefono=None, email=None):
        with self.db_manager.driver.session() as session:
            session.run(
                "MATCH (p:Profesor {registro: $registro}) "
                "SET p.nombre = COALESCE($nombre, p.nombre), "
                "p.apellido = COALESCE($apellido, p.apellido), "
                "p.direccion = COALESCE($direccion, p.direccion), "
                "p.telefono = COALESCE($telefono, p.telefono), "
                "p.email = COALESCE($email, p.email)",
                registro=registro,
                nombre=nombre,
                apellido=apellido,
                direccion=direccion,
                telefono=telefono,
                email=email
            )
            print(f"Profesor con registro {registro} actualizado.")

    def update_carrera(self, nombre, duracion=None, costo=None, titulo=None):
        with self.db_manager.driver.session() as session:
            session.run(
                "MATCH (c:Carrera {nombre: $nombre}) "
                "SET c.duracion = COALESCE($duracion, c.duracion), "
                "c.costo = COALESCE($costo, c.costo), "
                "c.titulo = COALESCE($titulo, c.titulo)",
                nombre=nombre,
                duracion=duracion,
                costo=costo,
                titulo=titulo
            )
            print(f"Carrera {nombre} actualizada.")

    def delete_profesor(self, registro):
        with self.db_manager.driver.session() as session:
            session.run("MATCH (p:Profesor {registro: $registro}) DETACH DELETE p", registro=registro)
            print(f"Profesor con registro {registro} eliminado.")

    def delete_carrera(self, nombre):
        with self.db_manager.driver.session() as session:
            session.run("MATCH (c:Carrera {nombre: $nombre}) DETACH DELETE c", nombre=nombre)
            print(f"Carrera {nombre} eliminada.")

    def run_examples(self):
        self.create_example_data()

        # Actualización de un profesor y una carrera
        self.update_profesor("REG011", nombre="Mario Alberto", direccion="Calle Actualizada 456")
        self.update_carrera("Licenciatura en Letras", duracion="5 años", costo=1500.00)

        # Eliminación de un profesor y una carrera
        self.delete_profesor("REG011")
        self.delete_carrera("Licenciatura en Letras")

    def close(self):
        self.db_manager.close()


crud_operations = CRUDOperations()
crud_operations.run_examples()
crud_operations.close()
