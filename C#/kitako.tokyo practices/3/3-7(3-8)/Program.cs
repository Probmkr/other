using System;

namespace _3_7
{
    class Program
    {
        static void Main(string[] args)
        {
            int n1 = 0, n2 = 0;
            Console.Write(" > ");
            n1 = int.Parse(Console.ReadLine());
            Console.Write(" > ");
            n2 = int.Parse(Console.ReadLine());
            judge(n1, n2);
        }

        static void judge(int score1, int score2)
        {
            bool flag = false;
            if (score1 >= 60 & score2 >= 60)
            {
                flag = true;
            }
            else if (score1 + score2 >= 130)
            {
                flag = true;
            }
            else if ((score1 + score2 >= 100) & (score1 >= 90 | score2 >= 90))
            {
                flag = true;
            }

            if (flag == true)
            {
                Console.WriteLine("Pass");
            }
            else
            {
                Console.WriteLine("Failure");
            }
        }
    }
}
