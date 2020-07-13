from repositories.TodoRepo import *
from helpers.ConnectionFactoryModule import *
from helpers.ConnectionStringModule import *
from helpers.ConnectionTypeModule import *
from sqlalchemy.orm import sessionmaker


class UnitOfWork(object):
	def __init__(self):
		# get adapter
		adapter  = ConnectionStringAdapter(ConnectionStringModel(
			dbUrl= ""
		),ConnectionType.sql_lite)
		# get connection
		helper = ConnectionFactory(adapter)
		# bind the engine with session
		Session = sessionmaker(bind = helper.getEngine())
		# pass the session object to the repositories
		self.todoRepo = TodoRepository(Session())
		pass
