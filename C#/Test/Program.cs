using System;

namespace Test
{
    public class Test
    {
        public static void Main(string[] arg)
        {
            Console.WriteLine("Hello World!");
            if(arg.Length >= 1)
            {
                Console.WriteLine(arg[0]);
            }
        }
    }
}