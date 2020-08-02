# -*- coding: utf-8 -*-
"""
ID: ion11
LANG: PYTHON3
PROB: milk2
"""

f = open("milk2.in","r")
fout = open("milk2.out","w")

f_lines = f.readlines()

N = int(f_lines[0])
milker_times = [time.split() for time in f_lines[1:]]

for times in range(N):
    for time in range(2):
        milker_times[times][time] = int(milker_times[times][time])
        
milker_times.sort()

milk_intervals = []
no_milk_intervals = []

start = int(milker_times[0][0])
end = int(milker_times[0][1])
no_milk_intervals.append(0)

for times in milker_times:
    
    starting = int(times[0])
    ending = int(times[1])
    
    if starting >= start and starting <= end:
        if ending > end:
            end = ending
            
    else:
        milk_intervals.append(end-start)
        no_milk_intervals.append(starting - end)
        start = starting
        end = ending

milk_intervals.append(end-start)

fout.write(str(max(milk_intervals)) + " " + str(max(no_milk_intervals)) + "\n")