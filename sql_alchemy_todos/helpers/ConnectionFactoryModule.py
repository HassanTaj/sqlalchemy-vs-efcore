import urllib
import pyodbc
from sqlalchemy import create_engine
from helpers.ConnectionStringAdapterModule import ConnectionStringAdapter

class ConnectionFactory(object):
    # initialize connection helper with connection string
    def __init__(self, connectionAdapter:ConnectionStringAdapter=None):
        self.engine = None
        self.adapter = connectionAdapter

    # get SqlAchemy Database Engine using this function
    def getEngine(self):
        try:
            self.engine = create_engine(self.adapter.getConnectionString())
            return self.engine
        except Exception as engex:
            print(engex)

    # get connection object after connectng with database through engine
    def getConnection(self):
        try:
           return self.engine.connect()
        except Exception as ex:
            print(ex)