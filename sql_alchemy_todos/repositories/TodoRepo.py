
from models.todo import Todos;
from repositories.BaseRepo import BaseRepository

class TodoRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        # initialize base repository
        super().__init__(self.session,Todos,True)

    # method that will get all the shit
    #def getAll(self):
    #    res = self.session.query(Todos).all()
    #    #print("get all records from SQL Server")
    #    for row in res:
    #         print ("{\n\tId: ",row.id ,"\n\tName: ",row.task, "\n\tDescription: ",row.description,"\n}")

    # use this method to insert into db
    #def create(self,todo):
    #    try:
    #        # call base class and get a unique id
    #        todo.id = self.generateUniqueId()
    #        self.session.add(todo)
    #        self.session.commit()
    #        pass
    #    except Exception as ex:
    #        print(ex)

