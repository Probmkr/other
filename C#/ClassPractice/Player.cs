using System;

namespace ClassPractice
{
    public class Player
    {
        protected string name;
        protected int HP;

        public Player(string name, int startHP)
        {
            this.name = name;
            this.HP = startHP;
        }

        public virtual void Attack(int value)
        {
            Console.WriteLine($"Player {this.name} attacked enemy {value} damages!");
        }

        public virtual void Defence()
        {
            Console.WriteLine($"Player {this.name} defended!");
        }

        public virtual void Damage(int value)
        {
            this.HP -= value;
            Console.WriteLine($"Player {this.name} tooked {value} damages!");
        }

        public int GetHP()
        {
            return this.HP;
        }
    }
}