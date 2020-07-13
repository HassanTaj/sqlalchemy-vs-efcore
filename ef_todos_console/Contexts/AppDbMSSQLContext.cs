using ef_todos_console.Models;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Text;

namespace ef_todos_console.Contexts {
    public class AppDbMSSQLContext : DbContext {


        public DbSet<Todo> Todos { get; set; }
        public DbSet<Answer> Answers { get; set; }
        public DbSet<Question> Questions { get; set; }


        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder) {
            optionsBuilder.UseSqlServer("Data Source=.;Initial Catalog=todo_db;User=sa;Password=123;Integrated Security=False;");
            //base.OnConfiguring(optionsBuilder);
        }
    }
}
