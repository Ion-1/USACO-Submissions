# -*- coding: utf-8 -*-
"""
ID: ion11
LANG: PYTHON3
PROB: friday
"""

f = open('friday.in','r')
fout = open('friday.out','w')
n = int(f.readline())
Day = 0
days = {'Monday':0,'Tuesday':0,'Wendsday':0,'Thursday':0,'Friday':0,'Saturday':0,'Sunday':0}
for a in range(n):
    year = 1900 + a
    leap = False
    if year%100 == 0:
        if year%400 == 0:
            leap = True
    else:
        if year%4 == 0:
            leap = True
    for b in range(12):
        if b == 0:
            for i in range(31):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 1:
            if leap:
                for i in range(29):
                    if i == 12:
                        if Day == 0:
                            days['Monday'] += 1
                        elif Day == 1:
                            days['Tuesday'] += 1
                        elif Day == 2:
                            days['Wendsday'] += 1
                        elif Day == 3:
                            days['Thursday'] += 1
                        elif Day == 4:
                            days['Friday'] += 1
                        elif Day == 5:
                            days['Saturday'] += 1
                        elif Day == 6:
                            days['Sunday'] += 1
                    if Day == 6:
                        Day = 0
                    else:
                        Day += 1
            else:
                for i in range(28):
                    if i == 12:
                        if Day == 0:
                            days['Monday'] += 1
                        elif Day == 1:
                            days['Tuesday'] += 1
                        elif Day == 2:
                            days['Wendsday'] += 1
                        elif Day == 3:
                            days['Thursday'] += 1
                        elif Day == 4:
                            days['Friday'] += 1
                        elif Day == 5:
                            days['Saturday'] += 1
                        elif Day == 6:
                            days['Sunday'] += 1
                    if Day == 6:
                        Day = 0
                    else:
                        Day += 1
        elif b == 2:
            for i in range(31):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 3:
            for i in range(30):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 4:
            for i in range(31):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 5:
            for i in range(30):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 6:
            for i in range(31):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 7:
            for i in range(31):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 8:
            for i in range(30):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 9:
            for i in range(31):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 10:
            for i in range(30):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
        elif b == 11:
            for i in range(31):
                if i == 12:
                    if Day == 0:
                        days['Monday'] += 1
                    elif Day == 1:
                        days['Tuesday'] += 1
                    elif Day == 2:
                        days['Wendsday'] += 1
                    elif Day == 3:
                        days['Thursday'] += 1
                    elif Day == 4:
                        days['Friday'] += 1
                    elif Day == 5:
                        days['Saturday'] += 1
                    elif Day == 6:
                        days['Sunday'] += 1
                if Day == 6:
                    Day = 0
                else:
                    Day += 1
fout.write(str(days['Saturday'])+' '+str(days['Sunday'])+' '+str(days['Monday'])+' '+str(days['Tuesday'])+' '+str(days['Wendsday'])+' '+str(days['Thursday'])+' '+str(days['Friday'])+'\n')