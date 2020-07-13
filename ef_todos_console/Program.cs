using ef_todos_console.Contexts;
using ef_todos_console.Repository;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.IO;
using System.Linq;

namespace ef_todos_console {
    class Program {
        static void Main(string[] args) {
          
            var repo = new TodoRepo();
            Console.WriteLine($"number of Todos in db : {repo.GetAll().Count()}");
            //repo.Create(new Models.Todo() { Task = "Do something form .net console" });
            Console.WriteLine($"number of Todos in db : {repo.GetAll().Count()}");

            Console.ReadKey();
        }

    }
}
