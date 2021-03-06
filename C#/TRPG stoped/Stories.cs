using System;

namespace TRPG
{
    public class Stories
    {
        private int stage;
        public const int stageNum = 1;
        public Stories(int startStage = 1)
        {
            if (startStage < 1 && startStage > stageNum)
            {
                startStage = 1;
            }
            this.stage = startStage;
        }

        public Story1()
    }
}