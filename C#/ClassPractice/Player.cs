using System;

namespace ClassPractice
{
    public class Player
    {
        private string name;
        private int HP;

        public Player(string name, int startHP)
        {
            this.name = name;
            this.HP = startHP;
        }
    }
}