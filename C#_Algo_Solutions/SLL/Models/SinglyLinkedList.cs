using System.Transactions;
using System.Reflection.Metadata.Ecma335;
using System.Text.RegularExpressions;
using System;

namespace SLL.Models
{
    public class SinglyLinkedList
    {
        public SLLNode Head;
        public SinglyLinkedList() 
        {
            Head = null;
        }
        // SLL methods go here. As a starter, we will show you how to add a node to the list.
        public void Add(int value) 
        {
            SLLNode newNode = new SLLNode(value);
            if(Head == null) 
            {
                Head = newNode;
            } 
            else
            {
                SLLNode runner = Head;
                while(runner.Next != null){
                    runner = runner.Next;
                }
                runner.Next = newNode;
            }
        }  

        public SinglyLinkedList Remove(){
            if(Head == null){
                 return null;
            }
            else{
                SLLNode runner = Head;
                if(this.Size() < 2){
                    while(runner.Next != null){
                        runner = runner.Next;
                    }
                    runner.Next = null;
                }
                while(runner.Next.Next != null){
                     runner = runner.Next;
                }
                Console.WriteLine($"{runner.Next.Value}");
                runner.Next = null;
                return this; 
            }
        }  

        public object PrintVals(){
            if(Head == null){
                return null;
            }
            else{
                SLLNode runner = Head;
                Console.Write("[ ");
                while(runner.Next != null){
                    Console.Write($"{runner.Value}, ");
                    runner = runner.Next;
                }
                Console.Write($"{runner.Value}, ");
                Console.WriteLine(" ]");
                return this;
            }
        }

        public SLLNode Find(int val){
            if(Head == null){
                Console.WriteLine("No Nodes in SLL");
                return null;
            }
            else{
                SLLNode runner = Head;
                while(runner.Next != null){
                    if(runner.Value == val){
                       return runner;
                    }
                    runner = runner.Next;
                     continue;
                }
                if(runner.Value == val){
                    return runner;
                }
                else{
                    return null;
                }
            }
        }

        public int Size(){
            SLLNode runner = Head;
            int Count = 0;
            if(this == null){
                return Count;
            }
            while(runner.Next != null){
                Count++;
                runner = runner.Next;
            }
            Count++;
            Console.WriteLine($"{Count}");
            return Count;
        }

        public SinglyLinkedList RemoveAt(int n){
            int x = Size();
            if( n > x ){
                Console.WriteLine("Position Does Not Exist");
                return null;
            }
            else if ( n < 0 ){
                Console.WriteLine("Position Does Not Exist");
                return null;
            }
            else if( n == 0){
                Head = Head.Next;
                return this;
            }
            else{
                int i = 0;
                SLLNode runner = Head;
                while( i < n && runner.Next !=null){
                    runner = runner.Next;
                    i++;
                }
                runner.Next = runner.Next?.Next;
                return this;
            }

        }

        public SinglyLinkedList Reverse(){
            SLLNode runner = Head;
            SLLNode prev = null;
            SLLNode next = null;
            while(runner != null){
                next = runner.Next;
                runner.Next = prev;
                prev = runner;
                runner = next;
            }
            Head = prev;
            return this;
        }
    }
}