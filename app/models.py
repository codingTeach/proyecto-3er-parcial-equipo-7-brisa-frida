from neo import Neo4jConnection
from .neo import Neo4jConnection

def obtener_departamentos():
    conn = Neo4jConnection()
    session = conn.get_session()

    # Realizar una consulta Cypher para obtener los departamentos
    query = "MATCH (d:Departamento) RETURN d.nombre"
    result = session.run(query)
    departamentos = [record['d.nombre'] for record in result]

    conn.close()
    return departamentos
