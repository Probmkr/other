using System;

namespace _3_2
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

            if (x >= y)
            {
                Console.WriteLine("\n{0}", x);
            }
            else
            {
                Console.WriteLine("\n{0}", y);
            }
        }
    }
}
