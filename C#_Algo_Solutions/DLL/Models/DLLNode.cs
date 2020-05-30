using System.Runtime.InteropServices.ComTypes;
namespace DLL
{
    public class DLLNode
    {
    public int Value;
    public DLLNode Next;
    public DLLNode Prev;
    public DLLNode(int val){
    // your code here
        Value = val;
        Next = null;
        Prev = null;
    }
    public DLLNode(int val, DLLNode pnode){
        Value = val;
        Prev = pnode;
        Next = null;
        pnode.Next = this;
    }
    }
}