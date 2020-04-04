using ef_todos_console.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace ef_todos_console.Repository {
    public interface ITodoRepo  {
        IEnumerable<Todo> GetAll();
        bool Create(Todo todo);
        bool Update(Todo todo);
        bool Delete(Todo todo);
        Todo GetById(string id);
    }
}
