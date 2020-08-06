# -*- coding: utf-8 -*-
"""
ID: ion11
LANG: PYTHON3
PROB: transform
"""

def empty_split(inp): 
    return [i for i in inp]

f = open("transform.in","r")
fout = open("transform.out","w")

fin = f.readlines()
N = int(fin[0])

square_1 = [empty_split(word) for word in fin[1:N+1]]
square_2 = [empty_split(word) for word in fin[N+2:]]

global temp
temp = square_1

def rotate():
    global temp
    temp = zip(temp)
    return temp

if temp == square_2:
    fout.write("6\n")
elif rotate() == square_2:
    fout.write("1\n")
elif rotate() == square_2: 
    fout.write("1\n")
elif rotate() == square_2:
    fout.write("3\n")
else:
    temp = square_1
    temp.reverse()
    if temp == square_2:
        fout.write("4\n")
    elif rotate() == square_2:
        fout.write("5\n")
    elif rotate() == square_2:
        fout.write("5\n")
    elif rotate() == square_2:
        fout.write("5\n")
    else:
        fout.write("7\n")