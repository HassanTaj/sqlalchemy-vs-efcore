
import uuid

class BaseRepository(object):
	# initialize base repository
	# session is the Session Object from sessionmaker
	# queryType is the type of object/ domain model/ table in question
	# hasGuidPrimarykey determins if the quried table has a GUID as Primary key or not
	def __init__(self,session,queryType,hasGuidPrimarykey=False):
		self._session = session
		self.hasGuidAsPrimary = hasGuidPrimarykey
		self.quertType = queryType

	# this method gets all the shit from database table
	def getAll(self):
		try:
			res = self._session.query(self.quertType).all()
			return res
		except Exception as ex:
		    print(ex)

	# Insert object in database
	def create(self,obj):
		try:
			# if the primary key is guid then it generates and inserts it
			if(self.hasGuidAsPrimary): obj.id = self.generateUniqueId()

			self._session.add(obj)
			self._session.commit()
			pass
		except Exception as ex:
			print(ex)

	# Update 
	def update(self,id,obj):
		pass

	# delete a complete object
	def delete(self,obj):
		try:
			self._session.delete(obj)
			self._session.commit()
			return res
		except Exception:
		    print(ex)

	# Get single object from db based on id
	def getById(self,id):
		try:
			res = self._session.query(self.quertType).filter(self.quertType.id == id)
			return res[0]
		except Exception:
		   print(ex)

	# generates a Guid for inserting shit in sql server with a GUID as a primary key
	def generateUniqueId(self): return str(uuid.uuid4())
