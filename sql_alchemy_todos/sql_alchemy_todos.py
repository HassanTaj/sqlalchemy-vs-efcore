import sys
import json
from repositories.UnitOfWorkModule import UnitOfWork
from models.todo import Todos;


def printTodos(res):
    for row in res:
     print ("{\n\tId: ",row.id ,"\n\tName: ",row.task, "\n\tDescription: ",row.description,"\n}")

def dump(res):
    json.dumps(res)

def main():
    print("Lets see what we can do")    
    try:
        #-------------------- Unit Of Work
        #uow = UnitOfWork()

        #------------------- Read All
        #printTodos(uow.todoRepo.getAll())
        #------------------- Read All

        #------------------- Create
        #print("\n\n we're gonna add some new shit here\n\n")
        #todo = Todos()
        #todo.task = input("Enter Task name : ")
        #todo.description = input("Enter Task description : ")
        #uow.todoRepo.create(todo);
        #------------------- Create

        #------------------- Read All
        #printTodos(uow.todoRepo.getAll())
        #------------------- Read All

        #------------------- Get Single by id
        #id = input("Enter id To be deleted : ");
        #res  = uow.todoRepo.getById(id)
        #printTodos(res)
        #------------------- Get Single by id

        #------------------- Delete
        # delete test
        #res = uow.todoRepo.delete(res);
        #print("deleted: ",res)
        #------------------- Delete

        #------------------- Read All
        #printTodos(uow.todoRepo.getAll())
        #------------------- Read All

        pass
    except Exception as ex:
        print(ex)
        pass


if __name__ == "__main__":
    sys.exit(int(main() or 0))
