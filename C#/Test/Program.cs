using System;

public static class Store
{
    public static void Main(string[] args)
    {
        Console.WriteLine(QueueWithMinimalWaitingTime(10, 20, 30));
        Console.WriteLine(QueueWithMinimalWaitingTime(90, 13, 40));
        Console.WriteLine(QueueWithMinimalWaitingTime(12, 13, 11));
        Console.WriteLine(QueueWithMinimalWaitingTime(4,  13, 40));
    }

    public static int QueueWithMinimalWaitingTime(int customersInQueue1, int customersInQueue2, int customersInQueue3)
    {
        int timeForQ1 = 0, timeForQ2 = 0, timeForQ3 = 0;

        timeForQ1 = customersInQueue1 * 45;
        timeForQ2 = customersInQueue2 * 30;
        timeForQ3 = customersInQueue3 * 12;

        if (timeForQ1 <= timeForQ2)
        {
            if (timeForQ1 <= timeForQ3)
            {
                return 1;
            }
            else
            {
                return 3;
            }
        }
        else if (timeForQ2 <= timeForQ3)
        {
            return 2;
        }
        else
        {
            return 3;
        }
    }
}