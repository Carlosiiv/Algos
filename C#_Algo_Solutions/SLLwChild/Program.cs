﻿using System;
using System.Collections.Generic;
using SLL.Models;

namespace SLL
{
    class Program
    {
        static void Main(string[] args)
        {
           SinglyLinkedList newList = new SinglyLinkedList();
           for(int i = 0; i <= 20; i++){
               newList.Add(i);
           }
           SinglyLinkedList ChildList = new SinglyLinkedList();
           for(int j = 20; j <= 40; j++){
               ChildList.Add(j);
           }
           newList.Head.Child = ChildList;
           newList.PrintVals();
           newList.Flatten();
           newList.PrintVals();
        //    Console.WriteLine("--------------------------------------------------");
        //    newList.Size();
        //    Console.WriteLine("--------------------------------------------------");
        //    newList.Remove();
        //    Console.WriteLine
        //    ("--------------------------------------------------");
        //    newList.RemoveAt(4);
        //    Console.WriteLine
        //    ("--------------------------------------------------");
        //    newList.PrintVals();
        //    Console.WriteLine("--------------------------------------------------");
        //    SLLNode x = newList.Find(15);
        //    Console.WriteLine($"{x.Value}");
        //    Console.WriteLine("--------------------------------------------------");
        //    newList.Size();
        //    Console.WriteLine("--------------------------------------------------");
        //    newList.Reverse();
        //    newList.PrintVals();
        //    Console.WriteLine("--------------------------------------------------");
            // Console.WriteLine("Hello World!");
        }
    }
}
