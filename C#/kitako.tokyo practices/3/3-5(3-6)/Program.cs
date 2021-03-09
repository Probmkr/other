using System;

namespace _3_5
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 0;
            Console.Write(" > ");
            n = int.Parse(Console.ReadLine());
            if (n >= 0)
            {
                if (n % 2 == 0)
                {
                    Console.WriteLine("n is positive and even");
                }
                else
                {
                    Console.WriteLine("n is positive and add");
                }
            }
            else
            {
                if (n % 2 == 0)
                {
                    Console.WriteLine("n is negative and even");
                }
                else
                {
                    Console.WriteLine("n is negative and odd");
                }
            }
        }
    }
}
