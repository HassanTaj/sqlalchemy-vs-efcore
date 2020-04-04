using ef_todos_console.Contexts;
using ef_todos_console.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ef_todos_console.Repository {
    public class TodoRepo : ITodoRepo {
        private readonly AppDbMSSQLContext db = new AppDbMSSQLContext();
        public TodoRepo() {
        }

        public bool Create(Todo todo) {
            try {
                db.Add(todo);
                db.SaveChanges();
                return true;
            }
            catch (Exception) {
                return false;
            }
        }

        public bool Delete(Todo todo) {
            throw new NotImplementedException();
        }

        public IEnumerable<Todo> GetAll() {
            return db.Todos.ToList();
        }

        public Todo GetById(string id) {
            throw new NotImplementedException();
        }

        public bool Update(Todo todo) {
            throw new NotImplementedException();
        }
    }
}
