using System;

namespace ClassPractice
{
    class Wizard : Player
    {
        protected int MP;

        public Wizard(string name, int startHP, int startMP) : base(name, startHP)
        {
            this.MP = startMP;
        }

        public override void Attack(int value)
        {
            Console.WriteLine($"Wizard {this.name} attacked enemy {value} damages!");
        }

        public override void Defence()
        {
            Console.WriteLine($"Wizard {this.name} defended!");
        }

        public override void Damage(int value)
        {
            this.HP -= value;
            Console.WriteLine($"Wizard {this.name} tooked {value} damages!");
        }

        public void MagicAttack(int UseMP)
        {
            this.MP -= UseMP;
            Console.WriteLine($"Wizard {this.name} use MP attacked enemy {UseMP} damages!");
        }

        public int GetMP()
        {
            return this.MP;
        }
    }
}