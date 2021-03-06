using System;

namespace TRPG
{
    public class GameControl
    {
        private int stage;

        public GameMaster(int startStage = 1)
        {
            if (startStage < 1)
            {
                startStage = 1;
            }
            this.stage = startStage;
        }
    }
}