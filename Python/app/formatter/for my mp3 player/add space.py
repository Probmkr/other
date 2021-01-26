import sys

def fileNotFound(num):
    print(f'\n\nThe error occured at {"first" if num == 1 else "second"} paramater\nPlease enter correct path!')
    exit()

if len(sys.argv) != 3:
    print('\n\nPlease enter 2 parameter!')
    exit()

rf = None
try:
    rf = open(sys.argv[1], 'r', encoding='utf-8')
except FileNotFoundError:
    fileNotFound(1)

rawText = rf.read()
rf.close()

writeText = ''

for i in rawText:
    writeText += i if i != ' ' else '    '

wf = None
try:
    wf = open(sys.argv[2], 'w', encoding='utf-8')
except FileNotFoundError:
    fileNotFound(2)
wf.write(writeText)