using System;
using System.Collections.Generic;

namespace DLL.Models
{
    public class DoublyLinkedList
    {
        public DLLNode Head;
        public DLLNode Tail;

        public DoublyLinkedList(){
            Head=null;
            Tail=null;
        }
        public void Add(int val){
            DLLNode newnode = new DLLNode(val);
            if(Head == null){
                Head = newnode;
                Tail = newnode;
            }
            else{
                Tail.Next = newnode;
                newnode.Prev = Tail;
                Tail = newnode;
            }
        }
        public DoublyLinkedList Pop(){
            if(Head == null){
                return null;
            }
            else{
                Tail = Tail.Prev;
                Console.WriteLine($"{Tail.Next.Value}");
                Tail.Next = null;
                return this;
            }
        }
        public int Size(){
            int count = 0;
            DLLNode runner = Head;
            if (Head == null){
                return count;
            }
            else{
                while (runner.Next != null){
                    count++;
                    runner = runner.Next;
                }
                count++;
                return count;
            }
        }
        public object PrintVals(){
            if(Head == null){
                return null;
            }
            else{
                DLLNode runner = Head;
                Console.Write("[");
                while(runner.Next != null){
                    Console.Write($"{runner.Value},");
                    runner = runner.Next;
                }
                Console.Write($"{runner.Value},");
                Console.WriteLine("]");
                return this;
            }
        }

        public DoublyLinkedList Reverse(){
            DLLNode x = null;
            DLLNode runner = Head;
            if(Head == null){
                return null;
            }
            else if( Size() == 1){
                return this;
            }
            else{
                while(runner != null){
                x = runner.Prev;
                runner.Prev = runner.Next;
                runner.Next = x;
                runner = runner.Prev;
                }
                Head = x.Prev;
                return this;
                // if(x != null){
                //      
                //    return this;
                // }
                // else{
                //    Head = runner;
                //     return this;
                // }
            }
            
            

        }
    }
    
}