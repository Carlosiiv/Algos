using System;
using DLL.Models;

namespace DLL
{
    class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine("Hello World!");
            DoublyLinkedList newList = new DoublyLinkedList();
            for(int i = 1; i <= 1; i++){
                newList.Add(i);
            }
            // Console.WriteLine("--------------------------------------------------");
            // // Console.WriteLine(newList.Size());
            // Console.WriteLine("--------------------------------------------------");
            // // newList.Pop();
            newList.PrintVals();
            // Console.WriteLine
            // ("--------------------------------------------------");
            // Console.WriteLine("--------------------------------------------------");
            // Console.WriteLine(newList.Size());
            Console.WriteLine("--------------------------------------------------");
            newList.Reverse();
            newList.PrintVals();
        }
    }
}
