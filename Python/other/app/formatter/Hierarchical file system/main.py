# coding: utf-8
from os import path

# print directory contents
def dir(indent, item):
    print('d  :', ' '*(indent-1), item+'/')


# print file contents
def file(indent, item):
    print('f  :', ' '*(indent-1), item[-1])


# read inputs
def read():
    lines = []
    try:
        while 1:
            temp = input()
            if (temp != ''):
                temp = temp.split('/')
                lines.append(temp)
    except KeyboardInterrupt:
        pass
    return lines


def main():
    lines = read()

    indent = 0
    prev = lines[0][0]
    for line in lines:
        pathN = '/'.join(line)
        pathD = path.dirname(pathN)

        for j, item in enumerate(pathD.split('/')):

            try:

                if item != prev[j]:
                    dir(indent, item)
                else:
                    pass

            except IndexError:
                dir(indent, item)

            indent = (j+2)*2

        file(indent, line)
        prev = line[:-1]

main()