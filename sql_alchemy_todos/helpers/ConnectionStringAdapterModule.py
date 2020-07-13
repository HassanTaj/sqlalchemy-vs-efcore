from helpers.ConnectionTypeModule import ConnectionType
from helpers.ConnectionStringModule import ConnectionStringModel

class ConnectionStringAdapter(object):
    def __init__(self,connectionStringObj:ConnectionStringModel=None,connectionType:ConnectionType=None):
        self.conString = ''
        # for Sqlite connection based on a database url
        if(self.conType == ConnectionType.sql_lite):
            # path to sqlite.db file     
            self.conString = 'sqlite:////$s' % self.conS.databaseUrl
        # for mssql connection based on credidentials
        elif(self.conType == ConnectionType.mssql):
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
        elif(self.conType == ConnectionType.postgresql):
            # username:password@host/databasename
            con = f"""{self.conS.username}:{self.conS.password}@{self.conS.host}/{self.conS.username}"""
            params = urllib.parse.quote_plus(con)
            self.conString = "postgresql://" % params

        self.conType = connectionType
        self.conS = connectionStringObj

    # connection string builder
    def getConnectionString(self):
        return self.conString