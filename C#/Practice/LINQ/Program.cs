using System;
using System.Collections.Generic;
using System.Linq;

namespace LINQ
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array = {20, 420, 560 ,315, 290, 600};

            var newArray = array.Where(n => n >= 500);

            foreach (int n in newArray)
            {
                Console.WriteLine(n);
            }
        }
    }
}
