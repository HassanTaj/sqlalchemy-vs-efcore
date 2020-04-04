import urllib
import pyodbc
from sqlalchemy import create_engine

class ConnectionHelper(object):
    # initialize connection helper with connectionstring
    def __init__(self, connstring=None):
        if(connstring == '' or connstring == None):
            connstring = (r'DRIVER={SQL Server};'
                r'SERVER=.;'
                r'DATABASE=todo_db;'
                r'UID=sa;'
                r'PWD=123;'
                r'Trusted_Connection=yes;')

        self.connstring = connstring
        self.engine = None

    # get SqlAchemy Database Engine using this function
    def getEngine(self):
        try:
            params = urllib.parse.quote_plus(self.connstring)
            self.engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
            return self.engine
        except Exception as engex:
            print(engex)

    # get connection object after connectng with database through engine       
    def getConnection(self):
        try:
           return self.engine.connect()
        except Exception as ex:
            print(ex)
