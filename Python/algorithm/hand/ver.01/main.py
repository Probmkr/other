import random as rnd
import numpy as np

test = True

hands = ['rock', 'scissors', 'paper']
count = 0
winlose = {
    'player': 0,
    'computer': 0,
    'tie': 0
}

# Data

phands = [0, 0, 0]

# Data

# Fucntion

def Frequency(phands):
    retVal = 0
    phands = phands.copy()
    sortBig = list(reversed(np.array(phands).argsort()))
    phands[sortBig[0]] *= 3
    phands[sortBig[1]] *= 2
    print(sortBig)
    print(phands)
    phandsSum = sum(phands)
    phandsPerc = [0]*3
    rndnum = rnd.randint(1, 100)

    try:
        for i in range(3):
            phandsPerc[i] = round(phands[i] / phandsSum * 100)
    except ZeroDivisionError:
        rndnum = 101

    if rndnum <= phandsPerc[0]:
        retVal = 2
    elif rndnum <= sum(phandsPerc[0:2]):
        retVal = 0
    elif rndnum <= sum(phandsPerc[0:3]):
        retVal = 1
    else:
        retVal = rnd.randint(0, 2)

    return retVal
# Function


while 1:
    cmd = -1
    try:
        cmd = int(input('Enter your hand [1: rock] [2: scissors] [3: paper] or enter [0: end] > ')) - 1
    except ValueError:
        if not test:
            print('Please enter correct number')
            break
    if cmd == -1:
        break
    iphand = cmd if test != True else 2
    iphand = rnd.randint(0, 2)
    try:
        sphand = hands[iphand]
    except IndexError:
        print('Please enter correct number')
        break

    # AI

    ichand = Frequency(phands)
    schand = hands[ichand]

    # AI

    print(f'Your hand is         {sphand}')
    print(f'The computer hand is {schand}')

    if sphand == schand:
        print('tie')
        winlose['tie'] += 1
    elif sphand == hands[ichand - 1]:
        print('You win!')
        winlose['player'] += 1
    else:
        print('You lose...')
        winlose['computer'] += 1
    count += 1

    # Calc data

    phands[iphand] += 1
    # print(phands)

    # Calc data

print(f'you played {count} games')
print('You won', winlose['player'])
print('computer wons', winlose['computer'])
print(winlose['tie'] if winlose['tie'] > 0 else 'no',
      'tie game{0}'.format('s' if winlose['tie'] > 1 else ''))
