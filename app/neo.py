from neo4j import GraphDatabase
from django.conf import settings

class Neo4jConnection:
    def __init__(self):
        self.uri = settings.NEO4J['uri']
        self.user = settings.NEO4J['user']
        self.password = settings.NEO4J['password']
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def get_session(self):
        return self.driver.session()

    def close(self):
        self.driver.close()
