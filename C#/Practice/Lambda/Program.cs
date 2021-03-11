using System;

namespace Lambda
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 10;
            Func<int, int> func = (num) => num + 10;
            n = func(n);
            Console.WriteLine(n);
        }
    }
}
