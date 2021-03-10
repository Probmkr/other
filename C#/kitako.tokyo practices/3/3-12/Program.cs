using System;

namespace _3_12
{
    class Program
    {
        static void Main(string[] args)
        {
            int month = 0;
            bool isCorrect = false;
            while(!isCorrect)
            {
                Console.Write("enter month > ");
                month = int.Parse(Console.ReadLine());
                isCorrect = judge(month);
                if (!isCorrect)
                {
                    Console.WriteLine("入力が正しくありません。");
                }
            }
        }

        static bool judge(int month)
        {
            int[] daysType = new int[3] {28, 30, 31};
            bool isCorrect = true;
            switch (month)
            {
                case 2:
                    Console.WriteLine(daysType[0]);
                    break;

                case 4: case 6: case 9: case 11:
                    Console.WriteLine(daysType[1]);
                    break;

                case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                    Console.WriteLine(daysType[2]);
                    break;

                default:
                    isCorrect = false;
                    break;
            }
            return isCorrect;
        }
    }
}
