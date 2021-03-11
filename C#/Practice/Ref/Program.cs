using System;

namespace Ref
{
    class Program
    {
        static void Main(string[] args)
        {
            int n1 = 0;
            int n2;

            Console.WriteLine("\ncase1 ref\n");

            Console.Write("enter one number > ");
            n1 = int.Parse(Console.ReadLine());
            Console.WriteLine("n1 = {0}", n1);
            case1(ref n1);
            Console.WriteLine("now, n1 = {0}", n1);

            Console.WriteLine("\ncase2 class\n");

            Console.Write("enter one number > ");
            n1 = int.Parse(Console.ReadLine());

            Case2Class class1 = new Case2Class(n1);
            Console.WriteLine("class1's num = {0}", class1.num);
            case2(class1);
            Console.WriteLine("now, class1's num = {0}", class1.num);

            Console.WriteLine("\ncase3 out\n");

            Console.Write("enter one number > ");
            n1 = int.Parse(Console.ReadLine());
            Console.WriteLine("n1 = {0}. n2 is unassigned.", n1);
            case3(out n2, n1);
            Console.WriteLine("now, n1 = {0}. n2 = {1}", n1, n2);
        }

        static void case1(ref int n)
        {
            n -= 10;
        }

        static void case2(Case2Class classTemp)
        {
            classTemp.num += 10;
        }

        static void case3(out int n2, int n1)
        {
            n2 = n1;
        }
    }
}
