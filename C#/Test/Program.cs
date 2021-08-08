using System;
using System.IO;

namespace Test
{
    public class Test
    {
        public static void Main(string[] arg)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("C:/Users/zhoy/source/");
            if(arg.Length >= 1)
            {
                Console.WriteLine(arg[0]);
            }
        }
    }
}