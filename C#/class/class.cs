using System;

namespace ClassPractice
{
    class Program
    {
        public static void Main(string[] arg)
        {
            classA A = new classA(12, 6);
            Console.WriteLine(A.GetPrivateInt());
            Console.WriteLine(A.GetProtectedInt());
        }
    }

    class classA
    {
        private int num;
        protected int share;

        public classA(int a)
        {
            this.num = a;
        }

        public classA(int a, int b)
        {
            this.num = a;
            this.share = b;
        }

        public int GetPrivateInt()
        {
            return this.num;
        }

        public int GetProtectedInt()
        {
            return this.share;
        }
    }
}