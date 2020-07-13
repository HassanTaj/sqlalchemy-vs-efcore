class ConnectionStringModel(object):
    def __init__(self,username,password,hostName,databaseName,dbUrl):
        self.username = username
        self.password = password
        self.host = hostName
        self.database = databaseName
        self.databaseUrl = dbUrl