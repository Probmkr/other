using System;

namespace _2_6
{
    class Program
    {
        static void Main(string[] args)
        {
            int age = 0;
            Console.Write(" > ");
            age = int.Parse(Console.ReadLine());
            Console.WriteLine("\nYou passed around {0} days!", 365 * age);
        }
    }
}
