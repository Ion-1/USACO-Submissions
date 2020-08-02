# -*- coding: utf-8 -*-
"""
ID: ion11
LANG: PYTHON3
PROB: gift1
"""
import math
f = open('gift1.in','r')
d = open('gift1.out','w')
a = f.readlines()
np = int(a[0])
P = {}
x = 0
giver = ''
m = 0
nps = 0
for i in range(np+1):
    if i != 0:
        P[a[i]] = 0
for i in range(len(a)):
    if i <= np:
        None
    elif x == 0:
        given = []
        giver = a[i]
        x += 1
    elif x == 1: 
        m,nps = a[i].split(' ') #m = money nps = # people shared
        m,nps = int(m),int(nps)
        if nps == 0:
            x -= 1
        else:
            x += nps
    else:
        given.append(a[i])
        if x != 2:
            x -= 1
        else:
            x -= 2
            if giver != '':
                if nps != 0:
                    P[giver] -= m
                    gm = math.floor(m/nps)
                    for b in given:
                        P[b] += gm
                    P[giver] += m%nps
for i in P:
    a = str(P[i])
    d.write(i.rstrip()+' '+a+'\n')