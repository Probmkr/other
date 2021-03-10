using System;

namespace _3_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 0, y = 0;
            Console.Write("x > ");
            x = int.Parse(Console.ReadLine());
            Console.Write("y > ");
            y = int.Parse(Console.ReadLine());

            if (x > y)
            {
                Console.WriteLine("\nx is bigger than y");
            }
        }
    }
}
