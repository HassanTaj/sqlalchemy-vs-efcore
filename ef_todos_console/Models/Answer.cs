using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace ef_todos_console.Models {
    public class Answer : BaseModel {
        public string Reply { get; set; }

        public string QuestionId { get; set; }
        [ForeignKey(nameof(QuestionId))]
        public Question Question { get; set; }
    }
}
