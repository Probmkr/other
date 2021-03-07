using System;

namespace _2_5
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 0, y = 0;
            Console.Write(" > ");
            x = int.Parse(Console.ReadLine());
            Console.Write(" > ");
            y = int.Parse(Console.ReadLine());

            Console.WriteLine("\nAverage is {0}", (x + y) / 2);
        }
    }
}
