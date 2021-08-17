using System;
using System.IO;
using System.Text.RegularExpressions;

namespace Test
{
    public class Test
    {
        public static void Main(string[] arg)
        {
            string test = "aaa=ttt&bbb=iii";
            string replaced = Regex.Replace(test, "(.+)=(.+)&(.+)=(.+)", "(.+) : (.+), (.+) : (.+)");
            Console.WriteLine(replaced);
        }
    }
}