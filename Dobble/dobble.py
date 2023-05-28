#!/usr/bin/env python3
import random
import sys
if len(sys.argv) < 2:
    print("Add meg parancssori paraméterként, hány szám legyen egy kártyán.")
    sys.exit()
n = int(sys.argv[1])
kartyadb = (n-1)**2 + (n-1) + 1
kartyak = []
while len(kartyak) != kartyadb:
    kartya = []
    while len(kartya) != n:
        szam = str(random.randint(0,kartyadb))
        if szam not in kartya:
            kartya.append(szam)
    test_failed = False
    for k in kartyak:
        if len(list(set(kartya).intersection(k))) != 1:
            test_failed = True
    if test_failed == False:
        kartyak.append(kartya)
for k in kartyak:
    print(' '.join(k))
