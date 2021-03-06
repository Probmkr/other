using System;

namespace ClassPractice
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("\n\nWizard\n\n");
            Wizard P2 = new Wizard("Player2", 80, 100);
            P2.Attack(20);
            P2.Defence();
            P2.Damage(10);
            int P2HP = P2.GetHP();
            Console.WriteLine(P2HP);
            P2.MagicAttack(30);
            Console.WriteLine(P2.GetMP());
        }
    }
}