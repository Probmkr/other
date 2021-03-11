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

            List<int> list = new List<int> {100, 34, 98, 8, 87, 56, 92, 10, 90, 86, 87, 97, 94, 43};

            var newArray = array.Where(n => n >= 500);

            var newList = list.Where(n => n >= 90);

            Console.WriteLine("\nint array\n");
            foreach (int n in newArray)
            {
                Console.WriteLine(n);
            }

            Console.WriteLine("\nList\n");
            foreach (int n in newList)
            {
                Console.WriteLine(n);
            }
        }
    }
}
