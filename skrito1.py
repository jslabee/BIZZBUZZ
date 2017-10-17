#!/usr/bin/env python
# -*- coding: utf-8 -*-



secret = 69
#
for x in range(5):
    guess = int(raw_input("ugani skrito število "))

    if  guess == secret:
        print "ćestitam"
        break
    else:
        print  str(guess)+ " je napačno število  "
