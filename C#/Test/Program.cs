using System;

namespace Test
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int numQuant = int.Parse(Console.ReadLine());
            int forTime = numQuant - 1;
            string[] input = Console.ReadLine().Split(' ');
            int[] numArr = new int[numQuant];
            for (int i = 0; i < forTime; i++)
            {
                numArr[i] = int.Parse(input[i]);
            }

            bool canDupMore = true;
            int count = 0;

            while(canDupMore)
            {
                count++;
                for (int i = 0; i < forTime; i++)
                {
                    if (numArr[i] % 2 == 0)
                    {
                        numArr[i] /= 2;
                    }
                    else
                    {
                        canDupMore = false;
                        count--;
                        break;
                    }
                }
            }

            Console.WriteLine(count);
        }
    }
}