using System;

namespace TRPG
{
    public class Player
    {
        private int HP;
        private bool isAlive;

        public Player(int startHP = 100)
        {
            if (startHP < 1)
            {
                startHP = 1;
            }
            this.HP = startHP;
            isAlive = true;
        }
    }
}