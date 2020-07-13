from helpers.ConnectionTypeModule import ConnectionType
from helpers.ConnectionStringModule import ConnectionStringModel

class ConnectionStringAdapter(object):
    def __init__(self,connectionStringObj:ConnectionStringModel=None,connectionType:ConnectionType=None):
        self.conString = ''
        self.connectionType = connectionType
        self.conS = connectionStringObj
        # for Sqlite connection based on a database url
        if(self.connectionType == ConnectionType.sql_lite):
            # path to sqlite.db file     
            self.conString = 'sqlite:////$s' % self.conS.databaseUrl
        # for mssql connection based on credidentials
        elif(self.connectionType == ConnectionType.mssql):
            # mssql connection string
            con = f"""DRIVER={{SQL Server}};
            SERVER={self.conS.host};
            DATABASE={self.conS.database};
            UID={self.conS.username};
            PWD={self.conS.password};
            Trusted_Connection=yes;"""
            params = urllib.parse.quote_plus(con)
            self.conString = "mssql+pyodbc:///?odbc_connect=%s" % params
        # for postgress sql based on credidentials
        elif(self.connectionType == ConnectionType.postgresql):
            # username:password@host/databasename
            con = f"""{self.conS.username}:{self.conS.password}@{self.conS.host}/{self.conS.username}"""
            params = urllib.parse.quote_plus(con)
            self.conString = "postgresql://" % params

    # connection string builder
    def getConnectionString(self):
        return self.conString