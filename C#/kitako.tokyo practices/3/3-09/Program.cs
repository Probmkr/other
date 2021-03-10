using System;

namespace _3_9
{
    class Program
    {
        static void Main(string[] args)
        {
            int day = -1, time = -1;
            Console.Write("0=日曜、1=月曜、2=火曜、3=水曜、4=木曜、5=金曜、6=土曜\n > ");
            day = int.Parse(Console.ReadLine());
            Console.Write("0=午前、1=午後、2=夜間\n > ");
            time = int.Parse(Console.ReadLine());
            judge(day, time);
        }

        static void judge(int day, int time)
        {
            bool flag = true;
            if (day == 0)
            {
                flag = false;
            }
            else if (day == 2 & time == 0)
            {
                flag = false;
            }
            else if (day == 3 & time == 2)
            {
                flag = false;
            }
            else if (day == 5 & time == 0)
            {
                flag = false;
            }
            else if (day == 6 & (time == 1 | time == 2))
            {
                flag = false;
            }

            if (flag == false)
            {
                Console.WriteLine("休診");
            }
            else
            {
                Console.WriteLine("開業");
            }
        }
    }
}
