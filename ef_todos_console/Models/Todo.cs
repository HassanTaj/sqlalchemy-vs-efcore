using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace ef_todos_console.Models {
    public class Todo {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public string Id { get; set; }
        public string Task { get; set; }
        public string Description { get; set; }
        public Nullable<DateTime> EndDate { get; set; }
    }
}
