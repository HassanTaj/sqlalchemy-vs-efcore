using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace ef_todos_console.Models {
    public class BaseModel {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public string Id { get; set; }
        public string CreatedBy { get; set; }
        public Nullable<DateTime> CreatedAt { get; set; }
        public string UpdatedBy { get; set; }
        public Nullable<DateTime> UpdatedAt { get; set; }
        public bool IsDeleted { get; set; }
    }
}
