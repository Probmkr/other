import random as rnd

test = False

hands = ['rock', 'scissors', 'paper']
count = 0
winlose = {
    'player' : 0,
    'computer' : 0,
    'tie' : 0
}

# Data



# /Data

# Fucntion



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

    ichand = rnd.randint(0, 2)
    schand = hands[ichand]

    # /AI

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



    # /Calc data

print(f'you played {count} games')
print('You won', winlose['player'])
print('computer wons', winlose['computer'])
print(winlose['tie'] if winlose['tie'] > 0 else 'no', 'tie game{0}'.format('s' if winlose['tie'] > 1 else ''))