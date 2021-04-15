using System;
using System.Collections.Generic;

namespace Test
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Dictionary<string, dynamic> dict1 = new Dictionary<string, dynamic>()
            {
                {"int", 12},
                {"string", "this is string"},
                {"float", 13.4}
            };

            Console.WriteLine("\n\ndict1\n");
            foreach (KeyValuePair<string, dynamic> item in dict1)
            {
                Console.WriteLine("{0, -10} : {1, -16}", item.Key, item.Value);
            }

            var dict2 = new Dictionary<string, dynamic>(dict1);

            Console.WriteLine("\n\ndict2\n");
            foreach (KeyValuePair<string, dynamic> item in dict2)
            {
                Console.WriteLine("{0, -10} : {1, -16}", item.Key, item.Value);
            }

            dict1["int"] = 13;

            Console.WriteLine("\n\nedited dict1  dict[\"int\"] = 13;");

            Console.WriteLine("\n\ndict1\n");
            foreach (KeyValuePair<string, dynamic> item in dict1)
            {
                Console.WriteLine("{0, -10} : {1, -16}", item.Key, item.Value);
            }

            Console.WriteLine("\n\ndict2\n");
            foreach (KeyValuePair<string, dynamic> item in dict2)
            {
                Console.WriteLine("{0, -10} : {1, -16}", item.Key, item.Value);
            }
        }
    }
}