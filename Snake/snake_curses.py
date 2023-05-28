#!/usr/bin/env python3
import random
import curses
import time
import sys
def main(stdscr):
    gamewin = curses.newwin(32,62,0,0)
    gamewin.resize(32,62)
    gamewin.border("*","*","*","*","*","*","*","*")
    inputwin = curses.newwin(2,62,32,0)
    inputwin.addstr(0,0,"Hova?")
    pos = [0, 0]
    pos[0] = random.randint(1,30)
    pos[1] = random.randint(1,60)
    gamewin.addstr(pos[0], pos[1],"@")
    curses.echo()
    gamewin.refresh()
    inputwin.refresh()
    while True:
        if pos[0] == 0 or pos[0] == 31 or pos[1] == 0 or pos[1] == 61:
            inputwin.addstr(1,0,"Most ennyi volt, szép napot!")
            inputwin.refresh()
            time.sleep(3)
            sys.exit()
        command = inputwin.getstr(1,0)
        if command == b"meguntam":
            inputwin.addstr(1,0,"Most ennyi volt, szép napot!")
            inputwin.refresh()
            time.sleep(3)
            sys.exit()
        elif command == b"balra":
            gamewin.addstr(pos[0],pos[1]," ")
            pos[1] -= 1
            gamewin.addstr(pos[0],pos[1],"@")
        elif command == b"jobbra":
            gamewin.addstr(pos[0],pos[1]," ")
            pos[1] += 1
            gamewin.addstr(pos[0],pos[1],"@")
        elif command == b"fel":
            gamewin.addstr(pos[0],pos[1]," ")
            pos[0] -= 1
            gamewin.addstr(pos[0],pos[1],"@")
        elif command == b"le":
            gamewin.addstr(pos[0],pos[1]," ")
            pos[0] += 1
            gamewin.addstr(pos[0],pos[1],"@")
        inputwin.clrtoeol()
        gamewin.refresh()
        inputwin.refresh()
curses.wrapper(main)
