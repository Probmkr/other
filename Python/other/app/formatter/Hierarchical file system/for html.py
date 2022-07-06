# coding: utf-8
from os import path

# print directory contents
def dir(indent, item):
    print('<span class="dir">', '&nbsp;'*(indent-1), item+'/' + '</span><br>')


# print file contents
def file(indent, item):
    print('<span class="file">', '&nbsp;'*(indent-1), item[-1] + '</span><br>')


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
    print('<link rel="stylesheet" href="style.css">')
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