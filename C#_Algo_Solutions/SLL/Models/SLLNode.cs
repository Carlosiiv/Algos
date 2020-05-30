

namespace SLL.Models
{
    public class SLLNode
    {
       public int Value;
        public SLLNode Next;
        public SLLNode(int value) 
        {
            Value = value;
            Next = null;
        } 
    }
}