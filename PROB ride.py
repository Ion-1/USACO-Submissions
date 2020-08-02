# -*- coding: utf-8 -*-
"""
ID: ion11
LANG: PYTHON3
PROB: ride
"""

f = open('ride.in','r') 
fo = open('ride.out','w') 
a,b = f.readlines() 
x = 1 
y = 1 
for i in a: 
    x *= (ord(i)-64) 
for i in b: 
    y *= (ord(i)-64) 
if x%47 == y%47: 
    fo.write('GO\n') 
else: 
    fo.write('STAY\n') 