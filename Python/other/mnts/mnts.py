#!/usr/bin/env python
import curses
import shutil
import time
from random import randint


def main():
    clear = False
    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        stdscr.nodelay(True)
        started = time.time()
        sec = ""
        pos = 0
        numl = [randint(0, 2) for _ in range(5)]
        while len(set(numl)) != 3:
            numl = [randint(0, 2) for _ in range(5)]
        while True:
            if len(set(numl)) == 1:
                clear = True
                break
            try:
                k = stdscr.getch()
                with open("test.py.log", "a") as f:
                    f.write(f"{k}\n")
                if k == ord("l") or k == "KEY_RIGHT":
                    if pos != 4:
                        pos += 1
                        numl[pos] = (numl[pos] + 1) % 10
                if k == ord("h") or k == "KEY_LEFT":
                    if pos != 0:
                        pos -= 1
                        numl[pos] = (numl[pos] + 1) % 10
                if k == ord("s"):
                    _numl = numl
                    _numl = [randint(0, 2) for _ in range(5)]
                    while len(set(_numl)) != 3:
                        _numl = [randint(0, 2) for _ in range(5)]
                    numl = _numl
                if k == ord("q"):
                    break
            except curses.error:
                pass
            stdscr.clear()
            nums = " ".join([str(i) for i in numl])
            sec = str(int(time.time() - started))
            ty = shutil.get_terminal_size().lines
            tx = shutil.get_terminal_size().columns
            stdscr.addstr(0, 0, "Make numbers the same")
            stdscr.addstr(1, 0, "q: quit, s: shuffle, h: left, l: right")
            stdscr.addstr(int(ty / 2), int(tx / 2) - 4, nums)
            stdscr.addstr(int(ty / 2) + 1, int(tx / 2) - 4 + pos * 2, "^")
            stdscr.addstr(int(ty / 2) + 3, int(tx / 2) + 2 - len(str(sec)), f"{sec}s")
            stdscr.refresh()
            time.sleep(.1)
    except Exception as e:
        print(e)
        time.sleep(3)
        pass
    finally:
        curses.echo()
        curses.endwin()
        if clear:
            print(f"Clear!! ({sec}s)")
        else:
            exit(1)


if __name__ == "__main__":
    main()
