using System;

namespace _2_4
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
            Console.WriteLine(x + y);
            Console.WriteLine(x - y);
            Console.WriteLine(x * y);
            Console.WriteLine(x / y);
            Console.WriteLine(x % y);
        }
    }
}
