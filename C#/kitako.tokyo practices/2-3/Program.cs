using System;

namespace _2_3
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 0;
            x = int.Parse(Console.ReadLine());
            for (int i = 1; i <= 3; i++)
            {
                Console.WriteLine(Math.Pow(x, i));
            }
        }
    }
}