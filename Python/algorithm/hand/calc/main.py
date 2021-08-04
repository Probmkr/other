import random as rnd

test = True

hands = ['rock', 'scissors', 'paper']
count = 0
winlose = {
    'player' : 0,
    'computer' : 0,
    'tie' : 0
}

while 1:
    cmd = 1
    try:
        cmd = int(input('Enter your hand [0: rock] [1: scissors] [2: paper] or enter [3: end] > '))
    except ValueError:
        if not test: exit()
    if cmd == 3:
        break
    iphand = cmd if test != True else 2
    sphand = hands[iphand]

    ichand = rnd.randint(0, 2)
    schand = hands[ichand]

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

print(f'you played {count} games')
print('You won', winlose['player'])
print('computer wons', winlose['computer'])
print(winlose['tie'] if winlose['tie'] > 0 else 'no', 'tie game{0}'.format('s' if winlose['tie'] > 1 else ''))