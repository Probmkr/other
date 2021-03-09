using System;

namespace _3_6
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 0;
            Console.Write(" > ");
            n = int.Parse(Console.ReadLine());
            case1(n);
            case2(n);
            case3(n);
        }

        static void case1(int score)
        {
            if(score >= 60)
            {
                Console.WriteLine("Pass");
            }
            else
            {
                Console.WriteLine("Failure");
            }
        }

        static void case2(int score)
        {
            if (score >= 80)
            {
                Console.WriteLine("Very well done");
            }
            else if (score >= 60)
            {
                Console.WriteLine("Good job");
            }
            else
            {
                Console.WriteLine("That's too bad");
            }
        }

        static void case3(int score)
        {
            if (score >= 80)
            {
                Console.WriteLine("優");
            }
            else if (score >= 70)
            {
                Console.WriteLine("良");
            }
            else if (score >= 60)
            {
                Console.WriteLine("可");
            }
            else
            {
                Console.WriteLine("不可");
            }
        }
    }
}
