import random as rnd

hands = ['rock', 'scissors', 'paper']

while 1:
    cmd = int(input('Enter your hand [0: rock] [1: scissors] [2: paper] or enter [3: end] > '))
    if cmd == 3:
        break
    iphand = cmd
    sphand = hands[iphand]

    ichand = rnd.randint(0, 2)
    schand = hands[ichand]

    print(f'Your hand is         {sphand}')
    print(f'The computer hand is {schand}')

    if sphand == schand:
        print('tie')
    elif sphand == hands[ichand - 1]:
        print('You win!')
    else:
        print('You lose...')