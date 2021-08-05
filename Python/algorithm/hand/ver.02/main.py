import random as rnd
import numpy as np
import copy as cpy

test = False

hands = ['rock', 'scissors', 'paper']
count = 0
winlose = {
    'player': 0,
    'computer': 0,
    'tie': 0
}

iphand = 0
sphand = ''
ichand = 0
schand = ''

# Data

phands = [0, 0, 0]
preHand = None
patterns = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Data

# Fucntion

def PercOfPattern(pattern):
    pattern = pattern.copy()
    return Percentage(pattern)

def Percentage(tList):
    tList = tList.copy()
    sumList = sum(tList)
    lenList = len(tList)
    percList = [None]*lenList

    try:
        for i in range(lenList):
            percList[i] = round(tList[i] / sumList * 100)
    except ZeroDivisionError:
        return False

    return percList

def Frequency(phands):
    retVal = 0
    phands = phands.copy()
    sortBig = list(reversed(np.array(phands).argsort()))
    phands[sortBig[0]] *= 3
    phands[sortBig[1]] *= 2
    phandsPerc = Percentage(phands)
    rndnum = rnd.randint(1, 100)

    if (not phandsPerc):
        return rnd.randint(0, 2)

    if rndnum <= phandsPerc[0]:
        retVal = 2
    elif rndnum <= sum(phandsPerc[0:2]):
        retVal = 0
    elif rndnum <= sum(phandsPerc[0:3]):
        retVal = 1
    else:
        retVal = rnd.randint(0, 2)

    return retVal

def FrequencyChange(phands):
    phands = phands.copy()
    # sortBig = list(reversed(np.array(phands).argsort()))
    # phands[sortBig[0]] *= 3
    # phands[sortBig[1]] *= 2

    return Percentage(phands)

def Pattern(patterns, phands):
    print(patterns)
    PatternSub(patterns, phands)
    return Frequency(phands)

def PatternSub(patterns, phands):
    phandsPerc = FrequencyChange(phands)
    patternPerc = None
    print(phandsPerc)
    try:
        patternPerc = PercOfPattern(patterns[preHand])
        print(patternPerc)
    except TypeError:
        return rnd.randint(0, 2)

    # Calc




# /Function


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
    try:
        sphand = hands[iphand]
    except IndexError:
        print('Please enter correct number')
        break

    # AI

    ichand = Pattern(patterns, phands)
    schand = hands[ichand]

    # AI

    print('\n')
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
    print('\n')

    # Calc data

    phands[iphand] += 1

    # print(preHand, iphand)
    try:
        patterns[preHand][iphand] += 1
    except TypeError:
        pass

    preHand = iphand

    # Calc data

print('\n'*3)
print(f'you played {count} games')
print('You won', winlose['player'])
print('computer wons', winlose['computer'])
print(winlose['tie'] if winlose['tie'] > 0 else 'no',
      'tie game{0}'.format('s' if winlose['tie'] > 1 else ''))
print('\n'*3)
