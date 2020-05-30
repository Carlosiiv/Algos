

namespace SLL.Models
{
    public class SLLNode
    {
       public int Value;
        public SLLNode Next;
        public SinglyLinkedList Child = new SinglyLinkedList();
        public SLLNode(int value) 
        {
            Value = value;
            Next = null;
            Child = null;
        } 
    }
}