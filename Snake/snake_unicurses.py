#!/usr/bin/env python3
import random
from unicurses import *
import time
import sys
stdscr = initscr()
clear()
gamewin = newwin(32,62,0,0)
wborder(gamewin, SCS_LANTERN,SCS_LANTERN,SCS_LANTERN,SCS_LANTERN,SCS_LANTERN,SCS_LANTERN,SCS_LANTERN,SCS_LANTERN)
inputwin = newwin(2,62,32,0)
mvwaddstr(inputwin,0,0,"Hova?")
pos = [0, 0]
pos[0] = random.randint(1,30)
pos[1] = random.randint(1,60)
mvwaddstr(gamewin,pos[0], pos[1],"@")
wrefresh(gamewin)
wrefresh(inputwin)
while True:
    if pos[0] == 0 or pos[0] == 31 or pos[1] == 0 or pos[1] == 61:
        mvwaddstr(inputwin,1,0,"Most ennyi volt, szép napot!")
        wrefresh(gamewin)
        wrefresh(inputwin)
        time.sleep(3)
        endwin()
        sys.exit()
    command = mvwgetstr(inputwin, 1,0)
    if command == "meguntam":
        mvwaddstr(inputwin,1,0,"Most ennyi volt, szép napot!")
        wrefresh(gamewin)
        wrefresh(inputwin)
        time.sleep(3)
        endwin()
        sys.exit()
    elif command == "balra":
        mvwaddstr(gamewin,pos[0],pos[1]," ")
        pos[1] -= 1
        mvwaddstr(gamewin,pos[0],pos[1],"@")
    elif command == "jobbra":
        mvwaddstr(gamewin,pos[0],pos[1]," ")
        pos[1] += 1
        mvwaddstr(gamewin,pos[0],pos[1],"@")
    elif command == "fel":
        mvwaddstr(gamewin,pos[0],pos[1]," ")
        pos[0] -= 1
        mvwaddstr(gamewin,pos[0],pos[1],"@")
    elif command == "le":
        mvwaddstr(gamewin,pos[0],pos[1]," ")
        pos[0] += 1
        mvwaddstr(gamewin,pos[0],pos[1],"@")
    wmove(inputwin, 1, 0)
    wclrtoeol(inputwin)
    wrefresh(gamewin)
    wrefresh(inputwin)
