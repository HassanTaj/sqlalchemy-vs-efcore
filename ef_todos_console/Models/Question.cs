using System;
using System.Collections.Generic;
using System.Text;

namespace ef_todos_console.Models {
    public class Question : BaseModel {
        public Question() {
            Answers = new List<Answer>();
        }
        public string Inquery { get; set; }
        public IEnumerable<Answer> Answers { get; set; }    
    }
}
