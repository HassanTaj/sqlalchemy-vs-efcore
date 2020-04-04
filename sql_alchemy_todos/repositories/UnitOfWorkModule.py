from repositories.TodoRepo import *
from helpers.ConnectionHelperModule import *
from sqlalchemy.orm import sessionmaker


class UnitOfWork(object):
	def __init__(self):
		# get connection
		helper = ConnectionHelper()
		# bind the engine with session
		Session = sessionmaker(bind = helper.getEngine())
		# pass the session object to the repositories
		self.todoRepo = TodoRepository(Session())
		pass
